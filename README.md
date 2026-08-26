# Data Science Interview Prep — Ebook 02 (revised)

A focused, print-ready revision guide for data science interviews.
Static HTML/CSS/JS site that also renders to a polished A5 PDF via headless Chrome.

**Publisher:** @data.science.beginners
**Format:** A5 (148 × 210 mm) · dark theme · print-ready
**Sections:** Statistics & Probability · Python · SQL · Cleaning & Preprocessing · ML Fundamentals

---

## Preview locally

```bash
npm start
# then open http://localhost:3000
```

## Generate the PDF

```bash
npm run build:pdf
# outputs → build/output/DataScienceInterviewPrep.pdf
```

The build script uses Playwright/Chromium (already installed in dev containers)
and prints `index.html` with `--print-background` at A5 size.

## Project layout

```
index.html               Main ebook — every page is a <section class="page">
assets/css/main.css      Design system + screen styles
assets/css/print.css     @page rules, page breaks, print-only tweaks
assets/js/main.js        Optional screen nav (TOC scroll, keyboard shortcuts)
assets/img/              Cover, logo, any raster assets
build/build-pdf.mjs      Headless-Chrome print → PDF
```

## What changed from Ebook 02 (original)

- Fixed missing spaces around bolded phrases in every interview-question page
- Fixed wrapped/broken question layout on A/B-testing and scaling questions
- Priority % now sits below the progress bar consistently
- Added missing formulas (Poisson, Normal, Exponential)
- Added Python code snippets inline for each concept
- Added SVG diagrams (confusion matrix, bias-variance, ROC curve, sigmoid)
- Added SQL worked-example schemas + anti-join / gaps-and-islands patterns
- Added sklearn Pipeline snippet
- Added one-line model answers to every rapid-fire question
- Per-section accent colors + section-aware footer
- PDF bookmarks + hyperlinked contents

## License

All rights reserved. © @data.science.beginners.
