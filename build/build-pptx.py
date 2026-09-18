#!/usr/bin/env python3
"""
Build two Canva-importable PPTX exports of the 11-slide carousel.

Usage:
    python3 build/build-pptx.py

Outputs:
    build/output/AICodingAgentPlaybook_image.pptx   (each slide = one PNG)
    build/output/AICodingAgentPlaybook_text.pptx    (native text + shapes)

Slide size = 1080 x 1350 px = 11.25 x 14.0625 inches (Instagram portrait 4:5).
"""

from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree

ROOT = Path("/home/user/datasciencecreator")
CAROUSEL_DIR = ROOT / "build" / "output" / "carousel"
OUT_DIR = ROOT / "build" / "output"

# 1080 x 1350 px  at 96 DPI  = 11.25 x 14.0625 inches
SLIDE_W = Inches(11.25)
SLIDE_H = Inches(14.0625)

# Brand palette
INK       = RGBColor(0xF0, 0xF4, 0xFF)
INK_SOFT  = RGBColor(0xC7, 0xCE, 0xE8)
INK_MUTE  = RGBColor(0x8E, 0x99, 0xC0)
BG_1      = RGBColor(0x0B, 0x16, 0x38)
BG_2      = RGBColor(0x06, 0x0B, 0x1C)
CARD      = RGBColor(0x14, 0x22, 0x4E)
TEAL      = RGBColor(0x4C, 0xE0, 0xD6)
VIOLET    = RGBColor(0x7A, 0x5C, 0xFF)
AMBER     = RGBColor(0xF5, 0xC4, 0x53)
PINK      = RGBColor(0xF5, 0x8B, 0xB6)
GREEN     = RGBColor(0x6E, 0xE7, 0xA2)


def new_prs() -> Presentation:
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    return prs


# ---------------------------------------------------------------------------
# IMAGE-LOCKED PPTX
# ---------------------------------------------------------------------------
def build_image_pptx() -> Path:
    prs = new_prs()
    blank = prs.slide_layouts[6]
    slide_files = sorted(CAROUSEL_DIR.glob("slide-*.png"))
    if not slide_files:
        raise SystemExit(f"No slide PNGs in {CAROUSEL_DIR}")
    for png in slide_files:
        slide = prs.slides.add_slide(blank)
        slide.shapes.add_picture(str(png), 0, 0, width=SLIDE_W, height=SLIDE_H)
    out = OUT_DIR / "AICodingAgentPlaybook_image.pptx"
    prs.save(str(out))
    print(f"✓ {out}  ({len(slide_files)} slides)")
    return out


# ---------------------------------------------------------------------------
# TEXT-FIRST PPTX helpers
# ---------------------------------------------------------------------------
def add_bg(slide):
    """Solid dark background rectangle covering the whole slide."""
    rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, SLIDE_H)
    rect.line.fill.background()
    rect.fill.solid()
    rect.fill.fore_color.rgb = BG_2
    # Accent radial-ish overlay (top-right)
    over = slide.shapes.add_shape(MSO_SHAPE.OVAL,
                                  Inches(4.5), Inches(-3),
                                  Inches(10), Inches(9))
    over.line.fill.background()
    over.fill.solid()
    over.fill.fore_color.rgb = BG_1
    over.fill.transparency = 0.5 if hasattr(over.fill, "transparency") else 0
    return rect


def add_text(slide, x, y, w, h, text, *,
             size=24, bold=False, color=INK, align=PP_ALIGN.LEFT,
             font="Inter", letter_spacing=None, line_spacing=1.1):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = 0
    tf.margin_top = tf.margin_bottom = 0
    if isinstance(text, str):
        text = [text]
    for i, line in enumerate(text):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = line_spacing
        r = p.add_run()
        r.text = line
        f = r.font
        f.name = font
        f.size = Pt(size)
        f.bold = bold
        f.color.rgb = color
        if letter_spacing:
            # PPTX character spacing lives in a:rPr/@spc (1/100 pt)
            rPr = r._r.get_or_add_rPr()
            rPr.set('spc', str(int(letter_spacing * 100)))
    return tb


