import os

base = '/private/tmp/claude-501/-Users-matyas-Prace/17927987-3caf-477d-b942-1e1d9dec9288/scratchpad/ladenise/masaze-iva-nemcova'

# ---------- 1) CENIK: platnost pro obe provozovny + jeji poznamka + PROKLIKY ----------
p = os.path.join(base, 'cenik.html')
s = open(p, encoding='utf-8').read()
s = s.replace('''<p class="lead">Ceník platný od 1. 1. 2027 pro provozovnu Podfortenská 103, Chrudim.
      Délku i druh ošetření vždy doladíme při objednání podle toho, co vaše tělo potřebuje.</p>''',
'''<p class="lead">Ceník platí pro obě provozovny — Hemže 18 (Choceň) i Podfortenská 103 (Chrudim).
      Kliknutím na službu se dostanete na její popis.</p>''')

# radky prokliknout na popisy sluzeb
radky = [
    ('Bowenova technika <span class="doba">1 000 Kč / 60 min</span>', 'co-nabizim.html#bowen'),
    ('Bowenova technika + Access Bars <span class="doba">1 000 Kč / 60 min</span>', 'co-nabizim.html#kombinace'),
    ('Reflexní terapie <span class="doba">250 Kč / 15 min · 500 Kč / 30 min</span>', 'co-nabizim.html#reflexni'),
    ('Reiki na dálku <span class="doba">250 Kč / 15 min · 500 Kč / 30 min</span>', 'prace-s-energii.html'),
    ('Access Bars — dospělí <span class="doba">1 600 Kč / cca 90 min</span>', 'co-nabizim.html#access-bars'),
    ('Access Bars — děti do 15 let, důchodci, studenti <span class="doba">1 400 Kč / cca 90 min</span>', 'co-nabizim.html#access-bars'),
    ('Access Bars — děti do 10 let <span class="doba">500 Kč / 30–45 min</span>', 'co-nabizim.html#access-bars'),
    ('Access Bars tělesné procesy <span class="doba">1 400 Kč / cca 75 min</span>', 'prace-s-energii.html'),
    ('Bowen pro koně <span class="doba">individuálně dle dojezdu</span>', 'prace-s-konmi.html'),
]
for text, href in radky:
    stary = f'<div class="sl-item"><h3>{text}</h3></div>'
    novy = f'<a class="sl-item sl-link" href="{href}"><h3>{text}</h3></a>'
    assert stary in s, text[:40]
    s = s.replace(stary, novy)

# poukazy karta: pouze jeji veta + telefon po kliknuti
stary = '''    <div class="karta" style="margin-top:2rem">
      <h3>Dárkové poukazy</h3>
      <p>Poukazy na jednotlivá ošetření i zvýhodněné balíčky více návštěv (2×, 3×, 5× a 10×).
        Připravím je na počkání — stačí zavolat.</p>
    </div>'''
novy = '''    <div class="karta" style="margin-top:2rem">
      <h3>Dárkové poukazy</h3>
      <p>Poukazy na jednotlivá ošetření i balíčky na více návštěv (2×, 3×, 5× a 10×).</p>
      <p style="margin-top:.7rem"><a class="btn-mini" href="tel:+420732122344">Objednat poukaz — 732 122 344</a></p>
    </div>'''
assert stary in s
s = s.replace(stary, novy)

# jeji poznamka o delce / konzultaci
s = s.replace('''<p class="pozn" style="margin-top:1.6rem">Platba v hotovosti nebo převodem.''',
'''<p class="pozn" style="margin-top:1.6rem">Vzhledem k rozdílným délkám ošetření je potřeba se na konkrétním
      ošetření domluvit předem při objednávání — předem je možná i konzultace, co by v daném případě bylo účinnější.
      Platba v hotovosti nebo převodem.''')
open(p, 'w', encoding='utf-8').write(s)
print('cenik ok')

# ---------- 2) CO NABIZIM: kotvy na karty ----------
p = os.path.join(base, 'co-nabizim.html')
s = open(p, encoding='utf-8').read()
kotvy = [
    ('<div class="sluzba-karta">\n        <div class="sluzba-hlava"><svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M32 54C18', 'bowen'),
    ('<h3>Access Bars</h3>', 'access-bars'),
    ('<h3>Reflexní terapie</h3>', 'reflexni'),
    ('<h3>Kombinace Bowen + Access Bars</h3>', 'kombinace'),
]
s = s.replace('<div class="sluzba-karta">\n        <div class="sluzba-hlava"><svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M32 54C18',
              '<div class="sluzba-karta" id="bowen">\n        <div class="sluzba-hlava"><svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M32 54C18', 1)
def pridej_id(html, nadpis, idecko):
    i = html.index(f'<h3>{nadpis}</h3>')
    j = html.rindex('<div class="sluzba-karta">', 0, i)
    return html[:j] + f'<div class="sluzba-karta" id="{idecko}">' + html[j + len('<div class="sluzba-karta">'):]
for nadpis, idecko in [('Access Bars', 'access-bars'), ('Reflexní terapie', 'reflexni'), ('Kombinace Bowen + Access Bars', 'kombinace')]:
    s = pridej_id(s, nadpis, idecko)
open(p, 'w', encoding='utf-8').write(s)
print('kotvy ok')

