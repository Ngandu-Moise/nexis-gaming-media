// Capture image par image de page.html (même principe que Remotion) -> ffmpeg
// node frames.js timeline.json out.mp4 [stillFrames...]
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs'), path = require('path');
(async () => {
  const [tl, out, ...stills] = process.argv.slice(2);
  const T = JSON.parse(fs.readFileSync(tl));
  const total = T[T.length - 1].start + T[T.length - 1].dur;
  const N = Math.round(total * 30);
  const b = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.join(__dirname, 'page.html'));
  await p.evaluate(t => { window.setTimeline(t); return document.fonts.ready; }, T);
  if (stills.length) {
    for (const f of stills) { await p.evaluate(f => window.setFrame(f), +f);
      await p.screenshot({ path: `${out}-${f}.png` }); }
    await b.close(); return;
  }
  const ff = spawn('ffmpeg', ['-y', '-f', 'image2pipe', '-framerate', '30', '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p', out], { stdio: ['pipe', 'ignore', 'inherit'] });
  for (let f = 0; f < N; f++) {
    await p.evaluate(f => window.setFrame(f), f);
    const buf = await p.screenshot({ type: 'jpeg', quality: 92 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (f % 150 === 0) process.stderr.write(`frame ${f}/${N}\n`);
  }
  ff.stdin.end(); await new Promise(r => ff.on('close', r)); await b.close();
})();
