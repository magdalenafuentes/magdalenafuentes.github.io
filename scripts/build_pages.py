#!/usr/bin/env python3
"""Generate static HTML pages for the Magdalena Fuentes academic site."""

from pathlib import Path

from papers import PAPERS

ROOT = Path(__file__).resolve().parents[1]


def asset(prefix: str, path: str) -> str:
    return f"{prefix}{path}"


def nav_items(prefix: str, current: str) -> str:
    depth = 0 if prefix == "assets/" else 1 if prefix == "../assets/" else 2
    home = "./" if depth == 0 else "../" * depth
    publications = f"{home}publications/"
    people = f"{home}people/"
    activities = f"{home}activities/"
    resources = f"{home}resources/"
    links = [
        ("home", home if depth else "./", "Home"),
        ("publications", publications, "Publications"),
        ("people", people, "People"),
        ("activities", activities, "Activities"),
        ("resources", resources, "Resources"),
    ]
    html = []
    for key, href, label in links:
        current_attr = ' aria-current="page"' if key == current else ""
        html.append(f'<li><a href="{href}"{current_attr}><span>{label}</span></a></li>')
    return "\n            ".join(html)


def icons() -> dict:
    return {
        "scholar": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3L1 9l4 2.18v6L12 21l7-3.82v-6l2-1.09V17h2V9L12 3zm6.82 6L12 12.72 5.18 9 12 5.28 18.82 9zM17 15.99l-5 2.73-5-2.73v-3.72L12 15l5-2.73v3.72z"/></svg>',
        "linkedin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>',
        "github": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.387.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61-.546-1.387-1.333-1.757-1.333-1.757-1.09-.745.084-.729.084-.729 1.205.084 1.84 1.236 1.84 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>',
        "orcid": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 0C5.372 0 0 5.372 0 12s5.372 12 12 12 12-5.372 12-12S18.628 0 12 0zM7.37 4.368c.745 0 1.33.615 1.33 1.358 0 .745-.585 1.353-1.33 1.353-.746 0-1.348-.608-1.348-1.353 0-.743.602-1.358 1.348-1.358zm.955 3.497v10.272H6.418V7.865h1.907zm3.032 0h3.636c3.494 0 5.04 2.184 5.04 5.137 0 3.012-1.81 5.135-5.415 5.135h-3.261V7.865zm1.907 1.69v6.89h1.588c2.294 0 3.41-1.274 3.41-3.409 0-2.18-1.085-3.481-3.341-3.481h-1.657z"/></svg>',
        "email": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>',
    }


def layout(title: str, current: str, prefix: str, body: str, home: bool = False) -> str:
    ic = icons()
    nav = nav_items(prefix, current)
    body_class = "page-home" if home else f"page-{current}"
    page_title = "Magdalena Fuentes" if home else f"{title} – Magdalena Fuentes"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{page_title}</title>
  <meta name="description" content="Assistant Professor of Music Technology and Integrated Design &amp; Media at New York University. Machine listening, music information retrieval, and multimodal sound analysis.">
  <link rel="icon" href="{prefix}images/cropped-icon.jpeg" type="image/jpeg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,400;0,600;0,700;1,400;1,600;1,700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{prefix}css/style.css">
</head>
<body class="{body_class}">
  <div class="mobile-nav" id="mobile-nav">
    <button class="mobile-close" type="button" aria-label="Close menu">&times;</button>
    <ul>
            {nav}
    </ul>
  </div>
  <header class="site-header">
    <div class="container header-inner">
      <a class="logo" href="{'./' if prefix == 'assets/' else '../' if prefix == '../assets/' else '../../'}">
        <img class="logo-light" src="{prefix}images/logo-white.svg" alt="Magdalena Fuentes">
        <img class="logo-dark" src="{prefix}images/logo.svg" alt="Magdalena Fuentes">
      </a>
      <nav class="desktop-nav" aria-label="Primary">
        <ul class="nav-list">
            {nav}
        </ul>
      </nav>
      <button class="menu-toggle" type="button" aria-label="Open menu"><span></span></button>
    </div>
  </header>
  {body}
  <footer class="site-footer">
    <div class="container">
      <ul class="socials">
        <li><a href="https://scholar.google.com/citations?user=gz7oJAoAAAAJ" target="_blank" rel="noopener"> {ic['scholar']} <span>Google Scholar</span></a></li>
        <li><a href="https://www.linkedin.com/in/mfu3ntes/" target="_blank" rel="noopener"> {ic['linkedin']} <span>LinkedIn</span></a></li>
        <li><a href="https://github.com/magdalenafuentes" target="_blank" rel="noopener"> {ic['github']} <span>GitHub</span></a></li>
        <li><a href="https://orcid.org/0000-0003-4506-6639" target="_blank" rel="noopener"> {ic['orcid']} <span>ORCID</span></a></li>
        <li><a href="mailto:mfuentes@nyu.edu"> {ic['email']} <span>Email</span></a></li>
      </ul>
    </div>
  </footer>
  <script src="{prefix}js/main.js"></script>
</body>
</html>
"""


def home() -> str:
    prefix = "assets/"
    body = f"""
  <main>
    <section class="hero">
      <div class="container">
        <div class="hero-grid hero-desktop">
          <div>
            <h1 class="hero-name reveal-left">Magdalena Fuentes</h1>
            <img class="hero-portrait reveal-left" src="{prefix}images/portrait.png" alt="Portrait of Magdalena Fuentes">
          </div>
          <div>
            <img class="hero-kicker reveal" src="{prefix}images/pattern-home.png" alt="">
            <div class="hero-bio reveal">
              <p>I am Assistant Professor of Music Technology and Integrated Design &amp; Media at New York University. My students and I are part of the Music and Audio Research Laboratory (MARL) and the Integrated Design &amp; Media (IDM) program. I grew up in Uruguay, studied electrical engineering at Universidad de la República, and did my Ph.D. at Université Paris-Saclay. I work on machine listening: signal processing and machine learning that help computers make sense of music and the sounds around us.</p>
              <p>I’m interested in methods at the intersection of sound, vision, and language, and in applying them to music information retrieval, environmental sound analysis, multimodal analysis and synthesis, and accessibility and health. I also spend time teaching and building research communities, especially around Latin American music and audio.</p>
            </div>
          </div>
        </div>
        <div class="hero-mobile">
          <h1 class="hero-name reveal-left">Magdalena Fuentes</h1>
          <p class="hero-subtitle reveal-left">Multimodal Adaptive Audio<br>and Music Processing</p>
          <img class="hero-portrait reveal-left" src="{prefix}images/portrait.png" alt="Portrait of Magdalena Fuentes">
          <div class="hero-bio reveal">
            <p>I am Assistant Professor of Music Technology and Integrated Design &amp; Media at New York University. My students and I are part of the Music and Audio Research Laboratory (MARL) and the Integrated Design &amp; Media (IDM) program. I grew up in Uruguay, studied electrical engineering at Universidad de la República, and did my Ph.D. at Université Paris-Saclay. I work on machine listening: signal processing and machine learning that help computers make sense of music and the sounds around us.</p>
            <p>I’m interested in methods at the intersection of sound, vision, and language, and in applying them to music information retrieval, environmental sound analysis, multimodal analysis and synthesis, and accessibility and health. I also spend time teaching and building research communities, especially around Latin American music and audio.</p>
          </div>
        </div>
      </div>
    </section>
    <section class="affiliations">
      <div class="container affiliations-inner">
        <div></div>
        <div class="reveal">
          <h2>Affiliations</h2>
          <h3>Assistant Professor of Interactive Design, Music and Sound</h3>
          <p>New York University<br>
            <a href="https://steinhardt.nyu.edu/music/technology/">Music Technology</a> at Steinhardt School of Culture, Education, and Human Development.<br>
            <a href="https://idm.engineering.nyu.edu/">Integrated Design &amp; Media (IDM)</a> at Tandon School of Engineering.
          </p>
          <h3>Core Faculty</h3>
          <p><a href="https://steinhardt.nyu.edu/marl">Music and Audio Research Laboratory (MARL)</a></p>
          <h3>Affiliated Faculty</h3>
          <p><a href="https://engineering.nyu.edu/academics/departments/computer-science-engineering">Department of Computer Science and Engineering</a><br>Tandon School of Engineering, New York University</p>
        </div>
      </div>
    </section>
  </main>
