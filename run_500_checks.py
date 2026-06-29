import os, re, sys
from pathlib import Path

SITE = Path('/sessions/confident-festive-thompson/mnt/Desktop/jassonfarrier-site')

PAGES = [
    'index.html','bio.html','blog.html','contact.html','free.html',
    'housing-market-updates.html','privacy.html',
    'blog-housing-market-splitting-in-two.html',
    'blog-housing-slowdown-2026.html','blog-ohio-dec-2025.html',
    'blog-ohio-feb-2026.html','blog-ohio-spring-2026.html',
    'blog-property-tax-sep-2025.html'
]

BLOG_PAGES = [p for p in PAGES if p.startswith('blog-')]
ALL_PAGES  = PAGES

fails = []
passes = 0

def chk(label, ok, detail=''):
    global passes
    if ok:
        passes += 1
    else:
        fails.append(f'FAIL [{label}]{" — "+detail if detail else ""}')

def read(p):
    f = SITE / p
    return f.read_text(errors='replace') if f.exists() else ''

# ── CATEGORY 1: DOCTYPE & HEAD (13 pages × 5 = 65 checks) ──
for p in ALL_PAGES:
    h = read(p)
    chk(f'{p} DOCTYPE',           '<!DOCTYPE html>' in h)
    chk(f'{p} charset UTF-8',     'charset="UTF-8"' in h)
    chk(f'{p} viewport meta',     'name="viewport"' in h)
    chk(f'{p} Montserrat font',   'Montserrat' in h)
    chk(f'{p} title tag',         bool(re.search(r'<title>[^<]+</title>', h)))

# ── CATEGORY 2: AGENT BAR (13 pages × 5 = 65 checks) ──
for p in ALL_PAGES:
    h = read(p)
    chk(f'{p} agent-bar class',           'class="agent-bar"' in h)
    chk(f'{p} agent-bar Kiger Realty',    'Kiger Realty' in h)
    chk(f'{p} agent-bar license',         '2018004483' in h)
    chk(f'{p} agent-bar phone',           '614-699-3007' in h)
    chk(f'{p} agent-bar Jasson Farrier',  'Jasson Farrier' in h)

# ── CATEGORY 3: NAV (13 pages × 6 = 78 checks) ──
for p in ALL_PAGES:
    h = read(p)
    chk(f'{p} nav tag',              '<nav' in h)
    chk(f'{p} nav-logo class',       'class="nav-logo"' in h)
    chk(f'{p} nav logo span gray',   'Jasson <span>Farrier</span>' in h)
    chk(f'{p} nav Market Updates',   'href="/housing-market-updates"' in h)
    chk(f'{p} nav Bio link',         'href="/bio"' in h)
    chk(f'{p} nav Free Guide CTA',   'nav-cta' in h)

# ── CATEGORY 4: HERO / PAGE HEADER (13 pages × 3 = 39 checks) ──
for p in ALL_PAGES:
    h = read(p)
    chk(f'{p} has h1',               bool(re.search(r'<h1', h)))
    chk(f'{p} navy hero/header bg',  '--navy' in h or 'background:var(--navy)' in h or "background: var(--navy)" in h)
    chk(f'{p} hero not centered (market/blog)',
        True if p not in ['housing-market-updates.html','blog.html']
        else 'text-align: center' not in re.search(r'\.hero\s*\{[^}]+\}', h, re.S).group(0)
             if re.search(r'\.hero\s*\{[^}]+\}', h, re.S) else False,
        p)

# ── CATEGORY 5: FOOTER (13 pages × 5 = 65 checks) ──
for p in ALL_PAGES:
    h = read(p)
    chk(f'{p} footer tag',           '<footer' in h)
    chk(f'{p} footer-logo',          'footer-logo' in h)
    chk(f'{p} footer Jasson Farrier','footer' in h and 'Jasson' in h)
    chk(f'{p} footer-compliance',    'footer-compliance' in h)
    chk(f'{p} footer license',       '#2018004483' in h)

# ── CATEGORY 6: CSS VARIABLES (13 pages × 3 = 39 checks) ──
for p in ALL_PAGES:
    h = read(p)
    chk(f'{p} --navy var',   '--navy:' in h or '--navy: ' in h)
    chk(f'{p} --gray var',   '--gray:' in h or '--gray: ' in h)
    chk(f'{p} --dark var',   '--dark:' in h or '--dark: ' in h)

# ── CATEGORY 7: RESPONSIVE / MOBILE (13 pages × 3 = 39 checks) ──
for p in ALL_PAGES:
    h = read(p)
    chk(f'{p} media query',     '@media' in h)
    chk(f'{p} 768px breakpoint','768px' in h)
    chk(f'{p} nav-links hidden mobile', 'display:none' in h.replace(' ','') or 'display: none' in h)

# ── CATEGORY 8: BLOG LIST / MARKET UPDATES CONSISTENCY ──
for p in ['blog.html','housing-market-updates.html']:
    h = read(p)
    chk(f'{p} uses blog-list class',  'class="blog-list"' in h)
    chk(f'{p} uses post class',       'class="post"' in h)
    chk(f'{p} uses post-date class',  'class="post-date"' in h)
    chk(f'{p} uses read-more class',  'class="read-more"' in h)
    chk(f'{p} no inline style articles', 'style="border-bottom' not in h)
    chk(f'{p} hero padding 60px',    'padding:60px 40px' in h.replace(' ','') or 'padding: 60px 40px' in h)
    chk(f'{p} hero not text-center', 'text-align: center' not in re.search(r'\.hero\s*\{[^}]+\}', h, re.S).group(0)
        if re.search(r'\.hero\s*\{[^}]+\}', h, re.S) else True)

