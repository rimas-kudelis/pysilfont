#!/usr/bin/env python
''' Test of script named in testname below
'''
__url__ = 'https://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2019 SIL International (https://www.sil.org)'
__license__ = 'Released under the MIT License (https://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'

import silfont.util

# Next 7 lines of code may be test-specific
import silfont.scripts.psfmakefea as testcommand
testname = "psfmakefea"
cl = "psfmakefea -i tests/input/psfmakefea.feax -o local/testresults/ufo/psfmakefea.fea -l local/testresults/ufo/psfmakefea.log tests/input/font-psf-test/source/PsfTest-Regular.ufo"
outfont = None # Set to None for commands which don't output a font
diffexts = [".fea", ".log"] # List of extensions of all output files
exp_errors = 0   # These may need updating if the test ufo is updated
exp_warnings = 1 # The test ufo should have some errors/warnings to test the code!

# Code after this can be the same for most/all tests; if needed to be different for a test remove this comment!

def test_run():
    result = silfont.util.test_run("UFO", cl, testcommand, outfont, exp_errors, exp_warnings)
    assert result

def test_diffs(): # Do a diff on all output files
    result = silfont.util.test_diffs("ufo", testname, diffexts)
    assert result

if __name__ == "__main__":
    test_run()
    test_diffs()





