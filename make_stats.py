"""Turn a CSV of real stats into stats.js.
CSV: first column must be player_name (same spelling as photos-needed.csv); every other column becomes a stat label.
Run:  python make_stats.py my_stats.csv   ->  overwrites stats.js
"""
import csv, json, sys
rows = list(csv.DictReader(open(sys.argv[1], encoding='utf-8-sig')))
out = {}
for r in rows:
    name = r.pop('player_name').strip()
    out[name] = {k.strip(): v.strip() for k, v in r.items() if v and v.strip()}
open('stats.js', 'w', encoding='utf-8').write('window.STATS = ' + json.dumps(out, indent=1, ensure_ascii=False) + ';\n')
print(len(out), 'players written to stats.js')
