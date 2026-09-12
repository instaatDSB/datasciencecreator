#!/usr/bin/env python3
"""
Build book/playbook/index.html from book/MASTER_MANUSCRIPT.md.

Structure of the produced document:
- Cover page (custom layout)
- Table of contents
- Part opener 1: The Workflow
- Chapters 2..29 (chapters 2..7 introduce the framework; 8..29 walk it)
- Part opener 2: Practice & Reference
- Chapters 30..32
- Glossary
- Final Reference Card

Each `## PAGE NN — TITLE` section in the master manuscript becomes a chapter.
The `## GLOSSARY` and `## FINAL REFERENCE CARD` sections get custom layouts.
"""

import re
import html
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent.parent
MASTER = REPO / "book" / "MASTER_MANUSCRIPT.md"
OUT = ROOT / "index.html"

CALLOUT_LABELS = {
    "KEY IDEA": "key",
    "WATCH OUT": "watch",
    "TRY THIS": "try",
    "REAL-WORLD EXAMPLE": "example",
    "REMEMBER": "remember",
    "BEGINNER NOTE": "beginner",
    "THE INTELLECTUAL PAYOFF, IN ONE LINE": "key",
}

CHAPTER_META = {
    # page-num -> (eyebrow, title override or None)
    "02": ("The problem", None),
    "03": ("The problem", None),
    "04": ("Foundations", None),
    "05": ("Foundations", None),
    "06": ("Foundations", None),
    "07": ("The framework", None),
    "08": ("Define", None),
    "09": ("Define", None),
    "10": ("Define", None),
    "11": ("Context", None),
    "12": ("Context", None),
    "13": ("Context", None),
    "14": ("Investigate", None),
    "15": ("Investigate", None),
    "16": ("Execute", None),
    "17": ("Execute", None),
    "18": ("Boundaries", None),
    "19": ("Boundaries", None),
    "20": ("Verify", None),
    "21": ("Verify", None),
    "22": ("Verify", None),
    "23": ("Verify", None),
    "24": ("Review", None),
    "25": ("Review", None),
    "26": ("Learn", None),
    "27": ("Learn", None),
    "28": ("The whole system", None),
    "29": ("Walkthrough", None),
    "30": ("Practice", None),
    "31": ("Practice", None),
    "32": ("Close", None),
}

md = markdown.Markdown(extensions=["extra", "tables", "sane_lists"])


def parse_master(text: str):
    """Yield ('page'|'glossary'|'ref', number-or-None, title, body_markdown) tuples."""
    # Remove the H1 top matter
    text = re.sub(r"(?ms)^# .*?\n\n", "", text, count=1)
    # Remove the italic top strapline the H1 was followed by
    text = re.sub(r"(?ms)^\*.*?\*\s*\n\s*---\s*\n", "", text, count=1)

    parts = re.split(r"(?m)^## ", text)
    parts = [p for p in parts if p.strip()]

    for chunk in parts:
        heading, _, body = chunk.partition("\n")
        heading = heading.strip()
        body = body.strip()
        m = re.match(r"PAGE (\d{2})\s*—\s*(.+)", heading)
        if m:
            yield ("page", m.group(1), m.group(2).strip(), body)
        elif heading.upper().startswith("GLOSSARY"):
            yield ("glossary", None, "Glossary", body)
        elif heading.upper().startswith("FINAL REFERENCE"):
            yield ("ref", None, "Final reference card", body)


