// Screenshot each carousel slide as a 1080x1350 PNG for Instagram.
//
//   npm run build:carousel
//
// Output: build/output/carousel/slide-01.png … slide-11.png

import { mkdir } from 'node:fs/promises';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { dirname, resolve } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(__dirname, '..');
const OUT_DIR = resolve(ROOT, 'build', 'output', 'carousel');
const HTML = pathToFileURL(resolve(ROOT, 'book', 'carousel', 'carousel.html')).href;

await mkdir(OUT_DIR, { recursive: true });

let playwright;
try {
  playwright = await import('playwright');
} catch {
  console.error('playwright not installed.  npm i -D playwright');
  process.exit(1);
}

const executablePath = process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH;
const launchOpts = executablePath ? { executablePath } : {};

const browser = await playwright.chromium.launch(launchOpts);
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
await page.goto(HTML, { waitUntil: 'networkidle' });

// Ensure fonts have painted
await page.evaluate(() => document.fonts && document.fonts.ready);

const slides = await page.$$('.slide');
console.log(`Found ${slides.length} slides.`);

for (let i = 0; i < slides.length; i++) {
  const el = slides[i];
  const n = String(i + 1).padStart(2, '0');
  const outPath = resolve(OUT_DIR, `slide-${n}.png`);
  // element.screenshot() auto-scrolls and clips to just this element.
  await el.screenshot({ path: outPath, omitBackground: false });
  console.log(`✓ ${outPath}`);
}

await browser.close();
console.log('\nAll slides written to', OUT_DIR);