def add_card(slide, x, y, w, h, *, fill=CARD, line=None, radius=True):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE,
        x, y, w, h)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    if line is None:
        shape.line.fill.background()
    else:
        shape.line.color.rgb = line
        shape.line.width = Pt(1)
    # subtle corner radius
    if radius and shape.adjustments:
        try:
            shape.adjustments[0] = 0.05
        except Exception:
            pass
    return shape


def add_pill(slide, x, y, text, *, color=TEAL):
    w, h = Inches(2.6), Inches(0.42)
    pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    pill.fill.background()
    pill.line.color.rgb = color
    pill.line.width = Pt(1)
    if pill.adjustments:
        try:
            pill.adjustments[0] = 0.5
        except Exception:
            pass
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = text
    r.font.name = "Inter"
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = color


def add_header(slide, num):
    add_pill(slide, Inches(0.75), Inches(0.75), "@DATA.SCIENCE.BEGINNERS", color=TEAL)
    add_text(slide,
             Inches(SLIDE_W.inches - 0.75 - 2.6), Inches(0.75),
             Inches(2.6), Inches(0.42),
             f"{num:02d} / 11",
             size=11, color=INK_MUTE, bold=True, align=PP_ALIGN.RIGHT)


def add_footer(slide, left_text, right_text=None):
    y = SLIDE_H - Inches(1.0)
    add_text(slide, Inches(0.75), y, Inches(7), Inches(0.4),
             left_text, size=10, color=INK_MUTE, bold=True)
    if right_text:
        add_text(slide, SLIDE_W - Inches(4.75), y, Inches(4), Inches(0.4),
                 right_text, size=10, color=TEAL, bold=True, align=PP_ALIGN.RIGHT)


def add_num_circle(slide, x, y, n, size=Inches(0.55)):
    c = slide.shapes.add_shape(MSO_SHAPE.OVAL, x, y, size, size)
    c.fill.solid()
    c.fill.fore_color.rgb = TEAL
    c.line.fill.background()
    tb = slide.shapes.add_textbox(x, y, size, size)
    tf = tb.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = str(n)
    r.font.name = "Inter"; r.font.size = Pt(18); r.font.bold = True
    r.font.color.rgb = BG_2