"""
    return layout("Home", "home", prefix, body, home=True)


def people() -> str:
    prefix = "../assets/"
    current = [
        dict(img="giovana.jpg", name="Giovana Morais", role="PhD Candidate<br>Computer Science<br>Tandon, NYU", dates="2023-present", url="https://giovana-morais.github.io/about.html"),
        dict(img="richa.jpg", name="Richa Namballa", role="PhD Candidate<br>Music Technology<br>Steinhardt, NYU", dates="2023-present", url="https://richa-namballa.github.io/"),
        dict(img="julia.jpg", name="Julia Wilkins", role="PhD Candidate<br>Computer Science<br>Tandon, NYU", extra="(with Juan Bello)", dates="2022-present", url="https://juliawilkins.github.io/"),
        dict(img="yi-wu.jpg", name="Yi Wu", role="PhD Candidate<br>Music Technology<br>Steinhardt, NYU", extra="(with Agnieszka Roginska)", dates="2025-present", url="https://wuyi.io/"),
        dict(img="xavier.jpg", name="Xavier Juanola Molet", role='PhD Candidate<br><a href="https://www.upf.edu/en/">IMVA, UPF</a>', extra="(with Gloria Haro)", dates="2023-present", url="https://xavijuanola.github.io/"),
        dict(img="leo.jpg", name="Leo Wu", role="PhD student<br>Computer Science<br>Tandon, NYU", dates="2026-present", url="https://binomial14.github.io/"),
        dict(img="yujin.jpg", name="Yujin Kim", role="Research Scholar<br>M.S. Music Technology, NYU", dates="2025-present", url="https://yujin-kimmm.github.io/"),
        dict(img="yigitcan.jpg", name="Yigitcan Özer", role="Affiliate Postdoc<br>NJIT and MARL", extra="(with Mark Cartwright)", dates="2026-present", url="https://yiitozer.com/"),
        dict(img="jonathan.jpg", name="Jonathan", role="Research Assistant<br>M.S. Music Technology, NYU", dates="2026-present", url="./"),
    ]

    def card(p):
        extra = f"<br>{p['extra']}" if p.get("extra") else ""
        btn = ""
        if p.get("url"):
            ext = ' target="_blank" rel="noopener"' if not p["url"].startswith("./") else ""
            btn = f'<a class="btn btn-sm" href="{p["url"]}"{ext}>Website</a>'
        return f"""
        <article class="person reveal">
          <img src="{prefix}images/people/{p['img']}" alt="{p['name']}">
          <div>
            <h3>{p['name']}</h3>
            <p>{p['role']}<br><span class="dates">{p['dates']}</span>{extra}</p>
            {btn}
          </div>
        </article>"""

    alumni = [
        ("Cecilia Bolaños", '<a href="https://signalprocessingsociety.org/community-involvement/signal-processing-mentorship-academy-sigma-program" target="_blank" rel="noopener">IEEE SigMA</a> Mentee, 2026.<br>PhD student in Computer Science,<br>Facultad de Ciencias Exactas y Naturales,<br>Universidad de Buenos Aires.', "https://ceciliabolanos.github.io/"),
        ("Atilay Kucukoglu", "Research Assistant, 2025-2026.<br>M.S. Music Technology,<br>Steinhardt, NYU.<br>Next: Orbit Creative Technologies.", "https://www.linkedin.com/in/atilay-kucukoglu-a07255189/"),
        ("Tai Wan Kim", "Research Assistant, 2025.<br>M.S. in Computer Science,<br>Courant, NYU.<br>Next: Student at NYU.", None),
        ("Emiliano Acevedo Piotti", '<a href="https://signalprocessingsociety.org/newsletter/2024/06/call-project-proposals-ieee-sps-me-uyr-program-mentoring-experiences" target="_blank" rel="noopener">IEEE ME-UYR</a> Mentee, 2024.<br>Bs. Eng. in Electrical Engineering,<br>Facultad de Ingeniería,<br>Universidad de la República.<br>Next: R&amp;D Engineer at BMAT.', "https://www.linkedin.com/in/eacevedo1/"),
        ("Tanmay Khandelwal", "Research Assistant, 2023-2024.<br>M.S. in Computer Science,<br>Courant, NYU.<br>Next: Data Engineer at Amazon.", "https://github.com/tanmayy24"),
        ("Liqian Zhang", "Research Assistant, 2023-2024.<br>M.S. Integrated Design &amp; Media,<br>Tandon, NYU.<br>Next: AI developer at Atly.", "https://zxxwxyyy.github.io/"),
        ("Ana Elisa Mendez", "Research Assistant, 2023.<br>PhD in Music Technology,<br>Steinhardt, NYU.<br>Next: Research scientist at Apple (via Volt).", "https://anaelisamendez.com/"),
        ("Pauline Wee", "Undergraduate Research Assistant, 2023.<br>M.S. in Computer Science, NYU.<br>Next: Design engineer at DAIR.", "https://paulinewee.com/"),
        ("Harsh Palan", "Research Assistant, 2022-2023.<br>M.S. Integrated Design &amp; Media,<br>Tandon, NYU.<br>Next: Creative technologist at Madwell.", "https://harshpalan.tech/"),
        ("Saksham Singh", "Research Assistant, 2022-2023.<br>M.S. in Computer Science,<br>Courant, NYU.<br>Next: PhD Candidate at the University of Texas at Dallas.", "https://sakshamsingh1.github.io/"),
    ]
    alumni_html = ""
    for name, bio, url in alumni:
        link = f'<a class="more" href="{url}" target="_blank" rel="noopener">Website →</a>' if url else ""
        alumni_html += f'<article class="reveal"><h3>{name}</h3><p>{bio}</p>{link}</article>'

    body = f"""
  <main class="page-main">
    <div class="container">
      <h1 class="page-title reveal">People</h1>
      <p class="section-intro reveal">Current students, collaborators, and alumni.</p>
      <div class="people-grid">
        {''.join(card(p) for p in current)}
      </div>
      <section class="alumni">
        <h2 class="reveal">Alumni</h2>
        <div class="alumni-grid">
          {alumni_html}
        </div>
      </section>
    </div>
  </main>
