# -*- coding: utf-8 -*-
"""Build Book 09 — Brand Operations (EXPAND of master Governance + appendices)."""
import _bookgen as bg

COVER = '''
  <section id="cover" class="cover">
    <div class="bg-photo" style="background-image: linear-gradient(180deg, rgba(1,14,33,.35), rgba(1,14,33,.80)), url('./images/photos/generated/b09_hero.png');"></div>
    <div class="bg-grad"></div>
    <div class="pad">
      <span class="pill yellow-pill">Book 09 · Brand Operations</span>
      <div class="cover-logo" aria-label="TOD by beIN"><span class="tod-logo"><svg><use href="#tod-by-bein"/></svg></span></div>
      <h1 style="font-size: clamp(40px,7vw,96px); font-weight:800; letter-spacing:-.02em; margin:18px 0 0; line-height:1;">Brand Operations.</h1>
      <p class="sub">How the brand runs day to day. Four authority tiers, one contact point, clear SLAs, and a compliance checklist — so decisions are faster and the output stays clean.</p>
      <div class="signature"><div class="label">Master Signature</div><div class="line">#1 Sports &amp; Stories</div></div>
      <div class="meta"><div class="meta-tags"><span>Authority</span><span>Single Entry</span><span>Workflow</span><span>Roles</span><span>QA</span><span>Versioning</span></div><div>From beIN Media Group · brand@tod.tv</div></div>
      <div class="scroll-hint">Scroll to begin</div>
    </div>
  </section>
'''

