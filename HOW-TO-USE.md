# 🚀 How to Upload Your HTML Apps

**Put HTML files in `apps/template/` — done!**

---

## Step-by-Step

1. Save your HTML in `apps/template/`:
   ```
   apps/template/dialogue-editor.html
   apps/template/dialogue-player.html
   apps/template/seat-sample-designer.html
   ```

2. Apps auto-available at `/apps/dialogue-editor/`, etc.

---

## Testing Locally

```bash
./serve.sh          # Default port 8000
./serve.sh 8080     # Custom port
```

---

## Pushing to GitHub

```bash
# First time: ensure correct branch
git checkout your-branch-name

# Every update
git add apps/template/
git commit -m "Update HTML apps"
git push -u origin YOUR-BRANCH-NAME
```

---

## Quick Reference

| Task | Command |
|------|---------|
| Update an app | Edit `apps/template/[name].html` |
| Test locally | `./serve.sh` |
| Push | `git add . && git commit -m "msg" && git push` |

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Permission denied | `chmod +x serve.sh` |
| App not showing | Check file is in `apps/template/`, refresh with Ctrl+F5 |
| Changes stale | Clear cache (Ctrl+Shift+Delete), restart server |

---

## GitHub Pages (Optional)

Repo Settings → Pages → select branch + root folder → Save.
Site: `https://YOUR-USERNAME.github.io/outbreak-activity/`

---

**Remember:** Edit in `apps/template/`, test with `./serve.sh`, push with `git`. That's it! 🎉
