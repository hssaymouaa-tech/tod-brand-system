# -*- coding: utf-8 -*-
"""Build Book 10 — PR & Media Kit (NEW; lifts approved boilerplate + locked lines)."""
import _bookgen as bg

COVER = '''
  <section id="cover" class="cover">
    <div class="bg-photo" style="background-image: linear-gradient(180deg, rgba(1,14,33,.35), rgba(1,14,33,.80)), url('./images/photos/generated/b10_hero.png');"></div>
    <div class="bg-grad"></div>
    <div class="pad">
      <span class="pill yellow-pill">Book 10 · PR &amp; Media Kit</span>
      <div class="cover-logo" aria-label="TOD by beIN"><span class="tod-logo"><svg><use href="#tod-by-bein"/></svg></span></div>
      <h1 style="font-size: clamp(40px,7vw,96px); font-weight:800; letter-spacing:-.02em; margin:18px 0 0; line-height:1;">PR &amp; Media Kit.</h1>
      <p class="sub">The brand as the press meets it. Approved boilerplate, locked names and facts, press-release standards, spokespeople, media assets, and crisis comms — one consistent story, every outlet, every market.</p>
      <div class="signature"><div class="label">Master Signature</div><div class="line">#1 Sports &amp; Stories</div></div>
      <div class="meta"><div class="meta-tags"><span>Boilerplate</span><span>Facts</span><span>Releases</span><span>Spokespeople</span><span>Assets</span><span>Crisis</span></div><div>From beIN Media Group · brand@tod.tv</div></div>
      <div class="scroll-hint">Scroll to begin</div>
    </div>
  </section>
'''

