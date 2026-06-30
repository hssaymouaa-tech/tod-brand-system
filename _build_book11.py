# -*- coding: utf-8 -*-
"""Build Book 11 — TOD360 Features (NEW; from the TOD 2.0 Video Experience deck)."""
import _bookgen as bg

P1 = '<span class="pill" style="background:rgba(34,197,94,.14); color:#22C55E; border:1px solid rgba(34,197,94,.3); font-size:10px; letter-spacing:.1em;">PHASE 1</span>'
P2 = '<span class="pill" style="background:rgba(255,199,44,.14); color:var(--tod-yellow); border:1px solid rgba(255,199,44,.3); font-size:10px; letter-spacing:.1em;">PHASE 2</span>'

COVER = '''
  <section id="cover" class="cover">
    <div class="bg-photo" style="background-image: linear-gradient(180deg, rgba(1,14,33,.35), rgba(1,14,33,.80)), url('./images/photos/generated/b11_hero.png');"></div>
    <div class="bg-grad"></div>
    <div class="pad">
      <span class="pill yellow-pill">Book 11 · TOD360 Features</span>
      <div class="cover-logo" aria-label="TOD by beIN"><span class="tod-logo"><svg><use href="#tod-by-bein"/></svg></span></div>
      <h1 style="font-size: clamp(40px,7vw,96px); font-weight:800; letter-spacing:-.02em; margin:18px 0 0; line-height:1;">TOD360 Features.</h1>
      <p class="sub">The TOD 2.0 video experience. A premium, interactive player across every screen — VOD for series and film, a live sport player built for the moment, and the TOD360 layer that turns watching into taking part.</p>
      <div class="signature"><div class="label">Master Signature</div><div class="line">#1 Sports &amp; Stories</div></div>
      <div class="meta"><div class="meta-tags"><span>VOD</span><span>Live Sport</span><span>Interactive Timeline</span><span>Fan Engagement</span><span>Multi-View</span><span>Security</span></div><div>From beIN Media Group · brand@tod.tv</div></div>
      <div class="scroll-hint">Scroll to begin</div>
    </div>
  </section>
'''

