"""
╔══════════════════════════════════════════════════════════╗
║       RAMADAN APP — Day 1 + Day 2 + Day 3 + Day 4        ║
║  Day 1 : renderRamadanHero()    →  HTML Hero Section     ║
║  Day 2 : nextPrayerIndex()      →  Prayer Scheduler      ║
║  Day 3 : tasbihSessionStats()   →  Tasbih Counter        ║
║  Day 4 : typedProfileSummary()  →  Profile Label         ║
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
#  DAY 3 — Tasbih Counter
#  tasbihSessionStats(target, current)
# ══════════════════════════════════════════════════════════

def tasbihSessionStats(target: int, current: int) -> dict:
    """
    Returns session statistics for a Tasbih (dhikr) counting session.

    Args:
        target  (int): The goal — total number of repetitions to complete.
        current (int): How many repetitions have been done so far.

    Returns:
        dict: {
            "total"     : int  → the original target (unchanged),
            "remaining" : int  → how many left (never below 0),
            "done"      : int  → how many completed (clamped to target),
            "percent"   : int  → completion percentage (0–100)
        }

    Key rule:
        remaining can NEVER go below zero, even if current > target.
        Uses max(0, target - current) to clamp the value.
    """
    remaining = max(0, target - current)          # ← clamp: never negative
    done      = min(current, target)              # ← clamp: never above target
    percent   = round((done / target) * 100) if target > 0 else 0

    return {
        "total"    : target,
        "remaining": remaining,
        "done"     : done,
        "percent"  : percent,
    }


# ══════════════════════════════════════════════════════════
#  DAY 4 — TypeScript Profile Label (Python equivalent)
#  typedProfileSummary(name, role)
# ══════════════════════════════════════════════════════════

def typedProfileSummary(name: str, role: str = "Student") -> str:
    """
    Returns a formatted profile label: "<name> (<role>)".
    Mirrors TypeScript's optional parameter pattern.

    TypeScript signature:
        function typedProfileSummary(name: string, role: string = "Student"): string

    Args:
        name (str)          : The person's display name.
        role (str, optional): Their role/title. Defaults to "Student" if omitted.

    Returns:
        str: Formatted as "name (role)"

    Python ↔ TypeScript mapping:
        Python  → def typedProfileSummary(name: str, role: str = "Student") -> str
        TS      → function typedProfileSummary(name: string, role: string = "Student"): string
    """
    resolved_role = role.strip() if role and role.strip() else "Student"
    return f"{name} ({resolved_role})"


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

    /* ═══════════════════════════════════════
       DAY 3 — TASBIH COUNTER WIDGET
    ════════════════════════════════════════ */
    .tasbih-section {{
      position: relative; z-index: 2;
      width: 100%; max-width: 700px;
      margin: 0 auto 5rem;
      padding: 0 1.5rem;
      animation: fadeSlideDown .8s 1s ease both;
    }}
    .tasbih-section__label {{
      text-align: center;
      font-size: .7rem; letter-spacing: .3em;
      text-transform: uppercase; color: var(--gold);
      margin-bottom: 1.5rem; opacity: .8;
    }}
    .tasbih-panel {{
      background: rgba(255,255,255,.03);
      border: 1px solid rgba(201,168,76,.15);
      border-radius: 16px;
      padding: 2rem 1.5rem;
      display: flex; flex-direction: column;
      align-items: center; gap: 1.5rem;
    }}

    /* Dhikr selector tabs */
    .dhikr-tabs {{
      display: flex; gap: .6rem; flex-wrap: wrap;
      justify-content: center;
    }}
    .dhikr-tab {{
      background: transparent;
      border: 1px solid rgba(201,168,76,.25);
      border-radius: 20px;
      color: rgba(245,240,232,.5);
      font-family: 'Lato', sans-serif;
      font-size: .72rem; letter-spacing: .08em;
      padding: .4rem 1rem; cursor: pointer;
      transition: all .2s ease;
    }}
    .dhikr-tab.active,
    .dhikr-tab:hover {{
      background: rgba(201,168,76,.15);
      border-color: var(--gold);
      color: var(--gold-light);
    }}

    /* Big counter button */
    .tasbih-btn {{
      width: 160px; height: 160px;
      border-radius: 50%;
      background: radial-gradient(circle at 35% 35%,
        rgba(201,168,76,.25) 0%,
        rgba(201,168,76,.08) 60%,
        transparent 100%);
      border: 2px solid rgba(201,168,76,.4);
      cursor: pointer;
      display: flex; flex-direction: column;
      align-items: center; justify-content: center;
      transition: transform .1s ease, box-shadow .2s ease, border-color .2s ease;
      box-shadow: 0 0 30px rgba(201,168,76,.1);
      position: relative;
      -webkit-tap-highlight-color: transparent;
    }}
    .tasbih-btn:hover {{
      border-color: var(--gold);
      box-shadow: 0 0 40px rgba(201,168,76,.25);
    }}
    .tasbih-btn:active {{
      transform: scale(.94);
      box-shadow: 0 0 50px rgba(201,168,76,.4);
    }}
    .tasbih-btn.complete {{
      border-color: #2E7D5E;
      box-shadow: 0 0 40px rgba(46,125,94,.3);
      background: radial-gradient(circle at 35% 35%,
        rgba(46,125,94,.2) 0%,
        transparent 70%);
    }}
    .tasbih-count {{
      font-family: 'Cinzel Decorative', serif;
      font-size: 3rem; font-weight: 700;
      color: var(--gold); line-height: 1;
    }}
    .tasbih-btn.complete .tasbih-count {{ color: #4CAF82; }}
    .tasbih-tap-hint {{
      font-size: .65rem; letter-spacing: .12em;
      text-transform: uppercase;
      color: rgba(245,240,232,.3); margin-top: .3rem;
    }}

    /* Progress ring */
    .progress-ring-wrap {{
      position: absolute; inset: -8px;
      pointer-events: none;
    }}
    .progress-ring {{
      width: 100%; height: 100%;
      transform: rotate(-90deg);
    }}
    .progress-ring__bg {{
      fill: none; stroke: rgba(201,168,76,.1); stroke-width: 3;
    }}
    .progress-ring__fill {{
      fill: none; stroke: var(--gold); stroke-width: 3;
      stroke-linecap: round;
      transition: stroke-dashoffset .4s ease;
    }}

    /* Stats row */
    .tasbih-stats {{
      display: grid; grid-template-columns: repeat(3,1fr);
      gap: .75rem; width: 100%;
    }}
    .stat-box {{
      background: rgba(255,255,255,.04);
      border: 1px solid rgba(201,168,76,.1);
      border-radius: 10px;
      padding: .8rem .5rem;
      text-align: center;
    }}
    .stat-box__val {{
      font-family: 'Cinzel Decorative', serif;
      font-size: 1.4rem; color: var(--gold-light);
    }}
    .stat-box__label {{
      font-size: .65rem; letter-spacing: .1em;
      text-transform: uppercase;
      color: rgba(245,240,232,.4); margin-top: .2rem;
    }}

    /* Progress bar */
    .progress-bar-wrap {{
      width: 100%;
    }}
    .progress-bar-track {{
      width: 100%; height: 6px;
      background: rgba(255,255,255,.06);
      border-radius: 3px; overflow: hidden;
    }}
    .progress-bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, var(--gold-light), var(--gold));
      border-radius: 3px;
      transition: width .4s ease;
    }}
    .progress-bar-fill.complete {{
      background: linear-gradient(90deg, #4CAF82, #2E7D5E);
    }}
    .progress-label {{
      display: flex; justify-content: space-between;
      font-size: .68rem; color: rgba(245,240,232,.4);
      margin-top: .4rem;
    }}

    /* Reset button */
    .tasbih-reset {{
      background: transparent;
      border: 1px solid rgba(255,255,255,.1);
      border-radius: 4px;
      color: rgba(245,240,232,.35);
      font-family: 'Lato', sans-serif;
      font-size: .7rem; letter-spacing: .1em;
      text-transform: uppercase;
      padding: .4rem 1.2rem; cursor: pointer;
      transition: all .2s ease;
    }}
    .tasbih-reset:hover {{
      border-color: rgba(255,100,100,.4);
      color: rgba(255,130,130,.7);
    }}

    /* Completion flash */
    @keyframes completeFlash {{
      0%   {{ box-shadow: 0 0 0   rgba(46,125,94,0); }}
      50%  {{ box-shadow: 0 0 60px rgba(46,125,94,.6); }}
      100% {{ box-shadow: 0 0 30px rgba(46,125,94,.2); }}
    }}
    .tasbih-btn.just-complete {{
      animation: completeFlash .6s ease;
    }}

    /* ═══════════════════════════════════════
       DAY 4 — PROFILE LABEL WIDGET
    ════════════════════════════════════════ */
    .profile-section {{
      position: relative; z-index: 2;
      width: 100%; max-width: 700px;
      margin: 0 auto 5rem;
      padding: 0 1.5rem;
      animation: fadeSlideDown .8s 1.2s ease both;
    }}
    .profile-section__label {{
      text-align: center;
      font-size: .7rem; letter-spacing: .3em;
      text-transform: uppercase; color: var(--gold);
      margin-bottom: 1.5rem; opacity: .8;
    }}
    .profile-panel {{
      background: rgba(255,255,255,.03);
      border: 1px solid rgba(201,168,76,.15);
      border-radius: 16px;
      padding: 2rem 2rem;
      display: flex; flex-direction: column;
      gap: 1.5rem;
    }}

    /* Input row */
    .profile-inputs {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
    }}
    @media (max-width: 480px) {{
      .profile-inputs {{ grid-template-columns: 1fr; }}
    }}
    .profile-field {{
      display: flex; flex-direction: column; gap: .4rem;
    }}
    .profile-field label {{
      font-size: .68rem; letter-spacing: .15em;
      text-transform: uppercase;
      color: rgba(245,240,232,.4);
    }}
    .profile-field input {{
      background: rgba(255,255,255,.05);
      border: 1px solid rgba(201,168,76,.2);
      border-radius: 6px;
      color: var(--white);
      font-family: 'Lato', sans-serif;
      font-size: .95rem;
      padding: .65rem .9rem;
      outline: none;
      transition: border-color .2s ease, box-shadow .2s ease;
    }}
    .profile-field input::placeholder {{
      color: rgba(245,240,232,.2);
    }}
    .profile-field input:focus {{
      border-color: var(--gold);
      box-shadow: 0 0 0 3px rgba(201,168,76,.1);
    }}

    /* Output label display */
    .profile-output-wrap {{
      display: flex; flex-direction: column;
      align-items: center; gap: .75rem;
    }}
    .profile-output-hint {{
      font-size: .68rem; letter-spacing: .1em;
      text-transform: uppercase;
      color: rgba(245,240,232,.3);
    }}
    .profile-output {{
      font-family: 'Cinzel Decorative', serif;
      font-size: clamp(1.1rem, 3vw, 1.7rem);
      color: var(--gold-light);
      text-align: center;
      background: rgba(201,168,76,.07);
      border: 1px solid rgba(201,168,76,.25);
      border-radius: 8px;
      padding: .9rem 2rem;
      min-width: 260px;
      letter-spacing: .04em;
      transition: all .25s ease;
      word-break: break-word;
    }}
    .profile-output .role-part {{
      color: rgba(201,168,76,.65);
    }}
    .profile-output.default-role .role-part {{
      color: rgba(245,240,232,.35);
      font-style: italic;
    }}

    /* TypeScript badge */
    .ts-badge {{
      display: inline-flex; align-items: center; gap: .4rem;
      background: rgba(49,120,198,.15);
      border: 1px solid rgba(49,120,198,.3);
      border-radius: 4px;
      padding: .3rem .8rem;
      font-size: .68rem; letter-spacing: .08em;
      color: #6ab0f5;
    }}
    .ts-dot {{
      width: 8px; height: 8px;
      background: #3178c6;
      border-radius: 2px;
      flex-shrink: 0;
    }}

    /* Signature line */
    .profile-signature {{
      background: rgba(0,0,0,.25);
      border: 1px solid rgba(255,255,255,.06);
      border-radius: 6px;
      padding: .7rem 1rem;
      font-size: .72rem;
      color: rgba(245,240,232,.3);
      font-family: 'Courier New', monospace;
      letter-spacing: .02em;
      text-align: center;
    }}
    .profile-signature .kw  {{ color: #c678dd; }}
    .profile-signature .fn  {{ color: #61afef; }}
    .profile-signature .param {{ color: #e5c07b; }}
    .profile-signature .type  {{ color: #56b6c2; }}
    .profile-signature .def   {{ color: #98c379; }}
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

      <!-- ── Tasbih Counter Widget (Day 3) ── -->
      <section class="tasbih-section" id="tasbih" aria-label="Tasbih Counter">
        <p class="tasbih-section__label">✦ Tasbih Counter ✦</p>

        <div class="tasbih-panel">

          <!-- Dhikr selector -->
          <div class="dhikr-tabs" role="tablist" id="dhikrTabs">
            <!-- Filled by JS -->
          </div>

          <!-- Big tap button with SVG ring -->
          <div style="position:relative; width:176px; height:176px;">
            <button class="tasbih-btn" id="tasbihBtn"
                    aria-label="Tap to count" aria-live="polite">
              <div class="progress-ring-wrap">
                <svg class="progress-ring" viewBox="0 0 176 176">
                  <circle class="progress-ring__bg" cx="88" cy="88" r="82"/>
                  <circle class="progress-ring__fill" id="progressRing"
                          cx="88" cy="88" r="82"
                          stroke-dasharray="515"
                          stroke-dashoffset="515"/>
                </svg>
              </div>
              <div class="tasbih-count" id="tasbihCount">0</div>
              <div class="tasbih-tap-hint">tap to count</div>
            </button>
          </div>

          <!-- Stats row -->
          <div class="tasbih-stats">
            <div class="stat-box">
              <div class="stat-box__val" id="statDone">0</div>
              <div class="stat-box__label">Done</div>
            </div>
            <div class="stat-box">
              <div class="stat-box__val" id="statTotal">33</div>
              <div class="stat-box__label">Target</div>
            </div>
            <div class="stat-box">
              <div class="stat-box__val" id="statRemaining">33</div>
              <div class="stat-box__label">Remaining</div>
            </div>
          </div>

          <!-- Progress bar -->
          <div class="progress-bar-wrap">
            <div class="progress-bar-track">
              <div class="progress-bar-fill" id="progressBar" style="width:0%"></div>
            </div>
            <div class="progress-label">
              <span id="progressPct">0%</span>
              <span id="progressStatus">Keep going...</span>
            </div>
          </div>

          <!-- Reset -->
          <button class="tasbih-reset" id="tasbihReset">↺ Reset</button>

        </div>
      </section>

      <!-- ── Profile Label Widget (Day 4) ── -->
      <section class="profile-section" id="profile" aria-label="Profile Label Generator">
        <p class="profile-section__label">✦ Profile Label ✦</p>

        <div class="profile-panel">

          <!-- TypeScript badge -->
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:.5rem;">
            <span style="font-size:.75rem; color:rgba(245,240,232,.4); letter-spacing:.05em;">
              TypeScript Optional Parameter Demo
            </span>
            <span class="ts-badge">
              <span class="ts-dot"></span>
              TypeScript
            </span>
          </div>

          <!-- TS function signature -->
          <div class="profile-signature" aria-label="TypeScript function signature">
            <span class="kw">function</span>
            <span class="fn"> typedProfileSummary</span>(<span class="param">name</span>:
            <span class="type">string</span>,
            <span class="param"> role</span>:
            <span class="type">string</span> =
            <span class="def">"Student"</span>):
            <span class="type">string</span>
          </div>

          <!-- Inputs -->
          <div class="profile-inputs">
            <div class="profile-field">
              <label for="profileName">Name</label>
              <input type="text" id="profileName"
                     placeholder="e.g. Ali Hassan"
                     maxlength="40" />
            </div>
            <div class="profile-field">
              <label for="profileRole">Role <span style="opacity:.4;">(optional)</span></label>
              <input type="text" id="profileRole"
                     placeholder='leave blank → "Student"'
                     maxlength="40" />
            </div>
          </div>

          <!-- Live output -->
          <div class="profile-output-wrap">
            <span class="profile-output-hint">→ typedProfileSummary() returns</span>
            <div class="profile-output default-role" id="profileOutput">
              <span id="profileNamePart">Name</span>
              <span class="role-part"> (Student)</span>
            </div>
          </div>

        </div>
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

  <!-- ════════════════════════════════════════════
       DAY 3 — tasbihSessionStats  (JavaScript)
  ═════════════════════════════════════════════ -->
  <script>
    // ─────────────────────────────────────────────
    //  tasbihSessionStats
    //  @param {{number}} target  - goal repetitions
    //  @param {{number}} current - repetitions done so far
    //  @returns {{{{ total, remaining, done, percent }}}}
    //  KEY RULE: remaining is NEVER below zero (Math.max clamp)
    // ─────────────────────────────────────────────
    function tasbihSessionStats(target, current) {{
      const remaining = Math.max(0, target - current);   // ← clamp: never negative
      const done      = Math.min(current, target);       // ← clamp: never above target
      const percent   = target > 0 ? Math.round((done / target) * 100) : 0;
      return {{ total: target, remaining, done, percent }};
    }}

    // ── Dhikr options ──
    const DHIKR = [
      {{ label: "SubhanAllah",    arabic: "سُبْحَانَ ٱللَّٰهِ",   target: 33  }},
      {{ label: "Alhamdulillah",  arabic: "ٱلْحَمْدُ لِلَّٰهِ", target: 33  }},
      {{ label: "Allahu Akbar",   arabic: "ٱللَّٰهُ أَكْبَرُ",   target: 34  }},
      {{ label: "Astaghfirullah", arabic: "أَسْتَغْفِرُ ٱللَّٰهَ", target: 100 }},
    ];

    // ── State ──
    let currentDhikr  = 0;
    let count         = 0;
    const CIRCUMF     = 2 * Math.PI * 82;   // r=82 → 515.2

    // ── DOM refs ──
    const btn          = document.getElementById("tasbihBtn");
    const countEl      = document.getElementById("tasbihCount");
    const statDone     = document.getElementById("statDone");
    const statTotal    = document.getElementById("statTotal");
    const statRem      = document.getElementById("statRemaining");
    const progressBar  = document.getElementById("progressBar");
    const progressRing = document.getElementById("progressRing");
    const progressPct  = document.getElementById("progressPct");
    const progressStat = document.getElementById("progressStatus");
    const resetBtn     = document.getElementById("tasbihReset");
    const tabsEl       = document.getElementById("dhikrTabs");

    // ── Build tabs ──
    function buildTabs() {{
      tabsEl.innerHTML = DHIKR.map((d, i) => `
        <button class="dhikr-tab ${{i === currentDhikr ? 'active' : ''}}"
                onclick="selectDhikr(${{i}})"
                aria-label="Select ${{d.label}}">
          ${{d.label}} (${{d.target}})
        </button>
      `).join("");
    }}

    function selectDhikr(i) {{
      currentDhikr = i;
      count = 0;
      buildTabs();
      updateUI();
    }}

    // ── Core UI update — calls tasbihSessionStats ──
    function updateUI() {{
      const dhikr  = DHIKR[currentDhikr];
      const stats  = tasbihSessionStats(dhikr.target, count);  // ← Day 3 function
      const isComplete = stats.remaining === 0;

      // Counter number
      countEl.textContent = count;

      // Stat boxes
      statDone.textContent  = stats.done;
      statTotal.textContent = stats.total;
      statRem.textContent   = stats.remaining;

      // Progress bar
      progressBar.style.width = stats.percent + "%";
      progressPct.textContent = stats.percent + "%";
      progressBar.classList.toggle("complete", isComplete);

      // Status label
      if (isComplete) {{
        progressStat.textContent = "✓ Complete! Masha'Allah!";
        progressStat.style.color = "#4CAF82";
      }} else if (stats.percent >= 75) {{
        progressStat.textContent = "Almost there...";
        progressStat.style.color = "rgba(245,240,232,.6)";
      }} else {{
        progressStat.textContent = "Keep going...";
        progressStat.style.color = "rgba(245,240,232,.4)";
      }}

      // SVG ring
      const offset = CIRCUMF - (stats.percent / 100) * CIRCUMF;
      progressRing.style.strokeDashoffset = offset;
      progressRing.style.stroke = isComplete ? "#4CAF82" : "var(--gold)";

      // Button state
      btn.classList.toggle("complete", isComplete);
    }}

    // ── Tap handler ──
    btn.addEventListener("click", () => {{
      const target = DHIKR[currentDhikr].target;
      if (count >= target) return;           // stop at target
      count++;
      const wasComplete = count === target;
      updateUI();
      if (wasComplete) {{
        btn.classList.add("just-complete");
        setTimeout(() => btn.classList.remove("just-complete"), 700);
      }}
    }});

    // ── Reset handler ──
    resetBtn.addEventListener("click", () => {{
      count = 0;
      updateUI();
    }});

    // ── Init ──
    buildTabs();
    updateUI();
  </script>

  <!-- ════════════════════════════════════════════
       DAY 4 — typedProfileSummary  (TypeScript → JS)
  ═════════════════════════════════════════════ -->
  <script>
    // ─────────────────────────────────────────────
    //  typedProfileSummary
    //  TypeScript: function typedProfileSummary(name: string, role: string = "Student"): string
    //  @param {{string}} name          - person's display name
    //  @param {{string}} [role]        - optional role; defaults to "Student"
    //  @returns {{string}}             - formatted as "name (role)"
    //
    //  Key rule: if role is missing/empty → fall back to "Student"
    // ─────────────────────────────────────────────
    function typedProfileSummary(name, role = "Student") {{
      const resolvedRole = role || "Student";    // guard: catches empty string ""
      return `${{name}} (${{resolvedRole}})`;
    }}

    // ── DOM refs ──
    const nameInput    = document.getElementById("profileName");
    const roleInput    = document.getElementById("profileRole");
    const outputBox    = document.getElementById("profileOutput");
    const namePart     = document.getElementById("profileNamePart");

    // ── Live update ──
    function updateProfile() {{
      const name = nameInput.value.trim() || "Name";
      const role = roleInput.value.trim();         // empty string → default kicks in

      const label        = typedProfileSummary(name, role);  // ← Day 4 function
      const isDefault    = !role;                            // true if role was omitted

      // Parse out name and role parts for styled rendering
      const match        = label.match(/^(.+) [(](.+)[)]$/);
      if (match) {{
        namePart.textContent = match[1];
        outputBox.querySelector(".role-part").textContent = ` (${{match[2]}})`;
      }}

      // Toggle italic style when showing default "Student"
      outputBox.classList.toggle("default-role", isDefault);
    }}

    nameInput.addEventListener("input", updateProfile);
    roleInput.addEventListener("input", updateProfile);

    // Seed with demo values
    nameInput.value = "Ali Hassan";
    updateProfile();
  </script>

</body>
</html>"""

    return html


