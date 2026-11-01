// Capture image par image de page.html (même principe que Remotion), fond transparent,
// superposée à la piste de fond (clips IA ou noir) par ffmpeg.
// node frames.js <spec.json> <timeline.json> <base.mp4> <sortie.mp4>
// node frames.js <spec.json> <timeline.json> --stills <prefixe> <frame> [frame...]   (PNG de contrôle)
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs'), path = require('path');
(async () => {
  const [specPath, tlPath, a3, a4, ...rest] = process.argv.slice(2);
  const spec = JSON.parse(fs.readFileSync(specPath)), T = JSON.parse(fs.readFileSync(tlPath));
  const N = Math.round((T.at(-1).start + T.at(-1).dur) * 30);
  const b = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.join(__dirname, 'page.html'));
  await p.evaluate(() => document.fonts.ready);
  await p.evaluate(([s, t]) => window.setup(s, t), [spec, T]);
  await p.evaluate(() => document.fonts.ready);
  if (a3 === '--stills') {
    for (const f of rest) { await p.evaluate(f => window.setFrame(f), +f);
      await p.screenshot({ path: `${a4}-${f}.png` }); }
    await b.close(); return;
  }
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-i', a3, '-f', 'image2pipe', '-framerate', '30', '-c:v', 'png', '-i', '-',
    '-filter_complex', '[0:v][1:v]overlay=format=auto:shortest=1,format=yuv420p[v]', '-map', '[v]',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-r', '30', a4], { stdio: ['pipe', 'inherit', 'inherit'] });
  for (let f = 0; f < N; f++) {
    await p.evaluate(f => window.setFrame(f), f);
    const buf = await p.screenshot({ type: 'png', omitBackground: true });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (f % 150 === 0) process.stderr.write(`image ${f}/${N}\n`);
  }
  ff.stdin.end();
  const code = await new Promise(r => ff.on('close', r)); await b.close();
  process.exit(code);
})();
