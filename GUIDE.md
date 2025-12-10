# 📘 Complete Guide - outbreak-activity

**Everything you need to know in one place.**

---

## 📋 Table of Contents

1. [Quick Start](#quick-start)
2. [File Structure](#file-structure)
3. [Daily Workflow](#daily-workflow)
4. [Commands Reference](#commands-reference)
5. [How It Works](#how-it-works)
6. [Troubleshooting](#troubleshooting)

---

## Quick Start

### The One Rule
**Put your HTML files here:**
```
apps/template/dialogue-editor.html       ← Edit this
apps/template/dialogue-player.html       ← Edit this
apps/template/seat-sample-designer.html  ← Edit this
```

### Three Steps to Update
```bash
# 1. Edit your files in apps/template/

# 2. Test locally
./serve.sh

# 3. Push to GitHub
./update.sh
```

**Done!** 🎉

---

## File Structure

```
outbreak-activity/
│
├── 📄 README.md          ← Overview
├── 📄 GUIDE.md           ← This file (complete guide)
├── 📄 CHEATSHEET.md      ← Quick command reference
├── 📄 CLAUDE.md          ← AI assistant docs
│
├── 🚀 serve.sh           ← Test locally
├── 🚀 update.sh          ← Push to GitHub
│
├── 🌐 index.html         ← Landing page
│
└── 📁 apps/
    ├── 📁 dialogue-editor/
    │   └── index.html             (wrapper - don't edit)
    │
    ├── 📁 dialogue-player/
    │   └── index.html             (wrapper - don't edit)
    │
    ├── 📁 seat-sample-designer/
    │   └── index.html             (wrapper - don't edit)
    │
    └── 📁 template/               ← EDIT FILES HERE!
        ├── dialogue-editor.html       ✏️
        ├── dialogue-player.html       ✏️
        └── seat-sample-designer.html  ✏️
```

### What Files Do What

| File | Purpose | Do You Edit It? |
|------|---------|-----------------|
| `apps/template/*.html` | Your actual apps | ✅ YES |
| `apps/*/index.html` | Tiny wrappers that load templates | ❌ NO |
| `index.html` | Landing page | ⚠️ Only if adding new apps |
| `serve.sh` | Start local server | ❌ NO |
| `update.sh` | Push to GitHub | ❌ NO |

---

## Daily Workflow

### Standard Workflow
```bash
# 1. Edit files
vim apps/template/dialogue-editor.html

# 2. Test it
./serve.sh
# Open http://localhost:8000 in browser

# 3. Push to GitHub (easy way)
./update.sh
```

### Manual Git Workflow
```bash
# See what changed
git status

# Add all changes
git add .

# Commit with message
git commit -m "Updated dialogue editor"

# Push to GitHub
git push
```

### Undo Mistakes
```bash
# Undo last commit (not yet pushed)
git reset --soft HEAD~1

# Discard all local changes
git reset --hard HEAD

# Pull latest from GitHub
git pull
```

---

## Commands Reference

### Server Commands
```bash
# Start server (default port 8000)
./serve.sh

# Start on custom port
./serve.sh 8080

# Stop server
# Press Ctrl+C in terminal
```

### Git Commands
```bash
# Easy update (recommended)
./update.sh

# Check status
git status

# See your branch
git branch

# Switch branch
git checkout branch-name

# Pull latest changes
git pull

# Push changes
git push
```

### Common URLs (when server running)
- Home: http://localhost:8000/
- Dialogue Editor: http://localhost:8000/apps/dialogue-editor/
- Dialogue Player: http://localhost:8000/apps/dialogue-player/
- Seat Designer: http://localhost:8000/apps/seat-sample-designer/

---

## How It Works

### The Wrapper + Template Pattern

This repo uses a clever system to avoid code duplication.

**The Problem:** If you had multiple copies of the same file, updating one means updating all.

**The Solution:** One master file (template) loaded by tiny wrappers.

#### Master Templates (Real Files)
```
apps/template/dialogue-editor.html      (45 KB) ← EDIT THIS
apps/template/dialogue-player.html      (74 KB) ← EDIT THIS
apps/template/seat-sample-designer.html (30 KB) ← EDIT THIS
```

#### Wrappers (Just Pointers)
```
apps/dialogue-editor/index.html         (405 bytes) ← Loads template
apps/dialogue-player/index.html         (747 bytes) ← Loads template
apps/seat-sample-designer/index.html    (343 bytes) ← Loads template
```

#### How It Works
When you visit `http://localhost:8000/apps/dialogue-editor/`:

```
1. Browser loads: apps/dialogue-editor/index.html (wrapper)
2. Wrapper contains: <iframe src="/apps/template/dialogue-editor.html">
3. Browser loads: apps/template/dialogue-editor.html (real app)
4. You see the app!
```

It's like a desktop shortcut - the shortcut is tiny, the real program lives elsewhere.

#### Benefits
- ✅ Edit once, updates everywhere
- ✅ All editable files in one place (`apps/template/`)
- ✅ Each app has its own URL
- ✅ No code duplication

---

## Troubleshooting

### "Permission denied" when running scripts
```bash
chmod +x serve.sh update.sh
./serve.sh
```

### "Address already in use" (port 8000 busy)
```bash
# Option 1: Use different port
./serve.sh 8080

# Option 2: Kill existing server
ps aux | grep python
kill [PID]
```

### Changes not showing in browser
1. Hard refresh: **Ctrl+Shift+R** (Windows/Linux) or **Cmd+Shift+R** (Mac)
2. Clear cache: Ctrl+Shift+Delete
3. Restart server: Ctrl+C then `./serve.sh`

### Git won't let me push
```bash
# Pull latest changes first
git pull

# If conflicts, resolve them then
git add .
git commit -m "Resolved conflicts"
git push
```

### "Fatal: not a git repository"
You're in the wrong directory:
```bash
cd /path/to/outbreak-activity
```

### I edited the wrong file!
Check if you edited a wrapper by mistake:
```bash
# ❌ WRONG (wrapper)
apps/dialogue-editor/index.html

# ✅ CORRECT (template)
apps/template/dialogue-editor.html
```

If you edited a wrapper, undo it:
```bash
git checkout apps/dialogue-editor/index.html
```

### App not showing up
1. Check file exists: `ls apps/template/`
2. Check filename matches exactly (case-sensitive)
3. Refresh browser (Ctrl+F5)
4. Check browser console for errors (F12)

### Update script fails
Run commands manually:
```bash
git add .
git commit -m "Your message"
git push
```

---

## Advanced Topics

### Adding a New App

1. **Create the template:**
```bash
# Create your HTML file
nano apps/template/my-new-app.html
```

2. **Create the wrapper:**
```bash
mkdir -p apps/my-new-app

cat > apps/my-new-app/index.html << 'EOF'
<!doctype html>
<html>
<head><title>My New App</title></head>
<body style="margin:0;overflow:hidden">
  <iframe src="/apps/template/my-new-app.html"
          style="border:0;width:100%;height:100vh">
  </iframe>
</body>
</html>
EOF
```

3. **Update root index.html:**
Add a card linking to your new app.

4. **Test and push:**
```bash
./serve.sh
# Check http://localhost:8000/apps/my-new-app/
./update.sh
```

### Working with Branches

```bash
# Create new branch
git checkout -b feature/my-feature

# Switch branches
git checkout branch-name

# List branches
git branch

# Delete branch
git branch -d branch-name
```

### Deploying to GitHub Pages

1. Go to your repo on GitHub
2. Settings → Pages
3. Source: Select your branch and `/` (root)
4. Save

Your site will be at: `https://USERNAME.github.io/outbreak-activity/`

---

## Tips & Best Practices

### ✅ DO
- Edit files in `apps/template/`
- Test locally before pushing
- Write clear commit messages
- Use `./update.sh` for easy updates
- Keep your HTML self-contained (no external deps)

### ❌ DON'T
- Edit wrapper files in `apps/[app-name]/index.html`
- Push without testing
- Add npm dependencies
- Use absolute URLs (breaks when served from different roots)
- Commit sensitive data (.env files, credentials)

---

## Quick Checklist

Before pushing to GitHub:

- [ ] Edited files in `apps/template/`?
- [ ] Tested with `./serve.sh`?
- [ ] Checked in browser?
- [ ] Clear commit message?
- [ ] No sensitive data in commit?

If all yes, run `./update.sh` and you're done!

---

## Getting Help

**Still stuck?**

1. Check [CHEATSHEET.md](CHEATSHEET.md) for quick commands
2. Check [CLAUDE.md](CLAUDE.md) for technical details
3. Check git status: `git status`
4. Check what changed: `git diff`

**Common searches:**
- "How to undo git commit"
- "Git reset hard"
- "Clear browser cache"

---

**You got this! 🚀**
