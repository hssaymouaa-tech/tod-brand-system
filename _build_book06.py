# -*- coding: utf-8 -*-
"""Build Book 06 — Social & Live Content (NEW, fully authored)."""
import _bookgen as bg

COVER = '''
  <section id="cover" class="cover">
    <div class="bg-photo" style="background-image: linear-gradient(180deg, rgba(1,14,33,.35), rgba(1,14,33,.78)), url('./images/photos/generated/b06_hero.png');"></div>
    <div class="bg-grad"></div>
    <div class="pad">
      <span class="pill yellow-pill">Book 06 · Social &amp; Live</span>
      <div class="cover-logo" aria-label="TOD by beIN"><span class="tod-logo"><svg><use href="#tod-by-bein"/></svg></span></div>
      <h1 style="font-size: clamp(40px,7vw,96px); font-weight:800; letter-spacing:-.02em; margin:18px 0 0; line-height:1;">Social &amp; Live.</h1>
      <p class="sub">Where the brand moves fastest and meets the most people. Feed aesthetic, vertical video, match-day live playbook, captions, and community tone — the rules that keep TOD by beIN consistent at the speed of social.</p>
      <div class="signature"><div class="label">Master Signature</div><div class="line">#1 Sports &amp; Stories</div></div>
      <div class="meta"><div class="meta-tags"><span>Ecosystem</span><span>Feed</span><span>Vertical</span><span>Match-Day</span><span>Captions</span><span>Community</span></div><div>From beIN Media Group · brand@tod.tv</div></div>
      <div class="scroll-hint">Scroll to begin</div>
    </div>
  </section>
'''

