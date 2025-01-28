#!/usr/bin/env python3
__doc__ = '''Remove the specified key(s) from glif libs'''
__url__ = 'https://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2017-2025, SIL Global (https://www.sil.org)'
__license__ = 'Released under the MIT License (https://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'

from silfont.core import execute

argspec = [
    ('ifont',{'help': 'Input font file'}, {'type': 'infont'}),
    ('key',{'help': 'Key(s) to remove','nargs': '*' }, {}),
    ('-b', '--begins', {'help': 'Remove keys beginning with','nargs': '*' }, {}),
    ('-o', '--ofont',{'help': 'Output font file' }, {'type': 'outfont'}),
    ('-l','--log',{'help': 'Log file'}, {'type': 'outfile', 'def': '_removegliflibkeys.log'})]

def doit(args) :
    font = args.ifont
    logger = args.logger
    keys = args.key
    bkeys=args.begins if args.begins is not None else []
    keycounts = {}
    bkeycounts = {}
    for key in keys : keycounts[key] = 0
    for key in bkeys:
        if key in keycounts: logger.log("--begins key can't be the same as a standard key", "S")
        bkeycounts[key] = 0

    for glyphn in font.deflayer :
        glyph = font.deflayer[glyphn]
        if glyph["lib"] :
            for key in keys :
                if key in glyph["lib"] :
                    val = str( glyph["lib"].getval(key))
                    glyph["lib"].remove(key)
                    keycounts[key] += 1
                    logger.log(key + " removed from " + glyphn + ". Value was " + val, "I" )
                    if key == "com.schriftgestaltung.Glyphs.originalWidth": # Special fix re glyphLib bug
                        if glyph["advance"] is None: glyph.add("advance")
                        adv = (glyph["advance"])
                        if adv.width is None:
                            adv.width = int(float(val))
                            logger.log("Advance width for " + glyphn + " set to " + val, "I")
                        else:
                            logger.log("Advance width for " + glyphn + " is already set to " + str(adv.width) + " so originalWidth not copied", "E")
            for key in bkeys:
                gkeys = list(glyph["lib"])
                for gkey in gkeys:
                    if gkey[:len(key)] == key:
                        val = str(glyph["lib"].getval(gkey))
                        glyph["lib"].remove(gkey)
                        if gkey in keycounts:
                            keycounts[gkey] += 1
                        else:
                            keycounts[gkey] = 1
                        bkeycounts[key] += 1
                        logger.log(gkey + " removed from " + glyphn + ". Value was " + val, "I")

    for key in keycounts :
        count = keycounts[key]
        if count > 0 :
            logger.log(key + " removed from " + str(count) +  " glyphs", "P")
        else :
            logger.log("No lib entries found for " + key, "E")
    for key in bkeycounts:
        if bkeycounts[key] == 0: logger.log("No lib entries found for beginning with " + key, "E")

    return font

def cmd() : execute("UFO",doit,argspec)
if __name__ == "__main__": cmd()