def render_body_html(body_md: str) -> str:
    """Render manuscript body markdown, then dress blockquotes as callouts."""
    md.reset()
    raw = md.convert(body_md)

    # Wrap blockquotes into typed callouts when their first <strong> matches a label
    def replace_blockquote(m: re.Match) -> str:
        inner = m.group(1)
        # find first <strong>...</strong>
        sm = re.search(r"<strong>([^<]+)</strong>", inner)
        if not sm:
            return f'<blockquote>{inner}</blockquote>'
        label_raw = sm.group(1).strip()
        # normalize labels like "REAL-WORLD EXAMPLE" ; also handle "THE INTELLECTUAL PAYOFF, IN ONE LINE"
        label_key = None
        for label, cls in CALLOUT_LABELS.items():
            if label_raw.upper().startswith(label):
                label_key = (label, cls)
                break
        if not label_key:
            return f'<blockquote>{inner}</blockquote>'
        label, cls = label_key
        # strip the leading "<p><strong>LABEL</strong> ...</p>" and its trailing <br> if any
        stripped = re.sub(
            r"^\s*<p>\s*<strong>[^<]+</strong>\s*(<br\s*/?>)?\s*",
            "<p>",
            inner,
            count=1,
        )
        # remove empty leading <p></p>
        stripped = re.sub(r"^\s*<p>\s*</p>", "", stripped)
        return (
            f'<blockquote class="pb-callout pb-callout--{cls}">'
            f'<span class="pb-callout__label">{html.escape(label)}</span>'
            f"{stripped}"
            f"</blockquote>"
        )

    # Non-greedy match across newlines
    dressed = re.sub(r"<blockquote>(.*?)</blockquote>", replace_blockquote, raw, flags=re.S)
    return dressed


def render_cover() -> str:
    return """
<section class="page pb-cover" data-section="pb" id="cover">
  <div class="pb-cover__top">
    <span class="pill">Ebook · 01</span>
    <span>@data.science.beginners</span>
  </div>

  <div class="pb-cover__mark" aria-hidden="true">
    <svg viewBox="0 0 220 120" width="220" height="120" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="pbgrad" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stop-color="#4CE0D6"/>
          <stop offset="1" stop-color="#7A5CFF"/>
        </linearGradient>
      </defs>
      <!-- 8-stage ring dots -->
      <g>
        <circle cx="30"  cy="60" r="7" fill="url(#pbgrad)"/>
        <circle cx="55"  cy="30" r="6" fill="url(#pbgrad)" opacity="0.9"/>
        <circle cx="90"  cy="20" r="6" fill="url(#pbgrad)" opacity="0.85"/>
        <circle cx="125" cy="30" r="6" fill="url(#pbgrad)" opacity="0.8"/>
        <circle cx="150" cy="60" r="6" fill="url(#pbgrad)" opacity="0.75"/>
        <circle cx="125" cy="90" r="6" fill="url(#pbgrad)" opacity="0.7"/>
        <circle cx="90"  cy="100" r="6" fill="url(#pbgrad)" opacity="0.65"/>
        <circle cx="55"  cy="90" r="6" fill="url(#pbgrad)" opacity="0.6"/>
      </g>
      <path d="M30 60 L55 30 L90 20 L125 30 L150 60 L125 90 L90 100 L55 90 Z"
            stroke="#4CE0D6" stroke-opacity="0.35" stroke-width="1" fill="none"/>
      <!-- central icon -->
      <g transform="translate(180,40)">
        <rect x="0" y="0" width="24" height="30" rx="3"
              fill="none" stroke="#F0F4FF" stroke-opacity="0.9" stroke-width="1.5"/>
        <line x1="4" y1="8"  x2="14" y2="8"  stroke="#4CE0D6" stroke-width="1.5"/>
        <line x1="4" y1="14" x2="20" y2="14" stroke="#F0F4FF" stroke-opacity="0.6" stroke-width="1.5"/>
        <line x1="4" y1="20" x2="18" y2="20" stroke="#F0F4FF" stroke-opacity="0.6" stroke-width="1.5"/>
      </g>
    </svg>
  </div>

  <div class="pb-cover__body">
    <p class="pb-cover__eyebrow">The playbook</p>
    <h1 class="pb-cover__title">The AI Coding<br/>Agent Playbook.</h1>
    <p class="pb-cover__sub">A beginner-friendly guide to working with AI coding agents — from your first instruction to a reliable development workflow.</p>
    <div class="pb-cover__chips">
      <span class="chip">Prompt ≠ workflow</span>
      <span class="chip">Eight stages</span>
      <span class="chip">One running example</span>
      <span class="chip">Glossary + reference card</span>
    </div>
    <div class="pb-cover__foot">
      <div>
        <div class="publisher">@data.science.beginners</div>
        <div style="margin-top:2mm;">Ebook 01 · First edition</div>
      </div>
      <div style="text-align:right;">
        <div>32 pages · A5</div>
        <div style="margin-top:2mm;">For students, career switchers, junior devs</div>
      </div>
    </div>
  </div>
</section>
"""


