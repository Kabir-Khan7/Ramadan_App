"""
╔══════════════════════════════════════════════════════════╗
║       RAMADAN APP — Day 1 + Day 2 Combined               ║
║  Day 1 : renderRamadanHero()  →  HTML Hero Section       ║
║  Day 2 : nextPrayerIndex()    →  Prayer Scheduler        ║
╚══════════════════════════════════════════════════════════╝
"""

# ══════════════════════════════════════════════════════════
#  DAY 2 — JavaScript Logic (implemented in Python too)
#  nextPrayerIndex(currentMinutes, prayerMinutes)
# ══════════════════════════════════════════════════════════

def nextPrayerIndex(currentMinutes: int, prayerMinutes: list) -> int:
    """
    Returns the index of the next upcoming prayer.

    Args:
        currentMinutes (int)  : Current time expressed as minutes from midnight.
                                e.g. 1:30 PM = 13*60 + 30 = 810
        prayerMinutes  (list) : Sorted list of prayer times in minutes.
                                e.g. [300, 750, 945, 1095, 1200]

    Returns:
        int: Index of the next prayer in prayerMinutes.
             Returns 0 if all prayers have passed (rollover to next day).

    Logic:
        - Loop through each prayer time in order.
        - First prayer whose time is GREATER than currentMinutes → that's next.
        - If none found → all prayers passed → return 0 (Fajr tomorrow).
    """
    for i in range(len(prayerMinutes)):
        if prayerMinutes[i] > currentMinutes:
            return i          # ← next prayer found today

    return 0                  # ← rollover: next day's Fajr


# ══════════════════════════════════════════════════════════
#  DAY 1 — HTML Hero Builder
#  renderRamadanHero(title, cta_text)
#  Now ENHANCED: injects live prayer schedule via JS
# ══════════════════════════════════════════════════════════