"""
    return layout("People", "people", prefix, body)


def pub_html(p, prefix):
    href = p.get("href")
    thumb = ""
    no_thumb = ""
    if p.get("img"):
        img = f'<img src="{prefix}images/papers/{p["img"]}" alt="">'
        if href:
            img = f'<a href="{href}" target="_blank" rel="noopener">{img}</a>'
        thumb = f'<div class="pub-thumb">{img}</div>'
    else:
        no_thumb = " no-thumb"
    title = p["title"]
    if href:
        title = f'<a href="{href}" target="_blank" rel="noopener">{title}</a>'
    btns = ""
    if p.get("links"):
        btns = '<div class="btn-row">' + "".join(
            f'<a class="btn btn-xs" href="{url}" target="_blank" rel="noopener">{label}</a>'
            for label, url, *_ in p["links"]
        ) + "</div>"
    venue = f'<p class="venue">{p["venue"]}</p>' if p.get("venue") else ""
    note = f'<p class="pub-note">{p["note"]}</p>' if p.get("note") else ""
    return f"""
      <article class="pub{no_thumb} reveal">
        {thumb}
        <div>
          <h3>{title}</h3>
          <p class="year">{p['year']}</p>
          <p class="authors">{p['authors']}</p>
          {venue}
          {note}
          {btns}
        </div>
      </article>"""


def publications() -> str:
    prefix = "../assets/"
    pubs = "".join(pub_html(p, prefix) for p in PAPERS)
    body = f"""
  <main class="page-main">
    <div class="container">
      <h1 class="page-title reveal">Publications</h1>
      {pubs}
    </div>
  </main>
"""
    return layout("Publications", "publications", prefix, body)



def activities() -> str:
    prefix = "../assets/"
    body = f"""
  <main>
    <section class="page-main" style="padding-bottom:48px">
      <div class="container">
        <h1 class="page-title reveal">Activities</h1>
        <p class="research-lead reveal">Besides papers, a large part of the work is building the communities I want to belong to: Latin American MIR, IEEE mentoring, and the conferences of the field.</p>
        <p class="research-sub reveal">This page collects organizing, reviewing, mentoring, and selected talks. Courses and software live on <a href="../resources/">Resources</a>.</p>
      </div>
    </section>
    <section class="section-mint" id="community">
      <div class="container">
        <h2 class="reveal">Community</h2>
        <p class="section-intro reveal">The thread is Latin American networking in audio and music, and mentoring that is not only local to NYU.</p>
        <div class="theme-grid theme-grid-3">
          <article class="theme-card reveal">
            <div class="community-banner">
              <img class="community-logo community-logo-lamir" src="{prefix}images/activities/lamir.svg" alt="LAMIR">
            </div>
            <h3>Latin American MIR Workshop</h3>
            <p>I co-organize <a href="https://lamir-workshop.github.io/" target="_blank" rel="noopener">LAMIR</a>, a satellite of ISMIR for students and researchers in the region. The first workshop was in Rio de Janeiro in 2024, with <a href="https://doi.org/10.5281/zenodo.14908040" target="_blank" rel="noopener">open proceedings</a>. The next is in Belo Horizonte, 15–17 December 2026.</p>
          </article>
          <article class="theme-card reveal">
            <img src="{prefix}images/activities/bish.jpg" alt="BISH Bash LatAm">
            <h3>Latin American BISH Bash</h3>
            <p>Since 2021 I have organized the <a href="https://www.meetup.com/bish-bash-latam/" target="_blank" rel="noopener">BISH Bash LatAm</a> meetups: informal, free gatherings for researchers, students, and industry people working on audio, music, and machine listening in Latin America.</p>
          </article>
          <article class="theme-card reveal">
            <div class="community-banner">
              <img class="community-logo community-logo-ieee" src="{prefix}images/activities/ieee.png" alt="IEEE Signal Processing Society">
            </div>
            <h3>Mentoring</h3>
            <p>I mentor through <a href="https://signalprocessingsociety.org/community-involvement/signal-processing-mentorship-academy-sigma-program" target="_blank" rel="noopener">IEEE SigMA</a>, <a href="https://signalprocessingsociety.org/newsletter/2024/06/call-project-proposals-ieee-sps-me-uyr-program-mentoring-experiences" target="_blank" rel="noopener">IEEE ME-UYR</a> (2022, 2024), <a href="https://wimir.wordpress.com/mentoring-program/" target="_blank" rel="noopener">WiMIR</a>, and <a href="https://www.latinxinai.org/neurips-2023" target="_blank" rel="noopener">LXAI NeurIPS</a> (2023). At NYU I also mentor in ARISE and REU.</p>
          </article>
        </div>
      </div>
    </section>
    <section class="page-main" id="service" style="padding-bottom:48px">
      <div class="container">
        <h2 class="reveal">Professional service</h2>
        <ul class="service-list reveal">
          <li>Scientific Program Chair at <a href="https://ismir2025.ismir.net/" target="_blank" rel="noopener">ISMIR 2025</a>.</li>
          <li>Grants Chair at <a href="https://ismir2026.ismir.net/about/organizers" target="_blank" rel="noopener">ISMIR 2026</a>.</li>
          <li>Technical Program Chair at <a href="https://dcase.community/workshop2025/organizers" target="_blank" rel="noopener">DCASE Workshop</a> 2021, 2023, 2025.</li>
          <li>Member of the <a href="https://signalprocessingsociety.org/community-involvement/audio-and-acoustic-signal-processing" target="_blank" rel="noopener">IEEE Audio and Acoustic Signal Processing Technical Committee</a>, 2021–2023, 2023–2026.</li>
          <li>Area Chair at ICASSP 2022, 2023, 2024, 2025, 2026.</li>
          <li>Guest editor of the <a href="https://account.transactions.ismir.net/index.php/up-j-tismir/libraryFiles/downloadPublic/9" target="_blank" rel="noopener">TISMIR special collection</a> on open music data, 2026.</li>
          <li>Co-organizer of <a href="https://www.dagstuhl.de/26272" target="_blank" rel="noopener">Dagstuhl Seminar 26272</a>, Open Music Data for Music Processing Research, 2026.</li>
          <li>Diversity Chair at WASPAA 2023.</li>
          <li>Awards Chair at DCASE Workshop 2021, 2023, 2025.</li>
          <li>Meta-reviewer at ISMIR 2022, 2026.</li>
          <li>Special Session Chair at ISMIR 2020.</li>
          <li>Local committee at ISMIR 2018.</li>
          <li>Task coordinator for DCASE 2020 Urban Sound Tagging.</li>
          <li>Co-organizer of the <a href="http://www02.smt.ufrj.br/~starel/workshop/" target="_blank" rel="noopener">Computational Models for Rhythm and Expressiveness</a> workshop, 2019.</li>
          <li>Reviewer: ISMIR, ICASSP, DCASE, TASLP, PLOS ONE, JOSS, TISMIR, AAAI.</li>
        </ul>
      </div>
    </section>
    <section class="section-mint" id="talks">
      <div class="container">
        <h2 class="reveal">Selected talks</h2>
        <p class="section-intro reveal">Invited talks and a tutorial. Internal NYU seminars are omitted.</p>
        <div class="join-paths">
          <article class="join-path reveal">
            <span class="theme-num">December 2025</span>
            <h3>Advances and Challenges in Audio-Visual Sound Source Localization</h3>
            <p>IEEE Signal Processing Society SLTC / AASP webinar. <a href="https://signalprocessingsociety.org/events/sps-sltcaasp-webinar-advances-and-challenges-audio-visual-sound-source-localization" target="_blank" rel="noopener">Event</a> · <a href="https://resourcecenter.ieee.org/education/sl-tc-aasp-tc-webinars/sps_edu_sl_fuentes_120925" target="_blank" rel="noopener">Video</a></p>
          </article>
          <article class="join-path reveal">
            <span class="theme-num">October 2025</span>
            <h3>Challenges and Opportunities for Artificial Intelligence in Latin American Music</h3>
            <p>Invited talk, VIII Jornadas de Acústica, Audio y Sonido, Buenos Aires (remote).</p>
          </article>
          <article class="join-path reveal">
            <span class="theme-num">December 2024</span>
            <h3>Including Latin American Music in MIR</h3>
            <p>Keynote, <a href="https://lamir-workshop.github.io/" target="_blank" rel="noopener">Latin American Music Information Retrieval Workshop</a>, Rio de Janeiro.</p>
          </article>
          <article class="join-path reveal">
            <span class="theme-num">October 2023</span>
            <h3>Adaptive and Multimodal Learning in Audio</h3>
            <p>Invited talk, MUSAiC day, KTH Royal Institute of Technology, Stockholm.</p>
          </article>
          <article class="join-path reveal">
            <span class="theme-num">June 2023</span>
            <h3>Scales of Sound</h3>
            <p>Invited panelist, Simons Foundation Presents, New York. <a href="https://www.simonsfoundation.org/event/scales-of-sound/" target="_blank" rel="noopener">Event</a></p>
          </article>
          <article class="join-path reveal">
            <span class="theme-num">April 2023</span>
            <h3>Infectious Rhythm Colloquium</h3>
            <p>Invited panelist, NYU Center for Latin American and Caribbean Studies. <a href="https://as.nyu.edu/research-centers/clacs/events/spring-2023.html" target="_blank" rel="noopener">Event</a></p>
          </article>
          <article class="join-path reveal">
            <span class="theme-num">November 2021</span>
            <h3>Tempo, Beat, and Downbeat Estimation</h3>
            <p>Tutorial at ISMIR, with Matthew E. P. Davies and Sebastian Böck. <a href="https://tempobeatdownbeat.github.io/tutorial/intro.html" target="_blank" rel="noopener">Tutorial book</a></p>
          </article>
        </div>
      </div>
    </section>
  </main>
