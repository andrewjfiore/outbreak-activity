# 🚀 SUPER SIMPLE GUIDE - How to Upload Your HTML Apps

## The 3-Second Version

**Put your HTML files in `apps/template/` and you're done!**

---

## Step-by-Step (Foolproof Edition)

### Adding or Updating Your Apps

1. **Save your HTML file in the right place:**
   ```
   apps/template/dialogue-editor.html
   apps/template/dialogue-player.html
   apps/template/seat-sample-designer.html
   ```

2. **That's it!** The apps are automatically available at:
   - `http://localhost:8000/apps/dialogue-editor/`
   - `http://localhost:8000/apps/dialogue-player/`
   - `http://localhost:8000/apps/seat-sample-designer/`

---

## Testing Locally (Before Pushing to GitHub)

### Option 1: Quick Start (No setup needed)
```bash
./serve.sh
```
Then open: `http://localhost:8000/`

### Option 2: Custom Port
```bash
./serve.sh 8080
```
Then open: `http://localhost:8080/`

---

## Pushing to GitHub

### First Time Setup
```bash
# Make sure you're on your branch
git checkout claude/claude-md-mj00izt2oi1hcqth-012g24KPLaWm8ageS9vHfsmn

# Or create a new branch
git checkout -b my-updates
```

### Every Time You Update Files

```bash
# 1. Add your changes
git add apps/template/

# 2. Commit with a message
git commit -m "Update my HTML apps"

# 3. Push to GitHub
git push -u origin YOUR-BRANCH-NAME
```

**Replace `YOUR-BRANCH-NAME`** with your actual branch name!

---

## Quick Reference

### File Structure (What Goes Where)
```
outbreak-activity/
├── apps/
│   └── template/              ← PUT YOUR HTML FILES HERE!
│       ├── dialogue-editor.html
│       ├── dialogue-player.html
│       └── seat-sample-designer.html
│
├── index.html                 ← Root landing page (already set up)
└── serve.sh                   ← Run this to test locally
```

### Common Tasks

| What You Want | What To Do |
|---------------|------------|
| **Update an app** | Edit `apps/template/[app-name].html` |
| **Test locally** | Run `./serve.sh` then open browser |
| **Push to GitHub** | `git add . && git commit -m "message" && git push` |
| **Add new app** | Copy existing HTML to `apps/template/new-app.html` + update index.html |

---

## Troubleshooting

### "Permission denied" when running ./serve.sh
```bash
chmod +x serve.sh
./serve.sh
```

### "App not showing up"
1. Check file is in `apps/template/`
2. Check filename matches exactly (e.g., `dialogue-editor.html`)
3. Refresh your browser (Ctrl+F5 or Cmd+Shift+R)

### "Changes not reflected"
- Clear browser cache (Ctrl+Shift+Delete)
- Hard refresh (Ctrl+F5 or Cmd+Shift+R)
- Stop server (Ctrl+C) and restart `./serve.sh`

---

## GitHub Pages Deployment (Optional)

If you want to host this on GitHub Pages:

1. Go to your GitHub repo settings
2. Navigate to "Pages"
3. Select your branch and `/` (root) folder
4. Save
5. Your site will be at: `https://YOUR-USERNAME.github.io/outbreak-activity/`

---

## Still Confused?

**Just remember these 3 things:**

1. **Edit files in**: `apps/template/`
2. **Test with**: `./serve.sh`
3. **Push with**: `git add . && git commit -m "your message" && git push`

That's it! 🎉
