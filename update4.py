import glob
import os
import re

base = '/private/tmp/claude-501/-Users-matyas-Prace/17927987-3caf-477d-b942-1e1d9dec9288/scratchpad/ladenise/masaze-iva-nemcova'

# ============ A) INDEX: 7 dlazdic dle jejiho docx ============
p = os.path.join(base, 'index.html')
s = open(p, encoding='utf-8').read()

tiles = '''    <div class="grid-2" style="margin-top:2.2rem">
      <div class="karta">
        <h3>Bowen</h3>
        <p class="tile-tag">Dopřejte si život bez bolesti!</p>
        <ul class="tile-ul"><li>bolesti zad, šíje, kloubů, nohou i rukou</li><li>bolesti hlavy, nespavost</li><li>tenisový loket, karpální tunel, ztuhlé rameno</li><li>úrazy, otoky, úleva pro Bechtěreviky</li></ul>
        <p style="margin-top:.8rem"><a class="vice" href="co-nabizim.html#bowen">Chci vědět víc! →</a></p>
      </div>
      <div class="karta">
        <h3>Access Bars</h3>
        <p class="tile-tag">Dopřejte si hlubokou změnu!</p>
        <ul class="tile-ul"><li>zklidnění těla i mysli při přetížení a stresu</li><li>pomoc při úrazech, šocích nebo traumatech</li><li>hluboká relaxace, změna návyků</li><li>odbourávání strachů, nespavost</li></ul>
        <p style="margin-top:.8rem"><a class="vice" href="co-nabizim.html#access-bars">Chci vědět víc! →</a></p>
      </div>
      <div class="karta">
        <h3>Bowen + Access Bars</h3>
        <p class="tile-tag">Dopřejte si rozproudění lymfy a celkovou relaxaci!</p>
        <ul class="tile-ul"><li>Bowen technika zaměřená na lymfatický systém</li><li>prohloubení účinku pomocí Access Bars</li></ul>
        <p style="margin-top:.8rem"><a class="vice" href="co-nabizim.html#kombinace">Chci vědět víc! →</a></p>
      </div>
      <div class="karta">
        <h3>Stimulace chodidel</h3>
        <p class="tile-tag">Dopřejte si chůzi jako po obláčku!</p>
        <ul class="tile-ul"><li>prohřátí a uvolnění chodidel</li><li>stimulace a ovlivnění orgánů</li><li>zvýšení citlivosti chodidel</li></ul>
        <p style="margin-top:.8rem"><a class="vice" href="co-nabizim.html#chodidla">Chci vědět víc! →</a></p>
      </div>
      <div class="karta">
        <h3>Působení na dálku</h3>
        <p class="tile-tag">Dopřejte si péči v pohodlí Vašeho domova!</p>
        <ul class="tile-ul"><li>Reiki</li><li>Access Bars</li><li>čištění prostor od energií</li></ul>
        <p style="margin-top:.8rem"><a class="vice" href="prace-s-energii.html">Chci vědět víc! →</a></p>
      </div>
      <div class="karta">
        <h3>Práce s koňmi</h3>
        <p class="tile-tag">I Vaše lásky potřebují péči!</p>
        <ul class="tile-ul"><li>hluboká relaxace a uvolnění</li><li>Bowen technika</li></ul>
        <p style="margin-top:.8rem"><a class="vice" href="prace-s-konmi.html">Chci vědět víc! →</a></p>
      </div>
      <div class="karta">
        <h3>Poukazy</h3>
        <p class="tile-tag">Dopřejte radost někomu blízkému!</p>
        <ul class="tile-ul"><li>Bowen · Access Bars · Bowen + Access Bars</li><li>Stimulace chodidel</li><li>balíčky na více návštěv (2×, 3×, 5× a 10×)</li></ul>
        <p style="margin-top:.8rem"><a class="vice" href="tel:+420732122344">Chci objednat! →</a></p>
      </div>
      <div class="karta">
        <h3>O mně</h3>
        <p class="tile-tag">Kdo se o vás bude starat?</p>
        <ul class="tile-ul"><li>individuální přístup ke každému</li><li>šetrné metody bez násilí</li><li>Hemže u Chocně a Chrudim</li></ul>
        <p style="margin-top:.8rem"><a class="vice" href="o-mne.html">Více o mně →</a></p>
      </div>
    </div>'''

start = s.index('    <div class="grid-2" style="margin-top:2.2rem">')
end = s.index('</section>', start)
konec_gridu = s.rindex('</div>', start, end) + len('</div>')
s = s[:start] + tiles + s[konec_gridu:]

