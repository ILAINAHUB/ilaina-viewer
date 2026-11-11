"""Build-time upgrade: password is sent only to /api/connect over HTTPS."""
from pathlib import Path
from shutil import copyfile

root=Path(__file__).resolve().parents[1]
common=root/'desktop/common.py'
s=common.read_text(encoding='utf-8')
old="r = requests.post(self.server+'api/connect', json={'role':self.role,'token':self.token,'pc':self.pc},timeout=10)"
new=("login = {'role':self.role,'pc':self.pc}\n"
     "                if self.role == 'admin':\n"
     "                    login['password'] = self.token\n"
     "                else:\n"
     "                    login['token'] = self.token\n"
     "                r = requests.post(self.server+'api/connect', json=login, timeout=10)")
assert s.count(old)==1, 'Bridge connection signature changed; review patch'
common.write_text(s.replace(old,new),encoding='utf-8')
for name in ('admin_compact.py','customer_compact.py'):
    copyfile(root/'patches'/name,root/'desktop'/name)
print('Compact V4 sources installed; no credentials bundled')