BODY = '''
<section id="p-kit" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 10.1 · The Media Kit</div>
    <h3>One kit. <span class="accent-purple">One story.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">When a journalist, partner, or platform writes about TOD by beIN, they should reach for the same approved facts, the same name, and the same assets. The media kit removes guesswork and keeps the story consistent across every outlet.</p>
    <div class="grid-3" style="margin-top:40px;">
      <div class="card"><span class="number">01 · Words</span><h4 style="color:var(--tod-navy);">Boilerplate &amp; facts</h4><p style="margin-top:10px;">Pre-approved short, medium, and long descriptions plus the locked names, promise, and signature.</p></div>
      <div class="card"><span class="number">02 · Assets</span><h4 style="color:var(--tod-navy);">Logos &amp; imagery</h4><p style="margin-top:10px;">Press-cleared logo files and photography, with the same usage rules as the rest of the system (Book 02).</p></div>
      <div class="card"><span class="number">03 · People</span><h4 style="color:var(--tod-navy);">Spokespeople &amp; contact</h4><p style="margin-top:10px;">Who can speak on the record, how to quote them, and the single contact point for all media.</p></div>
    </div>
    <div class="callout" style="background: rgba(255,199,44,.06); margin-top:24px;"><div class="label">One door for media</div><p>All press enquiries, interview requests, and asset requests route through <strong>brand@tod.tv</strong>. Nothing is confirmed to a journalist outside this channel.</p></div>
  </div>
</section>

<section id="p-boilerplate" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 10.2 · Boilerplate</div>
    <h3>Three lengths. <span class="accent">Use as written.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">The approved descriptions of TOD by beIN. Pick the length that fits the surface and use it verbatim — never paraphrase the boilerplate.</p>
    <div class="grid-3" style="margin-top:40px;">
      <div class="card"><span class="number">Short · PR · 25 words</span><p style="margin-top:10px;">TOD by beIN is a premium streaming destination — endorsed by beIN, growing market by market, and home to the sport, films, and series that matter.</p></div>
      <div class="card"><span class="number">Medium · Web · 50 words</span><p style="margin-top:10px;">TOD by beIN is a premium streaming destination endorsed by beIN — a globally trusted sports broadcaster. TOD by beIN delivers live sport, prestige series, and TOD Studios originals on every screen, scaling market by market.</p></div>
      <div class="card"><span class="number">Long · Corporate · 100 words</span><p style="margin-top:10px;">TOD by beIN is the streaming destination of beIN Media Group. Endorsed by beIN Sports — a globally trusted broadcaster — TOD by beIN combines premium live sport, prestige international series, TOD Studios originals, and international cinema on one platform, available across mobile, web, and connected TV. Multilingual by design, locally curated, and culturally fluent — market by market.</p></div>
    </div>
    <div class="callout flag" style="margin-top:24px;"><div class="label">Never</div><p>Don't edit, shorten, or "localise" the boilerplate ad hoc. New or market-specific versions are approved through brand@tod.tv (a Tier 2+ request, Book 09).</p></div>
  </div>
</section>

<section id="p-facts" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 10.3 · Brand Facts &amp; Naming</div>
    <h3>The locked facts <span class="accent-purple">every release leans on.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">The name, the promise, and the signature are locked (Books 01–03). In any press context they appear exactly as written.</p>
    <table class="data-table" style="margin-top:40px;">
      <thead><tr><th>Element</th><th>Locked form</th><th>Use</th></tr></thead>
      <tbody>
        <tr><td><strong>External name</strong></td><td>TOD by beIN</td><td>All external &amp; press use. "by beIN" is never stripped.</td></tr>
        <tr><td><strong>Master signature</strong></td><td>#1 Sports &amp; Stories</td><td>Brand-level moments only — never a feature tagline.</td></tr>
        <tr><td><strong>Brand promise</strong></td><td>Premium content. Without friction. On your terms.</td><td>Internal articulation; expressed externally through proof, not quoted as a slogan.</td></tr>
        <tr><td><strong>Parent</strong></td><td>beIN Media Group</td><td>TOD by beIN is the streaming destination of beIN Media Group.</td></tr>
        <tr><td><strong>Endorsement</strong></td><td>Endorsed by beIN Sports</td><td>A globally trusted sports broadcaster — the source of the trust.</td></tr>
      </tbody>
    </table>
    <div class="callout locked" style="margin-top:24px;"><div class="label">Locked</div><p>These are Tier 4 elements (Book 09). They do not change for a press cycle, a market, or an outlet's house style. If an editor must adapt, the meaning is preserved and the name is never altered.</p></div>
  </div>
</section>

  <section class="chapter-divider">
    <div class="bg" style="background-image: url('./images/photos/generated/b10_releases.png');"></div>
    <div class="content-block">
      <div class="module-label">Book 10 · On the Record</div>
      <h2>Releases &amp; spokespeople.</h2>
      <div class="tag-list">
        <span class="pill yellow-pill">Press Releases</span>
        <span class="pill">Quotes</span>
        <span class="pill">Approvals</span>
      </div>
    </div>
    <div class="ch-badge"><span class="dot"></span> Section 10.4–10.5</div>
  </section>

<section id="p-releases" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 10.4 · Press Release Standards</div>
    <h3>A release reads as TOD by beIN <span class="accent">before the logo loads.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Every release follows one structure and one voice (Book 03) — confident, clear, never hyperbolic. Facts first, claims backed, boilerplate at the foot.</p>
    <div class="grid-2" style="margin-top:40px; gap:24px;">
      <div class="card"><span class="number">Structure</span><h4>Headline → lede → quote → facts → boilerplate</h4><p style="margin-top:10px;">A factual headline, a one-line lede that answers what &amp; why, an approved quote, supporting detail, then the matching boilerplate and media contact.</p></div>
      <div class="card"><span class="number">Voice</span><h4>Confident, not hyperbolic</h4><p style="margin-top:10px;">No "revolutionary," no unverifiable superlatives. The master signature may headline brand-level releases; it is never a product claim.</p></div>
      <div class="card"><span class="number">Bilingual</span><h4>Arabic &amp; English in parallel</h4><p style="margin-top:10px;">Releases ship in both languages where the market needs it — written natively, not machine-translated, with correct RTL (Book 03).</p></div>
      <div class="card"><span class="number">Naming</span><h4>"TOD by beIN" on first mention</h4><p style="margin-top:10px;">First mention is the full endorsed name; subsequent mentions may use "TOD." Never "TOD.tv" or "Tod" in body copy.</p></div>
    </div>
  </div>
</section>

<section id="p-quotes" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 10.5 · Spokespeople &amp; Quotes</div>
    <h3>One voice <span class="accent-purple">on the record.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Only approved spokespeople speak for the brand publicly. Quotes are pre-cleared, attributed correctly, and consistent with the boilerplate and promise.</p>
    <div class="grid-3" style="margin-top:40px;">
      <div class="card"><span class="number">Who</span><h4 style="color:var(--tod-navy);">Approved spokespeople only</h4><p style="margin-top:10px;">A named, current list speaks on the record. No employee comments to media without clearance through brand@tod.tv.</p></div>
      <div class="card"><span class="number">What</span><h4 style="color:var(--tod-navy);">Pre-cleared quotes</h4><p style="margin-top:10px;">Quotes are written, approved, and attributed with correct name and title. They reinforce the promise; they never freestyle new claims.</p></div>
      <div class="card"><span class="number">How</span><h4 style="color:var(--tod-navy);">Interviews coordinated centrally</h4><p style="margin-top:10px;">Interview requests, briefing notes, and Q&amp;A prep are arranged through the single media contact, with talking points aligned to Book 03 voice.</p></div>
    </div>
    <div class="inline-image" style="background-image: url('./images/photos/generated/b10_media.png'); margin-top:40px;">
      <div class="caption"><div><div class="lbl">Media · Stories &amp; talent</div><div class="ttl">The "Stories" half of #1 Sports &amp; Stories — premium series and originals.</div></div><span class="tag">Book 10</span></div>
    </div>
  </div>
</section>

  <section class="chapter-divider">
    <div class="bg" style="background-image: url('./images/photos/generated/b10_press.png');"></div>
    <div class="content-block">
      <div class="module-label">Book 10 · Assets &amp; Readiness</div>
      <h2>Press assets &amp; crisis.</h2>
      <div class="tag-list">
        <span class="pill yellow-pill">Media Logos</span>
        <span class="pill">Imagery</span>
        <span class="pill">Crisis Comms</span>
      </div>
    </div>
    <div class="ch-badge"><span class="dot"></span> Section 10.6–10.8</div>
  </section>

<section id="p-assets" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 10.6 · Press Logos &amp; Imagery</div>
    <h3>Cleared assets, <span class="accent">same rules.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Media get a curated set of approved logo files and photography. The press relationship doesn't waive the brand rules — it relies on them.</p>
    <div class="grid-3" style="margin-top:40px;">
      <div class="card"><span class="number">Logos</span><h4>Master lockup, cleared formats</h4><p style="margin-top:10px;">The approved logo set in the formats outlets need, with the Book 02 clear-space and "do-not" rules attached. No partial or recoloured marks for press.</p></div>
      <div class="card"><span class="number">Imagery</span><h4>Approved photography only</h4><p style="margin-top:10px;">Press images come from the cleared library (Book 04 imagery direction) — rights-clear, on-brand, captioned. No grabbed screenshots.</p></div>
      <div class="card"><span class="number">Usage</span><h4>Attribution &amp; no alteration</h4><p style="margin-top:10px;">Outlets use assets as supplied — no stretching, recolouring, or compositing. Attribution as specified. Misuse is flagged via brand@tod.tv.</p></div>
    </div>
    <div class="callout" style="background: rgba(255,199,44,.06); margin-top:24px;"><div class="label">Source of truth</div><p>Press assets come from the same asset library as everything else (Book 09 · 9.6). There is one current version of every cleared file.</p></div>
  </div>
</section>

<section id="p-crisis" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 10.7 · Crisis Communications</div>
    <h3>Calm, fast, <span class="accent-purple">on one voice.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">In a sensitive moment, the brand slows down before it speaks. The goal is accuracy and care, not speed for its own sake — and everything funnels to one team.</p>
    <div class="grid-3" style="margin-top:40px;">
      <div class="card"><span class="number">Hold</span><h4 style="color:var(--tod-navy);">Acknowledge, don't speculate</h4><p style="margin-top:10px;">A holding line buys time: confirm awareness, commit to an update, say nothing unverified. No off-the-cuff comments from any channel.</p></div>
      <div class="card"><span class="number">Route</span><h4 style="color:var(--tod-navy);">Single team, single voice</h4><p style="margin-top:10px;">Comms and brand co-own the response through brand@tod.tv. Social and on-air pause sensitive content until cleared (Books 06 &amp; 08).</p></div>
      <div class="card"><span class="number">Stay neutral</span><h4 style="color:var(--tod-navy);">No politics or sides</h4><p style="margin-top:10px;">The brand carries no political, religious, or geopolitical position (Book 03). Responses are factual, respectful, and market-aware.</p></div>
    </div>
    <div class="callout flag" style="margin-top:24px;"><div class="label">Hard line</div><p>No individual speaks to media during a crisis without the comms team. A wrong word travels faster than a correction — hold and route.</p></div>
  </div>
</section>

<section id="p-contact" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 10.8 · Media Contact</div>
    <h3>One door <span class="accent">for the press.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Every press enquiry, asset request, interview, and crisis response funnels through one alias — so the brand always speaks with a single, coordinated voice.</p>
    <div style="margin-top: 40px; padding: 56px; border-radius: 24px; background: var(--tod-deep-navy, var(--tod-navy)); color: var(--tod-off-white); text-align: center;">
      <div style="font-size: 11px; letter-spacing: .24em; text-transform: uppercase; color: var(--tod-yellow); margin-bottom: 14px;">Media &amp; Press · Single Point of Entry</div>
      <div style="font-size: clamp(36px, 5.5vw, 72px); font-weight: 800; letter-spacing: -.02em;"><span class="accent">brand@tod.tv</span></div>
      <p style="margin: 18px auto 0; max-width: 56ch; opacity: .72;">Boilerplate, facts, logos, imagery, spokespeople, and crisis response — all coordinated here. No press confirmation happens outside this channel.</p>
    </div>
  </div>
</section>
'''

