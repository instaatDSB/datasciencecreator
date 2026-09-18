// Headless-Chrome print → PDF for the AI Coding Agent Playbook.
//
//   npm run build:playbook-pdf
//
// Output: build/output/AICodingAgentPlaybook.pdf

import { mkdir } from 'node:fs/promises';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { dirname, resolve } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(__dirname, '..');
const OUT_DIR = resolve(ROOT, 'build', 'output');
const OUT_FILE = resolve(OUT_DIR, 'AICodingAgentPlaybook.pdf');
const INDEX = pathToFileURL(resolve(ROOT, 'book', 'playbook', 'index.html')).href;

await mkdir(OUT_DIR, { recursive: true });

let playwright;
try {
  playwright = await import('playwright');
} catch {
  console.error(
    '\nplaywright is not installed. Install it once with:\n' +
    '  npm i -D playwright\n' +
    '(chromium is already available at /opt/pw-browsers in this environment.)\n'
  );
  process.exit(1);
}

const executablePath = process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH;
const launchOpts = executablePath ? { executablePath } : {};

const browser = await playwright.chromium.launch(launchOpts);
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
