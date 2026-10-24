// Render the hero as a seamless 12s loop and encode site/og.mp4 + site/og.png.
//
//   cd tools && npm i && npm run og
//
// Frames are stepped deterministically through window.__heroFrame(t) (index.html?capture),
// so the output is identical on every run and loops without a visible seam.
import { chromium } from "playwright";
import { execFileSync } from "node:child_process";
import { mkdtempSync, rmSync, statSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { pathToFileURL } from "node:url";

const SITE = resolve(import.meta.dirname, "../site");
const FPS = 30, LOOP = 12, W = 1200, H = 630;
const frames = mkdtempSync(join(tmpdir(), "og-frames-"));

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
await page.goto(pathToFileURL(join(SITE, "index.html")).href + "?capture");
await page.waitForFunction(() => typeof window.__heroFrame === "function");
await page.evaluate(() => document.fonts.ready);

const total = FPS * LOOP;
for (let i = 0; i < total; i++) {
  await page.evaluate((t) => window.__heroFrame(t), i / FPS);
  await page.screenshot({ path: join(frames, `f${String(i).padStart(4, "0")}.png`) });
  if (i % 60 === 0) process.stdout.write(`frame ${i}/${total}\n`);
}
await page.evaluate((t) => window.__heroFrame(t), 2.2);
await page.screenshot({ path: join(SITE, "og.png") });
await browser.close();

execFileSync("ffmpeg", [
  "-y", "-loglevel", "error", "-framerate", String(FPS), "-i", join(frames, "f%04d.png"),
  "-c:v", "libx264", "-preset", "slow", "-crf", "24", "-tune", "animation",
  "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an", join(SITE, "og.mp4"),
], { stdio: "inherit" });
rmSync(frames, { recursive: true, force: true });

const mb = (f) => (statSync(join(SITE, f)).size / 1e6).toFixed(2) + " MB";
console.log(`site/og.mp4 ${mb("og.mp4")} · site/og.png ${mb("og.png")}`);
