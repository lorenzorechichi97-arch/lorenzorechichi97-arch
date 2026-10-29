from pathlib import Path
from html import escape
p=Path(__file__).parent/'assets'
style='''<style>text{fill:#e9e2ce;font-family:Georgia,serif}.mono{font-family:monospace;fill:#a9ac92;letter-spacing:3px}.red{fill:#bd4b42}.muted{fill:#a9ac92}.sweep{animation:sweep 7s linear infinite}.pulse{animation:pulse 3s ease-in-out infinite}.draw{stroke-dasharray:1100;stroke-dashoffset:1100;animation:draw 5s ease-in-out infinite}.ember{animation:ember 6s ease-in-out infinite}.type{animation:type 8s steps(24,end) infinite}@keyframes sweep{from{transform:translateX(-900px)}to{transform:translateX(900px)}}@keyframes pulse{0%,100%{opacity:.3}50%{opacity:1}}@keyframes draw{0%{stroke-dashoffset:1100}55%,100%{stroke-dashoffset:0}}@keyframes ember{0%,100%{transform:translateY(10px);opacity:.1}50%{transform:translateY(-28px);opacity:.8}}@keyframes type{0%{width:0}35%,85%{width:800px}100%{width:0}}@media(prefers-reduced-motion:reduce){*{animation:none!important}.draw{stroke-dashoffset:0}.type{width:800px}}</style>'''
def svg(name,h,body):
 s=f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="{h}" viewBox="0 0 900 {h}" role="img"><title>{escape(name)}</title>{style}<defs><pattern id="grid" width="36" height="36" patternUnits="userSpaceOnUse"><path d="M36 0H0V36" fill="none" stroke="#32392b" stroke-width=".6"/></pattern><linearGradient id="fade"><stop stop-color="#b6483b" stop-opacity="0"/><stop offset=".5" stop-color="#b6483b" stop-opacity=".35"/><stop offset="1" stop-color="#b6483b" stop-opacity="0"/></linearGradient></defs><rect width="900" height="{h}" fill="#111710"/><rect width="900" height="{h}" fill="url(#grid)"/><rect x="12" y="12" width="876" height="{h-24}" fill="none" stroke="#596049"/><path d="M12 44V12H44 M856 12H888V44 M12 {h-44}V{h-12}H44 M856 {h-12}H888V{h-44}" fill="none" stroke="#c0b48b" stroke-width="2"/>{body}</svg>'''
 (p/(name+'.svg')).write_text(s)
def text(x,y,t,size=20,cls=''):return f'<text x="{x}" y="{y}" font-size="{size}" class="{cls}">{escape(t)}</text>'
wings='<g transform="translate(742 57)"><path d="M0 0L91 0L91 108L45 140L0 108Z" fill="#1d281e" stroke="#aaa381"/>'
for i in range(6):
 wings+=f'<path d="M44 {32+i*13}L{8+i*4} {12+i*11}L{12+i*4} {30+i*11}L44 {46+i*13}Z" fill="#c5c6b7"/><path d="M48 {32+i*13}L{84-i*4} {12+i*11}L{80-i*4} {30+i*11}L48 {46+i*13}Z" fill="#64828b"/>'
wings+='</g>'
svg('command-header',264,text(38,47,'SCOUT ARCHIVE / 進撃 / PERSONAL FILE',14,'mono')+text(36,131,'FORGENOX',77)+text(40,171,'LORENZO RECHICHI',23)+text(40,220,'OLTRE LE MURA. DENTRO IL CODICE.',16,'mono')+wings+'<path class="draw" d="M40 187H680" stroke="#b6483b" stroke-width="2"/><circle class="pulse" cx="853" cy="45" r="5" fill="#b6483b"/>')
svg('rumbling-label',84,text(38,51,'01 / IL FONDATORE',24)+text(590,50,'THE RUMBLING',17,'mono')+'<rect class="sweep" y="70" width="900" height="2" fill="url(#fade)"/>')
svg('dossier',300,text(38,48,'02 / DOSSIER DI ESPLORAZIONE',16,'mono')+text(38,104,'Costruisco strumenti. Esploro possibilità.',33)+text(38,154,'Sviluppo con il supporto dell’AI strumenti per il trading',23)+text(38,190,'e frontend web. Creo agenti AI in cloud e in locale',23)+text(38,226,'per automatizzare processi aziendali.',23)+text(38,270,'SPERIMENTARE  /  COSTRUIRE  /  CONDIVIDERE',14,'mono')+'<path class="draw" d="M38 120H850" stroke="#687351" fill="none"/>')
body=text(38,48,'03 / TERRITORI DI RICERCA',16,'mono')
for i,(title,sub,a,b) in enumerate([('AGENTI AI','RICOGNIZIONE','Cloud e locale','Automazione dei processi'),('TRADING','OSSERVAZIONE','Strumenti di analisi','Dati e workflow'),('FRONTEND','COSTRUZIONE','Interfacce web','Idee da rendere concrete')]):
 x=38+i*282
 body+=f'<rect x="{x}" y="76" width="260" height="194" fill="#182016" stroke="#48523c"/>'+text(x+18,109,'0'+str(i+1)+' / '+sub,12,'mono')+text(x+18,153,title,27)+text(x+18,197,a,18)+text(x+18,225,b,17)+f'<path class="draw" d="M{x+18} 246h222" stroke="#ac4b3b" stroke-width="2"/>'
svg('territories',294,body)
body=text(38,48,'04 / ROTTA DI ESPLORAZIONE',16,'mono')+text(38,95,'Dall’idea al prossimo esperimento.',29)
body+='<path d="M82 178C190 108 250 242 382 177S620 118 800 179" fill="none" stroke="#697256" stroke-width="2" stroke-dasharray="5 8"/><path class="draw" d="M82 178C190 108 250 242 382 177S620 118 800 179" fill="none" stroke="#c0b48b" stroke-width="3"/>'
for x,t in [(82,'ESPLORA'),(382,'COSTRUISCI'),(800,'CONDIVIDI')]:body+=f'<circle class="pulse" cx="{x}" cy="178" r="12" fill="#b6483b"/><circle cx="{x}" cy="178" r="4" fill="#eee4ce"/>'+f'<text x="{x}" y="227" text-anchor="middle" font-size="14" class="mono">{t}</text>'
svg('expedition',254,body)
svg('footer',174,'<defs><clipPath id="typing"><rect class="type" x="40" y="30" width="800" height="90"/></clipPath></defs><g clip-path="url(#typing)">'+text(40,91,'AVANZA. SEMPRE.',52)+'</g>'+text(40,136,'FORGENOX / CI VEDIAMO OLTRE LE MURA',15,'mono')+'<path class="draw" d="M40 110H850" stroke="#ac4b3b"/>')
print('6 animated SVG assets created')
# Narrow alternatives: same visual language, larger text at phone widths.
def mobile(name,h,body):
 svg(name,h,body)
 f=p/(name+'.svg');s=f.read_text().replace('width="900"','width="450"').replace(f'viewBox="0 0 900 {h}"',f'viewBox="0 0 450 {h}"').replace('width="876"','width="426"').replace('M856','M406').replace('H888','H438')
 f.write_text(s)
mobile('command-header-mobile',220,text(30,46,'SCOUT ARCHIVE / PERSONAL FILE',12,'mono')+text(28,108,'FORGENOX',52)+text(30,146,'LORENZO RECHICHI',22)+text(30,185,'OLTRE LE MURA.',17,'mono')+'<path class="draw" d="M30 160H420" stroke="#b6483b"/>')
mobile('dossier-mobile',306,text(28,45,'02 / DOSSIER',15,'mono')+text(28,94,'Costruisco strumenti.',27)+text(28,127,'Esploro possibilità.',27)+text(28,172,'AI per il trading e frontend web.',20)+text(28,206,'Agenti AI in cloud e in locale.',20)+text(28,240,'Automazione dei processi aziendali.',20)+'<path class="draw" d="M28 270H420" stroke="#b6483b"/>')
body=text(28,45,'03 / TERRITORI DI RICERCA',15,'mono')
for i,(title,desc) in enumerate([('AGENTI AI','Cloud, locale e automazioni'),('TRADING','Strumenti di analisi e workflow'),('FRONTEND','Interfacce e idee da costruire')]):
 y=76+i*112
 body+=f'<rect x="28" y="{y}" width="394" height="96" fill="#182016" stroke="#48523c"/>'+text(44,y+34,title,24)+text(44,y+68,desc,18)+f'<circle class="pulse" cx="395" cy="{y+28}" r="4" fill="#b6483b"/>'
mobile('territories-mobile',432,body)
mobile('footer-mobile',145,text(28,69,'AVANZA. SEMPRE.',34)+text(28,112,'CI VEDIAMO OLTRE LE MURA',12,'mono')+'<path class="draw" d="M28 85H420" stroke="#b6483b"/>')