# ── CATEGORY 9: BLOG POSTS — 6 REAL SLUGS LINKED ──
REAL_SLUGS = [
    '/blog-ohio-spring-2026','/blog-housing-market-splitting-in-two',
    '/blog-ohio-feb-2026','/blog-housing-slowdown-2026',
    '/blog-ohio-dec-2025','/blog-property-tax-sep-2025'
]
for slug in REAL_SLUGS:
    for p in ['blog.html','housing-market-updates.html']:
        h = read(p)
        chk(f'{p} links to {slug}', f'href="{slug}"' in h)

# ── CATEGORY 10: OLD DELETED SLUGS NOT IN INDEX PAGES ──
OLD_SLUGS = [
    'blog-ohio-home-prices-skyrocketing','blog-central-ohio-home-prices-all-time-high',
    'blog-shocking-reality-central-ohio-homebuyers','blog-686-home-listings-vanish'
]
for slug in OLD_SLUGS:
    for p in ['blog.html','housing-market-updates.html']:
        h = read(p)
        chk(f'{p} no dead slug {slug}', slug not in h)

# ── CATEGORY 11: INDIVIDUAL BLOG POSTS — DETAILED ──
for p in BLOG_PAGES:
    h = read(p)
    chk(f'{p} Back link present',        'Back to Market Updates' in h or 'housing-market-updates' in h)
    chk(f'{p} no Squarespace scripts',   not bool(re.search(r'<script[^>]*squarespace', h, re.I)))
    chk(f'{p} no YUI scripts',           not bool(re.search(r'<script[^>]*yui', h, re.I)))
    chk(f'{p} no external CDN other than fonts+kit',
        not bool(re.search(r'src="https?://(?!fonts\.googleapis|app\.kit\.com|farrier-crm)', h)))
    chk(f'{p} article h1 or h2 exists',  bool(re.search(r'<h[12]', h)))
    chk(f'{p} no empty href',            'href=""' not in h)
    chk(f'{p} no topbar class (old)',    'class="topbar"' not in h)

# ── CATEGORY 12: FORMS ──
for p in ['free.html','housing-market-updates.html','contact.html']:
    h = read(p)
    chk(f'{p} Kit form action', 'app.kit.com/forms' in h or 'kit.com' in h or 'handleFreeGuide' in h or 'handleMU' in h or 'handleContact' in h or 'submit-contact' in h)

chk('free.html Kit form ID 9195650', '9195650' in read('free.html'))
chk('free.html honeypot field', 'fg-hp' in read('free.html'))
chk('free.html thank-you div', 'fg-thankyou' in read('free.html'))

# ── CATEGORY 13: FREE.HTML SPECIFICS ──
fh = read('free.html')
chk('free.html agent-bar CSS exists',   '.agent-bar {' in fh or '.agent-bar{' in fh)
chk('free.html nav-links CSS exists',   '.nav-links {' in fh or '.nav-links{' in fh)
chk('free.html nav-cta CSS exists',     '.nav-cta {' in fh or '.nav-cta{' in fh)
chk('free.html nav sticky',             'sticky' in fh)
chk('free.html What-Inside removed',    "What's Inside" not in fh)
chk('free.html all 4 nav links',        all(x in fh for x in ['href="/housing-market-updates"','href="/bio"','href="/contact"','href="/free"']))

# ── CATEGORY 14: BIO.HTML ──
bh = read('bio.html')
chk('bio.html hero-body paragraph removed', 'Ohio Realtor. Real estate investor. The guy' not in bh)
chk('bio.html photo present',               'hero-img' in bh)
chk('bio.html creds section',               'class="creds"' in bh)
chk('bio.html contact-box',                 'contact-box' in bh)
chk('bio.html 614-699-3007 phone link',     'tel:6146993007' in bh)

# ── CATEGORY 15: HOUSING-MARKET-UPDATES.HTML ──
mh = read('housing-market-updates.html')
chk('MU page no text-align:center on hero',
    'text-align: center' not in re.search(r'\.hero\s*\{[^}]+\}', mh, re.S).group(0)
    if re.search(r'\.hero\s*\{[^}]+\}', mh, re.S) else True)
chk('MU page no orphan JS (mu-form)',        'mu-form' not in mh)
chk('MU page no "Recent Market Reports" header', 'Recent Market Reports' not in mh)
chk('MU page hero padding 60px',             'padding:60px 40px' in mh.replace(' ','') or 'padding: 60px 40px' in mh)

# ── CATEGORY 16: INDEX.HTML ──
ih = read('index.html')
chk('index.html has hero grid',     'grid-template-columns' in ih)
chk('index.html has CTA buttons',   'btn-primary' in ih)
chk('index.html free guide link',   'href="/free"' in ih)
chk('index.html market updates link','href="/housing-market-updates"' in ih)

# ── FINAL REPORT ──
total = passes + len(fails)
print(f'\n{"="*60}')
print(f'RESULTS: {passes}/{total} passed  |  {len(fails)} failed')
print(f'{"="*60}')
if fails:
    print('\nFAILURES:')
    for f in fails:
        print(f'  {f}')
else:
    print('\nAll checks passed!')
