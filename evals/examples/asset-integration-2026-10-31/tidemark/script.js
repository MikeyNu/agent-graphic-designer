// Native anchor navigation remains functional without JavaScript.
// Focus follows the chapter change without interrupting native smooth scrolling.
function focusChapter() {
  if (location.hash === '#journal') {
    document.getElementById('journal').focus({ preventScroll: true });
  } else if (location.hash === '#cover') {
    document.getElementById('open-journal').focus({ preventScroll: true });
  }
}
window.addEventListener('hashchange', focusChapter);
if (location.hash) requestAnimationFrame(focusChapter);
