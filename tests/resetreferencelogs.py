#!/usr/bin/env python
''' Reset the reference log files following changes to tests
Works on one test group at a time.
Copies the results logs to reference .lg files, replacing making file paths generic.
setupTestdata.py then generates correct log files from .lg files
'''
__url__ = 'https://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2018 SIL Global (https://www.sil.org)'
__license__ = 'Released under the MIT License (https://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'

import os, sys, shutil, glob, io
from silfont.util import text_diff

# Check being run in pysilfont root directory
cwd = os.getcwd()
if os.path.split(cwd)[1] != "pysilfont":
    print("resetReferenceLogs must be run in pysilfont root directory")
    sys.exit(1)

if len(sys.argv) != 2:
    print("Usage: resetReferenceLogs testgroupname")
    print("*** Should only be run when reference logs in the local/testresults/<testgorupname> directory"
          " are known to be good ***")
    sys.exit()

testgroup = sys.argv[1]

if testgroup not in ("ufo", "fontparts"):
    print("Invalid test group")
    sys.exit()

logsdir = "local/testresults/" + testgroup + "/"
refdir = "tests/reference/" + testgroup + "/"

if not os.path.isdir(logsdir):
    print(logsdir + " does not exist")
    sys.exit()


# Read the new log files and create new .lg files from them
logs = glob.iglob(logsdir + "*.log")
updates = False
for log in logs:
    inlog = io.open(log, mode="r", encoding="utf-8")
    testn = os.path.splitext(os.path.split(log)[1])[0]
    outtmp = refdir + testn + ".tmp"
    outlg = refdir + testn + ".lg"
    outlog = io.open(outtmp, mode="w", encoding="utf-8")
    for line in inlog:
        line = line.replace(cwd, "@cwd@") # Replace machine-specific cwd with placeholder
        line = line.replace("\\","/") # Replace Windows \ with /
        outlog.write(line)
    outlog.close()
    # Only update the .lg if it has changed
    diff = text_diff(outtmp, outlg, ignore_chars=20)
    if diff.returncode: # Either they are different or .lg file is missing
        try:
            os.remove(outlg)
        except:
            pass
        os.rename(outtmp, outlg)
        updates = True
        print(outlg + " recreated")
    else:
        os.remove(outtmp)
if updates: print("Run tests/setuptestdata.py to reset reference .log files")