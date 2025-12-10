# 📋 CHEATSHEET - Copy & Paste Edition

## Your 3 Main Files
```
apps/template/dialogue-editor.html       ← Edit this one
apps/template/dialogue-player.html       ← Edit this one
apps/template/seat-sample-designer.html  ← Edit this one
```

## Essential Commands

### Start Local Server
```bash
./serve.sh
```
Then open: http://localhost:8000/

### Easy Update Script (Recommended!)
```bash
./update.sh
```
It will ask for a commit message and push everything for you.

### Manual Git Commands
```bash
# See what changed
git status

# Add everything
git add .

# Commit with message
git commit -m "Your message here"

# Push to GitHub
git push
```

### Emergency: Undo Last Commit (Not Pushed)
```bash
git reset --soft HEAD~1
```

### Emergency: Discard All Changes
```bash
git checkout -- .
```

---

## File Structure (Visual)

```
outbreak-activity/
│
├── 📄 README.md              ← Start here
├── 📄 QUICK-START.md         ← Quick commands
├── 📄 HOW-TO-USE.md          ← Full guide
├── 📄 CHEATSHEET.md          ← This file
│
├── 🚀 serve.sh               ← Run to test
├── 🚀 update.sh              ← Run to push
│
├── 🌐 index.html             ← Landing page
│
└── 📁 apps/
    ├── 📁 dialogue-editor/
    │   └── index.html        (wrapper - don't edit)
    │
    ├── 📁 dialogue-player/
    │   └── index.html        (wrapper - don't edit)
    │
    ├── 📁 seat-sample-designer/
    │   └── index.html        (wrapper - don't edit)
    │
    └── 📁 template/          ← EDIT FILES HERE! ⭐
        ├── dialogue-editor.html       ✏️ EDIT THIS
        ├── dialogue-player.html       ✏️ EDIT THIS
        └── seat-sample-designer.html  ✏️ EDIT THIS
```

---

## URLs When Running Locally

| What | URL |
|------|-----|
| Home | http://localhost:8000/ |
| Dialogue Editor | http://localhost:8000/apps/dialogue-editor/ |
| Dialogue Player | http://localhost:8000/apps/dialogue-player/ |
| Seat Designer | http://localhost:8000/apps/seat-sample-designer/ |

---

## Typical Workflow

1. **Edit** your HTML files in `apps/template/`
2. **Test** by running `./serve.sh`
3. **Check** in browser at http://localhost:8000/
4. **Push** by running `./update.sh`
5. **Done!**

---

## Common Issues

### "Permission denied" on scripts
```bash
chmod +x serve.sh update.sh
```

### "Address already in use"
```bash
# Find and kill the process
ps aux | grep python
kill [PID_NUMBER]

# Or use a different port
./serve.sh 8080
```

### "Changes not showing"
- Hard refresh: **Ctrl+Shift+R** (Windows/Linux) or **Cmd+Shift+R** (Mac)
- Or clear browser cache

### "Git won't let me push"
```bash
# Pull latest changes first
git pull

# Then push
git push
```

---

## File Names Reference

If you're renaming files, they must match exactly:

| Template File | Accessed Via |
|---------------|--------------|
| `dialogue-editor.html` | `/apps/dialogue-editor/` |
| `dialogue-player.html` | `/apps/dialogue-player/` |
| `seat-sample-designer.html` | `/apps/seat-sample-designer/` |

---

## Quick Checks

### Did I edit the right file?
✅ YES if path contains: `apps/template/`
❌ NO if path contains: `apps/dialogue-editor/index.html` (that's just a wrapper)

### Is my server running?
```bash
ps aux | grep python
```
If you see `http.server`, it's running!

### What's my current git branch?
```bash
git branch
```
The one with `*` is your current branch.

---

**Print this and keep it next to your computer!** 📌
