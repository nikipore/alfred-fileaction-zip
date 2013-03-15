# -*- coding: utf-8 -*-
import os
from zipfile import ZipFile

import alfred

ARCHIVE = u'Archive'

def zip(files):
    path = os.path.dirname(os.path.commonprefix(files))
    zipfile = os.path.join(path, u'%s.zip' % ARCHIVE)
    with ZipFile(zipfile, 'a') as z:
        for file in files:
            z.write(file, os.path.join(ARCHIVE, file.replace(path, u'', 1)))
    return zipfile

files = alfred.args()[0].split('\t')
try:
    zipfile = zip(files)
except Exception as e:
    alfred.write('Could not create archive: %s' % e)
else:
    alfred.write('Archive created (%d files): %s' % (len(files), zipfile))
