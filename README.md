# 🦠 outbreak-activity

Interactive outbreak investigation simulation exercise featuring interviews, sample collection, and line list creation.

---

## 🚀 Quick Start

### 1. Edit Your HTML Apps
```
apps/template/dialogue-editor.html
apps/template/dialogue-player.html
apps/template/seat-sample-designer.html
```

### 2. Test Locally
```bash
./serve.sh
```
Open: **http://localhost:8000/**

### 3. Push to GitHub
```bash
./update.sh
```

**Done!** 🎉

---

## 📚 Documentation

- **[GUIDE.md](GUIDE.md)** - Complete guide (start here!)
- **[CHEATSHEET.md](CHEATSHEET.md)** - Quick command reference
- **[CLAUDE.md](CLAUDE.md)** - Technical documentation & AI assistant guide

---

## 📱 Apps

| App | Purpose | URL |
|-----|---------|-----|
| **Dialogue Editor** | Create branching dialogue scenarios | `/apps/dialogue-editor/` |
| **Dialogue Player** | Play dialogue with analytics | `/apps/dialogue-player/` |
| **Seat/Sample Designer** | Design spatial layouts | `/apps/seat-sample-designer/` |

---

## 💡 Key Points

✅ **Edit files in**: `apps/template/`
✅ **Test with**: `./serve.sh`
✅ **Push with**: `./update.sh`

❌ **Don't edit**: `apps/[app-name]/index.html` (wrappers only)

---

## 🏗️ Architecture

**Wrapper + Template Pattern:**
- Small wrapper files load actual apps via iframe
- All editable files in `apps/template/`
- Single source of truth - edit once, updates everywhere

See [GUIDE.md](GUIDE.md) for details.

---

## 🆘 Help

See [GUIDE.md](GUIDE.md) for troubleshooting, workflows, and detailed instructions.
