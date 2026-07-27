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
- Do NOT use regex or line-by-line CSS parsers to strip/replace CSS rules — always do targeted string replacements on exact known strings
- Do NOT edit CSS without verifying you have the FULL current CSS in context first

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

### Market update articles (live at /housing-market-updates/[slug])

- buying-a-home-in-ohio-price-cuts (July 2026)
- ohio-spring-2026 (March 2026)
- ohio-feb-2026 (February 2026)
- housing-slowdown-2026 (April 2026 — national, Housing Nerd channel)
- ohio-dec-2025 (December 2025)
- property-tax-sep-2025 (September 2025)

---

## Market Update Page — Standard HTML Structure

Every market update page MUST use this exact structure. No exceptions. No alternate class names.

### Page header (dark navy block at top)

```html
<div class="page-header">
  <div class="page-header-inner">
    <a href="/housing-market-updates" class="back-link">← Back to Market Updates</a>
    <span class="tag">[Category] · [Month Year]</span>
    <p class="article-byline">By <a href="/bio">Jasson Farrier</a> &nbsp;·&nbsp; <a href="[YouTube URL]" target="_blank" rel="noopener">[Channel Name]</a> &nbsp;·&nbsp; [Month Year]</p>
    <span class="article-date">Published: [Month Year]</span>
    <h1>[Article Title]</h1>
  </div>
</div>
```

**YouTube channel rules:**
- Ohio articles → `https://www.youtube.com/@ohiohousingnerd` / "Ohio Housing Nerd"
- National articles → `https://www.youtube.com/@HousingNerd` / "Housing Nerd"

**Class names — these are the ONLY correct names:**
- `page-header` — the outer dark navy div
- `page-header-inner` — the inner max-width container
- `back-link` — the ← Back link
- `tag` — the category/date tag span
- `article-byline` — the byline paragraph
- `article-date` — the published date span
- These are NOT interchangeable with: `post-tag`, `post-meta`, `post-header`, `article-header`, `article-tag`

### Required CSS block (must appear in every market update page)

This exact CSS must be present in the `<style>` block of every market update page. Do not alter it. Do not generate variations of it.

```css
.page-header { background: #0D1E42; padding: 80px 64px 72px; }
.page-header-inner { max-width: 760px; margin: 0 auto; }
.page-header h1 { font-size: clamp(24px, 3.5vw, 42px); font-weight: 700; color: #fff; line-height: 1.2; margin: 20px 0 0; }
.back-link { font-size: 12px; font-weight: 600; color: rgba(255,255,255,0.5); text-decoration: none; display: block; margin-bottom: 20px; letter-spacing: 0.5px; }
.back-link:hover { color: #fff; }
.tag { font-size: 11px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: #9DA6AB; display: block; margin-bottom: 12px; }
.article-byline { font-size: 13px; color: rgba(255,255,255,0.5); margin: 10px 0 4px; }
.article-byline a { color: rgba(255,255,255,0.65) !important; text-decoration: none; border-bottom: 1px solid rgba(255,255,255,0.2); }
.article-date { font-size: 12px; color: rgba(255,255,255,0.35); display: block; margin-top: 4px; }
```

### Site-wide colors and fonts

- Dark navy: `#0D1E42`
- Gray: `#9DA6AB`
- White: `#ffffff`
- Border/divider: `#f5f5f5`
- Light background: `#f7f8fa`
- Font: Montserrat (Google Fonts)

### Contact CTA — required on every market update

Place this block immediately before the subscribe bar on every market update page:

```html
<div class="contact-cta">
  <p>Buying or selling in Ohio? <a href="/contact">Let's talk.</a></p>
</div>
```

Required CSS (add to `<style>` block):

```css
.contact-cta { background: #f7f8fa; border-left: 3px solid #0D1E42; padding: 20px 28px; margin: 48px 0; }
.contact-cta p { font-size: 16px; font-weight: 700; color: #0D1E42; margin: 0; }
.contact-cta a { color: #0D1E42; text-decoration: underline; }
.contact-cta a:hover { opacity: 0.7; }
```

---

### Footer requirements

Every page must include:
- Navigation links
- `fair-housing.webp` image
- Legal disclaimer text with license number
- No phone numbers anywhere on the site

---

## CSS editing rules — critical

1. **Never use a script to strip or parse CSS line-by-line.** Scripts that loop through CSS lines and skip blocks based on class name matches will cascade-delete adjacent rules. Always use exact string replacement on a known string.
2. **Before editing any CSS, print the full current `<style>` block** and confirm you can see every rule you intend to touch.
3. **When adding new CSS rules**, inject them at a specific known anchor point using exact string replacement (e.g., replace `.back-link {` with `[new rule]\n.back-link {`).
4. **Never assume a class name is present** in a file's CSS — always check first.

---

### Rules Jasson has set — permanent

- NEVER ask Jasson to run a terminal command
- NEVER use cute slogans, taglines, or clever phrases
- NEVER tell Jasson you cannot deploy — always deploy via Netlify CLI above
- ALWAYS verify every page returns 200 after deploy
- GitHub token: ask Jasson at the start of each session if not already provided
- Jasson is a solo creator — always "I" not "we" in any content
- No phone numbers on any page
- REALTOR® must always be capitalized with ® symbol, linked to https://www.nar.realtor/ when used inline in article text
