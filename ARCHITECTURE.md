# 🏗️ Architecture Explained (For the Curious)

## The Wrapper + Template Pattern

This repo uses a clever trick to avoid code duplication.

### The Problem

If you had 3 HTML apps, you'd normally have:
```
apps/dialogue-editor/dialogue-editor.html    (45 KB)
apps/dialogue-player/dialogue-player.html    (74 KB)
apps/seat-sample-designer/seat-sample.html   (30 KB)
```

If you wanted to update one, you'd have to remember which folder it's in. Confusing!

### The Solution

Instead, we have:

**1. Master Templates** (the real files)
```
apps/template/dialogue-editor.html           (45 KB) ← EDIT THIS
apps/template/dialogue-player.html           (74 KB) ← EDIT THIS
apps/template/seat-sample-designer.html      (30 KB) ← EDIT THIS
```

**2. Tiny Wrappers** (just pointers)
```
apps/dialogue-editor/index.html              (405 bytes) ← Just loads template
apps/dialogue-player/index.html              (747 bytes) ← Just loads template
apps/seat-sample-designer/index.html         (343 bytes) ← Just loads template
```

### How It Works

When you visit `http://localhost:8000/apps/dialogue-editor/`:

```
1. Browser loads: apps/dialogue-editor/index.html (the wrapper)

2. Wrapper contains: <iframe src="/apps/template/dialogue-editor.html">

3. Browser loads: apps/template/dialogue-editor.html (the real app)

4. You see the app!
```

It's like a shortcut on your desktop. The shortcut is tiny, the real program is somewhere else.

---

## Benefits

### ✅ Single Source of Truth
- Update `apps/template/dialogue-editor.html`
- It automatically updates everywhere

### ✅ Easy to Find
- All your editable files are in ONE place: `apps/template/`

### ✅ Flexible URLs
- Each app has its own URL path
- Works from any server root (localhost, GitHub Pages, etc.)

### ✅ Clean Organization
- Templates separate from app routing
- Easy to add new apps

---

## Example Wrapper File

Here's what a wrapper looks like:

```html
<!doctype html>
<html>
<head>
  <title>Dialogue Editor</title>
</head>
<body style="margin:0;overflow:hidden">
  <iframe src="/apps/template/dialogue-editor.html"
          style="border:0;width:100%;height:100vh">
  </iframe>
</body>
</html>
```

That's it! Just 9 lines that load the real app via iframe.

---

## Why iframe?

**Q: Why use an iframe instead of just copying the file?**

A: If we copied files, you'd have to update 3+ copies every time you made a change. With iframes, you update once in `apps/template/` and all wrappers automatically get the update.

**Q: Are there downsides?**

A: Very minor. Iframes are slightly slower (microseconds), but in exchange you get:
- No code duplication
- One place to edit
- Impossible to have "version drift" between copies

---

## Adding a New App

### Step 1: Create the Master Template
```bash
# Create your HTML file
nano apps/template/my-new-app.html
```

### Step 2: Create a Wrapper
```bash
# Make the app directory
mkdir -p apps/my-new-app

# Create the wrapper
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

### Step 3: Update Root Index
Add a card to `index.html` linking to your new app.

### Done!
Your app is now at: `http://localhost:8000/apps/my-new-app/`

---

## File Flow Diagram

```
📝 You edit
    ↓
apps/template/dialogue-editor.html (master file)
    ↑
    │ Loaded by iframe
    │
apps/dialogue-editor/index.html (wrapper)
    ↑
    │ Requested by browser
    │
http://localhost:8000/apps/dialogue-editor/
    ↑
    │ User visits
    │
🌐 Browser
```

---

## Why This Matters

When you understand this pattern, you'll never accidentally edit the wrong file again!

**Remember:**
- **Wrappers** = Tiny files in `apps/[app-name]/index.html` (don't edit)
- **Templates** = Real files in `apps/template/[app-name].html` (edit these!)

---

## Alternatives We Didn't Use

### ❌ Copy-Paste Files
```
apps/dialogue-editor/dialogue-editor.html
apps/dialogue-player/dialogue-player.html
```
**Problem**: Have to maintain multiple copies

### ❌ Symlinks
```
apps/dialogue-editor/index.html → ../../template/dialogue-editor.html
```
**Problem**: Symlinks break on Windows, complicated to maintain

### ❌ Build System (Webpack, Vite, etc.)
```
npm run build → generates files
```
**Problem**: Requires Node.js, npm, build step, configuration

### ✅ Wrapper + Template (What We Use)
```
Wrapper loads template via iframe
```
**Benefits**: Simple, works everywhere, no build step, single source of truth

---

## Questions?

See the other docs:
- [START-HERE.md](START-HERE.md) - Complete beginner guide
- [QUICK-START.md](QUICK-START.md) - Essential commands
- [CHEATSHEET.md](CHEATSHEET.md) - Copy-paste reference