def render_toc(page_meta):
    """page_meta: list of dicts with 'num','title','eyebrow'."""
    lines = []
    lines.append('<section class="page pb-toc-page" data-section="pb" id="toc">')
    lines.append('  <header class="page-head"><span class="pill">Contents</span><span>@data.science.beginners</span></header>')
    lines.append('  <h1 class="page-title">Contents.</h1>')
    lines.append('  <p class="page-lede">Thirty-two short chapters, one running example, and a workflow you can start using on your next task.</p>')
    lines.append('  <div class="pb-toc">')

    # Group by eyebrow into rough parts
    part_titles = [
        ("The problem", ["02", "03"]),
        ("Foundations", ["04", "05", "06"]),
        ("The framework", ["07"]),
        ("Define", ["08", "09", "10"]),
        ("Context", ["11", "12", "13"]),
        ("Investigate", ["14", "15"]),
        ("Execute", ["16", "17"]),
        ("Boundaries", ["18", "19"]),
        ("Verify", ["20", "21", "22", "23"]),
        ("Review", ["24", "25"]),
        ("Learn", ["26", "27"]),
        ("The whole system", ["28", "29"]),
        ("Practice", ["30", "31"]),
        ("Close", ["32"]),
    ]
    by_num = {p["num"]: p for p in page_meta}
    for section_title, nums in part_titles:
        lines.append(f'    <div class="pb-toc__section">{section_title}</div>')
        for n in nums:
            p = by_num.get(n)
            if not p:
                continue
            lines.append(
                f'    <div class="pb-toc__item"><span class="num">{n}</span>'
                f'<span class="title">{html.escape(p["title"])}</span>'
                f'<span class="pg">Ch. {int(n)-1}</span></div>'
            )
    lines.append('    <div class="pb-toc__section">Reference</div>')
    lines.append('    <div class="pb-toc__item"><span class="num">G</span><span class="title">Glossary</span><span class="pg">—</span></div>')
    lines.append('    <div class="pb-toc__item"><span class="num">R</span><span class="title">Final reference card</span><span class="pg">—</span></div>')
    lines.append('  </div>')
    lines.append('  <footer class="pb-foot"><span>The AI Coding Agent Playbook</span><span class="r">Contents</span></footer>')
    lines.append('</section>')
    return "\n".join(lines)


def render_part(eyebrow: str, title: str, sub: str) -> str:
    return f"""
<section class="page pb-part" data-section="pb">
  <div>
    <p class="pb-part__eyebrow">{html.escape(eyebrow)}</p>
    <h1 class="pb-part__title">{html.escape(title)}</h1>
    <p class="pb-part__sub">{html.escape(sub)}</p>
  </div>
</section>
"""


def render_chapter(num: str, title: str, body_md: str) -> str:
    meta = CHAPTER_META.get(num, ("", None))
    eyebrow = meta[0]
    body_html = render_body_html(body_md)
    return f"""
<section class="page pb-chapter" data-section="pb" id="ch-{num}">
  <header class="pb-chapter__opener">
    <div class="pb-chapter__eyebrow"><span class="num">{num}</span> <span>{html.escape(eyebrow)}</span></div>
    <h1 class="pb-chapter__title">{html.escape(title)}</h1>
  </header>
  <div class="pb-body">
    {body_html}
  </div>
  <footer class="pb-foot"><span>The AI Coding Agent Playbook</span><span class="r">{html.escape(eyebrow or "")}</span></footer>
</section>
"""


