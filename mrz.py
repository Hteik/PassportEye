#!/home/keith/.virtualenvs/passporteye/bin/python
# -*- coding: utf-8 -*-
import re
import sys
from passporteye.mrz.scripts import mrz
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(mrz())
