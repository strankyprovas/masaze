p = '/private/tmp/claude-501/-Users-matyas-Prace/17927987-3caf-477d-b942-1e1d9dec9288/scratchpad/ladenise/masaze-iva-nemcova/co-nabizim.html'
s = open(p, encoding='utf-8').read()

start = s.index('<section>\n  <div class="wrap-uzsi">\n    <div class="sl-item">')
end = s.index('</section>', start) + len('</section>')

novy = '''<section>
  <div class="wrap">
    <div class="sluzby-grid">

      <div class="sluzba-karta">
        <div class="sluzba-hlava"><svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M32 54C18 46 12 34 16 22c10-2 22 2 26 14 3 9-2 15-10 18z"/><path d="M28 50C24 38 26 28 34 20"/></svg></div>
        <div class="sluzba-telo">
          <h3>Bowenova technika</h3>
          <p>Šetrná celostní metoda jemných hmatů, která pomáhá tělu nastartovat vlastní ozdravné procesy. Vhodná i při dlouhodobých potížích — od bolestí zad a kloubů po celkové vyčerpání.</p>
          <div class="sluzba-akce"><a href="cenik.html" class="btn-mini">Ceník →</a><a href="tel:+420732122344" class="btn-mini line">Objednat</a></div>
        </div>
      </div>

      <div class="sluzba-karta">
        <div class="sluzba-hlava modra"><svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="32" cy="30" r="13"/><path d="M32 43v8M20 20l-4-4M44 20l4-4M14 32H8M56 32h-6M22 10l-2-5M42 10l2-5"/></svg></div>
        <div class="sluzba-telo">
          <h3>Access Bars</h3>
          <p>Jemné doteky 32 bodů na hlavě, které pomáhají zklidnit přehlcenou mysl, uvolnit stres a staré vzorce. Klienti popisují hluboký klid a lepší spánek.</p>
          <div class="sluzba-akce"><a href="prace-s-energii.html" class="btn-mini">Zjistit více →</a><a href="cenik.html" class="btn-mini line">Ceník</a></div>
        </div>
      </div>

      <div class="sluzba-karta">
        <div class="sluzba-hlava"><svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M24 8c8 0 10 8 10 16s4 10 8 12-2 14-10 14-14-6-14-16c0-12 2-26 6-26z"/><path d="M22 20h8M21 28h9M22 36h8"/></svg></div>
        <div class="sluzba-telo">
          <h3>Reflexní terapie</h3>
          <p>Práce s reflexními body na chodidlech — prokrvení, uvolnění a podpora přirozené rovnováhy organismu.</p>
          <div class="sluzba-akce"><a href="cenik.html" class="btn-mini">Ceník →</a><a href="tel:+420732122344" class="btn-mini line">Objednat</a></div>
        </div>
      </div>

      <div class="sluzba-karta">
        <div class="sluzba-hlava modra"><svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M32 52s-16-9.3-16-21a9 9 0 0 1 16-5.7A9 9 0 0 1 48 31c0 11.7-16 21-16 21z"/><path d="M12 14l2.2 2.2M52 14l-2.2 2.2M32 6v4"/></svg></div>
        <div class="sluzba-telo">
          <h3>Kombinace Bowen + Access Bars</h3>
          <p>Dvě terapie v jednom ošetření — tělo i mysl si konečně vydechnou. Nejoblíbenější volba klientek.</p>
          <div class="sluzba-akce"><a href="cenik.html" class="btn-mini">Ceník →</a><a href="tel:+420732122344" class="btn-mini line">Objednat</a></div>
        </div>
      </div>

      <div class="sluzba-karta">
        <div class="sluzba-hlava modra"><svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M32 10l3 8 8 1-6 6 2 9-7-5-7 5 2-9-6-6 8-1z"/><path d="M14 44l1.5 4 4 1.5-4 1.5L14 55l-1.5-4-4-1.5 4-1.5zM50 42l1.5 4 4 1.5-4 1.5L50 53l-1.5-4-4-1.5 4-1.5z"/></svg></div>
        <div class="sluzba-telo">
          <h3>Reiki — i na dálku</h3>
          <p>Energetická terapie pro zklidnění, harmonizaci a doplnění energie. Nabízím ji i na dálku — pomoc dostanete, i když nemůžete přijet.</p>
          <div class="sluzba-akce"><a href="prace-s-energii.html" class="btn-mini">Zjistit více →</a><a href="cenik.html" class="btn-mini line">Ceník</a></div>
        </div>
      </div>

      <div class="sluzba-karta">
        <div class="sluzba-hlava"><svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M14 50c0-10 4-18 10-24l6-6 4-8 6 4 6 2c4 2 6 6 6 10v4l-6-2-4 6c-4 6-6 10-6 14"/><path d="M26 50v-6M44 50v-8"/></svg></div>
        <div class="sluzba-telo">
          <h3>Bowen pro koně</h3>
          <p>Jemné ošetření pro koně — od ztuhlosti a nerovnováhy po zotavení. Přijedu za vámi do stáje; kůň si tempo určuje sám.</p>
          <div class="sluzba-akce"><a href="prace-s-konmi.html" class="btn-mini">Zjistit více →</a><a href="cenik.html" class="btn-mini line">Ceník</a></div>
        </div>
      </div>

    </div>

    <p class="pozn center" style="margin-top:2rem">Délku i druh ošetření vždy doladíme při objednání podle toho, co vaše tělo
      právě potřebuje. Kompletní ceny najdete v <a href="cenik.html">ceníku</a>.</p>

    <p class="center" style="margin-top:1.6rem">
      <a href="tel:+420732122344" class="btn">Objednat se — 732 122 344</a>
    </p>
  </div>
</section>'''

