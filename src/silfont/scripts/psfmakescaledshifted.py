#!/usr/bin/env python3
'''Creates duplicate versions of glyphs that are scaled and shifted.
Input is a csv with three fields: original,new,unicode'''
__url__ = 'https://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2019 SIL International (https://www.sil.org)'
__license__ = 'Released under the MIT License (https://opensource.org/licenses/MIT)'
__author__ = 'Victor Gaultney'

from silfont.core import execute
from silfont.util import parsecolors
from ast import literal_eval as make_tuple

argspec = [
    ('ifont', {'help': 'Input font filename'}, {'type': 'infont'}),
    ('ofont',{'help': 'Output font file','nargs': '?' }, {'type': 'outfont'}),
    ('-i','--input',{'help': 'Input csv file', 'required': True}, {'type': 'incsv', 'def': 'scaledshifted.csv'}),
    ('-c', '--colorcells', {'help': 'Color cells of generated glyphs', 'action': 'store_true'}, {}),
    ('--color', {'help': 'Color to use when marking generated glyphs'},{}),
    ('-t','--transform',{'help': 'Transform matrix or type', 'required': True}, {}),
    ('-l','--log',{'help': 'Set log file name'}, {'type': 'outfile', 'def': '_scaledshifted.log'})]

def doit(args) :
    font = args.ifont
    logger = args.logger
    transform = args.transform

    if transform[1] == "(":
        # Set transform from matrix - example: "(0.72, 0, 0, 0.6, 10, 806)"
        # (xx, xy, yx, yy, x, y)
        trans = make_tuple(args.transform)
    else:
        # Set transformation specs from UFO lib.plist org.sil.lcg.transforms
        # Will need to be enhanced to support adjustMetrics, boldX, boldY parameters for smallcaps
        try:
            trns = font.lib["org.sil.lcg.transforms"][transform]
        except KeyError:
            logger.log("Error: transform type not found in lib.plist org.sil.lcg.transforms", "S")
        else:
            try:
                adjM = trns["adjustMetrics"]
            except KeyError:
                adjM = 0
            try:
                skew = trns["skew"]
            except KeyError:
                skew = 0
            try:
                shiftX = trns["shiftX"]
            except KeyError:
                shiftX = 0
            try:
                shiftY = trns["shiftY"]
            except KeyError:
                shiftY = 0
            trans = (trns["scaleX"], 0, skew, trns["scaleY"], shiftX+adjM, shiftY)


    # Process csv list into a dictionary structure
    args.input.numfields = 3
    deps = {}
    for (source, newname, newuni) in args.input :
        if source in deps:
            deps[source].append({"newname": newname, "newuni": newuni})
        else:
            deps[source] = [({"newname": newname, "newuni": newuni})]

    # Iterate through dictionary (unsorted)
    for source in deps:
        # Check if source glyph is in font
        if source in font.keys() :
            for target in deps[source]:
                # Give warning if target is already in font, but overwrite anyway
                targetname = target["newname"]
                if targetname in font.keys() :
                    logger.log("Warning: " + targetname + " already in font and will be replaced")

                # Make a copy of source into a new glyph object
                sourceglyph = font[source]
                newglyph = sourceglyph.copy()

                newglyph.transformBy(trans)
                # Set width because transformBy does not seems to properly adjust width
                newglyph.width = (int(newglyph.width * trans[0])) + (adjM * 2)

                # Set unicode
                newglyph.unicodes = []
                if target["newuni"]:
                    newglyph.unicode = int(target["newuni"], 16)

                # mark glyphs as being generated by setting cell mark color (defaults to blue if args.color not set)
                if args.colorcells or args.color:
                    if args.color:
                        (color, name, logcolor, splitcolor) = parsecolors(args.color, single=True)
                        if color is None: logger.log(logcolor, "S")  # If color not parsed, parsecolors() puts error in logcolor
                        color = color.split(",") # Need to convert string to tuple
                        color = (float(color[0]), float(color[1]), float(color[2]), float(color[3]))
                    else:
                        color = (0.18, 0.16, 0.78, 1)
                    newglyph.markColor = color

                # Add the new glyph object to the font with name target
                font.__setitem__(targetname, newglyph)

                # Decompose glyph in case there may be components
                # It seems you can't decompose a glyph has hasn't yet been added to a font
                font[targetname].decompose()
                # Correct path direction
                font[targetname].correctDirection()

                logger.log(source + " duplicated to " + targetname)
        else :
            logger.log("Warning: " + source + " not in font")

    return font

def cmd() : execute("FP",doit,argspec)
if __name__ == "__main__": cmd()