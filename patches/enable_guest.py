"""Apply the one-click guest UI to verified V2 desktop sources at build time."""
from pathlib import Path
import shutil
root=Path(__file__).resolve().parents[1]
common=root/'desktop/common.py'
text=common.read_text(encoding='utf-8')
old="if not token:\n            self.callback({'type':'local_error'"
new="if not token and self.role != 'customer':\n            self.callback({'type':'local_error'"
if new not in text:
    assert text.count(old)==1, 'Unexpected bridge source'
    common.write_text(text.replace(old,new),encoding='utf-8')
shutil.copy2(root/'patches/customer_oneclick.py',root/'desktop/customer_oneclick.py')
print('Guest client + One-click UI enabled')
