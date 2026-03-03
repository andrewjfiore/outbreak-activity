# 🏗️ Architecture: Wrapper + Template Pattern

## The Idea

Instead of duplicating HTML across app folders, we keep **one master copy** per app in `apps/template/` and use tiny iframe wrappers to serve them at clean URLs.

```
apps/template/dialogue-editor.html        (45 KB) ← EDIT THIS
apps/dialogue-editor/index.html           (405 B) ← Wrapper, don't edit
```

## How It Works

1. Browser visits `/apps/dialogue-editor/`
2. Wrapper's iframe loads `/apps/template/dialogue-editor.html`
3. You see the app

## Wrapper Example

```html
<!doctype html>
<html>
<head><title>Dialogue Editor</title></head>
<body style="margin:0;overflow:hidden">
  <iframe src="/apps/template/dialogue-editor.html"
          style="border:0;width:100%;height:100vh"></iframe>
</body>
</html>
```

---

## Benefits

- **Single source of truth** — edit once, updates everywhere
- **All editable files in one place** — `apps/template/`
- **Clean URLs** — each app at its own path
- **No build step** — works on any static server

## Why Not Alternatives?

| Approach | Problem |
|----------|---------|
| Copy files | Maintain multiple copies |
| Symlinks | Break on Windows |
| Build system | Requires Node.js, config |
| **Wrappers (ours)** | Simple, universal, no deps |

---

## Adding a New App

```bash
# 1. Create template
nano apps/template/my-app.html

# 2. Create wrapper
mkdir -p apps/my-app
cat > apps/my-app/index.html << 'EOF'
<!doctype html>
<html>
<head><title>My App</title></head>
<body style="margin:0;overflow:hidden">
  <iframe src="/apps/template/my-app.html"
          style="border:0;width:100%;height:100vh"></iframe>
</body>
</html>
EOF

# 3. Add link in index.html
```

**Key rule:** Edit `apps/template/` (templates), not `apps/[name]/index.html` (wrappers).
