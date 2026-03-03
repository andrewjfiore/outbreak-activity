#!/usr/bin/env python3
"""
Outbreak Activity Fuzz & Chaos Test Suite
Tests: malformed dialogue JSON, XSS in text fields, huge node counts,
       circular references, server endpoint fuzzing
"""
import json
import sys
import copy
import time
import socket
import random
import string
import threading
import urllib.request
import urllib.error
import http.client
import subprocess
import os

RESULTS = []

def record(test_name, category, severity, finding, suggestion, passed=False):
    RESULTS.append({
        "test": test_name,
        "category": category,
        "severity": severity,
        "finding": finding,
        "suggestion": suggestion,
        "passed": passed,
    })
    status = "✅ PASS" if passed else severity
    print(f"[{status}] {test_name}: {finding}")


# ─── Valid Dialogue Fixture ───────────────────────────────────────────────────

VALID_DIALOGUE = {
    "title": "Sample Outbreak Dialogue",
    "startNode": "node_001",
    "approvalTypes": ["CDC", "WHO"],
    "nodes": [
        {
            "id": "node_001",
            "text": "You receive a report of a new outbreak. What do you do?",
            "speaker": "Narrator",
            "nextNode": "node_002",
            "choices": []
        },
        {
            "id": "node_002",
            "text": "You call the CDC.",
            "speaker": "Player",
            "nextNode": "",
            "choices": [
                {"text": "Report immediately", "nextNode": "node_003", "effects": {"approvals": {}, "stats": {}}},
                {"text": "Wait and observe", "nextNode": "node_003", "effects": {"approvals": {}, "stats": {}}}
            ]
        },
        {
            "id": "node_003",
            "text": "Decision made.",
            "speaker": "Narrator",
            "nextNode": "",
            "choices": []
        }
    ]
}


def simulate_dialogue_import(json_str):
    """Simulate what dialogue-editor.html importJSON() does."""
    try:
        data = json.loads(json_str)
        
        if not data.get("nodes") or not isinstance(data["nodes"], list):
            raise ValueError("Invalid format: missing nodes array")
        
        project_title = data.get("title", "Imported Dialogue")
        start_node = data.get("startNode", "")
        approval_types = data.get("approvalTypes", [])
        
        nodes = []
        for node in data["nodes"]:
            processed = {
                **node,
                "choices": [
                    {**c, "effects": c.get("effects", {"approvals": {}, "stats": {}})}
                    for c in (node.get("choices") or [])
                ] if isinstance(node.get("choices"), list) else []
            }
            nodes.append(processed)
        
        return True, {"title": project_title, "startNode": start_node, "nodes": nodes}
    except ValueError as e:
        return False, str(e)
    except json.JSONDecodeError as e:
        return False, f"JSON parse error: {e}"
    except Exception as e:
        return False, f"Unexpected: {e}"


# ─── Dialogue JSON Fuzzing ────────────────────────────────────────────────────

def test_malformed_dialogue_json():
    malformed = [
        ("empty", ""),
        ("null", "null"),
        ("empty_object", "{}"),
        ("missing_nodes", json.dumps({"title": "test", "startNode": "n1"})),
        ("nodes_not_array", json.dumps({"nodes": "not array", "startNode": "n1"})),
        ("nodes_with_nulls", json.dumps({"nodes": [None, None, {"id": "n1"}], "startNode": "n1"})),
        ("empty_nodes", json.dumps({"nodes": [], "startNode": "n1"})),
        ("truncated", '{"title": "test", "nodes": [{"id": "n1", "text": '),
    ]
    for name, payload in malformed:
        ok, result = simulate_dialogue_import(payload)
        if not ok:
            record(f"malformed_json/{name}", "Import", "🟢",
                   f"Graceful failure: {str(result)[:80]}", 
                   "Verify user sees helpful error, not raw exception", passed=True)
        else:
            record(f"malformed_json/{name}", "Robustness", "🟡",
                   f"Import accepted invalid dialogue: {name}",
                   "Add validation before importing — check nodes is non-empty array")


