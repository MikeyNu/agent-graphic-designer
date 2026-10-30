'use strict';
/* Run with Node. Executes the exact pure model embedded in index.html.
   It does NOT create a DOM, open a browser, or establish visual/motion QA. */
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');
const scripts = [...html.matchAll(/<script id="([^"]+)">([\s\S]*?)<\/script>/g)];
assert.equal(scripts.length, 2, 'Expected the state and interface scripts');
for (const [, id, source] of scripts) new vm.Script(source, {filename:id+'.js'});
const sandbox = {};
vm.createContext(sandbox);
vm.runInContext(scripts.find(([,id])=>id==='lantern-state')[2],sandbox);
const {createStore,visibleReservations} = sandbox.LanternState;

function fakeClock() {
  let time=0, next=0;
  const jobs=new Map(), history=[];
  return {
    history,
    schedule(callback, delay) { const id=++next; const job={id,at:time+delay,callback}; jobs.set(id,job);history.push(job);return id; },
    cancel(id) { jobs.delete(id); },
    advance(ms) {
      const end=time+ms;
      while(true) {
        const job=[...jobs.values()].filter(job=>job.at<=end).sort((a,b)=>a.at-b.at||a.id-b.id)[0];
        if(!job)break;
        time=job.at;jobs.delete(job.id);job.callback();
      }
      time=end;
    },
    pending:()=>jobs.size,
    now:()=>`fake-time-${time}`
  };
}
function setup() { const clock=fakeClock();return {clock,store:createStore(clock)}; }
const checks=[];
function check(name,fn) {fn();checks.push(name);console.log(`PASS  ${name}`);}
const ids = values => Array.from(values,record=>record.id).join(',');

