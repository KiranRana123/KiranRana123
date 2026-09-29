"""Render the profile README cards (assets/svg/*.svg) from the data below.

Edit PROFILE, then run:  python3 scripts/render_svgs.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "svg"
W = 840

# ---------------------------------------------------------------- data
PROFILE = {
    "name": "Kiran Rana",
    "roles": [
        "MS Computer Science & Engineering @ UC Santa Cruz",
        "Former Software Engineer @ JPMorgan Chase & Co.",
        "Building LLM-driven systems & Vision-Language Model tooling",
        "Backend, cloud (AWS) & full-stack engineering",
    ],
    "status": "Open to full-time SWE / ML roles",
    "intro": (
        "Software engineer and CS grad student at UC Santa Cruz. At JPMorgan Chase I automated "
        "credential rotation for 500+ databases, built monitoring and alerting tooling, and owned "
        "production releases. Now I work on making AI systems better and faster, like an "
        "evolutionary search framework that lets an LLM rewrite VLM inference code."
    ),
    "timeline": [
        ("2017", "B.Sc. (Hons) CS", "University of Delhi"),
        ("2021", "MCA", "NIT Warangal"),
        ("2023", "SWE Intern", "JPMorgan Chase"),
        ("2024", "Software Engineer", "JPMorgan Chase"),
        ("2025", "MS CSE", "UC Santa Cruz"),
        ("2026", "Graduate TA", "UC Santa Cruz"),
    ],
    "stack": [
        ("LANGUAGES", ["C++", "Python", "Java", "JavaScript", "SQL", "HTML", "CSS"]),
        ("FRAMEWORKS & ML", ["React", "Django", "Node.js", "PyTorch", "TensorFlow", "OpenCV", "Hugging Face"]),
        ("CLOUD", ["AWS S3", "EC2", "SQS", "Lambda", "CloudWatch", "Docker"]),
        ("TOOLS", ["Git", "Bitbucket", "Jira", "Confluence", "Geneos"]),
        ("AI TOOLS", ["Claude", "Gemini", "ChatGPT", "GitHub Copilot"]),
    ],
    "education": [
        ("University of California, Santa Cruz", "M.S. Computer Science & Engineering",
         "Sep 2025 - Mar 2027", "GPA 3.95 / 4.0"),
        ("National Institute of Technology Warangal", "Master of Computer Applications",
         "Oct 2021 - Jun 2024", "GPA 8.92 / 10"),
        ("University of Delhi", "B.Sc. (Hons) Computer Science",
         "Aug 2017 - Jul 2020", "GPA 8.62 / 10"),
    ],
    "leadership": [
        ("Engineer Committee Lead", "JPMorgan Chase & Co.", "Jan 2025 - Sep 2025",
         "Planned and ran large-scale tech talks and hackathons for JPMorgan employees"),
        ("Promotions Lead", "CS Department, NIT Warangal", "Aug 2022 - Aug 2023",
         "Led a team of 20+ students promoting CSE department events"),
    ],
}

# ---------------------------------------------------------------- style
BG = "#0c0a14"
BG2 = "#171226"
ACC = "#a78bfa"      # violet
ACC_D = "#7c3aed"
ACC2 = "#2dd4bf"     # teal
TXT = "#f5f3ff"
MUTED = "rgba(255,255,255,0.62)"
FAINT = "rgba(255,255,255,0.10)"
MONO = "'JetBrains Mono','SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace"
SANS = "'Segoe UI',Inter,-apple-system,BlinkMacSystemFont,Helvetica,Arial,sans-serif"
STYLE = (
    f"<style>.m{{font-family:{MONO};font-weight:700;letter-spacing:1.6px}}"
    f".h{{font-family:{SANS};font-weight:800}}"
    f".t{{font-family:{SANS};font-weight:700}}"
    f".s{{font-family:{SANS};font-weight:500}}</style>"
)


def e(s):
    return escape(s)


def svg(name, h, body, label, width=W):
    doc = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{h}" '
        f'viewBox="0 0 {width} {h}" role="img" aria-label="{e(label)}">{STYLE}{body}</svg>'
    )
    (OUT / f"{name}.svg").write_text(doc)


def card(h, width=W, rx=16):
    return (
        f'<rect x="0.5" y="0.5" width="{width - 1}" height="{h - 1}" rx="{rx}" '
        f'fill="{BG}" stroke="rgba(255,255,255,0.09)"/>'
    )


def fade(begin, dur=0.5):
    # Starts at 0s so content stays visible where SVG animation is unsupported.
    total = begin + dur
    return (
        f'<animate attributeName="opacity" values="0;0;1" keyTimes="0;{begin / total:.3f};1" '
        f'dur="{total:.2f}s" fill="freeze"/>'
    )


def wrap(text, max_chars):
    lines, cur = [], ""
    for word in text.split():
        if cur and len(cur) + 1 + len(word) > max_chars:
            lines.append(cur)
            cur = word
        else:
            cur = f"{cur} {word}".strip()
    if cur:
        lines.append(cur)
    return lines


def chip(x, y, text, color=ACC, size=11):
    w = int(len(text) * size * 0.62) + 20
    return w, (
        f'<rect x="{x}" y="{y}" width="{w}" height="{size + 13}" rx="{(size + 13) / 2}" '
        f'fill="{color}1a" stroke="{color}55"/>'
        f'<text class="s" x="{x + w / 2}" y="{y + size + 6}" text-anchor="middle" '
        f'fill="{TXT}" font-size="{size}">{e(text)}</text>'
    )


# ---------------------------------------------------------------- cards
def hero():
    p = PROFILE
    n = len(p["roles"])
    dur = 3.2 * n
    body = [
        '<defs><pattern id="g" width="22" height="22" patternUnits="userSpaceOnUse">'
        '<path d="M22 0H0V22" fill="none" stroke="rgba(255,255,255,0.035)"/></pattern>'
        f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG2}"/>'
        f'<stop offset="0.75" stop-color="{BG}"/></linearGradient>'
        f'<radialGradient id="glow" cx="0.85" cy="0.2" r="0.6"><stop offset="0" stop-color="{ACC_D}" stop-opacity="0.35"/>'
        f'<stop offset="1" stop-color="{ACC_D}" stop-opacity="0"/></radialGradient>'
        '<clipPath id="c"><rect x="1" y="1" width="838" height="258" rx="18"/></clipPath></defs>',
        f'<rect x="0.5" y="0.5" width="839" height="259" rx="18" fill="url(#bg)" stroke="rgba(255,255,255,0.09)"/>',
        '<g clip-path="url(#c)"><rect width="840" height="260" fill="url(#g)"/>'
        '<rect width="840" height="260" fill="url(#glow)"/></g>',
        f'<text class="m" x="44" y="64" fill="{ACC2}" font-size="12">HI THERE, I AM</text>',
        f'<text class="h" x="40" y="122" fill="{TXT}" font-size="58" letter-spacing="-1">{e(p["name"])}</text>',
    ]
    for i, role in enumerate(p["roles"]):
        a, b = i / n, (i + 1) / n
        if i == 0:
            vals, keys = "1;1;0;0;1", f"0;{b - 0.02:.3f};{b:.3f};{1 - 0.02:.3f};1"
        else:
            vals, keys = "0;0;1;1;0;0", f"0;{a:.3f};{a + 0.02:.3f};{b - 0.02:.3f};{b:.3f};1"
        body.append(
            f'<text class="s" x="44" y="158" fill="rgba(255,255,255,0.8)" font-size="18" opacity="{1 if i == 0 else 0}">'
            f'{e(role)}<animate attributeName="opacity" values="{vals}" keyTimes="{keys}" '
            f'dur="{dur}s" repeatCount="indefinite"/></text>'
        )
    sw = int(len(p["status"]) * 7.4) + 44
    body.append(
        f'<rect x="44" y="184" width="{sw}" height="30" rx="15" fill="#22c55e14" stroke="#22c55e55"/>'
        '<circle cx="63" cy="199" r="4.5" fill="#22c55e"><animate attributeName="opacity" '
        'values="1;0.3;1" dur="1.8s" repeatCount="indefinite"/></circle>'
        f'<text class="s" x="76" y="204" fill="#bbf7d0" font-size="13">{e(p["status"])}</text>'
    )
    # terminal panel
    tx, ty = 560, 40
    lines = [
        (ACC2, "$ whoami"),
        (TXT, "kiran_rana"),
        (ACC2, "$ cat focus.txt"),
        (TXT, "LLMs + VLMs"),
        (TXT, "Backend systems"),
        (TXT, "Cloud on AWS"),
        (ACC2, "$ location"),
        (TXT, "Santa Cruz, CA"),
    ]
    body.append(
        f'<rect x="{tx}" y="{ty}" width="240" height="180" rx="12" fill="rgba(0,0,0,0.35)" stroke="{FAINT}"/>'
        f'<circle cx="{tx + 16}" cy="{ty + 15}" r="4" fill="#f87171"/>'
        f'<circle cx="{tx + 30}" cy="{ty + 15}" r="4" fill="#fbbf24"/>'
        f'<circle cx="{tx + 44}" cy="{ty + 15}" r="4" fill="#34d399"/>'
    )
    for i, (c, t) in enumerate(lines):
        body.append(
            f'<text x="{tx + 16}" y="{ty + 44 + i * 17}" fill="{c}" font-family="{MONO}" '
            f'font-size="12">{e(t)}{fade(0.3 + i * 0.25, 0.2)}</text>'
        )
    body.append(
        f'<rect x="{tx + 16}" y="{ty + 44 + len(lines) * 17 - 11}" width="8" height="13" fill="{ACC}">'
        '<animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>'
    )
    svg("hero", 260, "".join(body), f'{p["name"]}. ' + ". ".join(p["roles"]))


def intro():
    lines = wrap(PROFILE["intro"], 104)
    h = 40 + len(lines) * 22
    body = [card(h), f'<rect x="0" y="18" width="4" height="{h - 36}" rx="2" fill="{ACC}"/>']
    for i, ln in enumerate(lines):
        body.append(f'<text class="s" x="28" y="{34 + i * 22}" fill="rgba(255,255,255,0.82)" font-size="14.5">{e(ln)}</text>')
    svg("intro", h, "".join(body), PROFILE["intro"])


CONNECT_ICONS = {
    # simple glyphs drawn in a 20x20 box
    "linkedin": '<rect x="0" y="0" width="20" height="20" rx="4" fill="{c}"/>'
                '<text x="10" y="15" text-anchor="middle" font-family="Arial" font-weight="700" font-size="12" fill="#0c0a14">in</text>',
    "email": '<rect x="1" y="3" width="18" height="14" rx="2" fill="none" stroke="{c}" stroke-width="2"/>'
             '<path d="M2 5l8 6 8-6" fill="none" stroke="{c}" stroke-width="2"/>',
    "github": '<circle cx="10" cy="10" r="9" fill="none" stroke="{c}" stroke-width="2"/>'
              '<path d="M7 17v-3c0-1 .5-1.6 1-2-2-.3-3.5-1-3.5-3.4 0-.8.3-1.5.8-2-.1-.3-.3-1.1.1-2.1 0 0 .7-.2 2.1.8a7 7 0 0 1 4 0c1.4-1 2.1-.8 2.1-.8.4 1 .2 1.8.1 2.1.5.5.8 1.2.8 2 0 2.4-1.5 3.1-3.5 3.4.5.4 1 1 1 2v3" fill="none" stroke="{c}" stroke-width="1.6"/>',
}


def connect():
    for key, label, color in [
        ("linkedin", "LinkedIn", "#60a5fa"),
        ("email", "Email", ACC2),
        ("github", "GitHub", ACC),
    ]:
        w, h = 240, 56
        icon = CONNECT_ICONS[key].format(c=color)
        body = (
            f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="14" fill="{BG}" stroke="{color}55"/>'
            f'<g transform="translate(70 18)">{icon}</g>'
            f'<text class="t" x="102" y="34" fill="{TXT}" font-size="16">{label}</text>'
        )
        svg(f"connect-{key}", h, body, label, width=w)


def header(slug, num, kicker, title):
    for mode, fg, line in [("dark", "#f5f3ff", "rgba(255,255,255,0.12)"), ("light", "#1e1b2e", "rgba(0,0,0,0.12)")]:
        kc = ACC if mode == "dark" else ACC_D
        body = (
            f'<defs><linearGradient id="sw" x1="0" x2="1"><stop offset="0" stop-color="{ACC}" stop-opacity="0"/>'
            f'<stop offset="0.5" stop-color="{kc}"/><stop offset="1" stop-color="{ACC}" stop-opacity="0"/></linearGradient></defs>'
            f'<rect x="0" y="12" width="4" height="32" rx="2" fill="{ACC_D}"/>'
            f'<text class="m" x="18" y="24" fill="{kc}" font-size="11">{num}  /  {e(kicker)}</text>'
            f'<text class="t" x="18" y="48" fill="{fg}" font-size="24">{e(title)}</text>'
            f'<line x1="0" y1="62" x2="840" y2="62" stroke="{line}"/>'
            f'<rect x="-160" y="61" width="160" height="2" fill="url(#sw)"><animateTransform attributeName="transform" '
            f'type="translate" values="0 0;1000 0" dur="4.5s" repeatCount="indefinite"/></rect>'
        )
        svg(f"header-{slug}-{mode}", 66, body, title)


def divider():
    body = (
        f'<defs><linearGradient id="p" x1="0" x2="1"><stop offset="0" stop-color="{ACC_D}" stop-opacity="0"/>'
        f'<stop offset="0.5" stop-color="{ACC}"/><stop offset="1" stop-color="{ACC_D}" stop-opacity="0"/></linearGradient></defs>'
        '<line x1="0" y1="7" x2="840" y2="7" stroke="rgba(127,127,127,0.28)"/>'
        f'<circle cx="420" cy="7" r="2.5" fill="{ACC}"/>'
        '<rect x="-220" y="6" width="220" height="2" fill="url(#p)"><animateTransform attributeName="transform" '
        'type="translate" values="0 0;1060 0" dur="3.6s" repeatCount="indefinite"/></rect>'
    )
    svg("divider", 14, body, "divider")


def timeline():
    items = PROFILE["timeline"]
    h, y, x0, x1 = 170, 80, 80, 760
    step = (x1 - x0) / (len(items) - 1)
    L = x1 - x0
    body = [
        card(h),
        f'<text class="m" x="24" y="30" fill="{ACC2}" font-size="10">JOURNEY</text>',
        f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{FAINT}" stroke-width="2"/>',
        f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{ACC_D}" stroke-width="2" '
        f'stroke-dasharray="{L}" stroke-dashoffset="{L}"><animate attributeName="stroke-dashoffset" '
        f'from="{L}" to="0" dur="2.4s" begin="0.3s" fill="freeze"/></line>',
    ]
    for i, (year, what, where) in enumerate(items):
        x = x0 + i * step
        t = 0.3 + 2.4 * i / (len(items) - 1)
        last = i == len(items) - 1
        c = ACC2 if last else ACC
        body.append(
            f'<g>{fade(t, 0.4)}'
            f'<circle cx="{x:.1f}" cy="{y}" r="7" fill="{BG}" stroke="{c}" stroke-width="2"/>'
            f'<circle cx="{x:.1f}" cy="{y}" r="3" fill="{c}"/>'
            f'<text class="m" x="{x:.1f}" y="{y - 20}" text-anchor="middle" fill="{c}" font-size="11">{year}</text>'
            f'<text class="t" x="{x:.1f}" y="{y + 32}" text-anchor="middle" fill="{TXT}" font-size="13">{e(what)}</text>'
            f'<text class="s" x="{x:.1f}" y="{y + 50}" text-anchor="middle" fill="{MUTED}" font-size="11">{e(where)}</text></g>'
        )
        if last:
            body.append(
                f'<circle cx="{x:.1f}" cy="{y}" r="7" fill="none" stroke="{ACC2}">'
                '<animate attributeName="r" values="7;16" dur="2s" repeatCount="indefinite"/>'
                '<animate attributeName="opacity" values="0.9;0" dur="2s" repeatCount="indefinite"/></circle>'
            )
    svg("timeline", h, "".join(body), "Journey: " + ", ".join(f"{a} {b}, {c}" for a, b, c in items))


def project_cards():
    w, h = 410, 210
    for p in PROFILE["projects"]:
        body = [
            f'<defs><linearGradient id="t" x1="0" x2="1"><stop offset="0" stop-color="{ACC_D}"/>'
            f'<stop offset="1" stop-color="{ACC2}"/></linearGradient></defs>',
            card(h, w, 14),
            f'<rect x="1" y="1" width="{w - 2}" height="4" rx="2" fill="url(#t)"/>',
            f'<text class="m" x="20" y="34" fill="{ACC2}" font-size="10">{e(p["tag"])}</text>',
            f'<text class="t" x="20" y="62" fill="{TXT}" font-size="20">{e(p["name"])}</text>',
        ]
        for i, ln in enumerate(wrap(p["desc"], 56)[:4]):
            body.append(f'<text class="s" x="20" y="{88 + i * 18}" fill="rgba(255,255,255,0.72)" font-size="12.5">{e(ln)}</text>')
        body.append(f'<text class="m" x="20" y="{h - 48}" fill="{ACC}" font-size="10.5" letter-spacing="0.6">&#9656; {e(p["metric"])}</text>')
        x = 20
        for s in p["stack"]:
            cw, c = chip(x, h - 36, s, ACC, 10)
            body.append(c)
            x += cw + 6
        svg(f'project-{p["slug"]}', h, "".join(body), f'{p["name"]}: {p["desc"]}', width=w)


def stack():
    groups = PROFILE["stack"]
    body, y = [], 22
    rows = []
    for label, items in groups:
        x, line, lines = 170, [], []
        for it in items:
            cw = int(len(it) * 12 * 0.62) + 20
            if x + cw > 816:
                lines.append(line)
                line, x = [], 170
            line.append((x, it))
            x += cw + 8
        lines.append(line)
        rows.append((label, lines, y))
        y += len(lines) * 34 + 10
    h = y + 12
    body.append(card(h))
    colors = [ACC, ACC2, "#60a5fa", "#f472b6", "#fbbf24"]
    for gi, (label, lines, top) in enumerate(rows):
        c = colors[gi % len(colors)]
        body.append(f'<g>{fade(0.15 + gi * 0.2)}')
        body.append(f'<text class="m" x="24" y="{top + 18}" fill="{c}" font-size="10.5">{e(label)}</text>')
        for li, line in enumerate(lines):
            for x, it in line:
                _, ch = chip(x, top + li * 34, it, c, 12)
                body.append(ch)
        body.append("</g>")
    svg("stack", h, "".join(body), "Tech stack: " + "; ".join(f"{a}: {', '.join(b)}" for a, b in groups))


def education():
    items = PROFILE["education"]
    h, gap = 150, 12
    w = (W - 40 - gap * 2) / 3
    body = [card(h)]
    for i, (school, degree, when, gpa) in enumerate(items):
        x = 20 + i * (w + gap)
        sl = wrap(school, 30)
        body.append(f'<g>{fade(0.2 + i * 0.25)}')
        body.append(f'<rect x="{x:.1f}" y="20" width="{w:.1f}" height="110" rx="12" fill="{BG2}" stroke="{FAINT}"/>')
        body.append(f'<text class="m" x="{x + 16:.1f}" y="42" fill="{ACC2}" font-size="9.5">{e(when.upper())}</text>')
        for j, ln in enumerate(sl[:2]):
            body.append(f'<text class="t" x="{x + 16:.1f}" y="{64 + j * 17}" fill="{TXT}" font-size="14">{e(ln)}</text>')
        dy = 64 + len(sl[:2]) * 17 + 2
        body.append(f'<text class="s" x="{x + 16:.1f}" y="{dy}" fill="{MUTED}" font-size="11.5">{e(degree)}</text>')
        body.append(f'<text class="m" x="{x + 16:.1f}" y="118" fill="{ACC}" font-size="11">{e(gpa)}</text>')
        body.append("</g>")
    svg("education", h, "".join(body), "Education: " + "; ".join(f"{b}, {a} ({c}), {d}" for a, b, c, d in items))


def leadership():
    items = PROFILE["leadership"]
    h, gap = 118, 12
    w = (W - 40 - gap) / 2
    body = [card(h)]
    for i, (title, org, when, desc) in enumerate(items):
        x = 20 + i * (w + gap)
        body.append(f'<g>{fade(0.2 + i * 0.25)}')
        body.append(f'<rect x="{x:.1f}" y="18" width="{w:.1f}" height="82" rx="12" fill="{BG2}" stroke="{FAINT}"/>')
        body.append(f'<text class="t" x="{x + 16:.1f}" y="42" fill="{TXT}" font-size="14.5">{e(title)}</text>')
        body.append(f'<text class="s" x="{x + 16:.1f}" y="59" fill="{ACC}" font-size="11.5">{e(org)}  ·  {e(when)}</text>')
        for j, ln in enumerate(wrap(desc, 58)[:2]):
            body.append(f'<text class="s" x="{x + 16:.1f}" y="{78 + j * 15}" fill="{MUTED}" font-size="11.5">{e(ln)}</text>')
        body.append("</g>")
    svg("leadership", h, "".join(body), "Leadership: " + "; ".join(f"{a}, {b}" for a, b, _, _ in items))


def footer():
    h = 90
    body = (
        f'<defs><linearGradient id="f" x1="0" x2="1"><stop offset="0" stop-color="{ACC}"/>'
        f'<stop offset="1" stop-color="{ACC2}"/></linearGradient></defs>'
        + card(h)
        + f'<text class="h" x="420" y="44" text-anchor="middle" fill="url(#f)" font-size="22">Thanks for stopping by!</text>'
        f'<text class="s" x="420" y="68" text-anchor="middle" fill="{MUTED}" font-size="13">'
        "Always happy to talk about AI systems, backend engineering and new opportunities.</text>"
    )
    svg("footer", h, body, "Thanks for visiting")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    hero()
    intro()
    connect()
    divider()
    for slug, num, kicker, title in [
        ("experience", "01", "WHERE I HAVE WORKED", "Experience"),
        ("projects", "02", "THINGS I HAVE BUILT", "Featured Projects"),
        ("stack", "03", "WHAT I WORK WITH", "Tech Stack"),
        ("stats", "04", "ACTIVITY ON GITHUB", "Contributions"),
        ("education", "05", "WHERE I STUDIED", "Education"),
        ("leadership", "06", "BEYOND CODE", "Leadership & Involvement"),
    ]:
        header(slug, num, kicker, title)
    timeline()
    project_cards()
    stack()
    education()
    leadership()
    footer()
    print(f"wrote {len(list(OUT.glob('*.svg')))} svgs to {OUT}")