BODY = '''
<section id="s-ecosystem" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 6.1 · The Social Ecosystem</div>
    <h3>One brand. <span class="accent-purple">Many feeds.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Each platform has its own rhythm, but the brand is one. TOD by beIN shows up native to every surface while never losing the master signature, the yellow, or the voice from Book 03.</p>
    <table class="data-table" style="margin-top:40px;">
      <thead><tr><th>Platform</th><th>Primary Role</th><th>Lead Format</th><th>Cadence</th></tr></thead>
      <tbody>
        <tr><td><strong>Instagram</strong></td><td>Brand showcase · stories &amp; culture</td><td>Reels · carousels · stories</td><td>3–5 / day</td></tr>
        <tr><td><strong>TikTok</strong></td><td>Reach &amp; discovery · younger audience</td><td>Vertical video</td><td>2–4 / day</td></tr>
        <tr><td><strong>X (Twitter)</strong></td><td>Live match-day · real-time reaction</td><td>Clips · text · score cards</td><td>Live + 10–20 / day</td></tr>
        <tr><td><strong>YouTube</strong></td><td>Long-form · highlights · shows</td><td>Horizontal + Shorts</td><td>Daily</td></tr>
        <tr><td><strong>Facebook</strong></td><td>Broad MENA reach · community</td><td>Video · links</td><td>2–3 / day</td></tr>
        <tr><td><strong>Snapchat</strong></td><td>Match moments · Gen-Z reach</td><td>Vertical · stickers</td><td>Live + daily</td></tr>
      </tbody>
    </table>
    <div class="callout" style="background: rgba(255,199,44,.06); margin-top:24px;"><div class="label">One rule across all six</div><p>Profile, voice, and the master lockup are identical everywhere. Only the <strong>format and cadence</strong> flex per platform — never the identity.</p></div>
  </div>
</section>

  <section class="chapter-divider">
    <div class="bg" style="background-image: url('./images/photos/generated/b06_feed.png');"></div>
    <div class="content-block">
      <div class="module-label">Book 06 · Identity on Social</div>
      <h2>Profiles, feed &amp; templates.</h2>
      <div class="tag-list">
        <span class="pill yellow-pill">Handles</span>
        <span class="pill">Grid Aesthetic</span>
        <span class="pill">Safe Zones</span>
      </div>
    </div>
    <div class="ch-badge"><span class="dot"></span> Section 6.2–6.4</div>
  </section>

<section id="s-profiles" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 6.2 · Profiles &amp; Handles</div>
    <h3>The same face <span class="accent">on every platform.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">A user who follows us on TikTok and X should recognise the same brand instantly. Handles, avatars, and bios are locked.</p>
    <div class="grid-4" style="margin-top:40px;">
      <div class="card"><span class="number">01 · Handle</span><h4>@TOD</h4><p style="margin-top:10px;">Use <strong>@TOD</strong> where available, else <strong>@TODbybeIN</strong>. Never @TOD_TV, @TODsports, or market-suffixed handles.</p></div>
      <div class="card"><span class="number">02 · Avatar</span><h4>Mono lockup on Navy</h4><p style="margin-top:10px;">The TOD by beIN monogram in Off-White on TOD Navy. Centred, full clear space. Never the wordmark cropped to fit a circle.</p></div>
      <div class="card"><span class="number">03 · Display name</span><h4>TOD by beIN</h4><p style="margin-top:10px;">Always the endorsed name. The "by beIN" carries the trust (Book 05, Law 03) and is never stripped for character limits.</p></div>
      <div class="card"><span class="number">04 · Bio</span><h4>#1 Sports &amp; Stories</h4><p style="margin-top:10px;">Lead with the master signature, one line on offer, one CTA link. Bilingual where the platform supports it (Book 03 RTL rules).</p></div>
    </div>
    <div class="callout flag" style="margin-top:24px;"><div class="label">Never</div><p>No personal-style avatars, no seasonal logo swaps without Brand Director sign-off, no unofficial regional accounts. One verified account per platform.</p></div>
  </div>
</section>

<section id="s-feed" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 6.3 · Feed &amp; Grid Aesthetic</div>
    <h3>The grid is a <span class="accent-purple">composition</span>, not a dumping ground.</h3>
    <p style="margin-top:18px; max-width:64ch;">Scroll the profile and the brand should read at a glance: confident, premium, unmistakably TOD. Rhythm beats volume.</p>
    <div class="grid-2" style="margin-top:40px; gap:24px;">
      <div class="card"><span class="number">Rhythm</span><h4 style="color:var(--tod-navy);">Alternate energy &amp; calm</h4><p style="margin-top:10px;">Sport action and entertainment stills carry energy; type-led brand cards and quote frames give the eye rest. Never three high-noise tiles in a row.</p></div>
      <div class="card"><span class="number">Colour</span><h4 style="color:var(--tod-navy);">Navy &amp; Off-White base, Yellow accent</h4><p style="margin-top:10px;">The feed reads as a TOD surface. Yellow is the accent that points, never the wallpaper. The Happy Spectrum is reserved for hero moments.</p></div>
      <div class="card"><span class="number">Type</span><h4 style="color:var(--tod-navy);">Alexandria, always</h4><p style="margin-top:10px;">Headlines in Alexandria 800, captions in the body weight. Bilingual lockups follow Book 03 mechanics — Arabic never an afterthought.</p></div>
      <div class="card"><span class="number">Logo</span><h4 style="color:var(--tod-navy);">Lower-corner, quiet</h4><p style="margin-top:10px;">A small mono lockup bottom-left or bottom-right. The content is the hero; the brand signs it, it doesn't shout over it.</p></div>
    </div>
    <div class="inline-image" style="background-image: url('./images/photos/generated/b06_stories.png'); margin-top:40px;">
      <div class="caption"><div><div class="lbl">Feed · Stories tile</div><div class="ttl">Entertainment stills carry the "Stories" half of #1 Sports &amp; Stories.</div></div><span class="tag">Book 06</span></div>
    </div>
  </div>
</section>

<section id="s-templates" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 6.4 · Post Templates &amp; Safe Zones</div>
    <h3>Built once. <span class="accent">Right everywhere.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Templates remove guesswork and protect content from platform UI. Design to the safe zone and one asset travels across every surface.</p>
    <div class="grid-3" style="margin-top:40px;">
      <div class="card"><span class="number">Square · 1:1</span><h4>Feed post</h4><p style="margin-top:10px;">1080×1080. Keep headline and logo inside a 64px margin. Carousels share one template, one accent.</p></div>
      <div class="card"><span class="number">Vertical · 9:16</span><h4>Stories · Reels · TikTok</h4><p style="margin-top:10px;">1080×1920. Keep all type and the logo inside the centre 1080×1420 safe zone — top 250px and bottom 250px belong to platform UI.</p></div>
      <div class="card"><span class="number">Landscape · 16:9</span><h4>X · YouTube · score cards</h4><p style="margin-top:10px;">1920×1080. Logo lower-corner, score/scoreline upper third, never under the platform timestamp.</p></div>
    </div>
    <div class="callout" style="background: rgba(255,199,44,.06); margin-top:24px;"><div class="label">The safe-zone test</div><p>Preview every asset <strong>inside the live app</strong> before it ships. If the avatar, caption shelf, or send bar covers a word or the logo, the layout is wrong — not the platform.</p></div>
  </div>
</section>

  <section class="chapter-divider">
    <div class="bg" style="background-image: url('./images/photos/generated/b06_vertical.png');"></div>
    <div class="content-block">
      <div class="module-label">Book 06 · The Live Edge</div>
      <h2>Vertical, live &amp; in the moment.</h2>
      <div class="tag-list">
        <span class="pill yellow-pill">Reels</span>
        <span class="pill">Match-Day</span>
        <span class="pill">Real-Time</span>
      </div>
    </div>
    <div class="ch-badge"><span class="dot"></span> Section 6.5–6.6</div>
  </section>

<section id="s-vertical" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 6.5 · Stories, Reels &amp; Vertical Video</div>
    <h3>Hook in <span class="accent-purple">one second.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Vertical is the brand's biggest reach engine. The craft is in the first frame, the motion, and the sign-off — every clip ends as a TOD clip.</p>
    <div class="grid-2" style="margin-top:40px; gap:24px;">
      <div class="card"><span class="number">Hook</span><h4 style="color:var(--tod-navy);">First frame earns the watch</h4><p style="margin-top:10px;">Open on the peak — the goal, the twist, the reveal. No slow logo stings at the top. Brand the <em>end</em>, not the start.</p></div>
      <div class="card"><span class="number">Motion</span><h4 style="color:var(--tod-navy);">TOD ease, never default</h4><p style="margin-top:10px;">Use the motion curves and transitions from Book 07. Text snaps on the beat; the yellow underline wipes left-to-right (RTL: right-to-left).</p></div>
      <div class="card"><span class="number">Captions</span><h4 style="color:var(--tod-navy);">Always burned-in</h4><p style="margin-top:10px;">Sound-off by default. Alexandria captions, high contrast, inside the safe zone. Bilingual where the audience is mixed.</p></div>
      <div class="card"><span class="number">Sign-off</span><h4 style="color:var(--tod-navy);">End card + sonic logo</h4><p style="margin-top:10px;">Close on the mono lockup and the sonic logo (Book 07). One CTA: "Watch on TOD by beIN."</p></div>
    </div>
    <div class="inline-image" style="background-image: url('./images/photos/generated/b06_clip.png'); margin-top:40px;">
      <div class="caption"><div><div class="lbl">Vertical · Match clip</div><div class="ttl">Peak moment first. Brand signs the end, never the open.</div></div><span class="tag">Book 06</span></div>
    </div>
  </div>
</section>

<section id="s-matchday" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 6.6 · Live Match-Day Playbook</div>
    <h3>The whistle blows. <span class="accent">The brand is ready.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Match-day is when social moves fastest and mistakes travel furthest. The playbook is a clock, not a vibe — everyone knows their lane before kick-off.</p>
    <table class="data-table" style="margin-top:40px;">
      <thead><tr><th>Phase</th><th>Window</th><th>What ships</th><th>Owner</th></tr></thead>
      <tbody>
        <tr><td><strong>Pre-match</strong></td><td>T–24h → T–1h</td><td>Fixture cards, line-ups, "how to watch" CTA</td><td>Social lead</td></tr>
        <tr><td><strong>Kick-off</strong></td><td>T–0</td><td>Live tune-in card, score card live</td><td>Live editor</td></tr>
        <tr><td><strong>In-play</strong></td><td>Live</td><td>Goal clips, reaction, score updates within 60s</td><td>Clipper + editor</td></tr>
        <tr><td><strong>Full-time</strong></td><td>FT +15m</td><td>Result card, key moment reel, ratings</td><td>Social lead</td></tr>
        <tr><td><strong>Post-match</strong></td><td>FT +1h → +24h</td><td>Highlights, interviews, long-form to YouTube</td><td>Content team</td></tr>
      </tbody>
    </table>
    <div class="grid-3" style="margin-top:32px;">
      <div class="card"><span class="number">Speed rule</span><h4>Goal clip live in 60s</h4><p style="margin-top:10px;">Pre-built score-card and clip templates mean the editor only swaps the moment. Speed wins reach; the template guarantees it stays on-brand.</p></div>
      <div class="card"><span class="number">Rights rule</span><h4>Only licensed footage</h4><p style="margin-top:10px;">Post only what TOD holds rights to in that market. When in doubt, score cards and reaction — never unlicensed clips.</p></div>
      <div class="card"><span class="number">Tone rule</span><h4>Hype, never bias</h4><p style="margin-top:10px;">Celebrate the sport and the moment, not one side. TOD is the home of the match, not a fan account (Book 03 voice).</p></div>
    </div>
    <div class="callout flag" style="margin-top:24px;"><div class="label">Live kill-switch</div><p>Any rights, legal, or sensitivity doubt during a live window — <strong>hold and escalate to brand@tod.tv</strong>. A 5-minute delay is always cheaper than a takedown.</p></div>
  </div>
</section>

<section id="s-captions" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 6.7 · Captions, Hashtags &amp; Emoji</div>
    <h3>Short. Sharp. <span class="accent-purple">On voice.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">The caption is the brand speaking. It follows Book 03 voice — confident, warm, never shouty — and the same rules in Arabic and English.</p>
    <div class="grid-2" style="margin-top:40px;">
      <div class="card" style="background: rgba(34,197,94,.06); border-color: rgba(34,197,94,.18);">
        <span class="number" style="color: var(--ui-success);">✓ Do</span>
        <ul style="font-size:14px; padding-left:20px; margin-top:12px; line-height:1.7; opacity:.85;">
          <li>Lead with the moment, then the CTA.</li>
          <li>One or two emoji, with intent — not a confetti line.</li>
          <li>Branded hashtag <strong>#TOD</strong> + one event tag.</li>
          <li>Bilingual where the audience is mixed; Arabic first in RTL markets.</li>
        </ul>
      </div>
      <div class="card" style="background: rgba(239,68,68,.06); border-color: rgba(239,68,68,.18);">
        <span class="number" style="color: var(--ui-error);">✗ Don't</span>
        <ul style="font-size:14px; padding-left:20px; margin-top:12px; line-height:1.7; opacity:.85;">
          <li>Hashtag walls (more than 3–4 tags).</li>
          <li>ALL CAPS shouting or clickbait ("you won't believe…").</li>
          <li>Emoji standing in for words the brand should say.</li>
          <li>Borrowing slang or memes that don't fit the voice.</li>
        </ul>
      </div>
    </div>
    <div class="callout" style="background: rgba(255,199,44,.06); margin-top:24px;"><div class="label">Hashtag system</div><p>Primary <strong>#TOD</strong> on everything. Add one campaign or event tag (e.g. a tournament tag) — no more. Hashtags are wayfinding, not decoration.</p></div>
  </div>
</section>

<section id="s-community" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 6.8 · Community &amp; Moderation</div>
    <h3>We host the conversation. <span class="accent">We don't join the fight.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Replies and DMs are the brand at human scale. The same voice, the same calm, even when the timeline isn't.</p>
    <div class="grid-3" style="margin-top:40px;">
      <div class="card"><span class="number">Respond</span><h4>Fast, warm, helpful</h4><p style="margin-top:10px;">Answer "how do I watch" and access questions first and fast. Point to the app, never make the fan hunt.</p></div>
      <div class="card"><span class="number">De-escalate</span><h4>Never argue, never pile on</h4><p style="margin-top:10px;">No dunking, no taking sides between fanbases. Acknowledge, inform, move on. The brand stays above the rivalry.</p></div>
      <div class="card"><span class="number">Moderate</span><h4>Hide hate, escalate threats</h4><p style="margin-top:10px;">Hide/limit abuse and spam per the moderation policy. Threats or safety issues escalate to brand@tod.tv and the platform.</p></div>
    </div>
    <div class="callout flag" style="margin-top:24px;"><div class="label">Hard line</div><p>No political, religious, or geopolitical commentary from brand accounts — ever. No engaging trolls. When unsure, don't reply; escalate.</p></div>
  </div>
</section>

<section id="s-governance" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 6.9 · Cadence &amp; Governance</div>
    <h3>Consistency is a <span class="accent-purple">system,</span> not a mood.</h3>
    <p style="margin-top:18px; max-width:64ch;">Who posts, who approves, and how fast — defined before the week starts so the brand never improvises under pressure.</p>
    <table class="data-table" style="margin-top:40px;">
      <thead><tr><th>Content type</th><th>Approval</th><th>Speed</th></tr></thead>
      <tbody>
        <tr><td><strong>Standard feed / reel</strong></td><td>Social lead</td><td>Same day</td></tr>
        <tr><td><strong>Live match-day</strong></td><td>Pre-cleared templates · live editor</td><td>Real-time (&lt;60s)</td></tr>
        <tr><td><strong>Campaign / brand moment</strong></td><td>Brand Director</td><td>Planned</td></tr>
        <tr><td><strong>Co-brand / partner post</strong></td><td>Per Book 05 tier + partner sign-off</td><td>Planned</td></tr>
        <tr><td><strong>Crisis / sensitive</strong></td><td>brand@tod.tv + comms</td><td>Hold until cleared</td></tr>
      </tbody>
    </table>
    <div class="callout locked" style="margin-top:24px;"><div class="label">Single point of entry</div><p>Every exception, escalation, and partner approval routes through <strong>brand@tod.tv</strong>. Speed on the routine is what buys care on the rare.</p></div>
  </div>
</section>
'''

