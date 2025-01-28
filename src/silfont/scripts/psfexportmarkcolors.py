#!/usr/bin/env python3
__doc__ = '''Write mapping of glyph name to cell mark color to a csv file
- csv format glyphname,colordef'''
__url__ = 'https://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2019-2025, SIL Global (https://www.sil.org)'
__license__ = 'Released under the MIT License (https://opensource.org/licenses/MIT)'
__author__ = 'Victor Gaultney'

from silfont.core import execute
from silfont.util import parsecolors, colortoname
import datetime

suffix = "_colormap"
argspec = [
    ('ifont',{'help': 'Input font file'}, {'type': 'infont'}),
    ('-o','--output',{'help': 'Output csv file'}, {'type': 'outfile', 'def': suffix+'.csv'}),
    ('-c','--color',{'help': 'Export list of glyphs that match color'},{}),
    ('-n','--names',{'help': 'Export colors as names', 'action': 'store_true', 'default': False},{}),
    ('-l','--log',{'help': 'Log file'}, {'type': 'outfile', 'def': suffix+'.log'}),
    ('--nocomments',{'help': 'No comments in output files', 'action': 'store_true', 'default': False},{})]

def doit(args) :
    font = args.ifont
    outfile = args.output
    logger = args.logger
    color = args.color

    # Add initial comments to outfile
    if not args.nocomments :
        outfile.write("# " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ") + args.cmdlineargs[0] + "\n")
        outfile.write("# "+" ".join(args.cmdlineargs[1:])+"\n\n")

    if color :
        (colorfilter, colorname, logcolor, splitcolor) = parsecolors(color, single=True)
        if colorfilter is None : logger.log(logcolor, "S") # If color not parsed, parsecolors() puts error in logcolor

    glyphlist = font.deflayer.keys()

    for glyphn in sorted(glyphlist) :
        glyph = font.deflayer[glyphn]
        colordefraw = ""
        colordef = ""
        if glyph["lib"] :
            lib = glyph["lib"]
            if "public.markColor" in lib :
                colordefraw = lib["public.markColor"][1].text
                colordef = '"' + colordefraw + '"'
                if args.names : colordef = colortoname(colordefraw, colordef)
            if color :
                if colorfilter == colordefraw : outfile.write(glyphn + "\n")
        if not color : outfile.write(glyphn + "," + colordef + "\n")
    return

def cmd() : execute("UFO",doit,argspec) 
if __name__ == "__main__": cmd()
