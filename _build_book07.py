# -*- coding: utf-8 -*-
"""Build Book 07 — Sonic & Motion (lifts EX-03 Motion + EX-04 Sonic, expands)."""
import _bookgen as bg

COVER = '''
  <section id="cover" class="cover">
    <div class="bg-photo" style="background-image: linear-gradient(180deg, rgba(1,14,33,.35), rgba(1,14,33,.80)), url('./images/photos/generated/b07_hero.png');"></div>
    <div class="bg-grad"></div>
    <div class="pad">
      <span class="pill yellow-pill">Book 07 · Sonic &amp; Motion</span>
      <div class="cover-logo" aria-label="TOD by beIN"><span class="tod-logo"><svg><use href="#tod-by-bein"/></svg></span></div>
      <h1 style="font-size: clamp(40px,7vw,96px); font-weight:800; letter-spacing:-.02em; margin:18px 0 0; line-height:1;">Sonic &amp; Motion.</h1>
      <p class="sub">How the brand moves and how it sounds. Motion serves clarity, never decoration. TOD Sonic is the brand you can hear in the dark — recognisable before a single frame loads.</p>
      <div class="signature"><div class="label">Master Signature</div><div class="line">#1 Sports &amp; Stories</div></div>
      <div class="meta"><div class="meta-tags"><span>Principles</span><span>Easing</span><span>Idents</span><span>Lower Thirds</span><span>Sonic</span><span>Mix</span></div><div>From beIN Media Group · brand@tod.tv</div></div>
      <div class="scroll-hint">Scroll to begin</div>
    </div>
  </section>
'''

