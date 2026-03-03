# 📋 CHEATSHEET

## Your 3 Files
```
apps/template/dialogue-editor.html
apps/template/dialogue-player.html
apps/template/seat-sample-designer.html
```

## Essential Commands

```bash
./serve.sh              # Start local server → http://localhost:8000/
./update.sh             # Commit + push (interactive)

git status              # See changes
git add .               # Stage all
git commit -m "msg"     # Commit
git push                # Push

git reset --soft HEAD~1 # Undo last commit (not pushed)
git checkout -- .       # Discard all changes
```

---

## File Structure

```
outbreak-activity/
├── 🚀 serve.sh / update.sh
├── 🌐 index.html
└── 📁 apps/
    ├── 📁 dialogue-editor/index.html     (wrapper — don't edit)
    ├── 📁 dialogue-player/index.html     (wrapper — don't edit)
    ├── 📁 seat-sample-designer/index.html (wrapper — don't edit)
    └── 📁 template/                       ← EDIT HERE ⭐
        ├── dialogue-editor.html       ✏️
        ├── dialogue-player.html       ✏️
        └── seat-sample-designer.html  ✏️
```

---

## Local URLs

| App | URL |
|-----|-----|
| Home | http://localhost:8000/ |
| Editor | http://localhost:8000/apps/dialogue-editor/ |
| Player | http://localhost:8000/apps/dialogue-player/ |
| Seat Designer | http://localhost:8000/apps/seat-sample-designer/ |

---

## Workflow

1. Edit `apps/template/` → 2. `./serve.sh` → 3. Check browser → 4. `./update.sh`

---

## Fixes

```bash
chmod +x serve.sh update.sh           # Permission denied
ps aux | grep python && kill [PID]    # Port in use
git pull && git push                  # Push rejected
```

Hard refresh: **Ctrl+Shift+R** / **Cmd+Shift+R**

---

## Quick Checks

- ✅ Right file? Path has `apps/template/`
- ❌ Wrong file? `apps/[name]/index.html` = wrapper only
- Server running? `ps aux | grep python`
- Current branch? `git branch`