# ---------- 3) INDEX: poukazy jen jeji veta ----------
p = os.path.join(base, 'index.html')
s = open(p, encoding='utf-8').read()
s = s.replace('''<p>Poukaz na ošetření je dárek, který opravdu pomůže — vybrat můžete jednorázové ošetření
        i zvýhodněné balíčky více návštěv. Poukazy připravím na počkání, stačí zavolat.</p>''',
'''<p>Poukazy na jednotlivá ošetření i balíčky na více návštěv (2×, 3×, 5× a 10×).</p>''')
open(p, 'w', encoding='utf-8').write(s)
print('index poukazy ok')

# ---------- 4) O MNE: fotky s efektem odskrabnuti ----------
p = os.path.join(base, 'o-mne.html')
s = open(p, encoding='utf-8').read()
stary = '''<section>
  <div class="wrap-uzsi">
    <p>K terapiím mě přivedla'''
novy = '''<section>
  <div class="wrap-uzsi">
    <div class="omne-grid">
      <div>
        <p>K terapiím mě přivedla'''
assert stary in s
s = s.replace(stary, novy)
stary = '''    <p class="center" style="margin-top:2.4rem">
      <a href="co-nabizim.html" class="btn">Podívejte se, co nabízím</a>
    </p>
  </div>
</section>'''
novy = '''    <p class="center" style="margin-top:2.4rem">
      <a href="co-nabizim.html" class="btn">Podívejte se, co nabízím</a>
    </p>
  </div>
</section>'''
# vlozit fotku vedle uvodnich odstavcu: ukoncit sloupec za "vdecne reaguji" karta
stary2 = '''    <div class="karta" style="margin-top:2.2rem">'''
novy2 = '''      </div>
      <figure class="stetec-foto" aria-label="Iva Němcová">
        <img src="photos/iva-portret.jpg" alt="Iva Němcová — Ladenise">
      </figure>
    </div>

    <div class="karta" style="margin-top:2.2rem">'''
assert stary2 in s
s = s.replace(stary2, novy2, 1)
open(p, 'w', encoding='utf-8').write(s)
print('o-mne fotka ok')

# ---------- 5) CSS: oval telefonu, sirka stranek, stetec maska, sl-link ----------
p = os.path.join(base, 'styles.css')
s = open(p, encoding='utf-8').read()
s = s.replace('.nav-tel { white-space: nowrap; font-weight: 700; color: var(--zelena-tm); text-decoration: none; font-size: .92rem; }',
'''.nav-tel { white-space: nowrap; font-weight: 700; color: #fff; background: var(--zelena); text-decoration: none;
  font-size: .88rem; padding: .5rem 1.15rem; border-radius: 999px; transition: .2s; }
.nav-tel:hover { background: var(--zelena-tm); }''')
s = s.replace('.wrap-uzsi { max-width: 820px; margin: 0 auto; }',
              '.wrap-uzsi { max-width: 1180px; margin: 0 auto; }')
s += '''
/* proklikavaci radky ceniku */
a.sl-link { display: block; text-decoration: none; color: inherit; transition: .2s; }
a.sl-link:hover { border-color: var(--zelena); box-shadow: 0 10px 26px rgba(95,138,52,.12); }
a.sl-link h3::after { content: " →"; color: var(--modra); font-family: "Nunito Sans", sans-serif; font-size: .85rem; }

/* O mne: text + fotka */
.omne-grid { display: grid; grid-template-columns: 1.15fr .85fr; gap: 2.6rem; align-items: start; }
@media (max-width: 860px) { .omne-grid { grid-template-columns: 1fr; } }

/* fotka "odskrabnuta stetcem" — par sirokych tahu odkryva fotografii */
.stetec-foto { position: relative; margin: 0; }
.stetec-foto img {
  width: 100%; border-radius: 14px;
  -webkit-mask-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 130'><g fill='black'><rect x='-12' y='8' width='124' height='21' rx='10' transform='rotate(-4 50 18)'/><rect x='-10' y='33' width='122' height='23' rx='11' transform='rotate(2.6 50 44)'/><rect x='-14' y='60' width='126' height='22' rx='11' transform='rotate(-2.2 50 71)'/><rect x='-10' y='86' width='122' height='21' rx='10' transform='rotate(3 50 96)'/><rect x='-12' y='110' width='118' height='18' rx='9' transform='rotate(-3.4 50 119)'/></g></svg>");
  -webkit-mask-size: 100% 100%;
  mask-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 130'><g fill='black'><rect x='-12' y='8' width='124' height='21' rx='10' transform='rotate(-4 50 18)'/><rect x='-10' y='33' width='122' height='23' rx='11' transform='rotate(2.6 50 44)'/><rect x='-14' y='60' width='126' height='22' rx='11' transform='rotate(-2.2 50 71)'/><rect x='-10' y='86' width='122' height='21' rx='10' transform='rotate(3 50 96)'/><rect x='-12' y='110' width='118' height='18' rx='9' transform='rotate(-3.4 50 119)'/></g></svg>");
  mask-size: 100% 100%;
}
.stetec-foto::after { content: ""; position: absolute; inset: 0; border-radius: 14px; pointer-events: none; }
'''
open(p, 'w', encoding='utf-8').write(s)
print('css ok')