"""
    return layout("Activities", "activities", prefix, body)


def resources() -> str:
    prefix = "../assets/"
    body = f"""
  <main>
    <section class="page-main" style="padding-bottom:48px">
      <div class="container">
        <h1 class="page-title reveal">Resources</h1>
      </div>
    </section>
    <section class="section-mint" id="tutorials">
      <div class="container">
        <h2 class="reveal">Tutorials</h2>
        <article class="media-row reveal">
          <img src="{prefix}images/resources/tutorial-beat-downbeat.png" alt="Double-time beat estimates compared with ground-truth annotations">
          <div>
            <h3>Tempo, Beat, and Downbeat Estimation</h3>
            <p>Matthew E. P. Davies, Sebastian Böck, Magdalena Fuentes<br>ISMIR, 2021</p>
            <div class="btn-row">
              <a class="btn" href="https://github.com/TempoBeatDownbeat/tutorial" target="_blank" rel="noopener">GitHub</a>
              <a class="btn" href="https://tempobeatdownbeat.github.io/tutorial/intro.html" target="_blank" rel="noopener">Book</a>
            </div>
          </div>
        </article>
      </div>
    </section>
    <section class="page-main" id="theses" style="padding-bottom:48px">
      <div class="container">
        <h2 class="reveal">Theses</h2>
        <article class="media-row reveal">
          <img src="{prefix}images/resources/thesis-phd.png" alt="Figure 1.1 from the PhD thesis: multi-scale rhythm analysis across sections, downbeats, beats, and microtiming">
          <div>
            <h3>Multi-scale computational rhythm analysis: a framework for sections, downbeats, beats, and microtiming</h3>
            <p>Magdalena Fuentes<br>Ph.D. thesis, Université Paris-Saclay, 2019</p>
            <div class="btn-row">
              <a class="btn" href="https://theses.hal.science/tel-02613433" target="_blank" rel="noopener">PDF</a>
            </div>
          </div>
        </article>
        <article class="media-row reveal">
          <img src="{prefix}images/resources/thesis-undergrad.png" alt="Multimodal recording setup with drums, microphones, and cameras">
          <div>
            <h3>Procesamiento multimodal de señales en la interpretación de música</h3>
            <p>Bernardo Marenco, Magdalena Fuentes, Florencia Lanzaro<br>B.Eng. thesis, Universidad de la República, 2015</p>
            <div class="btn-row">
              <a class="btn" href="https://www.colibri.udelar.edu.uy/server/api/core/bitstreams/c071e265-ce53-4684-b73a-14cb9de1e6a4/content" target="_blank" rel="noopener">PDF</a>
            </div>
          </div>
        </article>
      </div>
    </section>
    <section class="section-mint" id="courses">
      <div class="container">
        <h2 class="reveal">Courses</h2>
        <article class="media-row reveal">
          <img src="{prefix}images/resources/course-mir.png" alt="Music Information Retrieval">
          <div>
            <h3><a href="../teaching/music-information-retrieval/">Music Information Retrieval (MPATE-GE 2623)</a></h3>
            <p>Syllabus sample<br>Fall 2022, 2023, 2025</p>
            <a class="btn" href="../teaching/music-information-retrieval/">Read more</a>
          </div>
        </article>
        <article class="media-row reveal">
          <img src="{prefix}images/resources/course-dl.png" alt="Deep Learning for Media">
          <div>
            <h3><a href="../teaching/deep-learning-for-media/">Deep Learning for Media (MPATE-GE 2039)</a></h3>
            <p>Syllabus sample<br>Spring 2023, 2025</p>
            <a class="btn" href="../teaching/deep-learning-for-media/">Read more</a>
          </div>
        </article>
      </div>
    </section>
    <section class="page-main" style="padding-top:60px;padding-bottom:40px">
      <div class="container">
        <h2 class="reveal">Software</h2>
        <div class="software-grid">
          <article class="software-card reveal">
            <h3>mirdata</h3>
            <img src="{prefix}images/resources/mirdata.png" alt="mirdata logo">
            <div class="btn-row">
              <a class="btn" href="https://github.com/mir-dataset-loaders/mirdata/tree/master" target="_blank" rel="noopener">GitHub</a>
              <a class="btn" href="https://mirdata.readthedocs.io/en/stable/" target="_blank" rel="noopener">Docs</a>
            </div>
          </article>
          <article class="software-card reveal">
            <h3>soundata</h3>
            <img src="{prefix}images/resources/soundata.png" alt="soundata logo">
            <div class="btn-row">
              <a class="btn" href="https://github.com/soundata/soundata" target="_blank" rel="noopener">GitHub</a>
              <a class="btn" href="https://soundata.readthedocs.io/en/latest/" target="_blank" rel="noopener">Docs</a>
            </div>
          </article>
        </div>
      </div>
    </section>
    <section class="section-mint" id="datasets">
      <div class="container">
        <h2 class="reveal">Datasets</h2>
        <div class="dataset-grid">
          <article class="dataset-card reveal">
            <img src="{prefix}images/resources/urbansas.png" alt="Urbansas street scenes with moving vehicles">
            <h3>Urbansas</h3>
            <p>Audiovisual spatial urban scene understanding</p>
            <div class="btn-row">
              <a class="btn" href="https://zenodo.org/records/6658386" target="_blank" rel="noopener">Data</a>
              <a class="btn" href="https://beasteers.github.io/urbansas-website/#why" target="_blank" rel="noopener">Website</a>
            </div>
          </article>
          <article class="dataset-card reveal">
            <img src="{prefix}images/resources/monyc.png" alt="Map of MONYC sensor locations in New York City">
            <h3>MONYC</h3>
            <p>Music of New York City Dataset</p>
          </article>
          <article class="dataset-card reveal">
            <img src="{prefix}images/resources/sonyc-ust.png" alt="SONYC-UST sensor locations across New York City">
            <h3>SONYC-UST 2.1</h3>
            <p>Multilabel urban acoustic sensor network</p>
            <div class="btn-row">
              <a class="btn" href="https://zenodo.org/records/3693077" target="_blank" rel="noopener">Data</a>
            </div>
          </article>
          <article class="dataset-card reveal">
            <img src="{prefix}images/resources/sambaset.png" alt="SAMBASET website">
            <h3>SAMBASET</h3>
            <p>Historical samba de enredo recordings</p>
            <div class="btn-row">
              <a class="btn" href="https://www02.smt.ufrj.br/~starel/sambaset/" target="_blank" rel="noopener">Website</a>
            </div>
          </article>
          <article class="dataset-card reveal">
            <img src="{prefix}images/resources/brid.png" alt="Brazilian rhythmic instruments in BRID">
            <h3>BRID</h3>
            <p>Brazilian rhythmic instruments</p>
            <div class="btn-row">
              <a class="btn" href="https://www02.smt.ufrj.br/~starel/datasets/brid.html" target="_blank" rel="noopener">Website</a>
            </div>
          </article>
          <article class="dataset-card reveal">
            <img src="{prefix}images/resources/aucd.png" alt="Candombe recording session for the AUCD dataset">
            <h3>AUCD</h3>
            <p>Afro-Uruguayan Candombe</p>
            <div class="btn-row">
              <a class="btn" href="https://www02.smt.ufrj.br/~starel/datasets/aucd.html" target="_blank" rel="noopener">Website</a>
            </div>
          </article>
        </div>
      </div>
    </section>
  </main>