s = s[:start] + novy + s[end:]
open(p, 'w', encoding='utf-8').write(s)
print('co-nabizim prestaveno na karty')

# CSS pro karty
c = '/private/tmp/claude-501/-Users-matyas-Prace/17927987-3caf-477d-b942-1e1d9dec9288/scratchpad/ladenise/masaze-iva-nemcova/styles.css'
css = open(c, encoding='utf-8').read()
if 'sluzba-karta' not in css:
    css += '''
/* karty sluzeb (Co nabizim — vzor lenkajurickova/sluzby) */
.sluzby-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 1.6rem; }
.sluzba-karta { background: var(--bila); border: 1px solid var(--linka); border-radius: 18px; overflow: hidden; box-shadow: 0 10px 30px rgba(63,58,42,.05); display: flex; flex-direction: column; }
.sluzba-hlava { height: 150px; display: grid; place-items: center; color: var(--zelena); background: linear-gradient(135deg, #eef2e4, #f7f5ec); }
.sluzba-hlava.modra { color: var(--modra); background: linear-gradient(135deg, var(--modra-sv), #f4f8fb); }
.sluzba-hlava svg { width: 64px; height: 64px; opacity: .9; }
.sluzba-telo { padding: 1.5rem 1.7rem 1.7rem; display: flex; flex-direction: column; flex: 1; }
.sluzba-telo h3 { font-size: 1.35rem; margin-bottom: .5rem; }
.sluzba-telo p { font-size: .93rem; flex: 1; }
.sluzba-akce { display: flex; gap: .6rem; margin-top: 1.1rem; flex-wrap: wrap; }
.btn-mini { text-decoration: none; font-size: .85rem; font-weight: 700; padding: .55rem 1.2rem; border-radius: 999px; background: var(--zelena); color: #fff; transition: .2s; }
.btn-mini:hover { background: var(--zelena-tm); }
.btn-mini.line { background: transparent; border: 1.5px solid var(--linka); color: var(--kmen); }
.btn-mini.line:hover { border-color: var(--kmen); }
'''
    open(c, 'w', encoding='utf-8').write(css)
print('css ok')
