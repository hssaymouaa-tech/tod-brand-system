"""Shared builder for TOD standalone brand books.
Assembles each book from the master index.html shell (head/CSS, logo sprite,
top bar, footer/scripts) so every book stays visually identical, then injects a
cross-book drawer + per-book cover + body.
"""
import re

SRC = open('index.html', encoding='utf-8').read().splitlines(keepends=True)

def seg(a, b):
    return ''.join(SRC[a-1:b])  # 1-based inclusive

HEAD      = seg(1, 1595)        # <!doctype> .. </head>
SPRITE_TB = seg(1598, 1663)     # inline logo sprite + top bar
# Footer (footer markup + drawer script + </body></html>) located by marker so it
# survives any change in index.html's length. Falls back to the old fixed slice.
def _footer():
    txt = ''.join(SRC)
    marker = '<!-- ============ FOOTER ============ -->'
    i = txt.find(marker)
    if i == -1:
        return seg(3485, 3564)
    return txt[i:]
FOOTER    = _footer()

BOOKS = [
    ('01', 'Brand Book',          'index.html'),
    ('02', 'Logo System',         'Book02_Logo_System.html'),
    ('03', 'Voice &amp; Language','Book03_Voice_Language.html'),
    ('04', 'Design System',       'Book04_Design_System.html'),
    ('05', 'Co-Brand Playbook',   'Book05_CoBrand_Playbook.html'),
    ('06', 'Social &amp; Live',   'Book06_Social_Live.html'),
    ('07', 'Sonic &amp; Motion',  'Book07_Sonic_Motion.html'),
    ('08', 'Broadcast &amp; On-Air','Book08_Broadcast_OnAir.html'),
    ('09', 'Brand Operations',    'Book09_Brand_Operations.html'),
    ('10', 'PR &amp; Media Kit',  'Book10_PR_Media_Kit.html'),
    ('11', 'TOD360 Features',     'Book11_TOD360_Features.html'),
]

def build(title, active_idx, this_links, cover, body, out, topbar_label):
    h = HEAD.replace(
        '<title>TOD by beIN — Brand System v2.0 · #1 Sports & Stories</title>',
        f'<title>{title}</title>')
    nav = ''
    for n, name, href in BOOKS:
        style = ' style="color: var(--tod-yellow);"' if n == active_idx else ''
        nav += f'  <a class="nav-item" href="{href}"{style}><span class="num">{n}</span> {name}</a>\n'
    drawer = f'''
<div class="drawer-backdrop" id="drawerBackdrop"></div>
<nav class="drawer" id="drawer" aria-hidden="true">
  <div class="drawer-head">
    <a href="index.html" class="tod-logo"><svg><use href="#tod-by-bein"/></svg></a>
    <button class="close-x" id="closeBtn" aria-label="Close menu">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>
    </button>
  </div>
  <div class="nav-section">Brand System · 11 Books</div>
{nav}  <div class="nav-section">This Book</div>
{this_links}
  <div class="sig-line"><div class="label">Master Signature</div><div class="line">#1 Sports &amp; Stories</div></div>
  <p class="nav-meta"><strong>LOCKED v2.0</strong><br>Single point of entry: <strong>brand@tod.tv</strong></p>
</nav>
'''
    tb = SPRITE_TB.replace(
        '<div class="topbar-title"><strong>Brand System</strong> · v2.0 · Locked Reference</div>',
        f'<div class="topbar-title">{topbar_label}</div>')
    doc = h + '<body>\n' + tb + drawer + '\n<main>\n' + cover + '\n' + body + '\n' + FOOTER
    open(out, 'w', encoding='utf-8').write(doc)
    print('wrote', out, len(doc), 'bytes')