def test_xss_in_dialogue_text():
    """XSS payloads in dialogue text/speaker fields."""
    xss_payloads = [
        '<script>alert("XSS")</script>',
        '"><img src=x onerror=alert(1)>',
        '<svg/onload=alert(document.domain)>',
        'javascript:alert(1)',
        '<iframe src="javascript:alert(1)"></iframe>',
        '{{7*7}}',  # Template injection
        '${alert(1)}',  # Template literal injection
        '\u003cscript\u003ealert(1)\u003c/script\u003e',  # Unicode escaped
    ]
    
    for payload in xss_payloads:
        dialogue = copy.deepcopy(VALID_DIALOGUE)
        dialogue["nodes"][0]["text"] = payload
        dialogue["nodes"][0]["speaker"] = payload
        dialogue["nodes"][1]["choices"][0]["text"] = payload
        dialogue["title"] = payload
        
        json_str = json.dumps(dialogue)
        ok, data = simulate_dialogue_import(json_str)
        
        if ok:
            # Check if stored verbatim
            node_text = data["nodes"][0].get("text", "")
            if node_text == payload and ("<" in payload or "javascript:" in payload):
                record(f"xss_dialogue/{payload[:30]}", "XSS", "🔴",
                       f"XSS payload stored verbatim in dialogue text: {payload[:60]}",
                       "Use escapeHtml() (already defined in editor) on all text fields before rendering. "
                       "Audit all innerHTML assignments — especially in renderNodeList() and choice rendering. "
                       "Use DOMPurify for rich text or textContent for plain text.")


def test_circular_node_references():
    """Nodes that reference each other in loops."""
    circular_dialogue = {
        "title": "Circular",
        "startNode": "node_A",
        "approvalTypes": [],
        "nodes": [
            {"id": "node_A", "text": "Node A", "speaker": "Test", "nextNode": "node_B", "choices": []},
            {"id": "node_B", "text": "Node B", "speaker": "Test", "nextNode": "node_A", "choices": []},  # loops back
        ]
    }
    ok, data = simulate_dialogue_import(json.dumps(circular_dialogue))
    if ok:
        record("circular/two_node_loop", "Logic", "🟡",
               "Circular node reference (A→B→A) imported without warning",
               "In dialogue-player.html, detect cycles during playback (track visited node IDs) to prevent infinite loops")
    
    # Self-referencing node
    self_ref = {
        "title": "Self-ref",
        "startNode": "node_A",
        "approvalTypes": [],
        "nodes": [
            {"id": "node_A", "text": "Goes to itself", "speaker": "Test", "nextNode": "node_A", "choices": []}
        ]
    }
    ok2, _ = simulate_dialogue_import(json.dumps(self_ref))
    if ok2:
        record("circular/self_reference", "Logic", "🔴",
               "Self-referencing node (A→A) accepted — will cause infinite loop in player",
               "Detect self-references during import and warn; in player add visited-node tracking with max depth limit")


def test_huge_node_count():
    """Dialogue with enormous number of nodes."""
    huge_dialogue = copy.deepcopy(VALID_DIALOGUE)
    
    for i in range(5000):
        huge_dialogue["nodes"].append({
            "id": f"node_{i:05d}",
            "text": f"Node {i}: " + "A" * 200,
            "speaker": "Test",
            "nextNode": f"node_{(i+1):05d}",
            "choices": []
        })
    
    json_str = json.dumps(huge_dialogue)
    start = time.time()
    ok, data = simulate_dialogue_import(json_str)
    elapsed = time.time() - start
    
    size_mb = len(json_str) / (1024 * 1024)
    
    if elapsed > 2.0:
        record("huge_nodes/5000_nodes", "Performance", "🟡",
               f"5000-node dialogue took {elapsed:.2f}s to parse ({size_mb:.1f}MB)",
               "Add node count limit (e.g., 500 max) and payload size check before import")
    else:
        record("huge_nodes/5000_nodes", "Performance", "🟢",
               f"5000 nodes: {elapsed:.3f}s ({size_mb:.1f}MB) — OK", "", passed=True)
    
    # 10000 choices per node
    deep_choice_dialogue = copy.deepcopy(VALID_DIALOGUE)
    deep_choice_dialogue["nodes"][1]["choices"] = [
        {"text": f"Choice {i}", "nextNode": "node_003", "effects": {"approvals": {}, "stats": {}}}
        for i in range(10000)
    ]
    start2 = time.time()
    ok2, _ = simulate_dialogue_import(json.dumps(deep_choice_dialogue))
    elapsed2 = time.time() - start2
    
    if elapsed2 > 1.0:
        record("huge_nodes/10000_choices", "Performance", "🟡",
               f"10,000 choices on one node took {elapsed2:.2f}s",
               "Limit choices per node (e.g., max 20)")
    else:
        record("huge_nodes/10000_choices", "Performance", "🟢",
               f"10,000 choices: {elapsed2:.3f}s — OK", "", passed=True)