# poukazy velkou sekci nahradit jen fotkou s textem dle docx
s = s.replace('''      <div class="eyebrow">Dárkové poukazy</div>
      <h2 class="title">Darujte chvíli <em>klidu</em></h2>
      <p>Poukazy na jednotlivá ošetření i balíčky na více návštěv (2×, 3×, 5× a 10×).</p>
      <p style="margin-top:1.2rem"><a href="tel:+420732122344" class="btn">Objednat poukaz</a></p>''',
'''      <div class="eyebrow">Dárkové poukazy</div>
      <h2 class="title">Dopřejte radost <em>někomu blízkému</em></h2>
      <p>Poukazy na jednotlivá ošetření i balíčky na více návštěv (2×, 3×, 5× a 10×).</p>
      <p style="margin-top:1.2rem"><a href="tel:+420732122344" class="btn">Chci objednat! — 732 122 344</a></p>''')
open(p, 'w', encoding='utf-8').write(s)
print('index 8 dlazdic ok')

# ============ B) CO NABIZIM: detailni texty ============
p = os.path.join(base, 'co-nabizim.html')
s = open(p, encoding='utf-8').read()

# hero lead
s = s.replace('<p class="lead">Všechny metody, se kterými pracuji, jsou šetrné a bez násilí. Při objednání\n      si krátce popovídáme a vybereme, co je pro vás právě teď nejvhodnější.</p>',
'<p class="lead">Všechny metody, se kterými pracuji, jsou šetrné a bez násilí. U každého ošetření\n      najdete, co vás čeká — aktuální ceny jsou v <a href="cenik.html">ceníku</a>.</p>')