BODY = '''
<section id="m-principles" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 7.1 · Motion Principles</div>
    <h3>Motion serves clarity, <span class="accent-purple">never decoration.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">If a treatment delays the viewer reaching content, it is wrong. TOD motion is fast, purposeful, and premium — the same discipline on a 5-second ident as on a tap ripple.</p>
    <div class="grid-3" style="margin-top:40px;">
      <div class="card"><span class="number">01 · Purposeful</span><h4 style="color:var(--tod-navy);">Every move means something</h4><p style="margin-top:10px;">Motion guides the eye, signals state, or rewards an action. If it does none of those, cut it.</p></div>
      <div class="card"><span class="number">02 · Fast</span><h4 style="color:var(--tod-navy);">UI motion ≤ 300ms</h4><p style="margin-top:10px;">Interface transitions stay under 300ms. Skeletons over spinners. The viewer reaches content first, always.</p></div>
      <div class="card"><span class="number">03 · Premium</span><h4 style="color:var(--tod-navy);">Confident, never frantic</h4><p style="margin-top:10px;">Smooth eases, no bounce gimmicks, no rapid flashing. The motion feels as considered as the wordmark.</p></div>
    </div>
    <h4 style="color:var(--tod-deep-purple); margin:40px 0 18px;">Easing — the three curves</h4>
    <div class="ease-grid" style="grid-template-columns: repeat(3,1fr);">
      <div class="ease-card">
        <svg viewBox="0 0 200 60" fill="none" stroke="var(--tod-deep-purple)" stroke-width="2.5"><path d="M4 56 C 60 56, 80 4, 196 4"/></svg>
        <div class="nm" style="color:var(--tod-navy);">Ease-out</div>
        <div class="use">Entrances — elements arriving</div>
      </div>
      <div class="ease-card">
        <svg viewBox="0 0 200 60" fill="none" stroke="var(--tod-deep-purple)" stroke-width="2.5"><path d="M4 56 C 70 56, 130 4, 196 4"/></svg>
        <div class="nm" style="color:var(--tod-navy);">Ease-in-out</div>
        <div class="use">Transitions — moving between states</div>
      </div>
      <div class="ease-card">
        <svg viewBox="0 0 200 60" fill="none" stroke="var(--tod-deep-purple)" stroke-width="2.5"><path d="M4 56 C 130 56, 150 4, 196 4"/></svg>
        <div class="nm" style="color:var(--tod-navy);">Ease-in</div>
        <div class="use">Exits — elements leaving</div>
      </div>
    </div>
  </div>
</section>

  <section class="chapter-divider">
    <div class="bg" style="background-image: url('./images/photos/generated/b07_idents.png');"></div>
    <div class="content-block">
      <div class="module-label">Book 07 · Brand in Motion</div>
      <h2>Idents, timing &amp; graphics.</h2>
      <div class="tag-list">
        <span class="pill yellow-pill">Logo Reveal</span>
        <span class="pill">Motion Specs</span>
        <span class="pill">Lower Thirds</span>
      </div>
    </div>
    <div class="ch-badge"><span class="dot"></span> Section 7.2–7.3</div>
  </section>

<section id="m-ident" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 7.2 · Logo Animation &amp; Timing</div>
    <h3>The reveal that <span class="accent">opens every session.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">The master splash animation is locked: the logo reveal that opens every TOD session and closes brand-level moments. It ends on the master lockup, holds for legibility, and pairs with the sonic signature.</p>
    <div style="display:grid; grid-template-columns: 1fr 1fr; gap:36px; align-items:start; margin-top:40px;">
      <div>
        <h4 style="color:var(--tod-yellow); margin-bottom:18px;">Master Logo Animation</h4>
        <div class="reveal-stage" style="padding:0; overflow:hidden; aspect-ratio:16/9; min-height:0;">
          <video src="./images/motion/logo-animation.mp4" autoplay muted loop playsinline poster="./images/TODbybeIN-01.svg" style="width:100%; height:100%; object-fit:contain; border-radius:18px; background:var(--tod-navy);"></video>
        </div>
        <p style="color:rgba(244,246,250,.7); font-size:13px; margin-top:14px; line-height:1.6;">Ends on the master lockup, holds for legibility, pairs with the sonic signature. Source: <strong style="color:var(--tod-yellow);">Motion / Animated Templates</strong>.</p>
      </div>
      <div>
        <h4 style="color:var(--tod-yellow); margin-bottom:18px;">Motion Specs</h4>
        <div style="border-top:1px solid rgba(255,255,255,.08);">
          <div class="motion-row"><span class="ev" style="color:var(--tod-off-white);">Tap feedback</span><div class="track"><div class="bar" style="--w: 12%;"></div></div><span class="dur">120ms · ease-out</span></div>
          <div class="motion-row"><span class="ev" style="color:var(--tod-off-white);">Page transition</span><div class="track"><div class="bar" style="--w: 24%;"></div></div><span class="dur">240ms · ease-in-out</span></div>
          <div class="motion-row"><span class="ev" style="color:var(--tod-off-white);">Sheet / modal entry</span><div class="track"><div class="bar" style="--w: 28%;"></div></div><span class="dur">280ms · ease-out</span></div>
          <div class="motion-row"><span class="ev" style="color:var(--tod-off-white);">Sheet / modal exit</span><div class="track"><div class="bar" style="--w: 20%;"></div></div><span class="dur">200ms · ease-in</span></div>
          <div class="motion-row"><span class="ev" style="color:var(--tod-off-white);">Bumper / ident</span><div class="track"><div class="bar" style="--w: 50%;"></div></div><span class="dur">5s · locked</span></div>
          <div class="motion-row"><span class="ev" style="color:var(--tod-off-white);">Logo reveal</span><div class="track"><div class="bar" style="--w: 38%;"></div></div><span class="dur">3,800ms · locked</span></div>
        </div>
        <p style="color:rgba(244,246,250,.6); font-size:13px; margin-top:16px;"><strong style="color:var(--tod-yellow);">Default rule:</strong> UI motion ≤ 300ms. Source: <strong>Motion/</strong> — idents, lower thirds, transitions, TVC 15s/30s.</p>
      </div>
    </div>
  </div>
</section>

<section id="m-graphics" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 7.3 · Lower Thirds &amp; On-Screen Graphics</div>
    <h3>Information arrives <span class="accent-purple">cleanly,</span> then gets out of the way.</h3>
    <p style="margin-top:18px; max-width:64ch;">Names, scores, and stats animate in fast and legibly, never obscuring the action. The full broadcast graphics package lives in Book 08 — these are the motion rules behind it.</p>
    <div class="grid-2" style="margin-top:40px; gap:24px;">
      <div class="card"><span class="number">Entry</span><h4 style="color:var(--tod-navy);">Wipe on the yellow</h4><p style="margin-top:10px;">Lower thirds enter with a left-to-right yellow underline wipe (right-to-left in Arabic / RTL), ease-out, 280ms. The bar draws, the text settles, the eye stays on the play.</p></div>
      <div class="card"><span class="number">Hold</span><h4 style="color:var(--tod-navy);">Long enough to read, twice</h4><p style="margin-top:10px;">Hold any text graphic for the time it takes to read it comfortably twice — bilingual graphics hold longer. Never strobe stats on and off.</p></div>
      <div class="card"><span class="number">Exit</span><h4 style="color:var(--tod-navy);">Ease-in, faster than entry</h4><p style="margin-top:10px;">Graphics leave on ease-in at ~200ms — quicker out than in. The departure is quiet; nothing animates the viewer away from the moment.</p></div>
      <div class="card"><span class="number">Type</span><h4 style="color:var(--tod-navy);">Alexandria, safe-zone bound</h4><p style="margin-top:10px;">All on-screen type is Alexandria, inside broadcast title-safe margins. Bilingual lockups follow Book 03 — Arabic is never an afterthought.</p></div>
    </div>
    <div class="callout" style="background: rgba(255,199,44,.06); margin-top:24px;"><div class="label">Cross-reference</div><p>Score bugs, fixture cards, and the full on-air package spec live in <strong>Book 08 · Broadcast &amp; On-Air</strong>. This section governs only how they move.</p></div>
  </div>
</section>

  <section class="chapter-divider">
    <div class="bg" style="background-image: url('./images/photos/generated/b07_sonic.png');"></div>
    <div class="content-block">
      <div class="module-label">Book 07 · The Brand You Can Hear</div>
      <h2>TOD Sonic.</h2>
      <div class="tag-list">
        <span class="pill yellow-pill">One Motif</span>
        <span class="pill">Ramadan Variant</span>
        <span class="pill">Duration Edits</span>
      </div>
    </div>
    <div class="ch-badge"><span class="dot"></span> Section 7.4–7.6</div>
  </section>

<section id="m-sonic" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 7.4 · Sonic Identity</div>
    <h3>A brand you can <span class="accent">hear in the dark.</span></h3>
    <p style="margin-top:18px; max-width:64ch;"><span style="color:var(--tod-yellow);">TOD Sonic</span> is the signature music system for tod.tv — recognisable before a single frame loads: on the splash, the goal, the notification.</p>
    <div style="display:inline-flex; align-items:center; gap:10px; padding:8px 16px; border-radius:999px; background:rgba(255,199,44,.12); border:1px solid rgba(255,199,44,.3); margin:28px 0 24px;">
      <span style="width:8px; height:8px; border-radius:50%; background:var(--tod-yellow); animation:wave 1.4s ease-in-out infinite;"></span>
      <span style="font-size:11px; letter-spacing:.18em; text-transform:uppercase; color:var(--tod-yellow); font-weight:600;">Work in Progress · In Production</span>
    </div>
    <div class="reveal-stage" style="min-height:180px; background: radial-gradient(ellipse 70% 90% at 50% 50%, rgba(255,199,44,.14), transparent 65%), var(--tod-deep-navy);">
      <div class="waveform">
        <span style="animation-delay:0s"></span><span style="animation-delay:.1s"></span><span style="animation-delay:.25s"></span><span style="animation-delay:.15s"></span><span style="animation-delay:.35s"></span><span style="animation-delay:.2s"></span><span style="animation-delay:.4s"></span><span style="animation-delay:.1s"></span><span style="animation-delay:.3s"></span><span style="animation-delay:.05s"></span><span style="animation-delay:.25s"></span><span style="animation-delay:.15s"></span><span style="animation-delay:.35s"></span><span style="animation-delay:.2s"></span><span style="animation-delay:.1s"></span><span style="animation-delay:.3s"></span><span style="animation-delay:.15s"></span><span style="animation-delay:.4s"></span><span style="animation-delay:.05s"></span><span style="animation-delay:.25s"></span>
      </div>
    </div>
    <h4 style="color:var(--tod-yellow); margin:36px 0 14px;">The Sonic System</h4>
    <div style="display:grid; grid-template-columns: repeat(3,1fr); gap:16px;">
      <div class="card" style="background:rgba(255,255,255,.04); border-color:rgba(255,199,44,.25);"><span class="number" style="color:var(--tod-yellow);">01 · Master</span><h4 style="color:var(--tod-off-white);">Main Sonic Signature</h4><p style="margin-top:10px; color:rgba(244,246,250,.7);">The original sonic identity — the signature music for tod.tv. The master from which every other cut is derived. The audio equivalent of the wordmark.</p></div>
      <div class="card" style="background:rgba(255,255,255,.04); border-color:rgba(255,255,255,.08);"><span class="number" style="color:var(--tod-yellow);">02 · Seasonal</span><h4 style="color:var(--tod-off-white);">Ramadan Signature</h4><p style="margin-top:10px; color:rgba(244,246,250,.7);">A Ramadan-themed adaptation — same core motif, re-voiced for the season's mood. The only approved seasonal variant.</p></div>
      <div class="card" style="background:rgba(255,255,255,.04); border-color:rgba(255,255,255,.08);"><span class="number" style="color:var(--tod-yellow);">03 · Edits</span><h4 style="color:var(--tod-off-white);">Background Music Edits</h4><p style="margin-top:10px; color:rgba(244,246,250,.7);">Duration-matched cuts of the signature for every surface — promos, bumpers, social, and long-form beds.</p></div>
    </div>
    <div class="callout flag" style="margin-top:24px;"><div class="label">Flag · Work in Progress</div><p>TOD Sonic is in active production. The system structure — main signature, Ramadan version, and the duration edits — is locked; final masters are being composed. Source: <strong>Music &amp; Sonic/</strong>. Coordinate via brand@tod.tv.</p></div>
  </div>
</section>

<section id="m-durations" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 7.5 · Durations &amp; Principles</div>
    <h3>One motif. <span class="accent-purple">Six lengths.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Every surface gets a duration-matched cut of the same signature — heard once, remembered. Editors pick a length, never re-score.</p>
    <div style="display:grid; grid-template-columns: repeat(6,1fr); gap:12px; margin-top:40px;">
      <div style="text-align:center; padding:20px 10px; border-radius:12px; background:rgba(1,14,33,.04); border:1px solid rgba(1,14,33,.08);"><div style="font-family:'Alexandria',sans-serif; font-size:26px; font-weight:800; color:var(--tod-deep-purple);">2s</div><div style="font-size:10px; letter-spacing:.12em; text-transform:uppercase; color:rgba(1,14,33,.55); margin-top:6px;">Sting</div></div>
      <div style="text-align:center; padding:20px 10px; border-radius:12px; background:rgba(1,14,33,.04); border:1px solid rgba(1,14,33,.08);"><div style="font-family:'Alexandria',sans-serif; font-size:26px; font-weight:800; color:var(--tod-deep-purple);">4s</div><div style="font-size:10px; letter-spacing:.12em; text-transform:uppercase; color:rgba(1,14,33,.55); margin-top:6px;">Bumper</div></div>
      <div style="text-align:center; padding:20px 10px; border-radius:12px; background:rgba(1,14,33,.04); border:1px solid rgba(1,14,33,.08);"><div style="font-family:'Alexandria',sans-serif; font-size:26px; font-weight:800; color:var(--tod-deep-purple);">6s</div><div style="font-size:10px; letter-spacing:.12em; text-transform:uppercase; color:rgba(1,14,33,.55); margin-top:6px;">Ident</div></div>
      <div style="text-align:center; padding:20px 10px; border-radius:12px; background:rgba(1,14,33,.04); border:1px solid rgba(1,14,33,.08);"><div style="font-family:'Alexandria',sans-serif; font-size:26px; font-weight:800; color:var(--tod-deep-purple);">15s</div><div style="font-size:10px; letter-spacing:.12em; text-transform:uppercase; color:rgba(1,14,33,.55); margin-top:6px;">Promo</div></div>
      <div style="text-align:center; padding:20px 10px; border-radius:12px; background:rgba(1,14,33,.04); border:1px solid rgba(1,14,33,.08);"><div style="font-family:'Alexandria',sans-serif; font-size:26px; font-weight:800; color:var(--tod-deep-purple);">30s</div><div style="font-size:10px; letter-spacing:.12em; text-transform:uppercase; color:rgba(1,14,33,.55); margin-top:6px;">Spot</div></div>
      <div style="text-align:center; padding:20px 10px; border-radius:12px; background:rgba(1,14,33,.04); border:1px solid rgba(1,14,33,.08);"><div style="font-family:'Alexandria',sans-serif; font-size:26px; font-weight:800; color:var(--tod-deep-purple);">45s</div><div style="font-size:10px; letter-spacing:.12em; text-transform:uppercase; color:rgba(1,14,33,.55); margin-top:6px;">Long bed</div></div>
    </div>
    <table class="data-table" style="margin-top:36px;">
      <thead><tr><th>Principle</th><th>Rule</th></tr></thead>
      <tbody>
        <tr><td><strong>One motif</strong></td><td>Every edit and the Ramadan version share the main signature's core motif — heard once, remembered.</td></tr>
        <tr><td><strong>Premium</strong></td><td>Warm, cinematic, never cheap or synthetic. Mixed for phone speakers and home cinema alike.</td></tr>
        <tr><td><strong>Restrained</strong></td><td>Sound enhances the moment, never competes with the content or commentary.</td></tr>
        <tr><td><strong>Bilingual-neutral</strong></td><td>No language, no lyrics — works identically in every market.</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section id="m-mix" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 7.6 · Mix &amp; Usage Governance</div>
    <h3>The sound supports the moment. <span class="accent">It never owns it.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Where and how the sonic plays is as governed as the music itself — so the brand sounds the same on a phone in a noisy café and a home cinema.</p>
    <div class="grid-3" style="margin-top:40px;">
      <div class="card"><span class="number">Mix</span><h4>Duck under voice</h4><p style="margin-top:10px;">Music and stings always duck beneath commentary, dialogue, and notifications. The sonic frames the content; it never fights it.</p></div>
      <div class="card"><span class="number">Loudness</span><h4>Broadcast-safe levels</h4><p style="margin-top:10px;">Deliver to platform loudness standards (broadcast and streaming). No surprise jumps between an ident and the programme.</p></div>
      <div class="card"><span class="number">Placement</span><h4>Brand moments only</h4><p style="margin-top:10px;">The signature marks brand moments — opens, goals, key reveals, sign-offs. It is not background wallpaper for every clip.</p></div>
    </div>
    <div class="callout locked" style="margin-top:24px;"><div class="label">Locked &amp; routed</div><p>The sonic system structure is locked. New cuts, third-party music, or any non-standard use must be cleared through <strong>brand@tod.tv</strong> with the Music &amp; Sonic team — for both brand consistency and rights.</p></div>
  </div>
</section>
'''

THIS_LINKS = '''  <a class="nav-item" href="#m-principles" data-close><span class="num">7.1</span> Motion Principles</a>
  <a class="nav-item" href="#m-ident" data-close><span class="num">7.2</span> Logo Animation &amp; Timing</a>
  <a class="nav-item" href="#m-graphics" data-close><span class="num">7.3</span> Lower Thirds</a>
  <a class="nav-item" href="#m-sonic" data-close><span class="num">7.4</span> Sonic Identity</a>
  <a class="nav-item" href="#m-durations" data-close><span class="num">7.5</span> Durations &amp; Principles</a>
  <a class="nav-item" href="#m-mix" data-close><span class="num">7.6</span> Mix &amp; Governance</a>
'''

bg.build(
    title='TOD by beIN — Book 07 · Sonic &amp; Motion',
    active_idx='07',
    this_links=THIS_LINKS,
    cover=COVER,
    body=BODY,
    out='Book07_Sonic_Motion.html',
    topbar_label='<strong>Book 07</strong> · Sonic &amp; Motion · Locked Reference',
)
