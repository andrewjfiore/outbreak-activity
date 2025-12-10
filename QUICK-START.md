# ⚡ QUICK START

## For the Impatient

### Update Your Apps (3 Commands)
```bash
# 1. Edit your HTML files in apps/template/

# 2. Test it works
./serve.sh

# 3. Push to GitHub
git add . && git commit -m "Updated apps" && git push
```

---

## File Locations

### ✅ DO - Edit these files:
- `apps/template/dialogue-editor.html`
- `apps/template/dialogue-player.html`
- `apps/template/seat-sample-designer.html`

### ❌ DON'T - Edit these files:
- `apps/dialogue-editor/index.html` (just a wrapper)
- `apps/dialogue-player/index.html` (just a wrapper)
- `apps/seat-sample-designer/index.html` (just a wrapper)

---

## URL Reference

When you run `./serve.sh`:

| App | URL |
|-----|-----|
| **Landing Page** | http://localhost:8000/ |
| **Dialogue Editor** | http://localhost:8000/apps/dialogue-editor/ |
| **Dialogue Player** | http://localhost:8000/apps/dialogue-player/ |
| **Seat Designer** | http://localhost:8000/apps/seat-sample-designer/ |

---

## One-Line Commands

```bash
# Start server
./serve.sh

# Git update (all-in-one)
git add . && git commit -m "Update" && git push

# Check what changed
git status

# See what's running
ps aux | grep python
```

---

**Need more help?** See [HOW-TO-USE.md](HOW-TO-USE.md)
