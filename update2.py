import os, glob, re

base = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'masaze-iva-nemcova')

# ---------- 1) lišta: Iva Němcová / Masáže a terapeutická ošetření (její přání 4.10.) ----------
stary_brand = '<span><span class="brand-name">LADENISE</span><span class="brand-sub">Iva Němcová · terapeutická ošetření</span></span>'
novy_brand = '<span><span class="brand-name">Iva Němcová</span><span class="brand-sub">Masáže a terapeutická ošetření</span></span>'

for path in glob.glob(os.path.join(base, '*.html')):
    s = open(path, encoding='utf-8').read()
    s = s.replace(stary_brand, novy_brand)
    open(path, 'w', encoding='utf-8').write(s)
print('brand zmenen ve vsech strankach')

# brand-name mene roztahly (jmeno je delsi nez LADENISE)
css = open(os.path.join(base, 'styles.css'), encoding='utf-8').read()
css = css.replace('.brand-name { font-family: "Cormorant Garamond", serif; font-size: 1.5rem; letter-spacing: .16em;',
                  '.brand-name { font-family: "Cormorant Garamond", serif; font-size: 1.35rem; letter-spacing: .08em; white-space: nowrap;')
open(os.path.join(base, 'styles.css'), 'w', encoding='utf-8').write(css)
print('css brand ok')

# ---------- 2) cenik.html: realne ceny ----------
p = os.path.join(base, 'cenik.html')
s = open(p, encoding='utf-8').read()
stare = re.search(r'    <div class="sl-item"><h3>Bowenova technika.*?individuálně dle dojezdu</span></h3></div>', s, re.S)
nove = '''    <div class="sl-item"><h3>Bowenova technika <span class="doba">1 000 Kč / 60 min</span></h3></div>
    <div class="sl-item"><h3>Bowenova technika + Access Bars <span class="doba">1 000 Kč / 60 min</span></h3></div>
    <div class="sl-item"><h3>Reflexní terapie <span class="doba">250 Kč / 15 min · 500 Kč / 30 min</span></h3></div>
    <div class="sl-item"><h3>Reiki na dálku <span class="doba">250 Kč / 15 min · 500 Kč / 30 min</span></h3></div>
    <div class="sl-item"><h3>Access Bars — dospělí <span class="doba">1 600 Kč / cca 90 min</span></h3></div>
    <div class="sl-item"><h3>Access Bars — děti do 15 let, důchodci, studenti <span class="doba">1 400 Kč / cca 90 min</span></h3></div>
    <div class="sl-item"><h3>Access Bars — děti do 10 let <span class="doba">500 Kč / 30–45 min</span></h3></div>
    <div class="sl-item"><h3>Access Bars tělesné procesy <span class="doba">1 400 Kč / cca 75 min</span></h3></div>
    <div class="sl-item"><h3>Bowen pro koně <span class="doba">individuálně dle dojezdu</span></h3></div>'''
s = s[:stare.start()] + nove + s[stare.end():]
s = s.replace('<p class="lead">Každou návštěvu přizpůsobuji tomu, co vaše tělo právě potřebuje —\n      proto cenu a délku ošetření vždy upřesním při objednání.</p>',
              '<p class="lead">Ceník platný od 1. 1. 2027 pro provozovnu Podfortenská 103, Chrudim.\n      Délku i druh ošetření vždy doladíme při objednání podle toho, co vaše tělo potřebuje.</p>')
open(p, 'w', encoding='utf-8').write(s)
print('cenik ok')

# ---------- 3) kontakt: FB odkaz ----------
p = os.path.join(base, 'kontakt.html')
s = open(p, encoding='utf-8').read()
s = s.replace('<div class="kont-udaj"><b>E-mail:</b> <a href="mailto:nemcova.iva@centrum.cz">nemcova.iva@centrum.cz</a></div>',
              '<div class="kont-udaj"><b>E-mail:</b> <a href="mailto:nemcova.iva@centrum.cz">nemcova.iva@centrum.cz</a></div>\n      <div class="kont-udaj"><b>Facebook:</b> <a href="https://www.facebook.com/masazenemcova" target="_blank" rel="noopener">facebook.com/masazenemcova</a></div>')
open(p, 'w', encoding='utf-8').write(s)
print('kontakt fb ok')

# footer FB (vsechny stranky)
for path in glob.glob(os.path.join(base, '*.html')):
    s = open(path, encoding='utf-8').read()
    s = s.replace('Objednání po telefonické domluvě.</p>',
                  'Objednání po telefonické domluvě.<br><a href="https://www.facebook.com/masazenemcova" target="_blank" rel="noopener">Facebook</a></p>')
    open(path, 'w', encoding='utf-8').write(s)
print('footer fb ok')

# ---------- 4) sluzby na dalku ----------
p = os.path.join(base, 'co-nabizim.html')
s = open(p, encoding='utf-8').read()
s = s.replace('<p>Energetická terapie pro zklidnění, harmonizaci a doplnění energie.\n        Více v sekci <a href="prace-s-energii.html">práce s energií</a>.</p>',
              '<p>Energetická terapie pro zklidnění, harmonizaci a doplnění energie — nabízím\n        ji i <b>na dálku</b>, takže nemusíte nikam jezdit. Více v sekci\n        <a href="prace-s-energii.html">práce s energií</a>.</p>')
open(p, 'w', encoding='utf-8').write(s)
p = os.path.join(base, 'prace-s-energii.html')
s = open(p, encoding='utf-8').read()
s = s.replace('mnoho klientů při ní usíná a odchází\n          odpočatých jako po dlouhém spánku.</p>',
              'mnoho klientů při ní usíná a odchází\n          odpočatých jako po dlouhém spánku. Reiki nabízím i <b>na dálku</b> —\n          pomoc dostanete, i když nemůžete přijet.</p>')
open(p, 'w', encoding='utf-8').write(s)
# index: badge + meta
p = os.path.join(base, 'index.html')
s = open(p, encoding='utf-8').read()
s = s.replace('<span>Bowen pro koně</span>', '<span>Bowen pro koně</span><span>Služby i na dálku</span>')
s = s.replace('Reiki a Bowen pro koně. Terapeutická ošetření Ivy Němcové',
              'Reiki (i na dálku) a Bowen pro koně. Terapeutická ošetření Ivy Němcové')
# ---------- 5) nove reference z FB ----------
s = s.replace('''      <div class="ref">
        <h3>Když se tělo i mysl nadechnou</h3>''', '''      <div class="ref">
        <h3>Zablokovaná krční páteř</h3>
        <p>„Už cestou domů jsem cítila, že mi ramena povolila. Zlepšil se mi spánek — prospala jsem celou noc. Pocit ztuhlého krku a ramen postupně téměř vymizel. Metoda je jemná, účinek okamžitý a dlouhodobý — určitě mohu doporučit.“</p>
      </div>
      <div class="ref">
        <h3>Když se tělo i mysl nadechnou</h3>''')
open(p, 'w', encoding='utf-8').write(s)
print('na dalku + reference ok')
