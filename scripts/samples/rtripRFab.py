import types, sys, os
from robofab.world import *

args = len(sys.argv)
# Open the font
if args>1:
    infont = sys.argv[1]
else:
    infont = "/home/david/UFO/UFOtest/TestBase.ufo"

if args>2:
    outfont = sys.argv[2]
else:
    (base,ext) = os.path.splitext(infont)
    outfont = base + "_Rfab" + ext

print "Opening "+infont
rbfont = OpenFont(infont)

print "Closing "+outfont
rbfont.save(outfont)