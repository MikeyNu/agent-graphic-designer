'use strict';
/* Isolated logic evidence only. This extracts the actual lifecycle helpers from
   index.html and executes them against explicit browser API stubs. It does not
   establish native dialog, focus, history, BFCache, or motion behavior in a browser. */
const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const assert=require('node:assert/strict');
const html=fs.readFileSync(path.join(__dirname,'index.html'),'utf8');
const helpers=html.split('/* LIFECYCLE_CHECK_START: these actual helpers are executed by check-lifecycle.cjs. */')[1].split('/* LIFECYCLE_CHECK_END */')[0];
const returnHandler=html.match(/    function returnToQueue\(\) \{[\s\S]*?\n    \}/)[0];
const prefix=`
  const log={closed:0,disposed:0,canceled:0,restored:[],cleared:[],back:0};
  const context={query:'audio',filter:'ready',sort:'time',scrollY:683,ids:['LN-1043','LN-1048']};
  const ui={selected:null};
  const dialog={open:true,close(){this.open=false;log.closed++;}};
  const store={dispose(){log.disposed++;}};
  const history={state:{lantern:'detail',fromQueue:true},back(){log.back++;}};
  let pendingClose={originId:'LN-1043',context},deferredReturn=null,routeClosing=true,returnRequested=false;
  let bodyLocked=true,sheetAnimation={cancel(){log.canceled++;}},announcementTimer=1,sheetFinishTimer=2,animationVersion=0;
  function unlockBody(){bodyLocked=false;}
  function lockBody(){bodyLocked=true;}
  function restoreQueueFocus(context,id){log.restored.push({context,id});}
  function clearTimeout(handle){log.cleared.push(handle);}
`;
function harness(){
  const sandbox={};vm.createContext(sandbox);
  vm.runInContext(prefix+helpers+returnHandler+`
    globalThis.api={
      hide:onPageHide,show:onPageShow,finish:finishPanelClose,back:returnToQueue,
      state:()=>({dialogOpen:dialog.open,routeClosing,returnRequested,pendingClose,deferredReturn,bodyLocked,animationVersion,log}),
      opened(){ui.selected='LN-1048';dialog.open=true;routeClosing=false;pendingClose=null;deferredReturn=null;},
      selectedDuringClose(){ui.selected='LN-1048';}
    };
  `,sandbox);
  return sandbox.api;
}
const checks=[];
function check(name,fn){fn();checks.push(name);console.log('PASS  '+name);}
check('Persisted pagehide settles an interrupted close and defers return restoration',()=>{
  const api=harness();api.hide({persisted:true});const state=api.state();
  assert.equal(state.dialogOpen,false);assert.equal(state.routeClosing,false);assert.equal(state.returnRequested,false);
  assert.equal(state.pendingClose,null);assert.equal(state.deferredReturn.originId,'LN-1043');assert.equal(state.bodyLocked,false);
  assert.equal(state.log.closed,1);assert.equal(state.log.disposed,0);assert.equal(state.log.canceled,1);assert.equal(state.log.restored.length,0);
});
check('Persisted pageshow restores the original queue query, position, and row exactly once',()=>{
  const api=harness();api.hide({persisted:true});api.show({persisted:true});api.show({persisted:true});
  const state=api.state();assert.equal(state.log.restored.length,1);assert.equal(state.log.restored[0].id,'LN-1043');
  assert.equal(state.log.restored[0].context.query,'audio');assert.equal(state.log.restored[0].context.scrollY,683);
  assert.equal(state.deferredReturn,null);assert.equal(state.bodyLocked,false);
});
check('Return handler is usable after resumed close and still guards rapid repeat Back',()=>{
  const api=harness();api.hide({persisted:true});api.show({persisted:true});api.opened();api.back();api.back();
  assert.equal(api.state().log.back,1);assert.equal(api.state().returnRequested,true);
});
check('An open, non-closing detail survives persisted pagehide and reacquires body lock',()=>{
  const api=harness();api.opened();api.hide({persisted:true});assert.equal(api.state().dialogOpen,true);assert.equal(api.state().bodyLocked,false);
  api.show({persisted:true});assert.equal(api.state().dialogOpen,true);assert.equal(api.state().bodyLocked,true);assert.equal(api.state().log.restored.length,0);
});
check('Non-persisted pagehide disposes pending operations',()=>{
  const api=harness();api.hide({persisted:false});assert.equal(api.state().log.disposed,1);
});
check('Obsolete close completion cannot close a newer selection',()=>{
  const api=harness();api.selectedDuringClose();api.finish();assert.equal(api.state().dialogOpen,true);assert.equal(api.state().log.closed,0);
});
check('Ordinary close completion restores context and unlocks the body',()=>{
  const api=harness();api.finish();const state=api.state();assert.equal(state.dialogOpen,false);assert.equal(state.routeClosing,false);assert.equal(state.bodyLocked,false);assert.equal(state.log.restored[0].id,'LN-1043');
});
console.log(`\n${checks.length} isolated lifecycle checks passed. Browser interaction, BFCache, layout, and temporal verification NOT RUN.`);
