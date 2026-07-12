# ⚡ QUICK START

## Play it (no server needed)

Open **`index.html`** and pick a role — **Investigator**, **Field & Lab Team**, or **Facilitator**. That's it.

- Works when you **open the file directly**, from a **shared drive/link**, or on **GitHub Pages** (Settings → Pages → deploy from your branch, root folder).
- A full outbreak case ("The Harvest Dinner") and a demo scene are **built in** — nothing to upload to start.

---

## Edit & publish (facilitators)

```bash
# Edit apps/template/*.html, then:
./serve.sh                                        # Optional: preview locally
git add . && git commit -m "Update" && git push   # Push
```

---

## Files

✅ Edit: `apps/template/dialogue-editor.html`, `dialogue-player.html`, `seat-sample-designer.html`
❌ Don't edit: `apps/[name]/index.html` (wrappers only)

## URLs (`./serve.sh`)

| App | URL |
|-----|-----|
| Home | http://localhost:8000/ |
| Editor | http://localhost:8000/apps/dialogue-editor/ |
| Player | http://localhost:8000/apps/dialogue-player/ |
| Seat Designer | http://localhost:8000/apps/seat-sample-designer/ |

**More help?** See [HOW-TO-USE.md](HOW-TO-USE.md)
