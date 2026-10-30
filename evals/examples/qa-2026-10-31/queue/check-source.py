"""Source checks only; no DOM, browser, layout, screen reader, or animation is executed."""
from html.parser import HTMLParser
from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parent
source = (ROOT / 'index.html').read_text()

class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.references = []
        self.external = []
        self.inline_events = []
        self.labels = []
        self.controls = []
        self.stack = []
        self.errors = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs: self.ids.append(attrs['id'])
        for name in ('aria-labelledby','aria-describedby','aria-controls'):
            for target in attrs.get(name,'').split(): self.references.append((name,target))
        if tag == 'label': self.labels.append(attrs.get('for'))
        if tag in ('input','select'): self.controls.append(attrs.get('id'))
        for name,value in attrs.items():
            if name.startswith('on'): self.inline_events.append(name)
            if name in ('src','href','action') and value and not value.startswith('#'):
                self.external.append((tag,name,value))
        if tag not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}:
            self.stack.append(tag)
    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1] != tag: self.errors.append((tag,list(self.stack[-4:])))
        else: self.stack.pop()
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag,attrs)
        if self.stack and self.stack[-1] == tag: self.stack.pop()

doc=Document();doc.feed(source)
checks=[]
def check(name,condition):
    assert condition,name
    checks.append(name)
    print('PASS ',name)

check('HTML nesting is balanced under the standard-library parser',not doc.errors and not doc.stack)
check('All static IDs are unique',len(doc.ids)==len(set(doc.ids)))
check('Static ARIA references point to existing IDs',all(target in doc.ids for _,target in doc.references))
check('Every input and select has an explicit label',all(control in doc.labels for control in doc.controls))
check('No external src/href/action resources',not doc.external)
check('No CSS imports, remote URLs, or network API calls in source',not re.search(r'@import|https?://|\bfetch\s*\(|\bXMLHttpRequest\b|\bWebSocket\b|\bEventSource\b|sendBeacon\s*\(',source))
check('No inline event attributes',not doc.inline_events)
check('Native dialog, modal lifecycle, cancel handling, and return-focus hooks exist',all(token in source for token in ['<dialog','dialog.showModal()','dialog.close()','dialog.addEventListener(\'cancel\'','restoreQueueFocus']))
check('320px-oriented reflow and independent reduced-motion paths are specified',all(token in source for token in ['@media (max-width: 620px)','prefers-reduced-motion: reduce',"spatial=!reducedMotion.matches",'.spinner { animation: none']))
check('Prototype, sample data, local-only updates, and reload reset are disclosed',all(token in source for token in ['Sample data','Local simulation','fictional sample data','reloading resets them','No connection or messages are sent']))

def rgb(value):
    return [int(value[i:i+2],16)/255 for i in (1,3,5)]
def luminance(value):
    linear=[c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4 for c in rgb(value)]
    return sum(c*w for c,w in zip(linear,[.2126,.7152,.0722]))
def contrast(a,b):
    light,dark=sorted([luminance(a),luminance(b)],reverse=True)
    return (light+.05)/(dark+.05)

pairs=[
 ('Ink / paper','#29332e','#faf7f0',4.5),
 ('Muted / canvas','#65645c','#ebe5db',4.5),
 ('Muted / paper','#65645c','#faf7f0',4.5),
 ('Muted / selected row','#65645c','#f4e2d9',4.5),
 ('Coral / paper','#b44735','#faf7f0',4.5),
 ('Success / green surface','#315c43','#e9eee4',4.5),
 ('Error / error surface','#9c3529','#fae9e1',4.5),
 ('Button text / ink','#fffdf8','#29332e',4.5),
 ('Pending button text / background','#fffdf8','#4e584f',4.5),
 ('Focus / paper','#8e3528','#faf7f0',3),
 ('Control boundary / light paper','#948c7e','#fffdf8',3),
]
for name,foreground,background,minimum in pairs:
    ratio=contrast(foreground,background)
    check(f'Configured color pair {name}: {ratio:.2f}:1 (required {minimum}:1)',ratio>=minimum)

print(f'\n{len(checks)} source/color checks passed. This is not a rendered contrast or accessibility audit.')
print('Artifact SHA-256:',hashlib.sha256(source.encode()).hexdigest())
