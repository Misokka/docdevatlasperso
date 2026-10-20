#!/usr/bin/env python3
"""Compile local Markdown documentation to deploy-ready static JS. Requires mistune and pygments."""
from pathlib import Path
import json, re, html
import mistune
from mistune import HTMLRenderer
from pygments import highlight
from pygments.lexers import get_lexer_by_name, TextLexer
from pygments.formatters import HtmlFormatter
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
GROUPS = ['Commencer','PHP','Laravel','SQL & BDD','Vue.js','JavaScript & TypeScript','Next.js','Java & Symfony','Outils & Web','Méthodes']

def slugify(s):
    import unicodedata
    s=''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c)!='Mn')
    return re.sub(r'(^-|-$)', '', re.sub(r'[^a-z0-9]+','-',s))

class Renderer(HTMLRenderer):
    def __init__(self):
        super().__init__(escape=True)
        self.headings=[]
        self.seen={}
    def heading(self, text, level, **attrs):
        t=BeautifulSoup(text,'html.parser').get_text(' ',strip=True)
        base=slugify(t)
        n=self.seen.get(base,0); self.seen[base]=n+1
        ident=base+(('-'+str(n+1)) if n else '')
        if level in (2,3): self.headings.append({'id':ident,'title':t,'level':level})
        return f'<h{level} id="{ident}">{text}<a class="heading-anchor" href="#{ident}" aria-label="Lien vers cette section">#</a></h{level}>\n'
    def block_code(self, code, info=None):
        lang=((info or '').strip().split(' ')[0] or 'text').lower()
        aliases={'blade':'html+php','vue':'html','bash':'bash','shell':'bash','text':'text','ts':'typescript','tsx':'tsx','js':'javascript','json':'json','yaml':'yaml','sql':'sql','php':'php','java':'java','html':'html','css':'css','typescript':'typescript'}
        try: lexer=get_lexer_by_name(aliases.get(lang,lang))
        except Exception: lexer=TextLexer()
        rendered=highlight(code.rstrip('\n'),lexer,HtmlFormatter(nowrap=True))
        return '<div class="code-block"><div class="code-toolbar"><span class="code-lang">'+html.escape(lang.upper())+'</span><button class="copy-code" type="button" aria-label="Copier le code"><span class="copy-icon">⧉</span> Copier</button></div><pre><code class="highlight">'+rendered+'</code></pre></div>\n'

records=[]
for mdpath in sorted((ROOT/'docs').glob('*.md')):
    content=mdpath.read_text(encoding='utf-8')
    if not content.startswith('---\n'): raise ValueError(f'Missing frontmatter: {mdpath}')
    _,meta,body=content.split('---\n',2)
    properties={}
    for line in meta.strip().splitlines():
        if ':' in line:
            k,v=line.split(':',1);properties[k.strip()]=v.strip()
    for prop in ('title','group','summary','order'):
        if prop not in properties:raise ValueError(f'Missing {prop}: {mdpath}')
    renderer=Renderer()
    md=mistune.create_markdown(renderer=renderer,plugins=['table','strikethrough','task_lists','url'])
    content_html=md(body)
    soup=BeautifulSoup(content_html,'html.parser')
    plain=soup.get_text(' ',strip=True)
    sections=[]
    for heading in renderer.headings:
        elt=soup.find(id=heading['id'])
        sectionbits=[]
        if elt:
            node=elt.next_sibling
            while node:
                if getattr(node,'name',None) in ('h2','h3'):
                    break
                if hasattr(node,'get_text'):sectionbits.append(node.get_text(' ',strip=True))
                else:sectionbits.append(str(node).strip())
                node=node.next_sibling
        sections.append({**heading,'text':' '.join(sectionbits)[:2200]})
    records.append({
        'slug':properties.get('slug',mdpath.stem.split('_',1)[-1]),
        'title':properties['title'],'group':properties['group'],
        'summary':properties['summary'],'order':int(properties['order']),
        'tags':[x.strip() for x in properties.get('tags','').split(',') if x.strip()],
        'html':content_html,'text':plain,'sections':sections,
        'minutes':max(2,round(len(plain.split())/225)),
    })
records.sort(key=lambda d:(GROUPS.index(d['group']) if d['group'] in GROUPS else 100,d['order']))
(RootOut:=ROOT/'public'/'assets'/'docs-data.js').write_text('window.DOCS='+json.dumps(records,ensure_ascii=False,separators=(',',':'))+';\nwindow.DOC_GROUPS='+json.dumps(GROUPS,ensure_ascii=False)+';\n',encoding='utf-8')
(RootOutCss:=ROOT/'public'/'assets'/'pygments.css').write_text(HtmlFormatter(style='monokai').get_style_defs('.highlight')+'\n',encoding='utf-8')
print('Compiled',len(records),'pages |',sum(len(d['sections']) for d in records),'indexed sections |',sum(len(d['text'].split()) for d in records),'words')
for gr in GROUPS:print(gr,sum(d['group']==gr for d in records))