def renderRamadanHero(title: str, cta_text: str) -> str:
    """
    Renders a semantic HTML hero section for a Ramadan landing page.
    Includes a live Prayer Scheduler widget powered by nextPrayerIndex JS logic.

    Args:
        title    (str): The main headline text displayed in the hero.
        cta_text (str): The call-to-action button label.

    Returns:
        str: A complete, semantic HTML string for the hero section.
    """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Ramadan — {title}</title>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Lato:wght@300;400;700&display=swap" rel="stylesheet"/>
  <style>
    *, *::before, *::after {{
      margin: 0; padding: 0; box-sizing: border-box;
    }}
    :root {{
      --gold:       #C9A84C;
      --gold-light: #EDD690;
      --deep-blue:  #0B1A2E;
      --mid-blue:   #122340;
      --white:      #F5F0E8;
      --accent:     #7B4F9E;
      --green:      #2E7D5E;
    }}
    body {{
      background: var(--deep-blue);
      font-family: 'Lato', sans-serif;
    }}

    /* ───── HERO ───── */
    .hero {{
      position: relative;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      background: radial-gradient(ellipse at 50% 0%, #1a2f50 0%, #0B1A2E 60%, #060e1a 100%);
    }}
    .hero::before {{
      content: '';
      position: absolute;
      inset: 0;
      background-image:
        radial-gradient(1px 1px at 10% 20%,  rgba(255,255,255,.8) 0%,transparent 100%),
        radial-gradient(1px 1px at 30% 50%,  rgba(255,255,255,.6) 0%,transparent 100%),
        radial-gradient(1px 1px at 55% 10%,  rgba(255,255,255,.9) 0%,transparent 100%),
        radial-gradient(1px 1px at 75% 35%,  rgba(255,255,255,.7) 0%,transparent 100%),
        radial-gradient(1px 1px at 90% 60%,  rgba(255,255,255,.5) 0%,transparent 100%),
        radial-gradient(1.5px 1.5px at 20% 75%,rgba(255,255,255,.8) 0%,transparent 100%),
        radial-gradient(1px 1px at 45% 85%,  rgba(255,255,255,.6) 0%,transparent 100%),
        radial-gradient(1px 1px at 65% 70%,  rgba(255,255,255,.4) 0%,transparent 100%),
        radial-gradient(2px 2px at 80% 15%,  rgba(201,168,76,.9)  0%,transparent 100%),
        radial-gradient(1px 1px at 5%  90%,  rgba(255,255,255,.7) 0%,transparent 100%);
      pointer-events: none;
    }}
    .hero::after {{
      content: '';
      position: absolute;
      top: -10%; left: 50%;
      transform: translateX(-50%);
      width: 600px; height: 600px;
      background: radial-gradient(circle,
        rgba(123,79,158,.15) 0%,
        rgba(201,168,76,.08) 40%,
        transparent 70%);
      pointer-events: none;
    }}

    /* ───── MOON ───── */
    .moon-wrap {{
      position: relative;
      width: 120px; height: 120px;
      margin: 0 auto 2rem;
      animation: floatMoon 6s ease-in-out infinite;
    }}
    .moon {{
      width: 100px; height: 100px;
      border-radius: 50%;
      background: transparent;
      box-shadow: 28px -8px 0 8px var(--gold);
      filter: drop-shadow(0 0 18px rgba(201,168,76,.7));
      margin: 10px auto 0;
    }}
    .star-deco {{
      position: absolute; top: 0; right: 0;
      font-size: 1.6rem; color: var(--gold-light);
      animation: twinkle 2s ease-in-out infinite alternate;
    }}

    /* ───── CONTENT ───── */
    .hero__content {{
      position: relative; z-index: 2;
      text-align: center;
      padding: 3rem 2rem;
      max-width: 760px;
    }}
    .hero__badge {{
      display: inline-block;
      font-weight: 300; font-size: .75rem;
      letter-spacing: .35em; text-transform: uppercase;
      color: var(--gold);
      border: 1px solid rgba(201,168,76,.4);
      border-radius: 2px;
      padding: .4rem 1.2rem; margin-bottom: 2rem;
      animation: fadeSlideDown .8s ease both;
    }}
    .hero__title {{
      font-family: 'Cinzel Decorative', serif;
      font-size: clamp(2.2rem, 6vw, 4.5rem);
      font-weight: 700; line-height: 1.15;
      color: var(--white);
      text-shadow: 0 0 40px rgba(201,168,76,.3);
      animation: fadeSlideDown .8s .2s ease both;
      margin-bottom: 1.5rem;
    }}
    .hero__title span {{
      background: linear-gradient(135deg, var(--gold-light), var(--gold), #a07830);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }}
    .hero__subtitle {{
      font-weight: 300;
      font-size: clamp(1rem, 2vw, 1.2rem);
      color: rgba(245,240,232,.65);
      letter-spacing: .04em; line-height: 1.8;
      max-width: 500px; margin: 0 auto 2.5rem;
      animation: fadeSlideDown .8s .4s ease both;
    }}
    .divider {{
      display: flex; align-items: center;
      justify-content: center; gap: 1rem;
      margin-bottom: 2.5rem;
      animation: fadeSlideDown .8s .5s ease both;
    }}
    .divider__line {{
      width: 80px; height: 1px;
      background: linear-gradient(to right, transparent, var(--gold));
    }}
    .divider__line:last-child {{
      background: linear-gradient(to left, transparent, var(--gold));
    }}
    .divider__icon {{ color: var(--gold); font-size: 1.1rem; }}
    .hero__cta {{
      display: inline-block; text-decoration: none;
      font-weight: 400; font-size: .9rem;
      letter-spacing: .2em; text-transform: uppercase;
      color: var(--deep-blue);
      background: linear-gradient(135deg, var(--gold-light) 0%, var(--gold) 100%);
      padding: 1rem 3rem; border-radius: 2px;
      border: none; cursor: pointer;
      position: relative; overflow: hidden;
      transition: transform .3s ease, box-shadow .3s ease;
      box-shadow: 0 4px 24px rgba(201,168,76,.35);
      animation: fadeSlideDown .8s .6s ease both;
    }}
    .hero__cta:hover {{
      transform: translateY(-3px);
      box-shadow: 0 8px 32px rgba(201,168,76,.5);
    }}

    /* ───── LANTERNS ───── */
    .lanterns {{
      position: absolute; top: 0; left: 0; right: 0;
      display: flex; justify-content: space-around;
      padding: 0 5%; pointer-events: none;
    }}
    .lantern {{
      font-size: 2.5rem;
      animation: swingLantern 4s ease-in-out infinite;
      transform-origin: top center; opacity: .75;
    }}
    .lantern:nth-child(2) {{ animation-delay: -1.3s; font-size: 2rem; }}
    .lantern:nth-child(3) {{ animation-delay: -2.6s; }}

    /* ───── ARCH ───── */
    .arch {{
      position: absolute; bottom: 0; left: 50%;
      transform: translateX(-50%);
      width: 100%; max-width: 900px; height: 80px;
      border-top: 1px solid rgba(201,168,76,.2);
      border-radius: 50% 50% 0 0 / 80px 80px 0 0;
      pointer-events: none;
    }}

    /* ═══════════════════════════════════════
       DAY 2 — PRAYER SCHEDULER WIDGET
    ════════════════════════════════════════ */
    .prayer-section {{
      position: relative; z-index: 2;
      width: 100%; max-width: 700px;
      margin: 0 auto 4rem;
      padding: 0 1.5rem;
      animation: fadeSlideDown .8s .8s ease both;
    }}
    .prayer-section__label {{
      text-align: center;
      font-size: .7rem; letter-spacing: .3em;
      text-transform: uppercase; color: var(--gold);
      margin-bottom: 1.2rem; opacity: .8;
    }}
    .prayer-grid {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: .75rem;
    }}
    .prayer-card {{
      background: rgba(255,255,255,.04);
      border: 1px solid rgba(201,168,76,.15);
      border-radius: 8px;
      padding: .9rem .5rem;
      text-align: center;
      transition: all .3s ease;
      cursor: default;
    }}
    .prayer-card.active {{
      background: rgba(201,168,76,.12);
      border-color: var(--gold);
      box-shadow: 0 0 20px rgba(201,168,76,.2), inset 0 0 20px rgba(201,168,76,.05);
      transform: translateY(-4px);
    }}
    .prayer-card__icon {{ font-size: 1.4rem; margin-bottom: .4rem; }}
    .prayer-card__name {{
      font-size: .7rem; letter-spacing: .1em;
      text-transform: uppercase; color: rgba(245,240,232,.5);
      margin-bottom: .3rem;
    }}
    .prayer-card.active .prayer-card__name {{ color: var(--gold-light); }}
    .prayer-card__time {{
      font-size: .95rem; font-weight: 700;
      color: var(--white); letter-spacing: .05em;
    }}
    .prayer-card.active .prayer-card__time {{ color: var(--gold); }}
    .prayer-card__badge {{
      display: none;
      font-size: .6rem; letter-spacing: .12em;
      text-transform: uppercase;
      background: var(--gold);
      color: var(--deep-blue);
      border-radius: 20px;
      padding: .2rem .6rem;
      margin-top: .4rem;
      font-weight: 700;
    }}
    .prayer-card.active .prayer-card__badge {{ display: inline-block; }}

    .countdown-wrap {{
      margin-top: 1rem;
      text-align: center;
      color: rgba(245,240,232,.5);
      font-size: .8rem; letter-spacing: .08em;
    }}
    .countdown-wrap span {{
      color: var(--gold-light); font-weight: 700;
    }}

    /* ───── ANIMATIONS ───── */
    @keyframes fadeSlideDown {{
      from {{ opacity: 0; transform: translateY(-20px); }}
      to   {{ opacity: 1; transform: translateY(0);     }}
    }}
    @keyframes floatMoon {{
      0%,100% {{ transform: translateY(0);     }}
      50%      {{ transform: translateY(-14px); }}
    }}
    @keyframes twinkle {{
      from {{ opacity: .4; transform: scale(.9); }}
      to   {{ opacity: 1;  transform: scale(1.1); }}
    }}
    @keyframes swingLantern {{
      0%,100% {{ transform: rotate(-8deg); }}
      50%      {{ transform: rotate( 8deg); }}
    }}

    @media (max-width: 520px) {{
      .prayer-grid {{ grid-template-columns: repeat(3,1fr); }}
    }}
  </style>
</head>
<body>

  <header>
    <section class="hero" aria-label="Ramadan Hero Banner">

      <!-- Decorative lanterns -->
      <div class="lanterns" aria-hidden="true">
        <span class="lantern">🪔</span>
        <span class="lantern">🏮</span>
        <span class="lantern">🪔</span>
      </div>

      <!-- ── Hero Content (Day 1) ── -->
      <div class="hero__content">
        <p class="hero__badge">✦ Ramadan Kareem ✦</p>

        <div class="moon-wrap" aria-hidden="true">
          <div class="moon"></div>
          <span class="star-deco">★</span>
        </div>

        <h1 class="hero__title">
          <span>{title}</span>
        </h1>

        <p class="hero__subtitle">
          A blessed month of reflection, gratitude, and togetherness.
          May this Ramadan fill your heart with peace and your home with light.
        </p>

        <div class="divider" aria-hidden="true">
          <div class="divider__line"></div>
          <span class="divider__icon">☽</span>
          <div class="divider__line"></div>
        </div>

        <a href="#prayer-times" class="hero__cta" role="button">
          {cta_text}
        </a>
      </div>

      <!-- ── Prayer Scheduler Widget (Day 2) ── -->
      <section class="prayer-section" id="prayer-times" aria-label="Today's Prayer Times">
        <p class="prayer-section__label">Today's Prayer Times</p>

        <div class="prayer-grid" id="prayerGrid">
          <!-- Filled by JS -->
        </div>

        <p class="countdown-wrap" id="countdownWrap">
          Next prayer in <span id="countdownTimer">--:--</span>
        </p>
      </section>

      <div class="arch" aria-hidden="true"></div>
    </section>
  </header>

  <!-- ════════════════════════════════════════════
       DAY 2 — nextPrayerIndex  (JavaScript)
  ═════════════════════════════════════════════ -->
  <script>
    // ─────────────────────────────────────────────
    //  nextPrayerIndex
    //  @param {{number}} currentMinutes  - current time in minutes from midnight
    //  @param {{number[]}} prayerMinutes - sorted array of prayer times in minutes
    //  @returns {{number}} index of next prayer (0 = rollover to Fajr next day)
    // ─────────────────────────────────────────────
    function nextPrayerIndex(currentMinutes, prayerMinutes) {{
      for (let i = 0; i < prayerMinutes.length; i++) {{
        if (prayerMinutes[i] > currentMinutes) {{
          return i;          // next prayer found today
        }}
      }}
      return 0;              // all prayers passed → rollover (Fajr tomorrow)
    }}

    // ── Prayer data ──
    const PRAYERS = [
      {{ name: "Fajr",    icon: "🌙", minutes: 300  }},   // 05:00
      {{ name: "Dhuhr",   icon: "☀️", minutes: 750  }},   // 12:30
      {{ name: "Asr",     icon: "🌤️", minutes: 945  }},   // 15:45
      {{ name: "Maghrib", icon: "🌅", minutes: 1095 }},   // 18:15
      {{ name: "Isha",    icon: "🌃", minutes: 1200 }},   // 20:00
    ];

    // ── Helper: minutes → "HH:MM AM/PM" ──
    function minsToTime(m) {{
      const h24 = Math.floor(m / 60);
      const mm  = String(m % 60).padStart(2, "0");
      const h12 = h24 % 12 || 12;
      const ampm = h24 < 12 ? "AM" : "PM";
      return `${{h12}}:${{mm}} ${{ampm}}`;
    }}

    // ── Helper: minutes → "Xh Ym" ──
    function minsToCountdown(m) {{
      if (m < 0) m += 1440;           // handle midnight rollover
      const h = Math.floor(m / 60);
      const s = m % 60;
      return h > 0 ? `${{h}}h ${{s}}m` : `${{s}}m`;
    }}

    // ── Render the prayer grid ──
    function renderPrayerGrid() {{
      const now     = new Date();
      const curMins = now.getHours() * 60 + now.getMinutes();
      const pMins   = PRAYERS.map(p => p.minutes);
      const nextIdx = nextPrayerIndex(curMins, pMins);   // ← Day 2 function

      const grid = document.getElementById("prayerGrid");
      grid.innerHTML = PRAYERS.map((p, i) => `
        <div class="prayer-card ${{i === nextIdx ? 'active' : ''}}"
             aria-label="${{p.name}} at ${{minsToTime(p.minutes)}}">
          <div class="prayer-card__icon">${{p.icon}}</div>
          <div class="prayer-card__name">${{p.name}}</div>
          <div class="prayer-card__time">${{minsToTime(p.minutes)}}</div>
          <div class="prayer-card__badge">Next ↑</div>
        </div>
      `).join("");

      // ── Countdown ──
      const nextMins  = PRAYERS[nextIdx].minutes;
      const diff      = nextMins > curMins ? nextMins - curMins : (1440 - curMins) + nextMins;
      const rollover  = nextIdx === 0 && curMins > PRAYERS[PRAYERS.length - 1].minutes;
      const label     = rollover ? "Tomorrow's Fajr in" : "Next prayer in";
      document.getElementById("countdownWrap").innerHTML =
        `${{label}} <span id="countdownTimer">${{minsToCountdown(diff)}}</span>`;
    }}

    // Initial render + refresh every minute
    renderPrayerGrid();
    setInterval(renderPrayerGrid, 60_000);
  </script>

</body>
</html>"""

    return html


# ══════════════════════════════════════════════════════════
#  TESTS — nextPrayerIndex
# ══════════════════════════════════════════════════════════

def run_tests():
    prayers = [300, 750, 945, 1095, 1200]
    names   = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]

    test_cases = [
        (100,  0, "Before Fajr → Fajr"),
        (300,  1, "Exactly on Fajr → Dhuhr"),
        (800,  2, "After Dhuhr → Asr"),
        (945,  3, "Exactly on Asr → Maghrib"),
        (1100, 4, "After Maghrib → Isha"),
        (1250, 0, "After Isha → rollover Fajr"),
        (1440, 0, "Midnight → rollover Fajr"),
        (0,    0, "00:00 → Fajr"),
    ]

    print("=" * 55)
    print("  nextPrayerIndex — Test Results")
    print("=" * 55)
    all_pass = True
    for current, expected, description in test_cases:
        result  = nextPrayerIndex(current, prayers)
        status  = "✅ PASS" if result == expected else "❌ FAIL"
        if result != expected:
            all_pass = False
        h, m    = divmod(current, 60)
        print(f"  {status}  {description}")
        print(f"         Input: {h:02d}:{m:02d}  →  Got index {result} ({names[result]}), Expected {expected} ({names[expected]})")
        print()
    print("=" * 55)
    print(f"  {'All tests passed! 🎉' if all_pass else 'Some tests failed ❌'}")
    print("=" * 55)


# ══════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════

if __name__ == "__main__":

    # ── Run tests first ──
    run_tests()
    print()

    # ── Generate the combined HTML page ──
    html_output = renderRamadanHero(
        title    = "Ramadan Mubarak",
        cta_text = "View Prayer Times"
    )

    with open("ramadan_app_output.html", "w", encoding="utf-8") as f:
        f.write(html_output)

    print(f"✅ Combined app generated → ramadan_app_output.html")
    print(f"   Characters : {len(html_output)}")
    print(f"   Open the HTML file in your browser to see the full app!")