"""
    return layout("Resources", "resources", prefix, body)


def redirect_page(href: str, label: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0;url={href}">
  <link rel="canonical" href="{href}">
  <title>{label} – Magdalena Fuentes</title>
  <script>location.replace("{href}");</script>
</head>
<body>
  <p>This page has moved to <a href="{href}">{label}</a>.</p>
</body>
</html>
"""


def dl_course() -> str:
    prefix = "../../assets/"
    body = """
  <main class="page-main">
    <div class="container course">
      <h1>MPATE-GE 2039: Deep Learning for Media</h1>
      <div class="meta">
        <p><strong>Instructor:</strong> Magdalena Fuentes<br>
        <strong>Email:</strong> <a href="mailto:mfuentes@nyu.edu">mfuentes@nyu.edu</a><br>
        Spring 2023, 3 credits<br>
        <strong>Class meetings:</strong> 2:00 PM – 4:30 PM W<br>
        <strong>Classroom:</strong> 35 West 4th Street, EDUC building, room 610<br>
        <strong>Office hours:</strong> <a href="https://bit.ly/mf_office_hours">https://bit.ly/mf_office_hours</a></p>
      </div>
      <h2>Course Description</h2>
      <p>Deep learning, a sub-field of machine learning and artificial intelligence, has promoted breakthroughs in managing and creating media content, and continues to shape the future of the multimedia landscape. This course provides a hands-on, project-oriented introduction to deep learning, for the classification, retrieval, and creation of media content, with emphasis in audio-visual content. Students will create and work with existing deep learning models using Python libraries, and think critically about the application of these models for media. This course will provide students with an understanding of how these tools work, and how to use them in the context of their work, so they can participate in the ongoing revolution between machine learning and media content.</p>
      <h2>Course Objectives</h2>
      <p>The goal of this course is to provide students with:</p>
      <ul>
        <li>Basic knowledge of deep learning, including definitions, pipeline development, and evaluation.</li>
        <li>Practical skills for working with open source deep learning resources in Python.</li>
        <li>Awareness of the current state-of-the art practices in the retrieval, classification and creation of audio-visual content.</li>
        <li>The ability to critically analyze the behavior of deep learning systems in the context of media.</li>
      </ul>
      <h2>Student Learning Outcomes</h2>
      <p>By the end of the course, students will be able to:</p>
      <ul>
        <li>Explain and describe basic concepts of deep learning, including definitions, pipeline development, and evaluation.</li>
        <li>Code deep learning pipelines using open source Python libraries.</li>
        <li>Assess deep learning systems in new audio-visual data.</li>
        <li>Explain current trends in deep learning for the classification and generation of audio and image.</li>
      </ul>
      <h2>Required Skills</h2>
      <p>Basic knowledge of Python is required. Basic knowledge of linear algebra is recommended.</p>
      <h2>Required Course Materials</h2>
      <p>A computer with Internet access.</p>
      <h2>Course Requirements</h2>
      <h3>Class participation</h3>
      <p>This course will be highly participatory and interactive. We will have conversational lectures, live-coding demonstrations and group readings. It is expected and essential that students participate actively in class. For the class readings, we are going to follow the role-playing paper reading format of Jacobson and Raffel. In this format, students read the same paper, but each student takes one specific role for that week. We will work with three different roles, to be determined at the beginning of the course. Each student will participate by choosing one role in the semester. Papers will be assigned to students during the first week of classes. See a short guide on how to read a paper.</p>
      <h3>Homework assignments</h3>
      <p>There will be 3 homework assignments. Each assignment will consist of Python code snippets and written components to be completed by you. These assignments are individual. You will have two weeks to complete each assignment. For the homework assignments, your lowest score will be dropped. If you can’t finish one assignment for any reason, you should make the time to cover the material, but no need to panic about late assignments.</p>
      <h3>Final Project</h3>
      <p>The final project can be done in groups of 2-3, and will have a code and presentation component. Projects will be presented during the last class. A project can cover the assessment of an existing deep learning system in new data, or a new system proposed by the students. The project will have four assignments through the semester as follows:</p>
      <p><em>Topic, group definition and data report.</em> Each group will propose a project’s topic and composition and will submit a short report (max. 2 pages) describing the scope of the work and data resources they will use. The project’s final scope and composition will be determined jointly with the instructor. Examples of feasible projects will be provided by the instructor in advance to guide the students in the definition of their project.</p>
      <p><em>Documented code, and data.</em> Students will submit their working (and well documented!) code along with the data they investigated. The code should run out-of-the-box, and should have instructions on how to run it if needed.</p>
      <p><em>Final Presentation.</em> All students from each group should participate in a final presentation. Presentations should last between 5-10 minutes, and will be followed by a short Q&amp;A from the class.</p>
      <p>Your grade for the class will be determined by the following break-down:</p>
      <ul>
        <li>40% assignments (individual)</li>
        <li>30% final project (groups)</li>
        <li>30% class participation (individual)</li>
      </ul>
      <p>Classes will be in person weekly unless indicated by the instructor, and materials will be available on NYU Brightspace.</p>
      <h2>Recommended Readings</h2>
      <p>Main textbook:</p>
      <ul><li>Chollet, F. (2021). Deep learning with python. Second Edition. Manning Publications. (DLwP)</li></ul>
      <p>Other recommended readings:</p>
      <ul>
        <li>Ian Goodfellow, Yoshua Bengio, Aaron Courville. Deep Learning. 2016. MIT Press.</li>
        <li>Abu-Mostafa, Yaser S. Learning from data: a short course. 2012. AMLBook.</li>
        <li>David Foster. Generative Machine Learning. 2019. O’Reilly Media, Inc</li>
        <li>Tuomas Virtanen, Mark D. Plumbley, Dan Ellis. Computational Analysis of Sound Scenes and Events, Chapter 4 (Brian McFee).</li>
      </ul>
      <h2>Class Environment</h2>
      <p>Please do your part by seeking to promote the success of others, and by treating each other in ways that respect and celebrate the diversity of talent.</p>
      <ul>
        <li><strong>Preparation:</strong> Students come to this class from a wide range of backgrounds. If you feel that there are gaps in your knowledge, please speak to me and I will help you find additional materials as needed.</li>
        <li><strong>Classroom environment:</strong> The classroom is an open forum for discussion. Please do not be afraid to ask any question, no matter how basic it may seem.</li>
        <li><strong>Accessibility:</strong> If you have any accessibility requirements, please present a letter from the <a href="https://www.nyu.edu/students/communities-and-groups/students-with-disabilities.html">Moses Center</a> so that I can ensure that materials comply with your needs.</li>
        <li><strong>Mental Health &amp; Wellness:</strong> The NYU Wellness Exchange (212-443-9999) offers a range of services. I am available to speak with you about stresses related to your work in my course.</li>
        <li><strong>Preferred name and pronouns:</strong> You are always welcome to write your preferred name on all class assignments. If you have a name and/or pronoun that doesn’t match the class roster, please let me know.</li>
        <li><strong>Class expenses:</strong> If obtaining any material for use in our class presents a financial hardship, please let me know and I will do my best to arrange for loaner materials.</li>
        <li><strong>Feedback:</strong> I will solicit (anonymous) feedback throughout the course. Please let me know if any aspect of our course or class community can be improved.</li>
        <li><strong>Academic Integrity and Honesty:</strong> All students are expected to do their own work on homework. Please also refer to the general <a href="https://www.nyu.edu/about/policies-guidelines-compliance/policies-and-guidelines/academic-integrity-for-students-at-nyu.html">NYU academic integrity statement</a>.</li>
        <li><strong>Diversity:</strong> NYU values an inclusive and equitable environment for all students. If this standard is not being upheld, please feel free to speak with me.</li>
      </ul>
      <h2>Resources at NYU</h2>
      <p><strong>Access your course materials:</strong> <a href="https://brightspace.nyu.edu">NYU Brightspace</a><br>
      <strong>Databases, journal articles, and more:</strong> <a href="https://library.nyu.edu">Bobst Library</a><br>
      <strong>Assistance with strengthening your writing:</strong> <a href="https://nyu.mywconline.com">NYU Writing Center</a><br>
      <strong>Obtain 24/7 technology assistance:</strong> <a href="https://nyu.edu/it/servicedesk">IT Service Desk</a></p>
      <h2>Weekly Schedule</h2>
      <div class="week"><strong>Week 0: Supplemental materials</strong>
        <ul>
          <li><a href="https://cs231n.github.io/python-numpy-tutorial/">This open source tutorial on Python and Numpy</a></li>
          <li>This GitHub starter course (we will do this in class as well)</li>
        </ul>
      </div>
      <div class="week"><strong>Week 1, 01/25: Introduction to Machine Learning</strong>
        <ul>
          <li>Course structure and schedule</li>
          <li>Why deep learning? Why now?</li>
          <li>Frame a machine learning problem, collect a dataset, understand your data, choose a measure of success</li>
          <li>Recommended reading: DLwP Chapter 1, Chapter 6</li>
          <li>Practice: GitHub basics, submitting homework</li>
        </ul>
      </div>
      <div class="week"><strong>Week 2, 02/01: The building blocks of neural networks</strong>
        <ul>
          <li>Data representations: scalars, vectors, matrices, tensors, sequential data</li>
          <li>Data operations</li>
          <li>Practice: train a first neural network for handwritten digit classification; adapt the network for audio instrument classification</li>
          <li>Recommended reading: DLwP Chapter 2.1-2.3</li>
        </ul>
      </div>
      <div class="week"><strong>Week 3, 02/08: The engine of neural networks</strong>
        <ul>
          <li>Gradient-based optimization: derivative, derivative of tensors, stochastic gradient descent, backpropagation</li>
          <li>Practice: gradient descent</li>
          <li>Recommended reading: DLwP Chapter 2.4</li>
        </ul>
      </div>
      <div class="week"><strong>Week 4, 02/15: Setting up a deep learning project</strong>
        <ul>
          <li>Keras and Tensorflow, layers and models, loss function, metrics, inference</li>
          <li>Recommended reading: DLwP Chapter 3</li>
          <li>ASSIGN: paper readings for the semester</li>
        </ul>
      </div>
      <div class="week"><strong>Week 5, 02/22: Classification, model generalization and evaluation</strong>
        <ul>
          <li>Underfitting and overfitting, improving model fit, model biases and ethical implications, interpretability</li>
          <li>Practical example: a biased classifier, an ethically questionable classifier, a classifier that doesn’t generalize</li>
          <li>Recommended reading: DLwP Chapters 4, 5</li>
          <li>ASSIGN: homework 1 · Role-playing paper reading 1</li>
        </ul>
      </div>
      <div class="week"><strong>Week 6, 03/01: Convolutional Neural Networks</strong>
        <ul>
          <li>An introduction to Computer Vision, convolutional networks, max-pooling</li>
          <li>Practical example: image classification, training from scratch</li>
          <li>Recommended reading: DLwP Chapter 8</li>
        </ul>
      </div>
      <div class="week"><strong>Week 7, 03/08: Transfer learning and Data augmentation</strong>
        <ul>
          <li>Image data augmentation, feature extraction with a pre-trained model</li>
          <li>Recommended reading: DLwP Chapter 8</li>
          <li>DUE: homework 1 · ASSIGN: homework 2 · Role-playing paper reading 2</li>
        </ul>
      </div>
      <div class="week"><strong>Week 8, 03/15: Spring Break</strong></div>
      <div class="week"><strong>Week 9, 03/22: Audio understanding</strong>
        <ul>
          <li>An introduction to Machine Listening, audio manipulation, spectrograms, audio data augmentation</li>
          <li>Recommended reading: Computational Analysis of Sound Scenes and Events, Chapter 4</li>
          <li>DUE: homework 2 · ASSIGN: homework 3</li>
        </ul>
      </div>
      <div class="week"><strong>Week 10, 03/29: Audio classification</strong>
        <ul>
          <li>Temporal convolutional networks for audio</li>
          <li>Training from scratch and feature extraction with a pre-trained model</li>
          <li>Role-playing paper reading 3</li>
        </ul>
      </div>
      <div class="week"><strong>Week 11, 04/05: Cross-modal retrieval</strong>
        <ul>
          <li>Overview and applications, embedding space, contrastive loss</li>
          <li>Practical example: audio-visual cross modal retrieval</li>
          <li>DUE: homework 3 · ASSIGN: project 1 · Role-playing paper reading 4</li>
        </ul>
      </div>
      <div class="week"><strong>Week 12, 04/12: Neural style transfer</strong>
        <ul>
          <li>Overview of style transfer in image and audio; style loss and content loss</li>
          <li>Recommended reading: DLwP Chapter 12.3</li>
          <li>DUE: project 1 · ASSIGN: project 2 · Role-playing paper reading 5</li>
        </ul>
      </div>
      <div class="week"><strong>Week 13, 04/19: Image generation</strong>
        <ul>
          <li>GANs for image generation, challenges and tricks, diffusion techniques overview</li>
          <li>Recommended reading: DLwP Chapter 12.5</li>
          <li>Role-playing paper reading 6</li>
        </ul>
      </div>
      <div class="week"><strong>Week 14, 04/26: Audio generation</strong>
        <ul>
          <li>Variational Autoencoders for audio generation, sampling from audio latent spaces</li>
          <li>Recommended reading: DLwP Chapter 12.4</li>
          <li>DUE: project 2 · ASSIGN: project 3 · Role-playing paper reading 7</li>
        </ul>
      </div>
      <div class="week"><strong>Week 15, 05/03: Final project presentations</strong>
        <ul><li>DUE: project 3</li></ul>
      </div>
    </div>
  </main>
"""
    return layout("Deep Learning for Media", "resources", prefix, body)


