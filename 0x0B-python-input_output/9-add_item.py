#!/usr/bin/python3

import sys
import os
save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file

new = []
filename = 'add_item.json'
if os.path.isfile(filename):
    if os.stat(filename).st_size > 0:
        new = load(filename)
new += [i for i in sys.argv[1:]]
save(new, filename)
