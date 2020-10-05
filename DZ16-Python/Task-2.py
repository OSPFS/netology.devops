#!/usr/bin/env python3

import os
import sys

if len(sys.argv) < 2:
    _PATH = os.getcwd()
else:
    _PATH = sys.argv[1]

print(_PATH)

bash_command = ["cd " + _PATH, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()

for result in result_os.split('\n'):    
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(prepare_result)