# ---------------------------------------------------------------------------
# TEXT-FIRST slide builders
# ---------------------------------------------------------------------------
def slide_cover(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(s)
    add_pill(s, Inches(0.75), Inches(0.75), "EBOOK 01 · PLAYBOOK", color=TEAL)
    add_text(s, SLIDE_W - Inches(4.5), Inches(0.85), Inches(3.75), Inches(0.4),
             "@DATA.SCIENCE.BEGINNERS", size=11, color=INK_SOFT, bold=True, align=PP_ALIGN.RIGHT)

    add_text(s, Inches(0.75), Inches(3.6), Inches(10), Inches(5.5),
             ["The AI Coding", "Agent Playbook."],
             size=88, bold=True, color=INK, line_spacing=0.95)

    add_text(s, Inches(0.75), Inches(8.9), Inches(10), Inches(2),
             ["Why AI writes 400 lines of code",
              "and still breaks your project —",
              "and how to fix it."],
             size=26, color=INK_SOFT, line_spacing=1.35)

    add_text(s, Inches(0.75), SLIDE_H - Inches(1.0), Inches(7), Inches(0.5),
             "11 SLIDES · SAVE THIS", size=12, color=INK_MUTE, bold=True)
    add_text(s, SLIDE_W - Inches(3.75), SLIDE_H - Inches(1.0), Inches(3), Inches(0.5),
             "SWIPE →", size=14, color=TEAL, bold=True, align=PP_ALIGN.RIGHT)


def slide_02_problem(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(s); add_header(s, 2)
    add_text(s, Inches(0.75), Inches(2.0), Inches(4), Inches(0.4),
             "THE PROBLEM", size=13, color=TEAL, bold=True)
    add_text(s, Inches(0.75), Inches(2.7), Inches(10), Inches(4),
             ["AI wrote", "400 lines.", "Nothing works."],
             size=64, bold=True, color=INK, line_spacing=1.0)
    add_text(s, Inches(0.75), Inches(7.6), Inches(10), Inches(1.6),
             ["You typed a normal instruction.",
              "The agent worked confidently.",
              "Now your app is broken."],
             size=22, color=INK_SOFT, line_spacing=1.35)
    add_card(s, Inches(0.75), Inches(10.4), Inches(9.75), Inches(2.0),
             fill=CARD, line=TEAL)
    add_text(s, Inches(1.15), Inches(10.55), Inches(9), Inches(0.4),
             "THE UNCOMFORTABLE TRUTH", size=11, color=TEAL, bold=True)
    add_text(s, Inches(1.15), Inches(10.95), Inches(9), Inches(1.5),
             ["It's almost never your prompt.",
              "It's everything MISSING around the prompt."],
             size=20, color=INK, line_spacing=1.3)
    add_footer(s, "The AI Coding Agent Playbook", "KEEP GOING →")


def slide_03_three(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(s); add_header(s, 3)
    add_text(s, Inches(0.75), Inches(2.0), Inches(6), Inches(0.4),
             "KNOW WHAT YOU'RE USING", size=13, color=TEAL, bold=True)
    add_text(s, Inches(0.75), Inches(2.6), Inches(10), Inches(3),
             ["Three tools.", "Big difference."],
             size=68, bold=True, color=INK, line_spacing=1.0)

    cards = [
        ("💬", "CHATBOT",   "Just talks.\nNo files. No actions.", CARD, INK_MUTE, False),
        ("⌨️", "ASSISTANT", "Suggests as you type.\nYou still drive.", CARD, AMBER, False),
        ("⚙️", "AGENT",     "Edits files. Runs tests.\nShips real work.", CARD, TEAL, True),
    ]
    x0 = Inches(0.75); gap = Inches(0.3); cw = (SLIDE_W - Inches(1.5) - gap * 2) / 3
    y0 = Inches(7.3); ch = Inches(3.4)
    for i, (icon, label, body, fill, col, hi) in enumerate(cards):
        x = x0 + i * (cw + gap)
        card = add_card(s, x, y0, cw, ch, fill=fill, line=col if hi else None)
        if hi:
            card.line.width = Pt(2.25)
        add_text(s, x, y0 + Inches(0.25), cw, Inches(0.9),
                 icon, size=42, align=PP_ALIGN.CENTER)
        add_text(s, x, y0 + Inches(1.4), cw, Inches(0.5),
                 label, size=13, color=col, bold=True, align=PP_ALIGN.CENTER,
                 letter_spacing=3)
        add_text(s, x + Inches(0.2), y0 + Inches(1.95), cw - Inches(0.4), Inches(1.4),
                 body.split("\n"),
                 size=18, color=INK, align=PP_ALIGN.CENTER, line_spacing=1.35)

    add_text(s, Inches(0.75), Inches(11.5), Inches(10), Inches(1),
             "The more it can do, the more your WORKFLOW matters.",
             size=22, color=INK_SOFT)
    add_footer(s, "Chatbot ≠ Assistant ≠ Agent", "SWIPE →")


def slide_04_prompt_workflow(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(s); add_header(s, 4)
    add_text(s, Inches(0.75), Inches(2.0), Inches(8), Inches(0.4),
             "THE ONE IDEA TO REMEMBER", size=13, color=TEAL, bold=True)

    add_text(s, Inches(0.75), Inches(4.0), Inches(10), Inches(1.6),
             "A prompt", size=64, bold=True, color=INK, align=PP_ALIGN.CENTER, line_spacing=1.0)
    add_text(s, Inches(0.75), Inches(5.6), Inches(10), Inches(1.6),
             "is not a", size=64, bold=True, color=INK, align=PP_ALIGN.CENTER, line_spacing=1.0)
    add_text(s, Inches(0.75), Inches(7.2), Inches(10), Inches(1.8),
             "WORKFLOW.", size=88, bold=True, color=TEAL, align=PP_ALIGN.CENTER, line_spacing=1.0)

    add_card(s, Inches(0.75), Inches(10.5), Inches(9.75), Inches(2.0), fill=CARD, line=TEAL)
    add_text(s, Inches(1.15), Inches(10.7), Inches(9), Inches(1.6),
             ["Prompt = one instruction. Life: minutes.",
              "Workflow = the system around it. Life: the whole project."],
             size=18, color=INK, align=PP_ALIGN.CENTER, line_spacing=1.5)
    add_footer(s, "Prompt ≠ Workflow", "THE SYSTEM →")


def slide_05_framework(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(s); add_header(s, 5)
    add_text(s, Inches(0.75), Inches(2.0), Inches(6), Inches(0.4),
             "THE WHOLE WORKFLOW", size=13, color=TEAL, bold=True)
    add_text(s, Inches(0.75), Inches(2.6), Inches(10), Inches(2.4),
             ["The 8 stages.", "Skip one = trouble."],
             size=52, bold=True, color=INK, line_spacing=1.0)

    stages = [
        ("DEFINE",       "What is the job?"),
        ("CONTEXT",      "What is this project?"),
        ("INVESTIGATE",  "What's already there?"),
        ("BOUNDARIES",   "What must NOT change?"),
        ("EXECUTE",      "Small step. Look. Repeat."),
        ("VERIFY",       "Prove it works."),
        ("REVIEW",       "Read every change."),
        ("LEARN",        "Turn surprise into rule."),
    ]
    y = Inches(5.4); row_h = Inches(0.85); gap = Inches(0.12)
    for i, (name, desc) in enumerate(stages):
        yy = y + i * (row_h + gap)
        add_card(s, Inches(0.75), yy, Inches(9.75), row_h, fill=CARD)
        # left accent bar
        bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.75), yy, Inches(0.10), row_h)
        bar.fill.solid(); bar.fill.fore_color.rgb = TEAL; bar.line.fill.background()
        add_num_circle(s, Inches(1.15), yy + Inches(0.15), i + 1, size=Inches(0.55))
        add_text(s, Inches(2.05), yy + Inches(0.10), Inches(4), Inches(0.4),
                 name, size=20, bold=True, color=INK)
        add_text(s, Inches(2.05), yy + Inches(0.45), Inches(7), Inches(0.4),
                 desc, size=13, color=INK_MUTE)
    add_footer(s, "The 8-stage operating system", "ZOOM IN →")


def slide_06_define(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(s); add_header(s, 6)
    add_text(s, Inches(0.75), Inches(2.0), Inches(8), Inches(0.4),
             "STAGE 01 · DEFINE", size=13, color=TEAL, bold=True)
    add_text(s, Inches(0.75), Inches(2.6), Inches(10), Inches(3),
             ["\"Improve the", "dashboard\" is a trap."],
             size=52, bold=True, color=INK, line_spacing=1.0)

    # two cards
    cw = Inches(4.6); ch = Inches(4.8); y = Inches(6.4)
    # Vague
    add_card(s, Inches(0.75), y, cw, ch, fill=CARD, line=PINK)
    add_text(s, Inches(0.95), y + Inches(0.3), cw - Inches(0.4), Inches(0.4),
             "VAGUE  ✕", size=13, color=PINK, bold=True, letter_spacing=3)
    for i, item in enumerate(['"Fix the bug"', '"Make it better"', '"Add rejected status"']):
        add_text(s, Inches(0.95), y + Inches(1.0 + i * 0.9), cw - Inches(0.4), Inches(0.7),
                 item, size=20, color=INK)
    # Clear
    x2 = Inches(0.75 + 4.6 + 0.4)
    add_card(s, x2, y, cw, ch, fill=CARD, line=TEAL)
    add_text(s, x2 + Inches(0.2), y + Inches(0.3), cw - Inches(0.4), Inches(0.4),
             "CLEAR  ✓", size=13, color=TEAL, bold=True, letter_spacing=3)
    for i, (a, b) in enumerate([("Objective", " · outcome"),
                                 ("Scope", " · which files"),
                                 ("Done", " · a checkable list"),
                                 ("Rules", " · what NOT to change")]):
        tb = s.shapes.add_textbox(x2 + Inches(0.2), y + Inches(1.0 + i * 0.85),
                                   cw - Inches(0.4), Inches(0.7))
        tf = tb.text_frame; tf.margin_left = tf.margin_right = 0
        p = tf.paragraphs[0]
        r1 = p.add_run(); r1.text = a
        r1.font.name = "Inter"; r1.font.size = Pt(18); r1.font.bold = True; r1.font.color.rgb = TEAL
        r2 = p.add_run(); r2.text = b
        r2.font.name = "Inter"; r2.font.size = Pt(18); r2.font.color.rgb = INK

    add_text(s, Inches(0.75), Inches(11.7), Inches(10), Inches(0.8),
             "If a stranger took your instruction literally — would you be happy?",
             size=18, color=INK_SOFT)
    add_footer(s, "Define · Context · Investigate", "SWIPE →")


def slide_07_boundaries(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(s); add_header(s, 7)
    add_text(s, Inches(0.75), Inches(2.0), Inches(8), Inches(0.4),
             "STAGE 04 · BOUNDARIES", size=13, color=TEAL, bold=True)
    add_text(s, Inches(0.75), Inches(2.6), Inches(10), Inches(3),
             ["The half", "everyone forgets."],
             size=52, bold=True, color=INK, line_spacing=1.0)

    y = Inches(6.4); cw = Inches(4.6); ch = Inches(3.6)
    # CHANGE
    add_text(s, Inches(0.75), y, cw, Inches(0.4),
             "CHANGE", size=13, color=TEAL, bold=True, letter_spacing=3)
    add_card(s, Inches(0.75), y + Inches(0.5), cw, ch, fill=CARD)
    for i, item in enumerate(["Applications list page", "Its stylesheet"]):
        add_text(s, Inches(0.95), y + Inches(0.8 + i * 0.75), cw - Inches(0.4), Inches(0.6),
                 f"→  {item}", size=18, color=INK)
    # DO NOT CHANGE
    x2 = Inches(0.75 + 4.6 + 0.4)
    add_text(s, x2, y, cw, Inches(0.4),
             "DO NOT CHANGE", size=13, color=PINK, bold=True, letter_spacing=3)
    add_card(s, x2, y + Inches(0.5), cw, ch, fill=CARD)
    for i, item in enumerate(["Sign-in / auth", "Database schema",
                               "The Add form", "Anything not listed"]):
        add_text(s, x2 + Inches(0.2), y + Inches(0.8 + i * 0.6), cw - Inches(0.4), Inches(0.6),
                 f"✕  {item}", size=17, color=INK)

    # Rule box
    rb_y = Inches(10.7); rb_h = Inches(1.8)
    box = add_card(s, Inches(0.75), rb_y, Inches(9.75), rb_h, fill=BG_1, line=TEAL)
    box.line.dash_style = 5  # DASH
    add_text(s, Inches(1.0), rb_y + Inches(0.2), Inches(9), Inches(0.4),
             "PASTE THIS IN EVERY TASK", size=11, color=TEAL, bold=True, letter_spacing=3)
    add_text(s, Inches(1.0), rb_y + Inches(0.7), Inches(9), Inches(1.0),
             '"If you believe another file must change, STOP and tell me — do not change it yourself."',
             size=17, color=INK, font="JetBrains Mono", line_spacing=1.35)
    add_footer(s, "One sentence · huge safety net", "NEXT →")


def slide_08_loop(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(s); add_header(s, 8)
    add_text(s, Inches(0.75), Inches(2.0), Inches(9), Inches(0.4),
             "STAGES 05 – 06 · EXECUTE + VERIFY", size=13, color=TEAL, bold=True)
    add_text(s, Inches(0.75), Inches(2.6), Inches(10), Inches(3),
             ["Code that looks right", "can be wrong."],
             size=48, bold=True, color=INK, line_spacing=1.0)

    steps = ["IMPLEMENT", "TEST", "FIX", "TEST AGAIN", "VALIDATE"]
    y = Inches(7.4); w = Inches(1.75); h = Inches(1.75); gap = Inches(0.2)
    total = w * len(steps) + gap * (len(steps) - 1)
    x0 = (SLIDE_W - total) / 2
    for i, name in enumerate(steps):
        x = x0 + i * (w + gap)
        card = add_card(s, x, y, w, h, fill=CARD)
        add_text(s, x, y + Inches(0.3), w, Inches(0.7),
                 str(i + 1), size=36, color=TEAL, bold=True, align=PP_ALIGN.CENTER)
        add_text(s, x, y + Inches(1.05), w, Inches(0.6),
                 name, size=11, color=INK, bold=True, align=PP_ALIGN.CENTER, letter_spacing=2)

    add_card(s, Inches(0.75), Inches(10.5), Inches(9.75), Inches(2.0), fill=CARD, line=TEAL)
    add_text(s, Inches(1.15), Inches(10.7), Inches(9), Inches(0.4),
             "A TEST IS NOTHING SCARY", size=11, color=TEAL, bold=True, letter_spacing=3)
    add_text(s, Inches(1.15), Inches(11.1), Inches(9), Inches(1.4),
             "A test = asking the software 'does this work?' — and getting an honest answer.",
             size=18, color=INK, line_spacing=1.35)
    add_footer(s, "The feedback loop", "READ THE DIFF →")


def slide_09_review(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(s); add_header(s, 9)
    add_text(s, Inches(0.75), Inches(2.0), Inches(10), Inches(0.4),
             "STAGES 07 – 08 · REVIEW + LEARN", size=13, color=TEAL, bold=True)
    add_text(s, Inches(0.75), Inches(2.6), Inches(10), Inches(3),
             ["Never ship a change", "you didn't read."],
             size=44, bold=True, color=INK, line_spacing=1.0)

    y = Inches(7.0); cw = Inches(4.6); ch = Inches(4.6)
    # Review
    add_card(s, Inches(0.75), y, cw, ch, fill=CARD)
    add_text(s, Inches(0.95), y + Inches(0.3), cw - Inches(0.4), Inches(0.4),
             "REVIEW THE DIFF", size=12, color=TEAL, bold=True, letter_spacing=3)
    for i, q in enumerate(["What changed?", "Why?",
                            "Anything unrelated?", "Simpler than needed?",
                            "Unexpected files?", "Actually solves it?"]):
        add_text(s, Inches(0.95), y + Inches(0.95 + i * 0.55), cw - Inches(0.4), Inches(0.5),
                 f"·  {q}", size=15, color=INK)
    # Learn
    x2 = Inches(0.75 + 4.6 + 0.4)
    add_card(s, x2, y, cw, ch, fill=CARD, line=TEAL)
    add_text(s, x2 + Inches(0.2), y + Inches(0.3), cw - Inches(0.4), Inches(0.4),
             "TURN SURPRISE INTO RULE", size=12, color=TEAL, bold=True, letter_spacing=3)
    for i, q in enumerate(["Notice the mistake",
                            "Write the rule",
                            "Save it in project memory",
                            "Never happens again"]):
        add_text(s, x2 + Inches(0.2), y + Inches(0.95 + i * 0.8), cw - Inches(0.4), Inches(0.6),
                 f"→  {q}", size=16, color=INK)

    add_text(s, Inches(0.75), Inches(11.9), Inches(10), Inches(0.6),
             "Your project should get EASIER over time — not harder.",
             size=18, color=INK_SOFT)
    add_footer(s, "Own the change · learn from every one", "REAL EXAMPLE →")


def slide_10_walkthrough(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(s); add_header(s, 10)
    add_text(s, Inches(0.75), Inches(2.0), Inches(10), Inches(0.4),
             "ONE REAL TASK · JOB TRACKER APP", size=13, color=TEAL, bold=True)
    add_text(s, Inches(0.75), Inches(2.6), Inches(10), Inches(2),
             ["\"Add a status filter.\""],
             size=48, bold=True, color=INK, line_spacing=1.0)

    steps = [
        ("DEFINE",      "Objective, scope, done — in writing."),
        ("CONTEXT",     "Agent reads project memory."),
        ("INVESTIGATE", "\"Summarize how status works today.\""),
        ("BOUNDARIES",  "Only the list page. Nothing else."),
        ("EXECUTE",     "Step 1 buttons. Step 2 wire them up."),
        ("VERIFY",      "Click every filter. Try edge cases."),
        ("REVIEW",      "Two files. No stray edits. Approved."),
        ("LEARN",       "One new naming rule → project memory."),
    ]
    y = Inches(5.8); row_h = Inches(0.75); gap = Inches(0.12)
    for i, (name, desc) in enumerate(steps):
        yy = y + i * (row_h + gap)
        add_card(s, Inches(0.75), yy, Inches(9.75), row_h, fill=CARD)
        bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.75), yy, Inches(0.08), row_h)
        bar.fill.solid(); bar.fill.fore_color.rgb = TEAL; bar.line.fill.background()
        add_num_circle(s, Inches(1.10), yy + Inches(0.13), i + 1, size=Inches(0.48))
        add_text(s, Inches(1.90), yy + Inches(0.15), Inches(2.6), Inches(0.5),
                 name, size=15, bold=True, color=INK)
        add_text(s, Inches(4.4), yy + Inches(0.15), Inches(6), Inches(0.5),
                 desc, size=13, color=INK_MUTE)
    add_footer(s, "One feature · one afternoon · zero drama", "LAST SLIDE →")


def slide_11_cta(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(s); add_header(s, 11)
    add_text(s, Inches(0.75), Inches(2.4), Inches(10), Inches(0.4),
             "THE ONE LINE TO REMEMBER",
             size=13, color=TEAL, bold=True, align=PP_ALIGN.CENTER, letter_spacing=3)

    add_text(s, Inches(0.75), Inches(3.4), Inches(10), Inches(4),
             ["Don't aim for", "max autonomy.", "Aim for control."],
             size=64, bold=True, color=INK, align=PP_ALIGN.CENTER, line_spacing=1.05)
    # highlight last line
    add_text(s, Inches(0.75), Inches(5.7), Inches(10), Inches(1.4),
             "Aim for control.",
             size=64, bold=True, color=TEAL, align=PP_ALIGN.CENTER)

    add_text(s, Inches(1.75), Inches(7.9), Inches(8), Inches(2),
             ["A prompt is one instruction.",
              "A workflow is the system that surrounds it.",
              "Good results come from good systems — not clever sentences."],
             size=18, color=INK_SOFT, align=PP_ALIGN.CENTER, line_spacing=1.5)

    y = Inches(10.5); h = Inches(0.9); gap = Inches(0.18)
    ctas = [
        ("🔖", "SAVE",  "so you can find it again on your next AI coding session."),
        ("💬", "SHARE", "with a friend who's fighting their AI right now."),
        ("📘", "DM",    "\"PLAYBOOK\" to @data.science.beginners for the full 32-page ebook."),
    ]
    for i, (icon, verb, rest) in enumerate(ctas):
        yy = y + i * (h + gap)
        add_card(s, Inches(1.0), yy, Inches(9.25), h, fill=CARD)
        add_text(s, Inches(1.2), yy + Inches(0.20), Inches(0.8), Inches(0.5),
                 icon, size=24)
        tb = s.shapes.add_textbox(Inches(2.1), yy + Inches(0.22), Inches(8), Inches(0.6))
        tf = tb.text_frame; tf.margin_left = tf.margin_right = 0
        p = tf.paragraphs[0]
        r1 = p.add_run(); r1.text = verb
        r1.font.name = "Inter"; r1.font.size = Pt(15); r1.font.bold = True; r1.font.color.rgb = TEAL
        r2 = p.add_run(); r2.text = " " + rest
        r2.font.name = "Inter"; r2.font.size = Pt(14); r2.font.color.rgb = INK


BUILDERS = [
    slide_cover, slide_02_problem, slide_03_three, slide_04_prompt_workflow,
    slide_05_framework, slide_06_define, slide_07_boundaries, slide_08_loop,
    slide_09_review, slide_10_walkthrough, slide_11_cta,
]


def build_text_pptx() -> Path:
    prs = new_prs()
    for fn in BUILDERS:
        fn(prs)
    out = OUT_DIR / "AICodingAgentPlaybook_text.pptx"
    prs.save(str(out))
    print(f"✓ {out}  ({len(BUILDERS)} slides)")
    return out


if __name__ == "__main__":
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    build_image_pptx()
    build_text_pptx()