THIS_LINKS = '''  <a class="nav-item" href="#s-ecosystem" data-close><span class="num">6.1</span> Social Ecosystem</a>
  <a class="nav-item" href="#s-profiles" data-close><span class="num">6.2</span> Profiles &amp; Handles</a>
  <a class="nav-item" href="#s-feed" data-close><span class="num">6.3</span> Feed &amp; Grid</a>
  <a class="nav-item" href="#s-templates" data-close><span class="num">6.4</span> Templates &amp; Safe Zones</a>
  <a class="nav-item" href="#s-vertical" data-close><span class="num">6.5</span> Vertical Video</a>
  <a class="nav-item" href="#s-matchday" data-close><span class="num">6.6</span> Match-Day Playbook</a>
  <a class="nav-item" href="#s-captions" data-close><span class="num">6.7</span> Captions &amp; Hashtags</a>
  <a class="nav-item" href="#s-community" data-close><span class="num">6.8</span> Community</a>
  <a class="nav-item" href="#s-governance" data-close><span class="num">6.9</span> Cadence &amp; Governance</a>
'''

bg.build(
    title='TOD by beIN — Book 06 · Social &amp; Live',
    active_idx='06',
    this_links=THIS_LINKS,
    cover=COVER,
    body=BODY,
    out='Book06_Social_Live.html',
    topbar_label='<strong>Book 06</strong> · Social &amp; Live · Locked Reference',
)
