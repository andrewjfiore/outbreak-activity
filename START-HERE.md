# 👋 START HERE - For Complete Beginners

## What You Need to Know (30 seconds)

This repo hosts 3 HTML apps:
1. **dialogue-editor.html** - Make branching conversations
2. **dialogue-player.html** - Play those conversations
3. **seat-sample-designer.html** - Draw seating charts

---

## The Only Rule

**🎯 All your HTML files go in ONE place:**

```
apps/template/
```

That's it. That's the whole system.

---

## How to Update Your Apps

### Method 1: Super Easy (Recommended)
```bash
./update.sh
```
Type a message like "Updated my app" and press Enter. Done!

### Method 2: Manual
```bash
# 1. Test it works
./serve.sh
# Open http://localhost:8000 in your browser

# 2. Push to GitHub
git add .
git commit -m "Updated my stuff"
git push
```

---

## What Files to Edit

### ✅ YES - Edit These:
```
apps/template/dialogue-editor.html       👈 YOUR FILE
apps/template/dialogue-player.html       👈 YOUR FILE
apps/template/seat-sample-designer.html  👈 YOUR FILE
```

### ❌ NO - Don't Touch These:
```
apps/dialogue-editor/index.html          (just a pointer)
apps/dialogue-player/index.html          (just a pointer)
apps/seat-sample-designer/index.html     (just a pointer)
```

Those tiny "pointer" files (called wrappers) just load your real files from `apps/template/`. You never need to edit them.

---

## Visual Map

```
📦 outbreak-activity
│
├── 📄 START-HERE.md        👈 You are here
├── 📄 QUICK-START.md       ← Quick commands
├── 📄 CHEATSHEET.md        ← All the commands
├── 📄 HOW-TO-USE.md        ← Detailed guide
│
├── 🚀 update.sh            ← Run this to push updates!
├── 🚀 serve.sh             ← Run this to test locally!
│
└── 📁 apps
    └── 📁 template
        ├── dialogue-editor.html       ✏️ EDIT THIS
        ├── dialogue-player.html       ✏️ EDIT THIS
        └── seat-sample-designer.html  ✏️ EDIT THIS
```

---

## Daily Workflow (Copy This)

1. Open your editor (VS Code, Sublime, whatever)
2. Edit files in `apps/template/`
3. Save
4. Run `./update.sh`
5. Done!

---

## I Messed Up! Help!

### Undo my last changes
```bash
git reset --hard HEAD
```

### Start fresh from GitHub
```bash
git fetch origin
git reset --hard origin/YOUR-BRANCH-NAME
```

### I don't know what I did
```bash
git status
```
This shows what you changed.

---

## Testing Your Apps Locally

```bash
./serve.sh
```

Then open your browser to:
- **http://localhost:8000/** - Home page
- **http://localhost:8000/apps/dialogue-editor/** - Dialogue Editor
- **http://localhost:8000/apps/dialogue-player/** - Dialogue Player
- **http://localhost:8000/apps/seat-sample-designer/** - Seat Designer

Press **Ctrl+C** in the terminal to stop the server.

---

## Why This Setup?

**Q: Why not just put HTML files in `apps/dialogue-editor/`?**
A: Because then you'd have to maintain multiple copies. This way, one file = one app. Simple!

**Q: What's a "wrapper"?**
A: A tiny HTML file that loads your real file. Think of it as a shortcut. You never edit shortcuts, you edit the real thing!

**Q: Do I need Node.js or npm?**
A: Nope! Just Python (which is already on your computer).

---

## Next Steps

1. ✅ Read this file (you just did!)
2. 📋 Check out [CHEATSHEET.md](CHEATSHEET.md) for copy-paste commands
3. 🚀 Run `./serve.sh` to see your apps
4. ✏️ Edit files in `apps/template/`
5. 📤 Run `./update.sh` to push to GitHub

---

## Still Confused?

**Read these in order:**
1. [QUICK-START.md](QUICK-START.md) - 5 minute read
2. [CHEATSHEET.md](CHEATSHEET.md) - Reference guide
3. [HOW-TO-USE.md](HOW-TO-USE.md) - Complete tutorial

**Or just run:**
```bash
./update.sh
```
And follow the prompts. It's hard to break things!

---

**You got this! 🎉**
