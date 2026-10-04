import os, glob

base = os.path.dirname(os.path.abspath(__file__))
hdr = open(os.path.join(base, '_header.html'), encoding='utf-8').read().strip()
ftr = open(os.path.join(base, '_footer.html'), encoding='utf-8').read().strip()

MAPA = {
    'index.html': 'index', 'o-mne.html': 'o-mne', 'co-nabizim.html': 'co-nabizim',
    'prace-s-konmi.html': 'kone', 'prace-s-energii.html': 'energie',
    'cenik.html': 'cenik', 'kontakt.html': 'kontakt',
}

for path in glob.glob(os.path.join(base, 'masaze-iva-nemcova', '*.html')):
    fn = os.path.basename(path)
    if fn not in MAPA:
        continue
    s = open(path, encoding='utf-8').read()
    h = hdr.replace(f'data-p="{MAPA[fn]}"', f'data-p="{MAPA[fn]}" class="akt"')
    s = s.replace('<!--HEADER-->', h).replace('<!--FOOTER-->', ftr)
    open(path, 'w', encoding='utf-8').write(s)
    ok = ('class="akt"' in s) and ('foot-grid' in s)
    print(fn, 'OK' if ok else 'CHYBA')
