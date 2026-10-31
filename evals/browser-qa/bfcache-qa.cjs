// Actual standalone Edge history restoration. No Playwright or CDP connection.
const fs=require('node:fs'),path=require('node:path'),http=require('node:http'),cp=require('node:child_process');
const root=__dirname,events=[];let child,profile,done=false;
const script=`<script>
function log(stage,extra={}){navigator.sendBeacon('/log',JSON.stringify({stage,persisted:false,dialog:document.querySelector('dialog')?.open,overflow:document.body.style.overflow,focus:document.activeElement?.dataset.open||document.activeElement?.id,...extra}));}
addEventListener('pagehide',e=>log('pagehide',{persisted:e.persisted}));
addEventListener('pageshow',e=>{
 log('pageshow',{persisted:e.persisted,reason:performance.getEntriesByType('navigation')[0]?.notRestoredReasons?.toJSON?.()});
 if(e.persisted){setTimeout(()=>{document.querySelector('[data-open="LN-1043"]').click();setTimeout(()=>{log('reopen');document.querySelector('#back-button').click();setTimeout(()=>log('finished'),300)},300)},100);return;}
 if(sessionStorage.getItem('ran')){log('failed-reload');return;}
 sessionStorage.setItem('ran','1');setTimeout(()=>{document.querySelector('[data-open="LN-1043"]').click();setTimeout(()=>{document.querySelector('#back-button').click();setTimeout(()=>{log('leaving-during-close');location.href='/away'},35)},350)},500);
});</script>`;
const server=http.createServer((req,res)=>{
 if(req.url==='/log'){let body='';req.on('data',x=>body+=x);req.on('end',()=>{const e=JSON.parse(body);events.push(e);console.log(JSON.stringify(e));res.end('ok');if(['finished','failed-reload'].includes(e.stage))setTimeout(finish,300);});return;}
 res.setHeader('Content-Type','text/html');
 if(req.url==='/bfcache'){return res.end(fs.readFileSync(path.join(root,'graphic/evals/examples/qa-2026-10-31/queue/index.html'),'utf8').replace('</body>',script+'</body>'));}
 if(req.url==='/away')return res.end('<title>QA history return</title><p>Returning to the queue.</p><script>setTimeout(()=>history.back(),300)</script>');
 res.end('');
});
function finish() {
  if (done) return;
  done = true;
  const leaving = events.find(e => e.stage === 'leaving-during-close');
  const cached = events.find(e => e.stage === 'pagehide' && e.persisted);
  const restored = events.find(e => e.stage === 'pageshow' && e.persisted);
  const reopened = events.find(e => e.stage === 'reopen');
  const end = events.find(e => e.stage === 'finished');
  const settled = e => e && !e.dialog && e.overflow !== 'hidden' && e.focus === 'LN-1043';
  const behaviorPassed = Boolean(leaving?.dialog && leaving.overflow === 'hidden' &&
    cached && settled(restored) && reopened?.dialog && reopened.overflow === 'hidden' && settled(end));

  // Edge may hand off to a new process before its launcher exits. Scope fallback
  // cleanup to this unique profile, never to every Edge process on the device.
  if (child) cp.spawnSync('taskkill', ['/PID', String(child.pid), '/T', '/F'], {stdio: 'ignore'});
  const cleanupScript = `
    $ErrorActionPreference = 'Stop'
    $qaProfile = $env:SKILL_QA_EDGE_PROFILE
    if ([string]::IsNullOrWhiteSpace($qaProfile)) { exit 2 }
    function Get-OwnedEdge {
      Get-CimInstance Win32_Process -Filter "Name='msedge.exe'" |
        Where-Object { $_.CommandLine -and $_.CommandLine.Contains($qaProfile) }
    }
    Get-OwnedEdge | ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
    for ($attempt = 0; $attempt -lt 20; $attempt++) {
      if (-not (Get-OwnedEdge)) { exit 0 }
      Start-Sleep -Milliseconds 100
    }
    exit 1
  `;
  const cleanup = cp.spawnSync('powershell.exe', ['-NoProfile', '-NonInteractive', '-Command', cleanupScript], {
    env: {...process.env, SKILL_QA_EDGE_PROFILE: profile}, encoding: 'utf8', timeout: 15000
  });
  const cleanupPassed = cleanup.status === 0;
  const success = behaviorPassed && cleanupPassed;
  const report = {
    method: 'Standalone headed Edge without an automation protocol connection; native history.back from an away document; instrumented fixture copy.',
    status: success ? 'PASS' : 'FAIL',
    behavior: behaviorPassed ? 'PASS' : 'FAIL',
    cleanup: cleanupPassed ? 'PASS' : 'FAIL',
    events
  };
  if (!cleanupPassed) report.cleanupError = String(cleanup.error || cleanup.stderr || 'Owned Edge process remained.');
  fs.writeFileSync(path.join(root, 'bfcache-report.json'), JSON.stringify(report, null, 2));
  console.log('RESULT ' + JSON.stringify({status: report.status, behavior: report.behavior, cleanup: report.cleanup}));
  server.close();
  process.exit(success ? 0 : 1);
}
server.listen(0,'127.0.0.1',()=>{const url='http://127.0.0.1:'+server.address().port+'/bfcache';profile=path.join(root,'bfcache-profile-'+Date.now());child=cp.spawn('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',['--user-data-dir='+profile,'--no-first-run','--no-default-browser-check','--disable-extensions','--new-window',url],{stdio:'ignore'});child.on('error',e=>{events.push({stage:'launch-error',error:String(e)});finish();});setTimeout(finish,25000);});