BODY = '''
<section id="o-howitworks" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 9.1 · How the Brand Operates</div>
    <h3>A system, <span class="accent-purple">not a gatekeeper.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Operations exist to make the right thing the easy thing. Most work runs self-serve inside locked templates; only genuinely new work needs a decision — and every decision has one owner and one clock.</p>
    <div class="grid-3" style="margin-top:40px;">
      <div class="card"><span class="number">01 · Self-serve first</span><h4 style="color:var(--tod-navy);">Templates do the heavy lifting</h4><p style="margin-top:10px;">If it lives inside a locked template, ship it — no approval needed. The system already encodes the rules.</p></div>
      <div class="card"><span class="number">02 · One owner</span><h4 style="color:var(--tod-navy);">Every tier has a name</h4><p style="margin-top:10px;">No committees. Each request maps to one accountable owner and a published SLA, so nothing stalls in limbo.</p></div>
      <div class="card"><span class="number">03 · One door</span><h4 style="color:var(--tod-navy);">brand@tod.tv routes it all</h4><p style="margin-top:10px;">A single alias logs every request from T1 to T4. No request bypasses it; nothing gets lost.</p></div>
    </div>
  </div>
</section>

<section id="o-authority" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 9.2 · Authority Matrix</div>
    <h3>Four tiers. <span class="accent">One contact point.</span> Faster decisions, cleaner output.</h3>
    <table class="data-table" style="margin-top:40px;">
      <thead><tr><th>Tier</th><th>Scope</th><th>Examples</th><th>Owner &amp; SLA</th></tr></thead>
      <tbody>
        <tr><td><strong>T1 · In-template</strong></td><td>Operations within locked templates.</td><td>Match-day social, in-app banners.</td><td>Channel lead · Self-serve.</td></tr>
        <tr><td><strong>T2 · Campaign</strong></td><td>New work within the existing system.</td><td>Seasonal campaigns, OOH, broadcast spots.</td><td>Brand Manager · 72-hour SLA.</td></tr>
        <tr><td><strong>T3 · Partner / Co-brand</strong></td><td>Anything involving a third-party mark.</td><td>FIFA rollouts, telco bundles.</td><td>Brand Director + Legal · 5 BD SLA.</td></tr>
        <tr><td><strong>T4 · System change</strong></td><td>Changes to the brand system itself.</td><td>Logo, palette, type, master signature.</td><td>CMO + CBO · Strategic.</td></tr>
      </tbody>
    </table>
    <div class="callout" style="background: rgba(255,199,44,.06); margin-top:24px;"><div class="label">How tiers map to the library</div><p>T3 partner work follows <strong>Book 05</strong> co-brand tiers. T4 system changes touch <strong>Books 02 &amp; 04</strong>. When in doubt about a tier, log it — triage will route it.</p></div>
  </div>
</section>

<section id="o-entry" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 9.3 · Single Point of Entry</div>
    <h3>No committee work. <span class="accent-purple">No chasing.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">One alias routes every brand request. It logs the ask, assigns the tier and owner, and starts the SLA clock — so the requester always knows where their work stands.</p>
    <div class="inline-image" style="background-image: url('./images/photos/generated/b09_onesignal.png'); margin-top:40px;">
      <div class="caption"><div><div class="lbl">Governance · One signal</div><div class="ttl">No committee work. No chasing. One alias routes every brand request.</div></div><span class="tag">Book 09</span></div>
    </div>
    <div style="margin-top: 56px; padding: 56px; border-radius: 24px; background: var(--tod-navy); color: var(--tod-off-white); text-align: center;">
      <div style="font-size: 11px; letter-spacing: .24em; text-transform: uppercase; color: var(--tod-yellow); margin-bottom: 14px;">9.3 · Single Point of Entry</div>
      <div style="font-size: clamp(36px, 5.5vw, 72px); font-weight: 800; letter-spacing: -.02em;"><span class="accent">brand@tod.tv</span></div>
      <p style="margin: 18px auto 0; max-width: 56ch; opacity: .72;">Every brand request — Tier 1 through Tier 4 — is logged through this central alias. No request bypasses it. No exceptions.</p>
    </div>
  </div>
</section>

  <section class="chapter-divider">
    <div class="bg" style="background-image: url('./images/photos/generated/b09_workflow.png');"></div>
    <div class="content-block">
      <div class="module-label">Book 09 · Getting Work Done</div>
      <h2>Workflow, roles &amp; assets.</h2>
      <div class="tag-list">
        <span class="pill yellow-pill">Request Flow</span>
        <span class="pill">Quick-Starts</span>
        <span class="pill">Asset Library</span>
      </div>
    </div>
    <div class="ch-badge"><span class="dot"></span> Section 9.4–9.6</div>
  </section>

<section id="o-workflow" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 9.4 · Request &amp; Approval Workflow</div>
    <h3>Intake to delivery, <span class="accent">in four steps.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Every non-template request follows the same path. The steps are fixed; only the owner and SLA change with the tier.</p>
    <div class="grid-4" style="margin-top:40px;">
      <div class="card"><span class="number">Step 01 · Log</span><h4>Submit to brand@tod.tv</h4><p style="margin-top:10px;">One email or ticket with the ask, deadline, and surfaces. Incomplete requests are triaged back, not silently dropped.</p></div>
      <div class="card"><span class="number">Step 02 · Triage</span><h4>Assign tier &amp; owner</h4><p style="margin-top:10px;">Triage sets the tier (T1–T4), names the owner, and starts the SLA clock. The requester gets the tier and ETA back same day.</p></div>
      <div class="card"><span class="number">Step 03 · Produce</span><h4>Build on the system</h4><p style="margin-top:10px;">Work is made against the locked books — logo (02), design (04), voice (03), co-brand (05). QA happens before review, not after.</p></div>
      <div class="card"><span class="number">Step 04 · Approve &amp; ship</span><h4>Owner signs, asset filed</h4><p style="margin-top:10px;">The tier owner approves; the final asset is filed to the library with correct naming so it is reusable, not lost.</p></div>
    </div>
    <div class="callout flag" style="margin-top:24px;"><div class="label">Escalation</div><p>Rights, legal, or sensitivity doubt at any step — hold and escalate. A short delay is always cheaper than a recall. Live broadcast and social windows follow the kill-switch rules in Books 06 &amp; 08.</p></div>
  </div>
</section>

<section id="o-roles" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 9.5 · Role Quick-Starts</div>
    <h3>Five-minute <span class="accent-purple">on-ramps.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">For the five roles most likely to use this brand system. Each names the books to read first and the question to answer before publishing.</p>
    <table class="data-table" style="margin-top:40px;">
      <thead><tr><th>Role</th><th>Read First</th><th>Question to Answer</th></tr></thead>
      <tbody>
        <tr><td><strong>Brand Manager</strong></td><td>Books 01, 03, 05, 09</td><td>Does this campaign ladder up to a PACE goal and a messaging pillar?</td></tr>
        <tr><td><strong>Designer / Agency</strong></td><td>Books 02, 04, 06</td><td>Is every element on the surface in the locked colour, type, and logo system?</td></tr>
        <tr><td><strong>Copywriter</strong></td><td>Books 03, 09</td><td>Have I matched the right tone for this surface, in the right register for this market?</td></tr>
        <tr><td><strong>Channel / Social Lead</strong></td><td>Books 06, 07</td><td>Am I inside a locked template, or am I escalating to a Tier 2 request?</td></tr>
        <tr><td><strong>Partnerships / BD</strong></td><td>Books 05, 09</td><td>Does this partner deal fit a Tier 1, 2, or 3 approval path?</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section id="o-assets" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 9.6 · Asset Library &amp; File Management</div>
    <h3>One source of truth. <span class="accent">Findable, current, correct.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">A brand is only as consistent as the files people actually grab. The library is the single source — versioned, named, and the only place to pull from.</p>
    <div class="grid-3" style="margin-top:40px;">
      <div class="card"><span class="number">Source of truth</span><h4>Pull from the library only</h4><p style="margin-top:10px;">Logos, fonts, colours, templates, and photography live in the asset library. Never re-create a logo or eyedrop a colour from a screenshot.</p></div>
      <div class="card"><span class="number">Naming</span><h4>Predictable &amp; searchable</h4><p style="margin-top:10px;">Consistent file names — brand, asset, variant, language, version. A teammate should find the right file without asking.</p></div>
      <div class="card"><span class="number">Versioning</span><h4>Latest is obvious</h4><p style="margin-top:10px;">Superseded files are archived, not left alongside the current ones. There is exactly one "current" of every locked asset.</p></div>
    </div>
    <div class="callout locked" style="margin-top:24px;"><div class="label">Locked</div><p>The master logo, colour, type, and sonic files are locked references (Books 02, 04, 07). Edits or new official variants are T4 changes — they go through brand@tod.tv, never produced ad hoc.</p></div>
  </div>
</section>

  <section class="chapter-divider">
    <div class="bg" style="background-image: url('./images/photos/generated/b09_compliance.png');"></div>
    <div class="content-block">
      <div class="module-label">Book 09 · Keeping It Clean</div>
      <h2>Compliance &amp; versioning.</h2>
      <div class="tag-list">
        <span class="pill yellow-pill">Pre-Publish QA</span>
        <span class="pill">Change Log</span>
      </div>
    </div>
    <div class="ch-badge"><span class="dot"></span> Section 9.7–9.8</div>
  </section>

<section id="o-qa" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 9.7 · Brand Compliance &amp; QA</div>
    <h3>One checklist <span class="accent-purple">before anything ships.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">QA happens before review, not after. Run the surface against the same short list every time — the questions map straight to the books that own each answer.</p>
    <div class="grid-2" style="margin-top:40px; gap:24px;">
      <div class="card"><span class="number">Identity</span><h4 style="color:var(--tod-navy);">Logo, clear space, lockup</h4><p style="margin-top:10px;">Correct master lockup, full clear space, no stretch/recolour, "by beIN" intact. → <strong>Book 02</strong>.</p></div>
      <div class="card"><span class="number">Design</span><h4 style="color:var(--tod-navy);">Colour, type, grid, a11y</h4><p style="margin-top:10px;">Locked palette, Alexandria, on-grid, AA contrast. → <strong>Book 04</strong>.</p></div>
      <div class="card"><span class="number">Voice</span><h4 style="color:var(--tod-navy);">Tone &amp; bilingual</h4><p style="margin-top:10px;">Right tone for the surface, correct register, Arabic equal and RTL-correct. → <strong>Book 03</strong>.</p></div>
      <div class="card"><span class="number">Rights</span><h4 style="color:var(--tod-navy);">Co-brand &amp; footage</h4><p style="margin-top:10px;">Partner marks at the right tier, only licensed footage, neutral commentary. → <strong>Books 05 &amp; 08</strong>.</p></div>
    </div>
    <div class="callout" style="background: rgba(255,199,44,.06); margin-top:24px;"><div class="label">The one-question test</div><p>If you can't say which book backs every choice on the surface, it isn't ready. When in doubt, log it through brand@tod.tv before it goes out.</p></div>
  </div>
</section>

<section id="o-versioning" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 9.8 · Versioning &amp; Change Log</div>
    <h3>The system evolves <span class="accent">on the record.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Changes to the brand system are deliberate, tier-4, and logged. The change log is the shared memory — what changed, when, and why.</p>
    <table class="data-table" style="margin-top:40px;">
      <thead><tr><th>Version</th><th>Date</th><th>Change</th></tr></thead>
      <tbody>
        <tr><td><strong>v1.0</strong></td><td>2025 Q4</td><td>Original brand book deployed. Established TOD wordmark, colour palette, photography direction, signature "The Choice Is Yours."</td></tr>
        <tr><td><strong>v2.0</strong></td><td>2026 Q2</td><td>Full system review. Renamed to "TOD by beIN" for all external use. Master signature locked as "#1 Sports &amp; Stories." Brand promise, SHIP values, PACE 2026 goals, six audience archetypes, three universal co-brand laws, single point of entry: brand@tod.tv.</td></tr>
        <tr><td><strong>v2.0 · Library</strong></td><td>2026</td><td>Brand system expanded into an 11-book library — Logo, Voice, Design, Co-Brand, Social, Sonic &amp; Motion, Broadcast, Operations, PR, and TOD360 — each a standalone reference sharing one visual system.</td></tr>
      </tbody>
    </table>
    <div class="callout locked" style="margin-top:24px;"><div class="label">Single point of entry</div><p>Every system change is a T4 decision (CMO + CBO) logged through <strong>brand@tod.tv</strong>. Nothing in the locked books changes informally.</p></div>
  </div>
</section>
'''

THIS_LINKS = '''  <a class="nav-item" href="#o-howitworks" data-close><span class="num">9.1</span> How the Brand Operates</a>
  <a class="nav-item" href="#o-authority" data-close><span class="num">9.2</span> Authority Matrix</a>
  <a class="nav-item" href="#o-entry" data-close><span class="num">9.3</span> Single Point of Entry</a>
  <a class="nav-item" href="#o-workflow" data-close><span class="num">9.4</span> Request Workflow</a>
  <a class="nav-item" href="#o-roles" data-close><span class="num">9.5</span> Role Quick-Starts</a>
  <a class="nav-item" href="#o-assets" data-close><span class="num">9.6</span> Asset Library</a>
  <a class="nav-item" href="#o-qa" data-close><span class="num">9.7</span> Compliance &amp; QA</a>
  <a class="nav-item" href="#o-versioning" data-close><span class="num">9.8</span> Versioning &amp; Change Log</a>
'''

bg.build(
    title='TOD by beIN — Book 09 · Brand Operations',
    active_idx='09',
    this_links=THIS_LINKS,
    cover=COVER,
    body=BODY,
    out='Book09_Brand_Operations.html',
    topbar_label='<strong>Book 09</strong> · Brand Operations · Locked Reference',
)