# ══════════════════════════════════════════════════════════
#  TESTS — typedProfileSummary
# ══════════════════════════════════════════════════════════

def run_profile_tests():
    test_cases = [
        # (name,    role,        expected,               description)
        ("Ali",    "Engineer",  "Ali (Engineer)",        "Both name & role provided"),
        ("Sara",   "Designer",  "Sara (Designer)",       "Different role"),
        ("Omar",   None,        "Omar (Student)",        "Role is None → default"),
        ("Omar",   "",          "Omar (Student)",        "Role is empty string → default"),
        ("Zara",   "Student",   "Zara (Student)",        "Role explicitly set to Student"),
        ("",       "Engineer",  " (Engineer)",           "Empty name edge case"),
        ("Ali",    "  ",        "Ali (Student)",         "Whitespace-only role → default"),
        ("Hassan", "Dev",       "Hassan (Dev)",          "Short role"),
    ]

    print("=" * 65)
    print("  typedProfileSummary — Test Results")
    print("=" * 65)
    all_pass = True
    for name, role, expected, desc in test_cases:
        result = typedProfileSummary(name) if role is None else typedProfileSummary(name, role)
        # treat whitespace-only as empty for the guard
        passed = result == expected
        status = "✅ PASS" if passed else "❌ FAIL"
        if not passed: all_pass = False
        role_display = repr(role) if role is not None else "NOT PROVIDED"
        print(f"  {status}  {desc}")
        print(f"         Input  : name={repr(name)}, role={role_display}")
        print(f"         Output : {repr(result)}   expected: {repr(expected)}")
        print()
    print("=" * 65)
    print(f"  {'All tests passed! 🎉' if all_pass else 'Some tests failed ❌'}")
    print("=" * 65)


