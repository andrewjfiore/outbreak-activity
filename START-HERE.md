# 👋 START HERE

## What This Is

3 HTML apps in one repo:
1. **dialogue-editor.html** — Make branching conversations
2. **dialogue-player.html** — Play those conversations
3. **seat-sample-designer.html** — Draw seating charts

**All files live in `apps/template/`** — that's the whole system.

---

## Updating Your Apps

### Easy Way (Recommended)
```bash
./update.sh
```

### Manual Way
```bash
./serve.sh          # Test locally at http://localhost:8000
git add .
git commit -m "Updated my stuff"
git push
```

---

## What to Edit

✅ `apps/template/*.html` — your actual files
❌ `apps/[app-name]/index.html` — wrappers, don't touch

---

## File Map

```
📦 outbreak-activity
├── 📄 START-HERE.md        👈 You are here
├── 🚀 update.sh / serve.sh ← Your two commands
└── 📁 apps/template/
    ├── dialogue-editor.html       ✏️
    ├── dialogue-player.html       ✏️
    └── seat-sample-designer.html  ✏️
```

---

## Daily Workflow

1. Edit files in `apps/template/`
2. Run `./update.sh`
3. Done!

---

## Troubleshooting

```bash
git reset --hard HEAD          # Undo all changes
git fetch origin               # Start fresh from GitHub
git reset --hard origin/YOUR-BRANCH
git status                     # See what changed
```

## Testing Locally

```bash
./serve.sh
```
- http://localhost:8000/apps/dialogue-editor/
- http://localhost:8000/apps/dialogue-player/
- http://localhost:8000/apps/seat-sample-designer/

Press **Ctrl+C** to stop.

---

## Next Steps

1. ✅ Read this (done!)
2. 📋 [CHEATSHEET.md](CHEATSHEET.md) for commands
3. 🚀 `./serve.sh` to see your apps
4. ✏️ Edit `apps/template/`
5. 📤 `./update.sh` to push

**You got this! 🎉**
