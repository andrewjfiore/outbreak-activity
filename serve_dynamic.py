#!/usr/bin/env python3
"""Simple static file server with a dynamic root index that lists apps in `apps/`.

Usage: python3 serve_dynamic.py [PORT]
"""
import http.server
import socketserver
import os
import sys
import urllib.parse

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else int(os.environ.get("PORT", 8000))

class DynamicIndexHandler(http.server.SimpleHTTPRequestHandler):
    def list_apps_html(self):
        apps_dir = os.path.join(os.getcwd(), 'apps')
        apps = []
        if os.path.isdir(apps_dir):
            for name in sorted(os.listdir(apps_dir)):
                path = os.path.join(apps_dir, name)
                if os.path.isdir(path):
                    has_index = os.path.exists(os.path.join(path, 'index.html'))
                    apps.append((name, has_index))

        # Build a simple HTML page
        parts = [
            "<!doctype html>",
            "<html lang=\"en\">",
            "<head>",
            "<meta charset=\"utf-8\">",
            "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">",
            "<title>Outbreak Activity — Apps</title>",
            "<style>body{font-family:system-ui,Arial;background:#071023;color:#e6eef6;padding:36px}a{color:#c9a227;text-decoration:none} .card{background:#081424;padding:14px;border-radius:8px;margin:12px 0;border:1px solid rgba(201,162,39,0.06)}</style>",
            "</head>",
            "<body>",
            "<h1>Outbreak Activity — Apps</h1>",
            "<p>Available apps (served from <code>apps/</code>)</p>",
            "<div>",
        ]

        for name, has_index in apps:
            href = f"/apps/{urllib.parse.quote(name)}/"
            note = "" if has_index else " (no index.html — directory served)"
            parts.append(f"<div class=\"card\"><a href=\"{href}\"><strong>{name}</strong></a><div style=\"color:#9fb0c4\">{note}</div></div>")

        parts.extend(["</div>", "<hr>", "<p>Run <code>./serve.sh dynamic</code> to use this server.</p>", "</body>", "</html>"])
        return "\n".join(parts)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path in ('/', '/index.html'):
            content = self.list_apps_html().encode('utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            return
        return super().do_GET()


if __name__ == '__main__':
    os.chdir(os.getcwd())
    with socketserver.TCPServer(("", PORT), DynamicIndexHandler) as httpd:
        print(f"Serving HTTP on 0.0.0.0 port {PORT} (dynamic index) ...")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down")
            httpd.server_close()
