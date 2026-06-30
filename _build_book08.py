# -*- coding: utf-8 -*-
"""Build Book 08 — Broadcast & On-Air (NEW, fully authored)."""
import _bookgen as bg

COVER = '''
  <section id="cover" class="cover">
    <div class="bg-photo" style="background-image: linear-gradient(180deg, rgba(1,14,33,.35), rgba(1,14,33,.80)), url('./images/photos/generated/b08_hero.png');"></div>
    <div class="bg-grad"></div>
    <div class="pad">
      <span class="pill yellow-pill">Book 08 · Broadcast &amp; On-Air</span>
      <div class="cover-logo" aria-label="TOD by beIN"><span class="tod-logo"><svg><use href="#tod-by-bein"/></svg></span></div>
      <h1 style="font-size: clamp(40px,7vw,96px); font-weight:800; letter-spacing:-.02em; margin:18px 0 0; line-height:1;">Broadcast &amp; On-Air.</h1>
      <p class="sub">The brand at full-screen, in front of millions, live. Idents, score bugs, lower thirds, studio branding, and broadcast-safe specs — every frame reads as TOD by beIN, in any market, in two languages.</p>
      <div class="signature"><div class="label">Master Signature</div><div class="line">#1 Sports &amp; Stories</div></div>
      <div class="meta"><div class="meta-tags"><span>Idents</span><span>Score Bug</span><span>Lower Thirds</span><span>Title-Safe</span><span>Studio</span><span>Delivery</span></div><div>From beIN Media Group · brand@tod.tv</div></div>
      <div class="scroll-hint">Scroll to begin</div>
    </div>
  </section>
'''