def render_glossary(body_md: str) -> str:
    # Filter out leading paragraphs that are prose intro before terms
    body_html = md.reset() or md.convert(body_md)
    return f"""
<section class="page pb-glossary-page" data-section="pb" id="glossary">
  <header class="page-head"><span class="pill">Reference</span><span>@data.science.beginners</span></header>
  <h1 class="page-title">Glossary.</h1>
  <p class="page-lede">Plain-English definitions of every technical term used in this book.</p>
  <div class="pb-body pb-glossary">
    {body_html}
  </div>
  <footer class="pb-foot"><span>The AI Coding Agent Playbook</span><span class="r">Glossary</span></footer>
</section>
"""


def render_reference(body_md: str) -> str:
    # Break the reference card body into blocks by leading <hr> and render as boxed blocks
    # Simpler: render markdown as-is, then wrap each top-level section (separated by <hr />) into pb-ref__block
    md.reset()
    raw = md.convert(body_md)
    # Split on horizontal rules
    parts = re.split(r"<hr\s*/?>", raw)
    blocks = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        blocks.append(f'<div class="pb-ref__block">{p}</div>')
    inner = "\n".join(blocks)
    return f"""
<section class="page pb-ref-page" data-section="pb" id="reference-card">
  <header class="page-head"><span class="pill">Take-away</span><span>@data.science.beginners</span></header>
  <h1 class="page-title">Reference card.</h1>
  <p class="page-lede">Tear this out. Keep it next to your keyboard. Or just remember it.</p>
  <div class="pb-body pb-ref">
    {inner}
  </div>
  <footer class="pb-foot"><span>The AI Coding Agent Playbook</span><span class="r">Reference</span></footer>
</section>
"""


def main():
    text = MASTER.read_text()
    sections = list(parse_master(text))

    pages = [s for s in sections if s[0] == "page"]
    glossary = next((s for s in sections if s[0] == "glossary"), None)
    reference = next((s for s in sections if s[0] == "ref"), None)

    # Build meta for TOC (skip page 01, which is the cover)
    page_meta = [
        {"num": num, "title": title, "eyebrow": CHAPTER_META.get(num, ("",))[0]}
        for kind, num, title, _ in pages
        if num != "01"
    ]

    parts_html = [render_cover(), render_toc(page_meta)]

    # Part 1 opener
    parts_html.append(render_part(
        "Part one",
        "The workflow.",
        "The problem with prompts alone, the foundations of working with agents, and the eight-stage system this book teaches."
    ))

    for kind, num, title, body in pages:
        if num == "01":
            continue  # cover already rendered
        # Insert a part divider before the practice chapters (Page 30)
        if num == "30":
            parts_html.append(render_part(
                "Part two",
                "Practice & reference.",
                "A reusable task template, the two working checklists, and a closing chapter on the only skill in this field that will still be worth having in ten years."
            ))
        parts_html.append(render_chapter(num, title, body))

    if glossary:
        parts_html.append(render_glossary(glossary[3]))
    if reference:
        parts_html.append(render_reference(reference[3]))

    html_doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>The AI Coding Agent Playbook — @data.science.beginners · Ebook 01</title>
<meta name="description" content="A beginner-friendly guide to working with AI coding agents — from your first instruction to a reliable development workflow." />
<meta name="author" content="@data.science.beginners" />
<link rel="stylesheet" href="../../assets/css/main.css" />
<link rel="stylesheet" href="../../assets/css/print.css" media="all" />
<link rel="stylesheet" href="style.css" />
</head>
<body class="screen">
<p class="screen-hint screen-only">Preview · Print (⌘/Ctrl-P) for a clean A5 PDF · or run <code>npm run build:playbook-pdf</code></p>

{"".join(parts_html)}

</body>
</html>
"""
    OUT.write_text(html_doc)
    print(f"Wrote {OUT} — {len(pages)} chapters, glossary + ref card = {sum(bool(x) for x in (glossary, reference))}")


if __name__ == "__main__":
    main()