def mir_course() -> str:
    prefix = "../../assets/"
    body = """
  <main class="page-main">
    <div class="container course">
      <h1>MPATE-GE 2623: Music Information Retrieval</h1>
      <div class="meta">
        <p><strong>Instructor:</strong> Assist. Prof. Magdalena Fuentes, PhD<br>
        <strong>Email:</strong> <a href="mailto:mfuentes@nyu.edu">mfuentes@nyu.edu</a><br>
        Fall 2023, 3 credits<br>
        <strong>Class meetings:</strong> 12:00 PM – 1:40 PM W<br>
        <strong>Classroom:</strong> 35 West 4th Street, EDUC building, room 610<br>
        <strong>Office hours:</strong> <a href="https://bit.ly/mf_office_hours">https://bit.ly/mf_office_hours</a></p>
      </div>
      <h2>Course description</h2>
      <p>This course gives a comprehensive overview of research in Music Information Retrieval (MIR). MIR is a multidisciplinary field which uses knowledge from areas as diverse as signal processing, machine learning, cognition and music theory. The course will explore how this knowledge is applied to different problems within MIR, with an emphasis on common research methodologies.</p>
      <h2>Course objectives</h2>
      <p>The goal of this course is to provide students with:</p>
      <ul>
        <li>Broad knowledge of common topics in MIR, including their definitions, challenges, and evaluation metrics.</li>
        <li>Awareness of the current state-of-the art and remaining challenges for each topic.</li>
        <li>The ability to critically analyze the behavior of MIR systems.</li>
        <li>Practical skills for working with open source MIR resources in Python.</li>
      </ul>
      <h2>Student Learning Outcomes</h2>
      <ul>
        <li>Explain and describe common tasks in MIR, including definitions, challenges and evaluation metrics.</li>
        <li>Code MIR pipelines using open source Python libraries.</li>
        <li>Assess and analyze the behavior of MIR systems.</li>
        <li>Explain current trends in MIR research.</li>
      </ul>
      <h2>Recommended Skills</h2>
      <p>Basic knowledge of Python programming and Digital Signal Theory are required.</p>
      <h2>Required Course Materials</h2>
      <p>A computer with Internet access.</p>
      <h2>Course Requirements</h2>
      <h3>Class participation</h3>
      <p>This course will be highly participatory and interactive. We will have conversational lectures and group readings. For the class readings, we follow the role-playing paper reading format of Jacobson and Raffel. Each student will participate by choosing one role in the semester.</p>
      <h3>Homework assignments</h3>
      <p>There will be 4 homework assignments. Each assignment will consist of Python code snippets and written components. These assignments are individual. You will have two weeks to complete each assignment. Your lowest score will be dropped.</p>
      <h3>Final Project</h3>
      <p>The final project can be done in groups of 2-3, and will have a code and presentation component. A project can cover the assessment of an existing MIR system in new data, or a new system proposed by the students. All projects should include a baseline system for comparison.</p>
      <p>Your grade for the class will be determined by the following break-down:</p>
      <ul>
        <li>40% assignments (individual)</li>
        <li>40% final project (groups)</li>
        <li>20% class participation (individual)</li>
      </ul>
      <h2>Recommended Readings</h2>
      <ul>
        <li><a href="https://www.audiolabs-erlangen.de/fau/professor/mueller/bookFMP">Meinard Müller, Fundamentals of Music Processing (FMP)</a></li>
      </ul>
      <p>Other recommended readings are suggested in the weekly schedule.</p>
      <h2>Class Environment</h2>
      <p>Please do your part by seeking to promote the success of others, and by treating each other in ways that respect and celebrate the diversity of talent. Policies on preparation, accessibility (Moses Center, 212-998-4980), mental health (NYU Wellness Exchange, 212-443-9999), preferred names and pronouns, class expenses, feedback, academic integrity, and inclusion match those of my other courses.</p>
      <h2>Resources at NYU</h2>
      <p><a href="https://brightspace.nyu.edu">NYU Brightspace</a> · <a href="https://library.nyu.edu">Bobst Library</a> · <a href="https://nyu.mywconline.com">NYU Writing Center</a> · <a href="https://nyu.edu/it/servicedesk">IT Service Desk</a></p>
      <h2>Weekly Schedule</h2>
      <div class="week"><strong>Week 0: Supplemental materials</strong><ul><li>Python/Numpy tutorial and GitHub starter course</li></ul></div>
      <div class="week"><strong>Week 1, 09/06: Course introduction &amp; Music representations</strong><ul><li>Overview of MIR field, course structure, GitHub classroom</li><li>Sheet music, piano-roll, MIDI, audio</li><li>ASSIGN: paper readings for the semester</li></ul></div>
      <div class="week"><strong>Week 2, 09/13: Time-Frequency Representations</strong><ul><li>STFT, log-frequency spectrogram, constant-Q transform</li><li>Recommended reading: McFee’s Digital Signals Theory, Chapters 5 and 9</li></ul></div>
      <div class="week"><strong>Week 3, 09/20: Machine Learning and MIR</strong><ul><li>Supervised learning, features, train/validation/test, classifiers, metrics, data augmentation</li><li>ASSIGN: Homework 1</li></ul></div>
      <div class="week"><strong>Week 4, 09/27: Sound Classification</strong><ul><li>Instrument identification, MFCCs, confusion matrices, precision/recall/F-measure</li><li>Pitch shifting, time stretching, resampling, background noise, dynamic range compression</li></ul></div>
      <div class="week"><strong>Week 5, 10/04: Beats and Downbeats</strong><ul><li>Beat and downbeat tracking, onsets and novelty curves, metrics</li><li>Recommended reading: FMP 6.1.1, 6.3 and ISMIR tutorial</li><li>DUE: Homework 1 · ASSIGN: Homework 2</li></ul></div>
      <div class="week"><strong>Week 6, 10/11: Music Similarity</strong><ul><li>Embeddings, fingerprinting, version identification, music recommendation</li><li>Recommended reading: FMP 3.2, 7.2, 7.3</li></ul></div>
      <div class="week"><strong>Week 7, 10/18: Chords [Class ONLINE]</strong><ul><li>Chord estimation, chroma, metrics</li><li>DUE: Homework 2 · ASSIGN: Homework 3</li></ul></div>
      <div class="week"><strong>Week 8, 10/25: Open Week</strong></div>
      <div class="week"><strong>Week 9, 11/01: Pitch</strong><ul><li>Pitch tracking, melody estimation, salience representations</li><li>DUE: Homework 3 · ASSIGN: Homework 4</li></ul></div>
      <div class="week"><strong>Week 10, 11/08: Transcription</strong><ul><li>Transcription, non-negative matrix factorization, metrics</li><li>ASSIGN: project topic, data and baseline</li></ul></div>
      <div class="week"><strong>Week 11, 11/15: Source Separation</strong><ul><li>Harmonic-percussive and instrument separation, stems, metrics</li><li>DUE: project topic, data and baseline · DUE: Homework 4 · ASSIGN: project code and data</li></ul></div>
      <div class="week"><strong>Week 12, 11/22: NO CLASS (Thanksgiving)</strong></div>
      <div class="week"><strong>Week 13, 11/29: Multimodal MIR</strong><ul><li>Overview and applications, embedding space, contrastive loss</li></ul></div>
      <div class="week"><strong>Week 14, 12/06: Music Generation</strong><ul><li>Stable diffusion models, variational models</li><li>DUE: project code and data · ASSIGN: project presentation</li></ul></div>
      <div class="week"><strong>Week 15, 12/13: Final Presentations</strong><ul><li>DUE: project presentation</li></ul></div>
    </div>
  </main>
"""
    return layout("Music Information Retrieval", "resources", prefix, body)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


def main() -> None:
    write(ROOT / "index.html", home())
    write(ROOT / "people" / "index.html", people())
    write(ROOT / "activities" / "index.html", activities())
    write(ROOT / "publications" / "index.html", publications())
    write(ROOT / "resources" / "index.html", resources())
    write(ROOT / "teaching" / "index.html", redirect_page("../resources/", "Resources"))
    write(ROOT / "data-software" / "index.html", redirect_page("../resources/", "Resources"))
    write(ROOT / "teaching" / "deep-learning-for-media" / "index.html", dl_course())
    write(ROOT / "teaching" / "music-information-retrieval" / "index.html", mir_course())


if __name__ == "__main__":
    main()
