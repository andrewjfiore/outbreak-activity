# 📋 CHEATSHEET - Copy & Paste Edition

## Your 3 Main Files
```
apps/dialogue-editor/index.html       ← Edit this one
apps/dialogue-player/index.html       ← Edit this one
apps/seat-sample-designer/index.html  ← Edit this one
```

## Essential Commands

### Start Local Server
```bash
./serve.sh
```
Then open: http://localhost:8000/apps/dialogue-editor/

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
├── 📄 GUIDE.md               ← Complete guide
├── 📄 CHEATSHEET.md          ← This file
├── 📄 CLAUDE.md              ← Technical docs
│
├── 🚀 serve.sh               ← Run to test
├── 🚀 update.sh              ← Run to push
│
├── 🌐 index.html             ← Landing page
│
└── 📁 apps/
    ├── dialogue-editor/
    │   └── index.html        ✏️ EDIT THIS
    ├── dialogue-player/
    │   └── index.html        ✏️ EDIT THIS
    └── seat-sample-designer/
        └── index.html        ✏️ EDIT THIS
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

1. **Edit** your HTML files in `apps/[app-name]/index.html`
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

**Need more help?** See [GUIDE.md](GUIDE.md)
