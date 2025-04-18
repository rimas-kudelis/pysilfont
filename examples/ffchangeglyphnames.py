#!/usr/bin/env python3
from __future__ import unicode_literals
'''Update glyph names in a font based on csv file
   - Using FontForge rather than UFOlib so it can work with ttf (or sfd) files'''
__url__ = 'https://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2016-2025, SIL Global (https://www.sil.org)'
__license__ = 'Released under the MIT License (https://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'

from silfont.core import execute

''' This  will need updating, since FontForge is no longer supported as a tool by execute() So:
- ifont and ofont will need to be changed to have type 'filename'
- ifont will then need to be opened using fontforge.open
- The font will need to be saved with font.save
- execute will need to be called with the tool set to None instead of "FF"
'''

argspec = [
    ('ifont',{'help': 'Input ttf font file'}, {'type': 'infont'}),
    ('ofont',{'help': 'Output font file','nargs': '?' }, {'type': 'outfont'}),
    ('-i','--input',{'help': 'Mapping csv file'}, {'type': 'incsv', 'def': 'psnames.csv'}),
    ('-l','--log',{'help': 'Log file'}, {'type': 'outfile', 'def': '_setPostNames.log'}),
    ('--reverse',{'help': 'Change names in reverse', 'action': 'store_true', 'default': False},{})]

def doit(args) :
    logger = args.paramsobj.logger

    font = args.ifont

    # Process csv
    csv = args.input
    csv.numfields = 2
    newnames={}
    namescheck=[]
    missingnames = False
    for line in csv :
        if args.reverse :
            newnames[line[1]] = line[0]
            namescheck.append(line[1])
        else :
            newnames[line[0]] = line[1]
            namescheck.append(line[0])

    for glyph in font.glyphs():
        gname = glyph.glyphname
        if gname in newnames :
            namescheck.remove(gname)
            glyph.glyphname = newnames[gname]
        else:
            missingnames = True
            logger.log(gname + " in font but not csv file","W")

    if missingnames : logger.log("Font glyph names missing from csv - see log for details","E")

    for name in namescheck : # Any names left in namescheck were in csv but not ttf
        logger.log(name + " in csv but not in font","W")

    if namescheck != [] : logger.log("csv file names missing from font - see log for details","E")

    return font

def cmd() : execute("FF",doit,argspec) 
if __name__ == "__main__": cmd()

