def renderRamadanHero(title: str, cta_text: str) -> str:
    """
    Renders a semantic HTML hero section for Ramadan landing page.

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
  <title>Ramadan Hero</title>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Lato:wght@300;400&display=swap" rel="stylesheet"/>
  <style>
    *, *::before, *::after {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }}

    :root {{
      --gold:       #C9A84C;
      --gold-light: #EDD690;
      --deep-blue:  #0B1A2E;
      --mid-blue:   #122340;
      --white:      #F5F0E8;
      --accent:     #7B4F9E;
    }}

    body {{
      background: var(--deep-blue);
      font-family: 'Lato', sans-serif;
    }}

    /* ── HERO SECTION ── */
    .hero {{
      position: relative;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      background: radial-gradient(ellipse at 50% 0%,
        #1a2f50 0%,
        #0B1A2E 60%,
        #060e1a 100%);
    }}

    /* Star field */
    .hero::before {{
      content: '';
      position: absolute;
      inset: 0;
      background-image:
        radial-gradient(1px 1px at 10%  20%, rgba(255,255,255,0.8) 0%, transparent 100%),
        radial-gradient(1px 1px at 30%  50%, rgba(255,255,255,0.6) 0%, transparent 100%),
        radial-gradient(1px 1px at 55%  10%, rgba(255,255,255,0.9) 0%, transparent 100%),
        radial-gradient(1px 1px at 75%  35%, rgba(255,255,255,0.7) 0%, transparent 100%),
        radial-gradient(1px 1px at 90%  60%, rgba(255,255,255,0.5) 0%, transparent 100%),
        radial-gradient(1.5px 1.5px at 20% 75%, rgba(255,255,255,0.8) 0%, transparent 100%),
        radial-gradient(1px 1px at 45%  85%, rgba(255,255,255,0.6) 0%, transparent 100%),
        radial-gradient(1px 1px at 65%  70%, rgba(255,255,255,0.4) 0%, transparent 100%),
        radial-gradient(2px 2px at 80%  15%, rgba(201,168,76,0.9)  0%, transparent 100%),
        radial-gradient(1px 1px at 5%   90%, rgba(255,255,255,0.7) 0%, transparent 100%);
      pointer-events: none;
    }}

    /* Glow orb */
    .hero::after {{
      content: '';
      position: absolute;
      top: -10%;
      left: 50%;
      transform: translateX(-50%);
      width: 600px;
      height: 600px;
      background: radial-gradient(circle,
        rgba(123,79,158,0.15) 0%,
        rgba(201,168,76,0.08) 40%,
        transparent 70%);
      pointer-events: none;
    }}

    /* ── CRESCENT MOON ── */
    .moon-wrap {{
      position: relative;
      width: 120px;
      height: 120px;
      margin: 0 auto 2rem;
      animation: floatMoon 6s ease-in-out infinite;
    }}

    .moon {{
      width: 100px;
      height: 100px;
      border-radius: 50%;
      background: transparent;
      box-shadow: 28px -8px 0 8px var(--gold);
      filter: drop-shadow(0 0 18px rgba(201,168,76,0.7));
      margin: 10px auto 0;
    }}

    .star-deco {{
      position: absolute;
      top: 0;
      right: 0;
      font-size: 1.6rem;
      color: var(--gold-light);
      animation: twinkle 2s ease-in-out infinite alternate;
    }}

    /* ── CONTENT BOX ── */
    .hero__content {{
      position: relative;
      z-index: 2;
      text-align: center;
      padding: 3rem 2rem;
      max-width: 760px;
    }}

    .hero__badge {{
      display: inline-block;
      font-family: 'Lato', sans-serif;
      font-weight: 300;
      font-size: 0.75rem;
      letter-spacing: 0.35em;
      text-transform: uppercase;
      color: var(--gold);
      border: 1px solid rgba(201,168,76,0.4);
      border-radius: 2px;
      padding: 0.4rem 1.2rem;
      margin-bottom: 2rem;
      animation: fadeSlideDown 0.8s ease both;
    }}

    .hero__title {{
      font-family: 'Cinzel Decorative', serif;
      font-size: clamp(2.2rem, 6vw, 4.5rem);
      font-weight: 700;
      line-height: 1.15;
      color: var(--white);
      text-shadow: 0 0 40px rgba(201,168,76,0.3);
      animation: fadeSlideDown 0.8s 0.2s ease both;
      margin-bottom: 1.5rem;
    }}

    .hero__title span {{
      background: linear-gradient(135deg, var(--gold-light), var(--gold), #a07830);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }}

    .hero__subtitle {{
      font-family: 'Lato', sans-serif;
      font-weight: 300;
      font-size: clamp(1rem, 2vw, 1.2rem);
      color: rgba(245,240,232,0.65);
      letter-spacing: 0.04em;
      line-height: 1.8;
      max-width: 500px;
      margin: 0 auto 2.5rem;
      animation: fadeSlideDown 0.8s 0.4s ease both;
    }}

    /* ── DIVIDER ── */
    .divider {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 1rem;
      margin-bottom: 2.5rem;
      animation: fadeSlideDown 0.8s 0.5s ease both;
    }}

    .divider__line {{
      width: 80px;
      height: 1px;
      background: linear-gradient(to right, transparent, var(--gold));
    }}

    .divider__line:last-child {{
      background: linear-gradient(to left, transparent, var(--gold));
    }}

    .divider__icon {{
      color: var(--gold);
      font-size: 1.1rem;
    }}

    /* ── CTA BUTTON ── */
    .hero__cta {{
      display: inline-block;
      text-decoration: none;
      font-family: 'Lato', sans-serif;
      font-weight: 400;
      font-size: 0.9rem;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: var(--deep-blue);
      background: linear-gradient(135deg, var(--gold-light) 0%, var(--gold) 100%);
      padding: 1rem 3rem;
      border-radius: 2px;
      border: none;
      cursor: pointer;
      position: relative;
      overflow: hidden;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      box-shadow: 0 4px 24px rgba(201,168,76,0.35);
      animation: fadeSlideDown 0.8s 0.6s ease both;
    }}

    .hero__cta::before {{
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(135deg, rgba(255,255,255,0.25), transparent);
      opacity: 0;
      transition: opacity 0.3s ease;
    }}

    .hero__cta:hover {{
      transform: translateY(-3px);
      box-shadow: 0 8px 32px rgba(201,168,76,0.5);
    }}

    .hero__cta:hover::before {{
      opacity: 1;
    }}

    /* ── LANTERNS ── */
    .lanterns {{
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      display: flex;
      justify-content: space-around;
      padding: 0 5%;
      pointer-events: none;
    }}

    .lantern {{
      font-size: 2.5rem;
      animation: swingLantern 4s ease-in-out infinite;
      transform-origin: top center;
      opacity: 0.75;
    }}

    .lantern:nth-child(2) {{ animation-delay: -1.3s; font-size: 2rem; }}
    .lantern:nth-child(3) {{ animation-delay: -2.6s; }}

    /* ── BOTTOM ARCH ── */
    .arch {{
      position: absolute;
      bottom: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 100%;
      max-width: 900px;
      height: 80px;
      border-top: 1px solid rgba(201,168,76,0.2);
      border-radius: 50% 50% 0 0 / 80px 80px 0 0;
      pointer-events: none;
    }}

    /* ── ANIMATIONS ── */
    @keyframes fadeSlideDown {{
      from {{ opacity: 0; transform: translateY(-20px); }}
      to   {{ opacity: 1; transform: translateY(0);     }}
    }}

    @keyframes floatMoon {{
      0%, 100% {{ transform: translateY(0);    }}
      50%       {{ transform: translateY(-14px); }}
    }}

    @keyframes twinkle {{
      from {{ opacity: 0.4; transform: scale(0.9); }}
      to   {{ opacity: 1.0; transform: scale(1.1); }}
    }}

    @keyframes swingLantern {{
      0%, 100% {{ transform: rotate(-8deg); }}
      50%       {{ transform: rotate( 8deg); }}
    }}
  </style>
</head>
<body>

  <!-- ═══════════════════════════════════════════
       SEMANTIC HERO SECTION
  ════════════════════════════════════════════ -->
  <header>
    <section class="hero" aria-label="Ramadan Hero Banner">

      <!-- Decorative lanterns -->
      <div class="lanterns" aria-hidden="true">
        <span class="lantern">🪔</span>
        <span class="lantern">🏮</span>
        <span class="lantern">🪔</span>
      </div>

      <!-- Main content -->
      <div class="hero__content">

        <!-- Badge -->
        <p class="hero__badge">✦ Ramadan Kareem ✦</p>

        <!-- Crescent moon icon -->
        <div class="moon-wrap" aria-hidden="true">
          <div class="moon"></div>
          <span class="star-deco">★</span>
        </div>

        <!-- H1 — dynamic title -->
        <h1 class="hero__title">
          <span>{title}</span>
        </h1>

        <!-- Supporting text -->
        <p class="hero__subtitle">
          A blessed month of reflection, gratitude, and togetherness.
          May this Ramadan fill your heart with peace and your home with light.
        </p>

        <!-- Ornamental divider -->
        <div class="divider" aria-hidden="true">
          <div class="divider__line"></div>
          <span class="divider__icon">☽</span>
          <div class="divider__line"></div>
        </div>

        <!-- CTA — dynamic cta_text -->
        <a href="#" class="hero__cta" role="button">
          {cta_text}
        </a>

      </div><!-- /.hero__content -->

      <!-- Decorative arch -->
      <div class="arch" aria-hidden="true"></div>

    </section>
  </header>

</body>
</html>"""

    return html


# ══════════════════════════════════════════
#  USAGE EXAMPLES
# ══════════════════════════════════════════

if __name__ == "__main__":

    # ── Example 1: Default Ramadan greeting ──
    html_output = renderRamadanHero(
        title    = "Ramadan Mubarak",
        cta_text = "Begin Your Journey"
    )

    # Save to file so you can open in a browser
    with open("ramadan_hero_output.html", "w", encoding="utf-8") as f:
        f.write(html_output)

    print("✅ Hero section generated!")
    print(f"   Characters in output : {len(html_output)}")
    print(f"   Saved to             : ramadan_hero_output.html")
    print()

    # ── Example 2: Charity campaign variant ──
    html_charity = renderRamadanHero(
        title    = "Give. Reflect. Unite.",
        cta_text = "Donate Your Zakat"
    )

    print("✅ Charity variant generated!")
    print(f"   Characters in output : {len(html_charity)}")
    print()

    # ── Example 3: E-commerce variant ──
    html_shop = renderRamadanHero(
        title    = "Light Up This Ramadan",
        cta_text = "Shop Ramadan Gifts"
    )

    print("✅ Shop variant generated!")
    print(f"   Characters in output : {len(html_shop)}")
