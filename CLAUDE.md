# jassonfarrier-site — Project Instructions for Claude

## MANDATORY: Read this before touching anything

### Tools you MUST use — no exceptions

1. **GitHub API** — this is the source of truth for all site files.
   - Token: stored by Jasson, ask him if needed.
   - Repo: `jassonfarrier/jassonfarrier-site`
   - NEVER edit files from local sandbox copies or from curling the live site.
   - ALWAYS read files from GitHub API before editing them.

2. **Netlify CLI deploy** — after pushing to GitHub, deploy via:
   ```
   NETLIFY_AUTH_TOKEN=nfp_RHQvRuKMsDZytmxXa4YuVQPe6GXJyhLrf323 npx netlify-cli deploy --site 38b33f0a-e248-4998-b444-340d66f310b0 --dir . --prod
   ```
   Site ID: `38b33f0a-e248-4998-b444-340d66f310b0`

3. **After every deploy** — curl every changed URL to confirm 200, not 404.

---

### Workflow for every site change — no shortcuts

1. Fetch the file from GitHub API (raw content)
2. Make the change
3. Push back to GitHub via API with a commit message
4. Deploy to Netlify via CLI
5. Curl the live URLs to verify

### What NOT to do — ever

- Do NOT use `web_fetch` to read site files (returns summaries, not raw HTML)
- Do NOT read files from `/Users/jassonfarrier/Desktop/jassonfarrier-site/` (local copies are stale)
- Do NOT curl the live site as a source for editing (live site may already be broken)
- Do NOT create files with `blog-` prefix — there is no blog section
- Do NOT deploy a file without first checking its byte size is non-zero

---

### Site structure

```
/                          → index.html
/bio                       → bio.html
/contact                   → contact.html
/free                      → free.html
/privacy                   → privacy.html
/ohio-housing-data         → ohio-housing-data.html
/housing-market-updates    → housing-market-updates.html
/market-updates            → market-updates.html (same as housing-market-updates)
/market-updates/[slug]     → market-updates/[slug].html
```

### Market update articles (live at /market-updates/[slug])

- ohio-spring-2026
- housing-market-splitting-in-two
- ohio-feb-2026
- housing-slowdown-2026
- ohio-dec-2025
- property-tax-sep-2025

---

### Rules Jasson has set — permanent

- NEVER ask Jasson to run a terminal command
- NEVER use cute slogans, taglines, or clever phrases
- NEVER tell Jasson you cannot deploy — always deploy via Netlify CLI above
- ALWAYS verify every page returns 200 after deploy
- GitHub token: ask Jasson at the start of each session if not already provided