BODY = '''
<style>
  .ui-shot { border-radius:16px; overflow:hidden; border:1px solid rgba(1,14,33,.12); box-shadow:0 30px 60px -22px rgba(1,14,33,.5); background:#010E21; }
  .dark .ui-shot { border-color:rgba(255,255,255,.1); }
  .ui-shot .bar { display:flex; gap:7px; padding:11px 16px; background:#02152f; align-items:center; }
  .ui-shot .bar i { width:10px; height:10px; border-radius:50%; background:rgba(255,255,255,.16); display:block; }
  .ui-shot .bar .lbl { margin-left:12px; font-size:10.5px; letter-spacing:.14em; text-transform:uppercase; color:rgba(244,246,250,.5); }
  .ui-shot img { display:block; width:100%; height:auto; }
  .ui-cap { font-size:12.5px; opacity:.58; margin-top:11px; line-height:1.5; }
  .ui-grid { display:grid; grid-template-columns:1fr 1fr; gap:24px; margin-top:40px; }
  .ui-grid-3 { display:grid; grid-template-columns:repeat(3,1fr); gap:18px; margin-top:32px; }
  .ui-phone { max-width:300px; margin:0 auto; border-radius:20px; overflow:hidden; border:1px solid rgba(255,255,255,.12); box-shadow:0 30px 60px -20px rgba(1,14,33,.55); }
  .ui-phone img { display:block; width:100%; }
  .feat-index { display:grid; grid-template-columns:repeat(3,1fr); gap:22px; margin-top:40px; }
  .feat-cat { border:1px solid rgba(244,246,250,.12); border-radius:16px; padding:22px; background:rgba(255,255,255,.03); }
  .feat-cat h4 { color:var(--tod-yellow); font-size:14px; letter-spacing:.04em; margin-bottom:6px; }
  .feat-cat .cnt { font-size:11px; opacity:.5; letter-spacing:.1em; text-transform:uppercase; }
  .feat-cat ul { list-style:none; padding:0; margin:14px 0 0; }
  .feat-cat li { font-size:12.5px; line-height:1.5; padding:6px 0; border-top:1px solid rgba(244,246,250,.07); display:flex; justify-content:space-between; gap:8px; align-items:center; }
  .feat-cat li:first-child { border-top:none; }
  .feat-cat li .p2 { font-size:8.5px; font-weight:700; letter-spacing:.1em; color:var(--tod-yellow); border:1px solid rgba(255,199,44,.4); border-radius:20px; padding:2px 7px; flex-shrink:0; }
  @media(max-width:900px){ .ui-grid,.ui-grid-3,.feat-index{ grid-template-columns:1fr; } }
</style>

<section id="t-overview" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 11.1 · The TOD 2.0 Video Experience</div>
    <h3>Watching becomes <span class="accent-purple">taking part.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">TOD360 is the next-generation player experience for TOD by beIN — designed to keep viewers immersed, in control, and connected. One design language across VOD and live sport, tuned per device, secured end to end.</p>
    <div class="grid-3" style="margin-top:40px;">
      <div class="card"><span class="number">01 · Immersive</span><h4 style="color:var(--tod-navy);">Content stays the hero</h4><p style="margin-top:10px;">Streamlined, intuitive controls that fade to keep viewers inside the content — smooth navigation on a film or a 90-minute match alike.</p></div>
      <div class="card"><span class="number">02 · Interactive</span><h4 style="color:var(--tod-navy);">Engage in real time</h4><p style="margin-top:10px;">The TOD360 layer adds timelines, stats, highlights, polls, and watch parties — a deeper connection with the game and with other fans.</p></div>
      <div class="card"><span class="number">03 · Secure</span><h4 style="color:var(--tod-navy);">Premium, protected</h4><p style="margin-top:10px;">DRM, watermarking, geo-fencing, and entitlement checks protect premium rights without getting in the viewer's way.</p></div>
    </div>
  </div>
</section>

<section id="t-platforms" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 11.2 · Platforms &amp; Phasing</div>
    <h3>Every screen. <span class="accent">Two phases.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">The experience spans Web, Mobile, TV, WebTV, and Huawei. Features roll out in two phases — Phase 1 at launch, Phase 2 as the experience deepens.</p>
    <div style="display:flex; gap:10px; flex-wrap:wrap; margin:28px 0 8px;">
      <span class="pill">Web</span><span class="pill">Mobile</span><span class="pill">TV</span><span class="pill">WebTV</span><span class="pill">Huawei</span>
    </div>
    <div style="display:flex; gap:16px; align-items:center; margin:24px 0 8px; font-size:13px;">''' + P1 + ''' <span style="opacity:.75;">Available at launch</span> &nbsp;&nbsp; ''' + P2 + ''' <span style="opacity:.75;">Proposed / next wave</span></div>
    <table class="data-table" style="margin-top:24px;">
      <thead><tr><th>Capability area</th><th>Highlights</th><th>Phase</th></tr></thead>
      <tbody>
        <tr><td><strong>VOD Player</strong></td><td>4K, seek preview, multi-audio &amp; subtitle, offline download, continue watching, PiP, skip intro</td><td>''' + P1 + '''</td></tr>
        <tr><td><strong>Live / Sport</strong></td><td>Go Live, channel switching, smart highlights, 4K, multi-audio, end-of-play for live</td><td>''' + P1 + '''</td></tr>
        <tr><td><strong>Interactive Timeline (OPTA)</strong></td><td>Key-moment markers, live commentary, match &amp; player stats</td><td>''' + P1 + '''</td></tr>
        <tr><td><strong>Fan Engagement</strong></td><td>Polls, trivia, predictions, watch party, chat, cheer meter</td><td>''' + P1 + '''</td></tr>
        <tr><td><strong>Multi-View &amp; Multi-Angle</strong></td><td>Multiple matches / angles on one screen, seamless switching</td><td>''' + P1 + '''</td></tr>
        <tr><td><strong>TOD One&nbsp;Play</strong></td><td>All language &amp; quality feeds in one place, saved preferences</td><td>''' + P2 + '''</td></tr>
        <tr><td><strong>Real-Time Alerts</strong></td><td>Cross-match key-event alerts with instant jump-to-action</td><td>''' + P2 + '''</td></tr>
        <tr><td><strong>HDR + Dolby · 50 FPS</strong></td><td>High-frame-rate, high-dynamic-range premium playback</td><td>''' + P2 + '''</td></tr>
      </tbody>
    </table>
  </div>
</section>

  <section class="chapter-divider">
    <div class="bg" style="background-image: url('./images/photos/generated/b11_vod.png');"></div>
    <div class="content-block">
      <div class="module-label">Book 11 · On Demand</div>
      <h2>The VOD player.</h2>
      <div class="tag-list">
        <span class="pill yellow-pill">TV Shows &amp; Film</span>
        <span class="pill">Controls</span>
        <span class="pill">End of Play</span>
      </div>
    </div>
    <div class="ch-badge"><span class="dot"></span> Section 11.3–11.4</div>
  </section>

<section id="t-vod" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 11.3 · VOD Player — Series &amp; Film</div>
    <h3>Streamlined controls. <span class="accent-purple">Effortless binge.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Built to enhance the overall viewing experience with seamless playback and a customisable, intuitive interface that keeps viewers immersed episode after episode.</p>
    <div class="grid-4" style="margin-top:40px;">
      <div class="card"><span class="number">Playback</span><h4 style="color:var(--tod-navy);">Core controls</h4><p style="margin-top:10px;">Play / pause, rewind &amp; forward, seek bar, volume, duration &amp; progress, full screen, back.</p></div>
      <div class="card"><span class="number">Quality</span><h4 style="color:var(--tod-navy);">Up to 4K</h4><p style="margin-top:10px;">4K VOD support, quality &amp; playback-speed switch, seek preview, and PiP for true multitasking.</p></div>
      <div class="card"><span class="number">Language</span><h4 style="color:var(--tod-navy);">Multi-audio &amp; subtitles</h4><p style="margin-top:10px;">Multiple audio languages, multi-subtitle (SRT) and CC support — bilingual by design (Book 03).</p></div>
      <div class="card"><span class="number">Continuity</span><h4 style="color:var(--tod-navy);">Pick up anywhere</h4><p style="margin-top:10px;">Continue watching, skip intro, next &amp; more episodes, offline download, screen lock, age/content rating on player.</p></div>
    </div>
    <div class="ui-shot" style="margin-top:44px;">
      <div class="bar"><i></i><i></i><i></i><span class="lbl">TOD · VOD Player — Web / TV</span></div>
      <img src="./images/tod360/vod-player.png" alt="TOD VOD player with seek-preview thumbnail, 4K badge and full control bar">
    </div>
    <div class="ui-cap">The VOD player — minimal chrome, seek-preview thumbnail, 4K badge, and the full control set fading over the content so the story stays the hero.</div>
    <div class="ui-grid">
      <div>
        <div class="ui-shot"><div class="bar"><i></i><i></i><i></i><span class="lbl">Episodes &amp; Seasons</span></div><img src="./images/tod360/vod-episodes.png" alt="Episode and season selector"></div>
        <div class="ui-cap">Season switcher and episode rail for effortless binge — next &amp; more episodes one tap away.</div>
      </div>
      <div>
        <div class="ui-shot"><div class="bar"><i></i><i></i><i></i><span class="lbl">Audio &amp; Subtitle</span></div><img src="./images/tod360/vod-audio-subtitle.png" alt="Audio and subtitle settings menu"></div>
        <div class="ui-cap">Multi-audio, multi-subtitle and CC — bilingual by design (Book 03).</div>
      </div>
      <div>
        <div class="ui-shot"><div class="bar"><i></i><i></i><i></i><span class="lbl">Quality &amp; Data</span></div><img src="./images/tod360/vod-quality.png" alt="Streaming quality selector"></div>
        <div class="ui-cap">Quality &amp; playback-speed switch, up to 4K, with a Data Saver option.</div>
      </div>
      <div>
        <div class="ui-shot"><div class="bar"><i></i><i></i><i></i><span class="lbl">Subtitle Styling</span></div><img src="./images/tod360/vod-subtitle-settings.png" alt="Subtitle size and colour customisation"></div>
        <div class="ui-cap">Viewer-controlled subtitle size and colour for an accessible, personal experience.</div>
      </div>
    </div>
  </div>
</section>

<section id="t-eop" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 11.4 · End-of-Play Experience</div>
    <h3>The story <span class="accent">never stops.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">As one title ends, an engaging Watch-Next screen keeps the journey going — surfacing the next episode or a smart recommendation before the viewer ever leaves.</p>
    <div class="grid-3" style="margin-top:40px;">
      <div class="card"><span class="number">Watch Next</span><h4>Auto next episode</h4><p style="margin-top:10px;">Next-episode and watch-credit handling keeps binge sessions seamless, with a clear, branded end card.</p></div>
      <div class="card"><span class="number">Recommend</span><h4>Smart suggestions</h4><p style="margin-top:10px;">Personalised recommendations surface the next thing to watch, tuned to the viewer's taste.</p></div>
      <div class="card"><span class="number">PopScene</span><h4>Moments that pop</h4><p style="margin-top:10px;">Signature in-player moments and the end-of-play experience reinforce the TOD by beIN brand at every hand-off.</p></div>
    </div>
    <div class="ui-grid">
      <div>
        <div class="ui-shot"><div class="bar"><i></i><i></i><i></i><span class="lbl">Watch Next — End Card</span></div><img src="./images/tod360/eop-watchnext.png" alt="End of play Watch Next screen with credits"></div>
        <div class="ui-cap">A branded Watch-Next card surfaces the next title before the credits finish.</div>
      </div>
      <div>
        <div class="ui-shot"><div class="bar"><i></i><i></i><i></i><span class="lbl">You May Like</span></div><img src="./images/tod360/eop-recommend.png" alt="You may like recommendations rail"></div>
        <div class="ui-cap">Personalised recommendations keep the journey going, tuned to the viewer's taste.</div>
      </div>
    </div>
  </div>
</section>

  <section class="chapter-divider">
    <div class="bg" style="background-image: url('./images/photos/generated/b11_sport.png');"></div>
    <div class="content-block">
      <div class="module-label">Book 11 · Live Sport</div>
      <h2>The sport player.</h2>
      <div class="tag-list">
        <span class="pill yellow-pill">Go Live</span>
        <span class="pill">Interactive Timeline</span>
        <span class="pill">Fan Engagement</span>
      </div>
    </div>
    <div class="ch-badge"><span class="dot"></span> Section 11.5–11.9</div>
  </section>

<section id="t-live" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 11.5 · Live &amp; Sport Player</div>
    <h3>At the heart <span class="accent-purple">of the action.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">A user-friendly interface keeps viewers focused on the live game — smooth, uninterrupted, and built for the moment. Instantly switch between live channels without missing a beat, with spoil-free updates for matches in progress.</p>
    <div class="grid-4" style="margin-top:40px;">
      <div class="card"><span class="number">Live controls</span><h4 style="color:var(--tod-navy);">Go Live &amp; switch</h4><p style="margin-top:10px;">Go-LIVE button, channel / event switching, volume, 4K quality switch, PiP, full screen.</p></div>
      <div class="card"><span class="number">Key Moment</span><h4 style="color:var(--tod-navy);">Jump to the action</h4><p style="margin-top:10px;">Real-time event markers let users jump straight to goals, substitutions, and highlights.</p></div>
      <div class="card"><span class="number">Audio</span><h4 style="color:var(--tod-navy);">Multi-language feeds</h4><p style="margin-top:10px;">Multiple audio &amp; commentary languages and quality options, per market.</p></div>
      <div class="card"><span class="number">Spoil-free</span><h4 style="color:var(--tod-navy);">Catch up safely</h4><p style="margin-top:10px;">Spoil-free updates for ongoing matches so late joiners stay in suspense.</p></div>
    </div>
    <div class="ui-shot" style="margin-top:44px;">
      <div class="bar"><i></i><i></i><i></i><span class="lbl">TOD · Live Sport Player</span></div>
      <img src="./images/tod360/live-player.png" alt="Live football player with Go Live timeline, key-moment popup and TOD 360 button">
    </div>
    <div class="ui-cap">Live football — the LIVE timeline, spoil-free score, an in-play key-moment popup, and the TOD 360 button that opens the interactive layer.</div>
    <div class="ui-grid">
      <div>
        <div class="ui-shot"><div class="bar"><i></i><i></i><i></i><span class="lbl">Channels &amp; Events</span></div><img src="./images/tod360/live-channels.png" alt="Live channels list overlay"></div>
        <div class="ui-cap">Switch between live channels and events without leaving full screen — never miss a beat.</div>
      </div>
      <div>
        <div class="ui-shot"><div class="bar"><i></i><i></i><i></i><span class="lbl">Smart Highlight</span></div><img src="./images/tod360/live-highlight.png" alt="Auto-generated highlight clip"></div>
        <div class="ui-cap">Auto-generated highlights let fans relive the best plays the instant they happen.</div>
      </div>
    </div>
  </div>
</section>

<section id="t-timeline" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 11.6 · Interactive Timeline &amp; Smart Highlights</div>
    <h3>Every key moment, <span class="accent">on a dynamic timeline.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Powered by OPTA data, the interactive timeline marks key moments — goals, tries, penalties, turnovers — and lets viewers move through the match while it happens.</p>
    <div class="grid-2" style="margin-top:40px; gap:24px;">
      <div class="card"><span class="number">Interactive Timeline</span><h4>Key moments, live</h4><p style="margin-top:10px;">A dynamic timeline keeps you in the action, with markers for every key event so you never scrub blindly.</p></div>
      <div class="card"><span class="number">Real-Time Commentary</span><h4>Live updates throughout</h4><p style="margin-top:10px;">Play-by-play commentary updates across the full match, right inside the player.</p></div>
      <div class="card"><span class="number">Match &amp; Player Stats</span><h4>Performance metrics</h4><p style="margin-top:10px;">Tackles, runs, points scored, and player metrics surfaced directly from the player interface.</p></div>
      <div class="card"><span class="number">Smart Highlights</span><h4>Relive it instantly</h4><p style="margin-top:10px;">Automatically generated key moments let fans relive the best plays the instant they happen.</p></div>
    </div>
    <div class="ui-grid">
      <div>
        <div class="ui-shot"><div class="bar"><i></i><i></i><i></i><span class="lbl">Key Moments — OPTA</span></div><img src="./images/tod360/live-keymoments.png" alt="Interactive key moments timeline panel"></div>
        <div class="ui-cap">Key Moments, Highlights, Lineups, Team Stats and Top Players — the TOD360 layer over the live feed.</div>
      </div>
      <div>
        <div class="ui-shot"><div class="bar"><i></i><i></i><i></i><span class="lbl">Match &amp; Team Stats</span></div><img src="./images/tod360/live-stats.png" alt="Live team and match statistics panel"></div>
        <div class="ui-cap">Possession, shots, corners and player metrics surfaced live from OPTA — without leaving the match.</div>
      </div>
    </div>
  </div>
</section>

<section id="t-fan" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 11.7 · Fan Mode &amp; Engagement</div>
    <h3>Watch together. <span class="accent-purple">Play along.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Fan Mode turns a stream into a shared event — stats, team and player updates, and interactive widgets that keep the audience excited and connected to friends and other fans in real time.</p>
    <div class="grid-3" style="margin-top:40px;">
      <div class="card"><span class="number">Fan Mode</span><h4 style="color:var(--tod-navy);">Stats &amp; updates</h4><p style="margin-top:10px;">Live stats, player and team updates, and informative widgets that keep fans informed without leaving the match.</p></div>
      <div class="card"><span class="number">Watch Party &amp; Chat</span><h4 style="color:var(--tod-navy);">Together, apart</h4><p style="margin-top:10px;">Watch parties and live chat connect fans with friends and the wider community in real time.</p></div>
      <div class="card"><span class="number">Interactive Widgets</span><h4 style="color:var(--tod-navy);">Play along</h4><p style="margin-top:10px;">Predictions, text &amp; image polls, emoji slider, image quiz, trivia, and a live cheer meter.</p></div>
    </div>
    <div style="display:flex; gap:10px; flex-wrap:wrap; margin-top:24px;">
      <span class="pill">Predictions</span><span class="pill">Text Poll</span><span class="pill">Image Poll</span><span class="pill">Emoji Slider</span><span class="pill">Image Quiz</span><span class="pill">Trivia</span><span class="pill">Cheer Meter</span>
    </div>
    <div class="ui-grid" style="grid-template-columns:300px 1fr; align-items:center;">
      <div>
        <div class="ui-phone"><img src="./images/tod360/fan-mobile.png" alt="Mobile Fan Zone with prediction, cheer meter and live poll"></div>
      </div>
      <div>
        <div class="ui-shot"><div class="bar"><i></i><i></i><i></i><span class="lbl">Mobile · Highlights Feed</span></div><img src="./images/tod360/live-mobile-highlights.png" alt="Mobile match highlights feed"></div>
        <div class="ui-cap">Fan Zone on mobile — Interacts, Group Chat, Influencer and Leaderboard tabs, with predictions, a cheer meter and live polls running alongside the match and a vertical highlights feed.</div>
      </div>
    </div>
  </div>
</section>

<section id="t-multiview" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 11.8 · Multi-View, OnePlay &amp; Alerts</div>
    <h3>Never miss <span class="accent">a moment, anywhere.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">For the fan following more than one game, TOD360 brings every feed, angle, and alert into a single, controllable experience.</p>
    <div class="grid-4" style="margin-top:40px;">
      <div class="card"><span class="number">Multi-View</span><h4>Many games, one screen</h4><p style="margin-top:10px;">Watch multiple live matches at once with multi-layouts, then switch between views without interrupting playback.</p></div>
      <div class="card"><span class="number">Multi-Angle</span><h4>Your point of view</h4><p style="margin-top:10px;">Different angles and feeds of the same event, on a single screen, under the viewer's control.</p></div>
      <div class="card"><span class="number">TOD One&nbsp;Play ''' + P2 + '''</span><h4>All feeds in one place</h4><p style="margin-top:10px;">Every language and quality feed in one player — no switching — with saved preferences applied automatically.</p></div>
      <div class="card"><span class="number">Real-Time Alerts ''' + P2 + '''</span><h4>Cross-match action</h4><p style="margin-top:10px;">Key-event alerts from other live matches with an instant jump-to-action, for a true multigame experience.</p></div>
    </div>
    <div class="ui-grid">
      <div>
        <div class="ui-shot"><div class="bar"><i></i><i></i><i></i><span class="lbl">Pick Your Live Events</span></div><img src="./images/tod360/multiview.png" alt="Multi-view layout picker — pick your live events"></div>
        <div class="ui-cap">Build a multi-view layout, then pick the live events to fill it — your screen, your games.</div>
      </div>
      <div>
        <div class="ui-shot"><div class="bar"><i></i><i></i><i></i><span class="lbl">Real-Time Alerts</span></div><img src="./images/tod360/alerts.png" alt="Cross-match real-time key-event alerts on the live player"></div>
        <div class="ui-cap">Cross-match key-event alerts appear over the live feed with an instant jump-to-action.</div>
      </div>
    </div>
  </div>
</section>

  <section class="chapter-divider">
    <div class="bg" style="background-image: url('./images/photos/generated/b11_security.png');"></div>
    <div class="content-block">
      <div class="module-label">Book 11 · Protected &amp; On-Brand</div>
      <h2>Security &amp; brand.</h2>
      <div class="tag-list">
        <span class="pill yellow-pill">DRM</span>
        <span class="pill">Analytics</span>
        <span class="pill">Brand in the Player</span>
      </div>
    </div>
    <div class="ch-badge"><span class="dot"></span> Section 11.9–11.10</div>
  </section>

<section id="t-security" class="light">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 11.9 · Security, DRM &amp; Analytics</div>
    <h3>Premium rights, <span class="accent-purple">protected end to end.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">Protecting premium sport and stories is non-negotiable. Security runs quietly beneath the experience; analytics keep quality honest.</p>
    <table class="data-table" style="margin-top:40px;">
      <thead><tr><th>Area</th><th>Capability</th></tr></thead>
      <tbody>
        <tr><td><strong>Anti-piracy</strong></td><td>Geo-fencing, app hardening, and code obfuscation</td></tr>
        <tr><td><strong>Entitlement</strong></td><td>Concurrency &amp; entitlement checks, device management</td></tr>
        <tr><td><strong>DRM</strong></td><td>DRM key rotation, forensic watermarking, secure DRM download</td></tr>
        <tr><td><strong>Analytics</strong></td><td>Conviva video / ECO quality-of-experience monitoring</td></tr>
      </tbody>
    </table>
    <div class="callout" style="background: rgba(255,199,44,.06); margin-top:24px;"><div class="label">Invisible by design</div><p>Security protects the rights without taxing the viewer. A legitimate user should never feel the DRM — only the seamless, premium experience.</p></div>
  </div>
</section>

<section id="t-brand" class="dark">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 11.10 · Brand in the Player</div>
    <h3>The product <span class="accent">is the brand.</span></h3>
    <p style="margin-top:18px; max-width:64ch;">TOD360 is where most people meet TOD by beIN. Every control, transition, and sound carries the system from the rest of this library.</p>
    <div class="grid-4" style="margin-top:40px;">
      <div class="card"><span class="number">Design</span><h4>Colour, type, components</h4><p style="margin-top:10px;">Player UI uses the locked palette, Alexandria, and components from <strong>Book 04</strong> — Navy surfaces, Yellow as the action accent.</p></div>
      <div class="card"><span class="number">Motion</span><h4>TOD ease, ≤300ms</h4><p style="margin-top:10px;">Controls and transitions follow <strong>Book 07</strong> motion — fast, purposeful, never decorative. Idents and the sonic sign moments.</p></div>
      <div class="card"><span class="number">Voice</span><h4>Bilingual &amp; clear</h4><p style="margin-top:10px;">Labels, empty states, and end cards follow <strong>Book 03</strong> — confident, warm, equal in Arabic &amp; English with correct RTL.</p></div>
      <div class="card"><span class="number">Accessibility</span><h4>Readable &amp; inclusive</h4><p style="margin-top:10px;">CC/subtitles, contrast, and touch targets meet the accessibility bar in <strong>Book 04</strong>. The premium experience is for everyone.</p></div>
    </div>
    <div class="callout locked" style="margin-top:24px;"><div class="label">Single point of entry</div><p>Player branding, new in-app features, and any change to the TOD360 experience are coordinated through <strong>brand@tod.tv</strong> with product (Book 09 governance).</p></div>
  </div>
</section>

<section id="t-index" class="deep">
  <div class="inner">
    <div class="chap-meta"><span class="line"></span> 11.11 · The TOD360 Feature Index</div>
    <h3>Everything TOD does, <span class="accent">on one page.</span></h3>
    <p style="margin-top:18px; max-width:66ch;">The complete capability set of the TOD360 experience, grouped by area. Items tagged ''' + P2 + ''' are proposed for the next wave; everything else is Phase&nbsp;1 at launch.</p>
    <div class="feat-index">
      <div class="feat-cat">
        <h4>VOD Player</h4><span class="cnt">Series &amp; Film · 14</span>
        <ul>
          <li>Play / pause</li><li>Rewind &amp; forward</li><li>Seek bar &amp; preview</li><li>Volume &amp; mute</li><li>Up to 4K</li><li>Quality switch</li><li>Playback speed</li><li>Picture-in-picture</li><li>Multi-audio</li><li>Multi-subtitle &amp; CC</li><li>Continue watching</li><li>Skip intro · next episode</li><li>Offline download</li><li>Age / content rating</li>
        </ul>
      </div>
      <div class="feat-cat">
        <h4>Live &amp; Sport Player</h4><span class="cnt">Built for the moment · 9</span>
        <ul>
          <li>Go Live</li><li>Channel &amp; event switching</li><li>Live channel list (EPG)</li><li>Up to 4K</li><li>Multi-language audio</li><li>Spoil-free updates</li><li>Picture-in-picture</li><li>Full screen</li><li>Smart highlights</li>
        </ul>
      </div>
      <div class="feat-cat">
        <h4>Interactive Timeline</h4><span class="cnt">Powered by OPTA · 7</span>
        <ul>
          <li>Key-moment markers</li><li>Real-time commentary</li><li>Match stats</li><li>Player stats</li><li>Team stats</li><li>Lineups</li><li>Top players</li>
        </ul>
      </div>
      <div class="feat-cat">
        <h4>Fan Mode &amp; Engagement</h4><span class="cnt">Watch together · 12</span>
        <ul>
          <li>Fan Zone</li><li>Group chat</li><li>Influencer feed</li><li>Leaderboard</li><li>Predictions</li><li>Text poll</li><li>Image poll</li><li>Emoji slider</li><li>Image quiz</li><li>Trivia</li><li>Cheer meter</li><li>Watch party</li>
        </ul>
      </div>
      <div class="feat-cat">
        <h4>Multi-View &amp; Angles</h4><span class="cnt">Many games, one screen · 6</span>
        <ul>
          <li>Multi-view layouts</li><li>Pick your live events</li><li>Multi-angle</li><li>Seamless switching</li><li>TOD OnePlay <span class="p2">P2</span></li><li>Real-time alerts <span class="p2">P2</span></li>
        </ul>
      </div>
      <div class="feat-cat">
        <h4>End of Play</h4><span class="cnt">The story never stops · 5</span>
        <ul>
          <li>Auto next episode</li><li>Watch credits</li><li>Smart recommendations</li><li>You May Like rail</li><li>Branded end card</li>
        </ul>
      </div>
      <div class="feat-cat">
        <h4>Premium Playback</h4><span class="cnt">Picture &amp; sound · 3</span>
        <ul>
          <li>4K Ultra HD</li><li>HDR + Dolby <span class="p2">P2</span></li><li>50 FPS high frame rate <span class="p2">P2</span></li>
        </ul>
      </div>
      <div class="feat-cat">
        <h4>Security &amp; DRM</h4><span class="cnt">Protected end to end · 9</span>
        <ul>
          <li>Geo-fencing</li><li>App hardening</li><li>Code obfuscation</li><li>Concurrency checks</li><li>Entitlement checks</li><li>Device management</li><li>DRM key rotation</li><li>Forensic watermarking</li><li>Secure download</li>
        </ul>
      </div>
      <div class="feat-cat">
        <h4>Quality &amp; Analytics</h4><span class="cnt">Honest performance · 4</span>
        <ul>
          <li>Conviva QoE monitoring</li><li>Playback diagnostics</li><li>Buffering &amp; bitrate insight</li><li>Cross-platform metrics</li>
        </ul>
      </div>
    </div>
    <div style="display:flex; gap:18px; flex-wrap:wrap; margin-top:30px; font-size:13px; opacity:.7;">
      <span>5 platforms — Web · Mobile · TV · WebTV · Huawei</span><span>·</span><span>69 features across 9 areas</span><span>·</span><span>4 proposed for Phase 2</span>
    </div>
  </div>
</section>
'''