def test_missing_startnode():
    """Dialogue where startNode doesn't exist in nodes array."""
    bad_start = copy.deepcopy(VALID_DIALOGUE)
    bad_start["startNode"] = "nonexistent_node"
    
    ok, data = simulate_dialogue_import(json.dumps(bad_start))
    if ok:
        record("bad_start/nonexistent", "Logic", "🟡",
               "Dialogue with invalid startNode accepted — player will fail to start",
               "Validate startNode references an existing node ID at import time")
    
    # Empty startNode
    no_start = copy.deepcopy(VALID_DIALOGUE)
    no_start["startNode"] = ""
    ok2, _ = simulate_dialogue_import(json.dumps(no_start))
    if ok2:
        record("bad_start/empty", "Logic", "🟡",
               "Dialogue with empty startNode accepted",
               "Require non-empty startNode or auto-set to first node")


def test_duplicate_node_ids():
    """Nodes with duplicate IDs."""
    dup_ids = copy.deepcopy(VALID_DIALOGUE)
    dup_ids["nodes"].append({
        "id": "node_001",  # duplicate!
        "text": "Duplicate node",
        "speaker": "Test",
        "nextNode": "",
        "choices": []
    })
    
    ok, data = simulate_dialogue_import(json.dumps(dup_ids))
    if ok:
        record("duplicate_ids/nodes", "Logic", "🟡",
               "Dialogue with duplicate node IDs imported without warning — last one silently wins",
               "Check for duplicate node IDs during import and warn user")


# ─── Server Fuzzing ───────────────────────────────────────────────────────────

def test_server_availability():
    """Check if the server is running for HTTP fuzzing."""
    try:
        conn = http.client.HTTPConnection("127.0.0.1", 8000, timeout=2)
        conn.request("GET", "/")
        resp = conn.getresponse()
        conn.close()
        return True, resp.status
    except (ConnectionRefusedError, OSError):
        return False, None


