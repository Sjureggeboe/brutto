"""Samler natt/funn/*.md til build/data/natt.json og bygger siden på nytt.

Hver funnfil starter med en enkel frontmatter:
---
id: N01
tittel: ...
fase: F1
dato: 2026-10-29
sikkerhet: Høy | Middels | Lav
---
og har overskriftene «## Kort svar», «## Funn», «## Konsekvens for Brutto», «## Nye spørsmål» og «## Kilder».
"""
import glob, json, os, re, subprocess, sys

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)

def parse(path):
    text = open(path, encoding='utf-8').read()
    meta, body = {}, text
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', text, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                meta[k.strip()] = v.strip()
        body = m.group(2)
    parts = re.split(r'^## ', body, flags=re.M)
    secs = {}
    for p in parts[1:]:
        head, _, rest = p.partition('\n')
        secs[head.strip().lower()] = rest.strip()
    return {
        'id': meta.get('id', os.path.basename(path)[:3]),
        'tittel': meta.get('tittel', ''),
        'fase': meta.get('fase', ''),
        'dato': meta.get('dato', ''),
        'sikkerhet': meta.get('sikkerhet', ''),
        'kort_md': secs.get('kort svar', ''),
        'md': body.strip(),
    }

funn = [parse(p) for p in sorted(glob.glob(os.path.join(here, 'funn', '*.md')))]
logg = ''
lp = os.path.join(here, 'logg.md')
if os.path.exists(lp):
    logg = open(lp, encoding='utf-8').read()
morgen = ''
mp = os.path.join(here, 'morgen.md')
if os.path.exists(mp):
    morgen = open(mp, encoding='utf-8').read()
data = {'natt': {'funn': funn, 'logg_md': logg, 'morgen_md': morgen}}
json.dump(data, open(os.path.join(root, 'build', 'data', 'natt.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{len(funn)} funn skrevet til build/data/natt.json')
r = subprocess.run([sys.executable, '-I', os.path.join(root, 'build', 'build.py'), 'brutto.html'], capture_output=True, text=True)
print(r.stdout.strip() or r.stderr.strip())
