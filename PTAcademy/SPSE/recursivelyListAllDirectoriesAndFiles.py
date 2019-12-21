"""
This script will go ahead and list all the 
directories and files in `/home/` and store 
the output in a json block and then will g-
o ahead and print that in the console
"""

import json
import os

_files   = {}

for presentDir, subdirs, files in os.walk('/home'):
    for file in files:
        if presentDir not in _files:
            _files[presentDir] = [str( os.path.join(presentDir, file) )]

        else:
            _files[presentDir].append( str( os.path.join(presentDir, file) ) )

print( json.dumps(_files, indent=4 ) )
