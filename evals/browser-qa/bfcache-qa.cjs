// Actual standalone Edge history restoration. No Playwright or CDP connection.
const fs=require('node:fs'),path=require('node:path'),http=require('node:http'),cp=require('node:child_process');
const root=__dirname,events=[];let child,done=false;
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
function finish(){if(done)return;done=true;const restored=events.some(e=>e.stage==='pageshow'&&e.persisted);const end=events.find(e=>e.stage==='finished');const success=restored&&end&&!end.dialog&&end.overflow!=='hidden'&&events.some(e=>e.stage==='reopen'&&e.dialog);fs.writeFileSync(path.join(root,'bfcache-report.json'),JSON.stringify({method:'Standalone headed Edge without an automation protocol connection; native history.back from an away document; instrumented fixture copy.',status:success?'PASS':'FAIL',events},null,2));console.log('RESULT '+(success?'PASS':'FAIL'));if(child)cp.spawnSync('taskkill',['/PID',String(child.pid),'/T','/F'],{stdio:'ignore'});server.close();process.exit(success?0:1);}
server.listen(0,'127.0.0.1',()=>{const url='http://127.0.0.1:'+server.address().port+'/bfcache';child=cp.spawn('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',['--user-data-dir='+path.join(root,'bfcache-profile-'+Date.now()),'--no-first-run','--no-default-browser-check','--disable-extensions','--new-window',url],{stdio:'ignore'});child.on('error',e=>{events.push({stage:'launch-error',error:String(e)});finish();});setTimeout(finish,25000);});
