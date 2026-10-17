from pathlib import Path
import json,re,struct
r=Path(__file__).resolve().parents[1]
m=json.loads((r/'project.json').read_text(encoding='utf-8'))
assert m['name']=='ai-to-agent-trc-3d' and m['version']=='0.1.0'
links=0
for f in r.rglob('*.md'):
 for target in re.findall(r'\]\(([^)]+)\)',f.read_text(encoding='utf-8')):
  if '://' not in target:
   assert (f.parent/target.split('#')[0]).exists(),(f,target)
   links+=1
cards=list((r/'assets/cards').glob('*.png'))
assert len(cards)==6
for p in cards:
 data=p.read_bytes();assert data[:8]==b'\x89PNG\r\n\x1a\n'
 w,h=struct.unpack('>II',data[16:24]);assert w>0 and h>0
for n in ['X','Y','Z']:
 assert n+'-A' in (r/'examples/paired-cases.md').read_text(encoding='utf-8')
 assert n+'-B' in (r/'examples/paired-cases.md').read_text(encoding='utf-8')
for p in r.rglob('*'):
 if p.is_file():assert p.suffix not in ['.pem','.key'] and p.name!='.env'
print(f'PASS: metadata, {links} relative links, 6 PNG headers, 6 case IDs, sensitive filename check')
print('NOT VERIFIED: real-world efficacy, source rights, remote repository / tag / release')
