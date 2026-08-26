// Headless-Chrome print → PDF for the ebook.
// Requires playwright (or use puppeteer). Falls back to a helpful message if
// neither is installed.
//
//   npm run build:pdf
//
// Output: build/output/DataScienceInterviewPrep.pdf

import { mkdir } from 'node:fs/promises';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { dirname, resolve } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(__dirname, '..');
const OUT_DIR = resolve(ROOT, 'build', 'output');
const OUT_FILE = resolve(OUT_DIR, 'DataScienceInterviewPrep.pdf');
const INDEX = pathToFileURL(resolve(ROOT, 'index.html')).href;

await mkdir(OUT_DIR, { recursive: true });

let playwright;
try {
  playwright = await import('playwright');
} catch {
  console.error(
    '\nplaywright is not installed. Install it once with:\n' +
    '  npm i -D playwright && npx playwright install chromium\n' +
    'or export a PDF manually from the browser (File → Print → Save as PDF, A5).\n'
  );
  process.exit(1);
}

const browser = await playwright.chromium.launch();
const page = await browser.newPage();
await page.goto(INDEX, { waitUntil: 'networkidle' });
await page.emulateMedia({ media: 'print' });
await page.pdf({
  path: OUT_FILE,
  format: 'A5',
  printBackground: true,
  preferCSSPageSize: true,
  margin: { top: '0', bottom: '0', left: '0', right: '0' },
});
await browser.close();

console.log(`✓ PDF written to ${OUT_FILE}`);
