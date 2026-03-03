# Multi-app workspace

Minimal workspace for hosting static HTML webapps.

## Structure
- `apps/` — each webapp in its own subfolder with `index.html`
- `serve.sh` — Python `http.server` wrapper

## Add a new app
```bash
cp -r apps/template apps/my-app
# Edit apps/my-app/index.html
```

## Run
```bash
./serve.sh          # http://localhost:8000
./serve.sh 8080     # custom port
```

Or via npm: `npm run start`