THIS_LINKS = '''  <a class="nav-item" href="#p-kit" data-close><span class="num">10.1</span> The Media Kit</a>
  <a class="nav-item" href="#p-boilerplate" data-close><span class="num">10.2</span> Boilerplate</a>
  <a class="nav-item" href="#p-facts" data-close><span class="num">10.3</span> Brand Facts &amp; Naming</a>
  <a class="nav-item" href="#p-releases" data-close><span class="num">10.4</span> Press Release Standards</a>
  <a class="nav-item" href="#p-quotes" data-close><span class="num">10.5</span> Spokespeople &amp; Quotes</a>
  <a class="nav-item" href="#p-assets" data-close><span class="num">10.6</span> Press Logos &amp; Imagery</a>
  <a class="nav-item" href="#p-crisis" data-close><span class="num">10.7</span> Crisis Communications</a>
  <a class="nav-item" href="#p-contact" data-close><span class="num">10.8</span> Media Contact</a>
'''

bg.build(
    title='TOD by beIN — Book 10 · PR &amp; Media Kit',
    active_idx='10',
    this_links=THIS_LINKS,
    cover=COVER,
    body=BODY,
    out='Book10_PR_Media_Kit.html',
    topbar_label='<strong>Book 10</strong> · PR &amp; Media Kit · Locked Reference',
)