# ══════════════════════════════════════════════════════════
#  TESTS — tasbihSessionStats
# ══════════════════════════════════════════════════════════

def run_tasbih_tests():
    test_cases = [
        # (target, current, expected_total, expected_remaining, expected_done, expected_pct, description)
        (100,  0,   100, 100,  0,   0,   "Not started"),
        (100, 50,   100,  50, 50,  50,   "Halfway done"),
        (100, 100,  100,   0, 100, 100,  "Exactly complete"),
        (100, 120,  100,   0, 100, 100,  "Overshot → remaining clamped to 0"),
        (33,  10,    33,  23,  10,  30,  "SubhanAllah — 10 done"),
        (33,  33,    33,   0,  33, 100,  "SubhanAllah — complete"),
        (0,    0,     0,   0,   0,   0,  "Zero target edge case"),
        (34,  20,    34,  14,  20,  59,  "Allahu Akbar — 20 done"),
    ]

    print("=" * 65)
    print("  tasbihSessionStats — Test Results")
    print("=" * 65)
    all_pass = True
    for target, current, exp_total, exp_rem, exp_done, exp_pct, desc in test_cases:
        result = tasbihSessionStats(target, current)
        passed = (
            result["total"]     == exp_total and
            result["remaining"] == exp_rem   and
            result["done"]      == exp_done  and
            result["percent"]   == exp_pct
        )
        status = "✅ PASS" if passed else "❌ FAIL"
        if not passed: all_pass = False
        print(f"  {status}  {desc}")
        print(f"         Input  : target={target}, current={current}")
        print(f"         Output : total={result['total']}, done={result['done']}, "
              f"remaining={result['remaining']}, percent={result['percent']}%")
        print()
    print("=" * 65)
    print(f"  {'All tests passed! 🎉' if all_pass else 'Some tests failed ❌'}")
    print("=" * 65)


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

    # ── Day 4 tests ──
    run_profile_tests()
    print()

    # ── Day 3 tests ──
    run_tasbih_tests()
    print()

    # ── Day 2 tests ──
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