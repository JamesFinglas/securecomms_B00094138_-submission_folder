#!"D:\Storage\USB Backup\Year 3\Secure Communications\Secure Communications Labs B00094138\securecomms\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'crt==0.0.4','console_scripts','crt'
__requires__ = 'crt==0.0.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('crt==0.0.4', 'console_scripts', 'crt')()
    )