THIS_LINKS = '''  <a class="nav-item" href="#t-overview" data-close><span class="num">11.1</span> The TOD 2.0 Experience</a>
  <a class="nav-item" href="#t-platforms" data-close><span class="num">11.2</span> Platforms &amp; Phasing</a>
  <a class="nav-item" href="#t-vod" data-close><span class="num">11.3</span> VOD Player</a>
  <a class="nav-item" href="#t-eop" data-close><span class="num">11.4</span> End-of-Play</a>
  <a class="nav-item" href="#t-live" data-close><span class="num">11.5</span> Live &amp; Sport Player</a>
  <a class="nav-item" href="#t-timeline" data-close><span class="num">11.6</span> Timeline &amp; Highlights</a>
  <a class="nav-item" href="#t-fan" data-close><span class="num">11.7</span> Fan Mode &amp; Engagement</a>
  <a class="nav-item" href="#t-multiview" data-close><span class="num">11.8</span> Multi-View &amp; OnePlay</a>
  <a class="nav-item" href="#t-security" data-close><span class="num">11.9</span> Security &amp; Analytics</a>
  <a class="nav-item" href="#t-brand" data-close><span class="num">11.10</span> Brand in the Player</a>
  <a class="nav-item" href="#t-index" data-close><span class="num">11.11</span> Feature Index</a>
'''

bg.build(
    title='TOD by beIN — Book 11 · TOD360 Features',
    active_idx='11',
    this_links=THIS_LINKS,
    cover=COVER,
    body=BODY,
    out='Book11_TOD360_Features.html',
    topbar_label='<strong>Book 11</strong> · TOD360 Features · Locked Reference',
)