BODY = '''
<section id="b-system" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 8.1 · The On-Air System</div>
    <h3>One package. <span class="accent-purple">Every screen, every match.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Broadcast is where the brand is biggest and least forgiving — a misaligned bug or a stripped logo is seen by millions in real time. The on-air system is a fixed kit so live operators never improvise.</p>
    <div class="grid-3" style="margin-top:40px;">
      <div class="card"><span class="number">01 · Consistent</span><h4 style="color:var(--tod-navy);">The same kit, every feed</h4><p style="margin-top:10px;">Idents, bugs, and supers come from one locked package. A viewer flipping between matches sees one brand, not many.</p></div>
      <div class="card"><span class="number">02 · Legible</span><h4 style="color:var(--tod-navy);">Readable at 3 metres</h4><p style="margin-top:10px;">Designed for living-room distance and small mobile streams alike. Type, scores, and the mark are clear on both.</p></div>
      <div class="card"><span class="number">03 · Bilingual</span><h4 style="color:var(--tod-navy);">Arabic &amp; English, equal</h4><p style="margin-top:10px;">Every graphic exists in both languages with correct RTL mechanics (Book 03). Arabic is never an afterthought.</p></div>
    </div>
    <div class="callout" style="background: rgba(255,199,44,.06); margin-top:24px;"><div class="label">How this book relates</div><p>Motion timing for everything here lives in <strong>Book 07 · 7.3</strong>. The master lockup spec is <strong>Book 02</strong>. Partner/event marks on-air follow <strong>Book 05</strong> co-brand tiers.</p></div>
  </div>
</section>

  <section class="chapter-divider">
    <div class="bg" style="background-image: url('./images/photos/generated/b08_idents.png');"></div>
    <div class="content-block">
      <div class="module-label">Book 08 · The Live Frame</div>
      <h2>Idents, bugs &amp; supers.</h2>
      <div class="tag-list">
        <span class="pill yellow-pill">Channel Ident</span>
        <span class="pill">Score Bug</span>
        <span class="pill">Name Supers</span>
      </div>
    </div>
    <div class="ch-badge"><span class="dot"></span> Section 8.2–8.4</div>
  </section>

<section id="b-idents" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 8.2 · Channel Idents &amp; Bumpers</div>
    <h3>The brand <span class="accent">arrives and signs off.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Idents and bumpers bookend every broadcast moment. They are built on the locked logo reveal (Book 07) and the sonic signature — never re-cut per producer.</p>
    <table class="data-table" style="margin-top:40px;">
      <thead><tr><th>Asset</th><th>Use</th><th>Duration</th><th>Sound</th></tr></thead>
      <tbody>
        <tr><td><strong>Channel ident</strong></td><td>Top of broadcast, return from break</td><td>5s · locked</td><td>Full sonic signature</td></tr>
        <tr><td><strong>Break bumper</strong></td><td>Into / out of ad break</td><td>4s</td><td>Bumper edit</td></tr>
        <tr><td><strong>Coming-up</strong></td><td>Next-on-TOD tease</td><td>6–10s</td><td>Bed + VO</td></tr>
        <tr><td><strong>Sign-off</strong></td><td>End of programme / window</td><td>5s · locked</td><td>Full sonic signature</td></tr>
      </tbody>
    </table>
    <div class="callout flag" style="margin-top:24px;"><div class="label">Never</div><p>No re-coloured idents, no stripped "by beIN", no local music swaps. Seasonal variants are limited to the approved Ramadan sonic (Book 07). Anything else routes through brand@tod.tv.</p></div>
  </div>
</section>

<section id="b-scorebug" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 8.3 · Score Bug &amp; Match Graphics</div>
    <h3>The score is always there. <span class="accent-purple">The action always wins.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">The score bug is the most-seen graphic TOD produces — on screen for 90 minutes straight. It is compact, fixed-position, and never covers the field of play.</p>
    <div class="grid-2" style="margin-top:40px; gap:24px;">
      <div class="card"><span class="number">Position</span><h4 style="color:var(--tod-navy);">Top-left, locked</h4><p style="margin-top:10px;">The bug anchors top-left inside title-safe (RTL: top-right). It does not move, bounce, or relocate between sports. Consistency is the feature.</p></div>
      <div class="card"><span class="number">Anatomy</span><h4 style="color:var(--tod-navy);">Teams · score · clock</h4><p style="margin-top:10px;">Team abbreviations or crests, the scoreline, and the match clock. A small TOD mono mark sits within the bug — the brand signs every score.</p></div>
      <div class="card"><span class="number">Colour</span><h4 style="color:var(--tod-navy);">Navy field, Yellow accent</h4><p style="margin-top:10px;">TOD Navy background, Off-White type, a Yellow accent on the live state. Team colours appear only as small crest chips, never as the bug field.</p></div>
      <div class="card"><span class="number">States</span><h4 style="color:var(--tod-navy);">Goal · VAR · HT · FT</h4><p style="margin-top:10px;">A defined animation per state — goal flash, VAR review, half/full-time. Each uses the Book 07 yellow wipe; none obscure the replay.</p></div>
    </div>
    <div class="inline-image" style="background-image: url('./images/photos/generated/b08_coverage.png'); margin-top:40px;">
      <div class="caption"><div><div class="lbl">On-air · Match coverage</div><div class="ttl">The bug is compact and fixed. The play is never covered.</div></div><span class="tag">Book 08</span></div>
    </div>
  </div>
</section>

<section id="b-supers" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 8.4 · Lower Thirds &amp; Name Supers</div>
    <h3>Who, what, where — <span class="accent">in and out, clean.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Name supers, stat strips, and fixture cards carry the story around the action. They follow one template family so a pundit super and a line-up card feel like one system.</p>
    <div class="grid-3" style="margin-top:40px;">
      <div class="card"><span class="number">Name super</span><h4>Person · role</h4><p style="margin-top:10px;">Lower-left, two lines: name in Alexandria 800, role beneath. Yellow underline wipe on entry. Bilingual where the talent or audience needs it.</p></div>
      <div class="card"><span class="number">Stat strip</span><h4>Possession · shots · form</h4><p style="margin-top:10px;">Lower band, Navy with Yellow data accents. Holds long enough to read twice, then exits faster than it entered (Book 07 timing).</p></div>
      <div class="card"><span class="number">Fixture / line-up</span><h4>Full-frame card</h4><p style="margin-top:10px;">Pre-match and half-time full-frame cards share the social fixture-card layout (Book 06) so on-air and social read as one brand.</p></div>
    </div>
    <div class="callout" style="background: rgba(255,199,44,.06); margin-top:24px;"><div class="label">Type &amp; safe-zone rule</div><p>All supers are Alexandria, inside title-safe margins, high contrast on a Navy plate. Never white type directly on bright pitch footage without the plate.</p></div>
  </div>
</section>

  <section class="chapter-divider">
    <div class="bg" style="background-image: url('./images/photos/generated/b08_studio.png');"></div>
    <div class="content-block">
      <div class="module-label">Book 08 · Built to Spec</div>
      <h2>Safe zones, studio &amp; delivery.</h2>
      <div class="tag-list">
        <span class="pill yellow-pill">Title-Safe</span>
        <span class="pill">Studio Branding</span>
        <span class="pill">Delivery</span>
      </div>
    </div>
    <div class="ch-badge"><span class="dot"></span> Section 8.5–8.8</div>
  </section>

<section id="b-specs" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 8.5 · Title-Safe &amp; Broadcast Specs</div>
    <h3>Designed to the <span class="accent-purple">safe zone,</span> delivered to spec.</h3>
    <p style="margin-top:18px; max-width:64ch;">Broadcast is unforgiving about edges and levels. Every graphic is built inside title-safe and delivered to a fixed technical standard so it survives any downstream feed.</p>
    <table class="data-table" style="margin-top:40px;">
      <thead><tr><th>Spec</th><th>Standard</th></tr></thead>
      <tbody>
        <tr><td><strong>Resolution</strong></td><td>1920×1080 (HD) master · 3840×2160 (UHD) where the feed supports it</td></tr>
        <tr><td><strong>Frame rate</strong></td><td>50i / 25p (PAL regions) — match the host feed</td></tr>
        <tr><td><strong>Title-safe</strong></td><td>All type &amp; logos inside the inner 90% · action-safe 93%</td></tr>
        <tr><td><strong>Bug position</strong></td><td>Top-left within title-safe (RTL: top-right), fixed offset</td></tr>
        <tr><td><strong>Colour</strong></td><td>Rec.709, broadcast-legal — no super-white or illegal saturation</td></tr>
        <tr><td><strong>Audio loudness</strong></td><td>Broadcast-safe target, sonic ducked under commentary (Book 07)</td></tr>
      </tbody>
    </table>
    <div class="callout locked" style="margin-top:24px;"><div class="label">Locked</div><p>These specs are fixed. Non-standard resolutions, frame rates, or out-of-gamut colour must be cleared with the broadcast team via <strong>brand@tod.tv</strong> before air.</p></div>
  </div>
</section>

<section id="b-studio" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 8.6 · Studio &amp; Set Branding</div>
    <h3>The set is a <span class="accent">brand surface.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Physical and virtual studios carry the brand in three dimensions — LED walls, desk marks, and lighting all read as TOD by beIN on camera.</p>
    <div class="grid-3" style="margin-top:40px;">
      <div class="card"><span class="number">LED &amp; walls</span><h4>Navy base, Yellow accent</h4><p style="margin-top:10px;">Backdrops sit on TOD Navy with controlled Yellow accents and the Happy Spectrum reserved for hero moments. Never a wall of competing colour.</p></div>
      <div class="card"><span class="number">Desk &amp; marks</span><h4>Master lockup, correct clear space</h4><p style="margin-top:10px;">On-set marks use the master lockup with full Book 02 clear space. Mono on dark, full-colour on light. No stretched or boxed logos.</p></div>
      <div class="card"><span class="number">Virtual sets</span><h4>Lit to read on camera</h4><p style="margin-top:10px;">Virtual environments match the palette and keep the mark legible under broadcast lighting. AR graphics follow Book 07 motion.</p></div>
    </div>
    <div class="callout flag" style="margin-top:24px;"><div class="label">Never</div><p>No off-brand set colours, no third-party marks on set without a cleared Book 05 tier, no logo as a repeating wallpaper texture. Set designs are approved through brand@tod.tv.</p></div>
  </div>
</section>

<section id="b-delivery" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 8.7 · Compliance &amp; Delivery</div>
    <h3>Cleared before air. <span class="accent-purple">Delivered to one standard.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Live broadcast carries rights, language, and compliance obligations. The brand stays neutral, the rights stay clean, and every asset is delivered the same way.</p>
    <div class="grid-2" style="margin-top:40px; gap:24px;">
      <div class="card"><span class="number">Compliance</span><h4 style="color:var(--tod-navy);">Neutral &amp; rights-clean</h4><p style="margin-top:10px;">On-air commentary and graphics carry no political, religious, or geopolitical commentary (Book 03). Only licensed footage and cleared marks reach air.</p></div>
      <div class="card"><span class="number">Languages</span><h4 style="color:var(--tod-navy);">Dual-feed ready</h4><p style="margin-top:10px;">Arabic and English graphic feeds are built in parallel, not translated last-minute. RTL layouts mirror correctly (Book 03), not just reverse type.</p></div>
      <div class="card"><span class="number">Delivery</span><h4 style="color:var(--tod-navy);">Fixed handover kit</h4><p style="margin-top:10px;">Graphics ship as a defined package — naming, formats, and safe-zone checks done — so any gallery or partner feed can run them unchanged.</p></div>
      <div class="card"><span class="number">Governance</span><h4 style="color:var(--tod-navy);">One point of entry</h4><p style="margin-top:10px;">New on-air templates, partner integrations, and exceptions are approved through brand@tod.tv with the broadcast team before they reach a live feed.</p></div>
    </div>
    <div class="callout locked" style="margin-top:24px;"><div class="label">Single point of entry</div><p>Every on-air exception — a new bug state, a partner integration, a non-standard ident — routes through <strong>brand@tod.tv</strong>. Live is the least forgiving surface; nothing improvised reaches air.</p></div>
  </div>
</section>
'''

THIS_LINKS = '''  <a class="nav-item" href="#b-system" data-close><span class="num">8.1</span> The On-Air System</a>
  <a class="nav-item" href="#b-idents" data-close><span class="num">8.2</span> Idents &amp; Bumpers</a>
  <a class="nav-item" href="#b-scorebug" data-close><span class="num">8.3</span> Score Bug &amp; Graphics</a>
  <a class="nav-item" href="#b-supers" data-close><span class="num">8.4</span> Lower Thirds &amp; Supers</a>
  <a class="nav-item" href="#b-specs" data-close><span class="num">8.5</span> Title-Safe &amp; Specs</a>
  <a class="nav-item" href="#b-studio" data-close><span class="num">8.6</span> Studio Branding</a>
  <a class="nav-item" href="#b-delivery" data-close><span class="num">8.7</span> Compliance &amp; Delivery</a>
'''

bg.build(
    title='TOD by beIN — Book 08 · Broadcast &amp; On-Air',
    active_idx='08',
    this_links=THIS_LINKS,
    cover=COVER,
    body=BODY,
    out='Book08_Broadcast_OnAir.html',
    topbar_label='<strong>Book 08</strong> · Broadcast &amp; On-Air · Locked Reference',
)