detaily = '''<section>
  <div class="wrap-uzsi">

    <article class="detail" id="bowen">
      <h2 class="title" style="font-size:1.8rem">Bowen — <em>dopřejte si život bez bolesti!</em></h2>
      <ul class="tile-ul"><li>fyzické bolesti zad, šíje, kloubů, nohou nebo rukou</li><li>brnění v rukách nebo nohách</li><li>tenisový loket, syndrom karpálního tunelu</li><li>bolesti hlavy · nespavost</li><li>lymfatické cesty a uzliny · úrazy, otoky</li><li>úleva pro Bechtěreviky · pocit neklidných nohou · ztuhlé rameno</li></ul>
      <h3 style="margin-top:1.3rem">Co vás čeká?</h3>
      <p>Na začátku se Vás zeptám, co Vás trápí, s čím přicházíte. Pokusíme se zavzpomínat, jak dlouho ten stav trvá a co bylo na jeho začátku. Následně Vám vysvětlím, jak Bowen terapie funguje a máme i prostor na Vaše otázky.</p>
      <p>Bowenova technika se provádí vleže na lehátku a v oblečení — doporučuji si proto vzít na sebe něco pohodlného. Během terapie zlehka brnkám (přejíždím) na různých bodech po celém těle a Vy můžete pozorovat různé stavy a jejich změny, například brnění, chlad, teplo. Celé ošetření je velice jemné; může se i stát, že během něj usnete. Nejprve uvolňuji celé tělo, pak se zaměřuji na místo, kde máte potíže.</p>
      <p>Následně máme ještě prostor pro zhodnocení a porovnání toho, jak se cítíte. A já Vám shrnu pár doporučení do příštích dnů — po Bowen terapii doporučuji 3 dny nepít alkohol, vynechat saunu nebo horkou vanu a vyhnout se zvýšené námaze. Po ošetření velice často přichází silná únava, zvlášť po prvním ošetření; během dalších 3–6 dnů můžete pociťovat i rozlámání celého těla — reakce jsou individuální.</p>
      <p class="pozn">Na terapii si rezervujte cca 60 minut. Aktuální cenu najdete v <a href="cenik.html">ceníku</a>.</p>
    </article>

    <article class="detail" id="access-bars">
      <h2 class="title" style="font-size:1.8rem">Access Bars — <em>dopřejte si hlubokou změnu!</em></h2>
      <ul class="tile-ul"><li>zklidnění těla i mysli při přetížení a stresu</li><li>uvolnění fyzického i psychického napětí</li><li>pomoc při úrazech, šocích nebo traumatech</li><li>hluboká relaxace · změna návyků</li><li>odbourávání strachů · nespavost · zdravotní problémy · tělesné procesy</li></ul>
      <h3 style="margin-top:1.3rem">Co vás čeká?</h3>
      <p>Nejprve si popovídáme. Řeknete mi, s čím přicházíte a co byste potřebovali řešit. Společně rozebereme Vaše téma více do hloubky a domluvíme se na závěru a záměru, se kterým budeme v sezení pracovat. Pokud přicházíte s dětmi, je pravděpodobné, že nejdříve se domluvíme na terapii s Vámi.</p>
      <p>Následně Vám vysvětlím, jak Access Bars terapie funguje, a máme i prostor na Vaše otázky. Cílem je vytvořit bezpečný, důvěrný prostor, ve kterém otevřeme místo pro sdílení.</p>
      <p>Samotné ošetření probíhá vleže na zádech na lehátku, kdy postupně stimuluji 32 bodů na hlavě. Jednotlivých bodů se dotýkám velice zlehka — může se i stát, že prsty budu mít lehce nad hlavou. Jde o velice jemnou techniku, u které je snadné usnout a zrelaxovat. Na závěr máme ještě prostor na sdílení toho, co se ve Vás během terapie odehrávalo.</p>
      <p>Doporučuji ten den po terapii nikam nespěchat a celý den si užít v poklidu pozorováním svého nového vnitřního nastavení.</p>
      <p class="pozn">Na terapii si rezervujte cca 90 minut. Nabízím také <b>Access Bars tělesné procesy</b> (cca 75 minut). Aktuální ceny včetně zvýhodněných pro děti, studenty a důchodce najdete v <a href="cenik.html">ceníku</a>.</p>
    </article>

    <article class="detail" id="kombinace">
      <h2 class="title" style="font-size:1.8rem">Bowen + Access Bars — <em>rozproudění lymfy a celková relaxace</em></h2>
      <ul class="tile-ul"><li>Bowen technika zaměřená na lymfatický systém</li><li>prohloubení účinku pomocí Access Bars</li></ul>
      <p style="margin-top:1rem">Spojením těchto dvou technik zaciluji na maximální uvolnění psychického napětí a zrelaxování těla i mysli v každodenním shonu. Pomocí Bowen terapie nejprve uvolním celé tělo, pak přes lymfu docílím uvolnění emocí a pročištění těla od nežádoucích usazenin. Celé to v závěru posílím stimulací první pozice z Access Bars.</p>
      <p>Odcházíte tak ve větší pohodě, odpočatí a s vnitřním nadhledem.</p>
      <p class="pozn">Na tuto kombinaci si rezervujte cca 60 minut. Aktuální cenu najdete v <a href="cenik.html">ceníku</a>.</p>
    </article>

    <article class="detail" id="chodidla">
      <h2 class="title" style="font-size:1.8rem">Stimulace chodidel — <em>chůze jako po obláčku</em></h2>
      <ul class="tile-ul"><li>prohřátí a uvolnění chodidel</li><li>stimulace a ovlivnění orgánů</li><li>zvýšení citlivosti chodidel</li></ul>
      <p style="margin-top:1rem">Stimulaci reflexních plosek nohou doporučuji zkombinovat s Bowenem se zaměřením na nohy — není to ale podmínkou a můžeme se na ní domluvit i samostatně.</p>
      <p>Na toto ošetření můžete přijít s konkrétním problémem, na který se zaměříme, anebo si prostě užít a vychutnat péči o svoje chodidla, kdy se postupně věnuji každému místu na vašich chodidlech. Stimulaci je možné provádět v ponožkách i naboso.</p>
      <p>Po stimulaci dochází k prohřátí a uvolnění chodidel a zvýšení jejich citlivosti, k celkovému odlehčení chodidel a lýtek — a také ke stimulaci a ovlivňování funkce jednotlivých orgánů v těle.</p>
      <p class="pozn">Službu nabízím ve dvou délkách — 15 nebo 30 minut (250 Kč / 500 Kč, viz <a href="cenik.html">ceník</a>).</p>
    </article>

    <div class="grid-2" style="margin-top:2.4rem">
      <div class="karta">
        <h3>Působení na dálku</h3>
        <p>Reiki, Access Bars i čištění prostor od energií — péče, kterou dostanete v pohodlí domova.</p>
        <p style="margin-top:.8rem"><a class="vice" href="prace-s-energii.html">Chci vědět víc! →</a></p>
      </div>
      <div class="karta">
        <h3>Práce s koňmi</h3>
        <p>Hluboká relaxace a uvolnění Bowenovou technikou — i Vaše lásky potřebují péči.</p>
        <p style="margin-top:.8rem"><a class="vice" href="prace-s-konmi.html">Chci vědět víc! →</a></p>
      </div>
    </div>

    <p class="center" style="margin-top:2.4rem">
      <a href="tel:+420732122344" class="btn">Objednat se — 732 122 344</a>
      <a href="cenik.html" class="btn-line" style="margin-left:.6rem">Ceník</a>
    </p>
  </div>
</section>'''

