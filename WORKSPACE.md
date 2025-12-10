# Multi‑app workspace

This folder contains a minimal workspace for hosting multiple static HTML webapps.

Structure

- `apps/` — put each webapp in its own subfolder, each with an `index.html`.
  - Example: `apps/my-app/index.html`
- `serve.sh` — simple server script using Python's `http.server`.
- `package.json` — convenience npm scripts (optional).

How to add a new app

1. Copy the template folder:

```bash
cp -r apps/template apps/my-app
# then edit apps/my-app/index.html
```

How to run

Option A — using the included shell script (no node required):

```bash
chmod +x serve.sh
./serve.sh        # serves on http://localhost:8000
./serve.sh 8080   # serves on port 8080
```

Option B — via npm (if you prefer):

```bash
# optional: npm install
npm run start
```

Notes

- This is intentionally minimal — you can replace `serve.sh` with a Node-based dev server if you like.
- When you're ready, add your HTML apps under `apps/` and they'll be available at `http://localhost:<port>/app-name/`.
