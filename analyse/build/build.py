import json, sys, glob, os

base = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(base, 'data')
D = json.load(open(os.path.join(data, 'core.json'), encoding='utf-8'))
LISTS = ('omrader', 'entiteter', 'sporsmal')
acc = {k: [] for k in LISTS}
notes = []

for p in sorted(glob.glob(os.path.join(data, '*.json'))):
    n = os.path.basename(p)
    if n == 'core.json':
        continue
    try:
        part = json.load(open(p, encoding='utf-8'))
    except Exception as e:
        notes.append(f'FEIL i {n}: {e}')
        continue
    for k, v in part.items():
        if k in LISTS and isinstance(v, list):
            for x in v:
                if isinstance(x, dict):
                    x.setdefault('_fil', n)
            acc[k].extend(v)
        elif isinstance(v, dict) and isinstance(D.get(k), dict):
            D[k].update(v)
        else:
            D[k] = v

# områder: slå sammen like koder, sorter etter fast rekkefølge
order = D.get('omrade_rekkefolge', [])
areas = {}
for a in acc['omrader']:
    if a['id'] in areas:
        areas[a['id']]['grupper'].extend(a.get('grupper', []))
        notes.append(f"Område {a['id']} finnes i flere filer")
    else:
        areas[a['id']] = a
D['omrader'] = sorted(areas.values(), key=lambda a: order.index(a['id']) if a['id'] in order else 99)

# entiteter: første vinner, felt slås sammen etter navn
ents = {}
for e in acc['entiteter']:
    if e['id'] in ents:
        have = {f['navn'] for f in ents[e['id']].get('felt', [])}
        extra = [f for f in e.get('felt', []) if f['navn'] not in have]
        ents[e['id']].setdefault('felt', []).extend(extra)
        notes.append(f"Entitet {e['id']} definert i {ents[e['id']]['_fil']} og {e['_fil']} (+{len(extra)} felt)")
    else:
        ents[e['id']] = e
D['entiteter'] = sorted(ents.values(), key=lambda e: (order.index(e.get('omrade')) if e.get('omrade') in order else 99, e['id']))

# spørsmål: fortløpende nummer
qs = acc['sporsmal']
for i, q in enumerate(qs, 1):
    q['nr'] = i
D['sporsmal'] = qs

# kontroll: funksjoner som viser til ukjente entiteter
known = set(ents)
missing = {}
nf = 0
for a in D['omrader']:
    for g in a.get('grupper', []):
        for f in g.get('funksjoner', []):
            nf += 1
            for d in f.get('data', []):
                if d not in known:
                    missing.setdefault(d, []).append(f['id'])
for d, fs in sorted(missing.items()):
    notes.append(f'Ukjent entitet {d} brukt av {len(fs)} funksjoner (f.eks. {fs[0]})')

s = json.dumps(D, ensure_ascii=False).replace('</', '<\\/')
css = open(os.path.join(base, 'base.css'), encoding='utf-8').read() + open(os.path.join(base, 'extra.css'), encoding='utf-8').read() + open(os.path.join(base, 'extra2.css'), encoding='utf-8').read()
t = open(os.path.join(base, 'template.html'), encoding='utf-8').read()
out = t.replace('/*__CSS__*/', css).replace('/*__DATA__*/', s)
target = os.path.join(base, sys.argv[1] if len(sys.argv) > 1 else 'brutto.html')
open(target, 'w', encoding='utf-8').write(out)
nfields = sum(len(e.get('felt', [])) for e in D['entiteter'])
print(f"ok {len(out)} bytes; {len(D['omrader'])} områder, {nf} funksjoner, {len(D['entiteter'])} entiteter, {nfields} felt, {len(qs)} spørsmål")
for n in notes:
    print(' -', n)