start = s.index('<section>\n  <div class="wrap">\n    <div class="sluzby-grid">')
end = s.index('</section>', start) + len('</section>')
s = s[:start] + detaily + s[end:]
open(p, 'w', encoding='utf-8').write(s)
print('co-nabizim detaily ok')

# ============ C) PUSOBENI NA DALKU (prace-s-energii.html) ============
p = os.path.join(base, 'prace-s-energii.html')
s = open(p, encoding='utf-8').read()
s = s.replace('<title>Práce s energií · Reiki a Access Bars — Ladenise</title>',
              '<title>Působení na dálku · Reiki, Access Bars, čištění prostor — Ladenise</title>')
s = s.replace('<div class="eyebrow">Práce s energií</div>', '<div class="eyebrow">Působení na dálku</div>')
s = s.replace('<h1 class="title">Když potřebuje odpočinout <em>i mysl</em></h1>',
              '<h1 class="title">Dopřejte si péči <em>v pohodlí domova</em></h1>')
s = s.replace('<p class="lead">Některá únava se nedá rozmasírovat — sedí hlouběji. Pro tyhle chvíle\n      nabízím energetická ošetření, která pomáhají zklidnit mysl a doplnit síly.</p>',
'<p class="lead">Reiki, Access Bars i čištění prostor od energií — na dálku, takže\n      nemusíte nikam jezdit. Pomoc dostanete, ať jste kdekoliv.</p>')
# pridat kartu cisteni prostor
s = s.replace('''    <div class="karta" style="margin-top:1.5rem">
      <h3>Pro koho je práce s energií</h3>''',
'''    <div class="karta" style="margin-top:1.5rem">
      <h3>Čištění prostor od energií</h3>
      <p>Prostor, ve kterém žijete nebo pracujete, si nese svou energii. Čištění prostor
        pomáhá uvolnit to staré a těžké — doma i na pracovišti. Provádím na dálku,
        stačí se domluvit telefonicky.</p>
    </div>

    <div class="karta" style="margin-top:1.5rem">
      <h3>Pro koho je působení na dálku</h3>''')
open(p, 'w', encoding='utf-8').write(s)
print('pusobeni na dalku ok')

# ============ D) CENIK: prejmenovat reflexni radek ============
p = os.path.join(base, 'cenik.html')
s = open(p, encoding='utf-8').read()
s = s.replace('Reflexní terapie <span class="doba">250 Kč / 15 min · 500 Kč / 30 min</span>',
              'Stimulace chodidel (reflexní terapie) <span class="doba">250 Kč / 15 min · 500 Kč / 30 min</span>')
s = s.replace('href="co-nabizim.html#reflexni"', 'href="co-nabizim.html#chodidla"')
open(p, 'w', encoding='utf-8').write(s)
print('cenik ok')

# ============ E) NAV vsude: Prace s energii -> Pusobeni na dalku ============
for path in glob.glob(os.path.join(base, '*.html')):
    s = open(path, encoding='utf-8').read()
    s = s.replace('<a href="prace-s-energii.html" data-p="energie">Práce s energií</a>',
                  '<a href="prace-s-energii.html" data-p="energie">Působení na dálku</a>')
    s = s.replace('<a href="prace-s-energii.html" data-p="energie" class="akt">Práce s energií</a>',
                  '<a href="prace-s-energii.html" data-p="energie" class="akt">Působení na dálku</a>')
    s = s.replace('<a href="prace-s-energii.html">Práce s energií</a>',
                  '<a href="prace-s-energii.html">Působení na dálku</a>')
    open(path, 'w', encoding='utf-8').write(s)
print('nav prejmenovan')

# ============ F) CSS pro dlazdice a detaily ============
p = os.path.join(base, 'styles.css')
s = open(p, encoding='utf-8').read()
if 'tile-tag' not in s:
    s += '''
/* dlazdice Domu + detailni texty Co nabizim (texty Ivy, 6. 10. 2026) */
.tile-tag { color: var(--modra); font-weight: 700; font-size: .92rem; margin-bottom: .5rem; }
.tile-ul { list-style: none; padding: 0; margin: 0; }
.tile-ul li { font-size: .9rem; padding-left: 1.15rem; position: relative; margin-bottom: .3rem; }
.tile-ul li::before { content: "✓"; position: absolute; left: 0; color: var(--zelena); font-weight: 700; }
article.detail { background: var(--bila); border: 1px solid var(--linka); border-radius: 18px; padding: 2.2rem 2.4rem; margin-bottom: 1.8rem; box-shadow: 0 10px 30px rgba(63,58,42,.05); }
article.detail h3 { font-size: 1.25rem; margin-bottom: .4rem; }
article.detail p { margin-top: .7rem; }
'''
    open(p, 'w', encoding='utf-8').write(s)
print('css ok')