def fuzz_http_server():
    """Fuzz the serve_dynamic.py HTTP server."""
    available, status = test_server_availability()
    
    if not available:
        record("server/availability", "Server", "🟡",
               "Server not running — skipping HTTP fuzz tests",
               "Start with: cd /home/andrew/repos/outbreak-activity && python3 serve_dynamic.py 8000")
        return
    
    record("server/availability", "Server", "🟢", 
           f"Server running (HTTP {status})", "", passed=True)
    
    # Malformed HTTP requests
    malformed_requests = [
        ("oversized_header", f"GET / HTTP/1.1\r\nHost: localhost\r\nX-Custom: {'A'*65535}\r\n\r\n"),
        ("null_byte_path", "GET /\x00evil HTTP/1.1\r\nHost: localhost\r\n\r\n"),
        ("path_traversal_1", "GET /../../../etc/passwd HTTP/1.1\r\nHost: localhost\r\n\r\n"),
        ("path_traversal_2", "GET /apps/../../../etc/passwd HTTP/1.1\r\nHost: localhost\r\n\r\n"),
        ("long_path", f"GET /{'A'*10000} HTTP/1.1\r\nHost: localhost\r\n\r\n"),
        ("method_fuzz", f"FUZZ / HTTP/1.1\r\nHost: localhost\r\n\r\n"),
        ("post_to_get_endpoint", "POST / HTTP/1.1\r\nHost: localhost\r\nContent-Length: 100\r\n\r\n" + "X"*100),
    ]
    
    for name, raw_req in malformed_requests:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect(("127.0.0.1", 8000))
            sock.sendall(raw_req.encode("latin-1", errors="replace"))
            
            response = b""
            try:
                while True:
                    chunk = sock.recv(4096)
                    if not chunk:
                        break
                    response += chunk
                    if len(response) > 100000:
                        break
            except socket.timeout:
                pass
            sock.close()
            
            resp_str = response.decode("utf-8", errors="replace")
            first_line = resp_str.split("\r\n")[0] if resp_str else "no response"
            
            if "500" in first_line:
                record(f"server_fuzz/{name}", "Server Error", "🟡",
                       f"Server returned 500: {first_line}",
                       "Add error handling for malformed requests in serve_dynamic.py")
            elif "etc/passwd" in resp_str.lower():
                record(f"server_fuzz/{name}", "Security", "🔴",
                       "PATH TRAVERSAL: /etc/passwd content in response!",
                       "Sanitize path before serving; use os.path.realpath() and check it starts within serve root")
            elif name == "path_traversal_1" or name == "path_traversal_2":
                record(f"server_fuzz/{name}", "Security", "🟢",
                       f"Path traversal blocked: {first_line}", "", passed=True)
            else:
                record(f"server_fuzz/{name}", "Server", "🟢",
                       f"Server handled gracefully: {first_line[:60]}", "", passed=True)
                       
        except ConnectionResetError:
            record(f"server_fuzz/{name}", "Server", "🟢",
                   "Server closed connection (graceful rejection)", "", passed=True)
        except Exception as e:
            record(f"server_fuzz/{name}", "Server", "🟡",
                   f"Connection error: {e}",
                   "Ensure server handles unexpected disconnects gracefully")


def fuzz_concurrent_connections():
    """Test server under concurrent connection load."""
    available, _ = test_server_availability()
    if not available:
        return
    
    errors = []
    responses = []
    
    def make_request():
        try:
            conn = http.client.HTTPConnection("127.0.0.1", 8000, timeout=5)
            conn.request("GET", "/")
            resp = conn.getresponse()
            responses.append(resp.status)
            conn.close()
        except Exception as e:
            errors.append(str(e))
    
    threads = [threading.Thread(target=make_request) for _ in range(50)]
    start = time.time()
    for t in threads:
        t.start()
    for t in threads:
        t.join(timeout=10)
    elapsed = time.time() - start
    
    success_count = sum(1 for r in responses if r == 200)
    
    if errors:
        record("server_concurrent/50_connections", "Performance", "🟡",
               f"50 concurrent: {success_count} OK, {len(errors)} errors in {elapsed:.2f}s. "
               f"Errors: {errors[0][:80]}",
               "Python's socketserver.TCPServer is single-threaded by default — consider ThreadingMixIn")
    else:
        record("server_concurrent/50_connections", "Performance", "🟢",
               f"50 concurrent connections: all {success_count} OK in {elapsed:.2f}s", "", passed=True)


# ─── Run All Tests ────────────────────────────────────────────────────────────

def run_all():
    print("=" * 70)
    print("Outbreak Activity Fuzz & Chaos Test Suite")
    print("=" * 70)
    
    test_malformed_dialogue_json()
    test_xss_in_dialogue_text()
    test_circular_node_references()
    test_huge_node_count()
    test_missing_startnode()
    test_duplicate_node_ids()
    fuzz_http_server()
    fuzz_concurrent_connections()
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    critical = [r for r in RESULTS if r["severity"] == "🔴"]
    medium = [r for r in RESULTS if r["severity"] == "🟡"]
    low = [r for r in RESULTS if r["severity"] == "🟢" and not r["passed"]]
    passed = [r for r in RESULTS if r["passed"]]
    
    print(f"✅ Passed:   {len(passed)}")
    print(f"🔴 Critical: {len(critical)}")
    print(f"🟡 Medium:   {len(medium)}")
    print(f"🟢 Low:      {len(low)}")
    print(f"Total: {len(RESULTS)}")
    
    return RESULTS


if __name__ == "__main__":
    results = run_all()
    with open("/home/andrew/repos/outbreak-activity/chaos-tests/results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("\nResults saved to chaos-tests/results.json")