check('Both embedded JavaScript programs parse without syntax errors',()=>{});
check('Eight unique, complete fictional reservations; six ready and two collected',()=>{
  const {store}=setup(),records=store.snapshot();
  assert.equal(records.length,8);assert.equal(new Set(records.map(r=>r.id)).size,8);
  assert.equal(records.filter(r=>r.status==='ready').length,6);assert.equal(records.filter(r=>r.status==='collected').length,2);
  assert.ok(records.every(r=>r.borrower&&r.member&&r.items.length&&r.items.every(item=>item.name&&item.tag)));
});
check('Snapshots and record reads cannot mutate the internal data',()=>{
  const {store}=setup();const list=store.snapshot();list[0].status='collected';list[0].items[0].name='changed';
  const copy=store.record('LN-1042');copy.borrower='changed';
  assert.equal(store.record('LN-1042').status,'ready');assert.equal(store.record('LN-1042').borrower,'Mira Ellis');
  assert.equal(store.record('LN-1042').items[0].name,'Canon EOS R50 + 18–45mm lens');
});
check('Search handles case, accents, member ID, reservation ID, asset tags, and multiple terms',()=>{
  const {store}=setup(),records=store.snapshot();
  for(const query of ['sofia','SOFÍA','LN-1046','m-2116','mic-011','chen wireless']) assert.equal(ids(visibleReservations(records,query)),'LN-1046',query);
  assert.equal(visibleReservations(records,'    ').length,8);
  assert.equal(visibleReservations(records,'not-a-sample-person').length,0);
});
check('Status filters intersect with search and stable sorting',()=>{
  const {store}=setup(),records=store.snapshot();
  assert.equal(visibleReservations(records,'','ready').length,6);
  assert.equal(ids(visibleReservations(records,'','collected')),'LN-1044,LN-1047');
  assert.equal(visibleReservations(records,'mira','collected').length,0);
  assert.equal(ids(visibleReservations(records,'','all','name')),'LN-1044,LN-1049,LN-1048,LN-1045,LN-1042,LN-1047,LN-1046,LN-1043');
});
check('Normal collection stays pending through 449 ms and commits once at 450 ms',()=>{
  const {store,clock}=setup(),events=[];store.subscribe(event=>events.push(event.type));
  assert.equal(store.collect('LN-1042','success').accepted,true);
  assert.equal(store.record('LN-1042').operation.phase,'pending');
  clock.advance(449);assert.equal(store.record('LN-1042').status,'ready');
  clock.advance(1);assert.equal(store.record('LN-1042').status,'collected');assert.equal(store.record('LN-1042').changedAt,'fake-time-450');
  assert.equal(events.join(','),'pending,success');
});
check('Rapid duplicate submissions and recollection are rejected without another timer',()=>{
  const {store,clock}=setup();store.collect('LN-1042','delay');
  assert.equal(store.collect('LN-1042','success').reason,'pending');assert.equal(clock.pending(),1);
  clock.advance(3000);assert.equal(store.collect('LN-1042','failure').reason,'already-collected');assert.equal(clock.pending(),0);
});
check('Delayed success remains Ready until exactly the simulated 3-second outcome',()=>{
  const {store,clock}=setup();assert.equal(store.collect('LN-1043','delay').delay,3000);
  clock.advance(2999);assert.equal(store.record('LN-1043').status,'ready');assert.equal(store.record('LN-1043').operation.phase,'pending');
  clock.advance(1);assert.equal(store.record('LN-1043').status,'collected');
});
check('Failed update preserves Ready and equipment, then retry succeeds after 450 ms',()=>{
  const {store,clock}=setup();const before=JSON.stringify(store.record('LN-1045').items);
  store.collect('LN-1045','failure');clock.advance(899);assert.equal(store.record('LN-1045').operation.phase,'pending');
  clock.advance(1);assert.equal(store.record('LN-1045').operation.phase,'error');assert.equal(store.record('LN-1045').status,'ready');
  assert.equal(store.record('LN-1045').changedAt,undefined);assert.equal(JSON.stringify(store.record('LN-1045').items),before);
  assert.equal(store.retry('LN-1045').accepted,true);assert.equal(store.retry('LN-1045').reason,'pending');
  clock.advance(449);assert.equal(store.record('LN-1045').status,'ready');
  clock.advance(1);assert.equal(store.record('LN-1045').status,'collected');assert.equal(store.record('LN-1045').operation.attempt,2);
});
check('Overlapping record updates remain independent when outcomes arrive out of order',()=>{
  const {store,clock}=setup();store.collect('LN-1042','delay');store.collect('LN-1043','failure');
  clock.advance(900);assert.equal(store.record('LN-1042').operation.phase,'pending');assert.equal(store.record('LN-1043').operation.phase,'error');
  store.retry('LN-1043');clock.advance(450);assert.equal(store.record('LN-1043').status,'collected');assert.equal(store.record('LN-1042').status,'ready');
  clock.advance(1650);assert.equal(store.record('LN-1042').status,'collected');assert.equal(store.record('LN-1043').operation.attempt,2);
});
check('A successful change reconciles Ready, Collected, and All result counts',()=>{
  const {store,clock}=setup();store.collect('LN-1042','success');clock.advance(450);
  assert.equal(visibleReservations(store.snapshot(),'','ready').length,5);
  assert.equal(visibleReservations(store.snapshot(),'','collected').length,3);
  assert.equal(visibleReservations(store.snapshot(),'','all').length,8);
});
check('Reset cancels pending work and ignores an explicitly replayed obsolete callback',()=>{
  const {store,clock}=setup();store.collect('LN-1042','delay');const old=clock.history[0].callback;
  store.reset();assert.equal(clock.pending(),0);assert.equal(store.record('LN-1042').status,'ready');
  old();assert.equal(store.record('LN-1042').status,'ready');assert.equal(store.record('LN-1042').operation,undefined);
  store.collect('LN-1042','success');old();assert.equal(store.record('LN-1042').operation.phase,'pending');
  clock.advance(450);assert.equal(store.record('LN-1042').status,'collected');
});
check('Unknown records and invalid retries are safe no-ops',()=>{
  const {store,clock}=setup();assert.equal(store.collect('missing').reason,'missing');assert.equal(store.retry('LN-1042').reason,'nothing-to-retry');assert.equal(clock.pending(),0);
});
check('Unsubscription and disposal remove listeners and scheduled callbacks',()=>{
  const {store,clock}=setup();let count=0;const unsubscribe=store.subscribe(()=>count++);
  store.collect('LN-1042','delay');assert.equal(count,1);unsubscribe();clock.advance(3000);assert.equal(count,1);
  store.collect('LN-1043','delay');const old=clock.history[1].callback;store.dispose();assert.equal(clock.pending(),0);old();assert.equal(store.record('LN-1043'),null);
});

console.log(`\n${checks.length} checks passed. Pure-state execution and syntax checks only; browser/layout/motion NOT RUN.`);
console.log(`Artifact SHA-256: ${crypto.createHash('sha256').update(html).digest('hex')}`);
