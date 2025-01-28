#!/usr/bin/env python
'Analyse a font and generate GDL to help with the creation of graphite fonts'
__url__ = 'https://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2015-2025, SIL Global (https://www.sil.org)'
__license__ = 'Released under the MIT License (https://opensource.org/licenses/MIT)'

from gdl.font import Font
import gdl.ot
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('infont')
parser.add_argument('outgdl')
parser.add_argument('-a','--ap')
parser.add_argument('-i','--include')
parser.add_argument('-y','--alias')
args = parser.parse_args()

f = Font(args.infont)
if args.alias : f.loadAlias(args.alias)
if args.ap : f.loadAP(args.ap)

f.createClasses()
f.calculateOTLookups()
f.calculatePointClasses()
f.ligClasses()

outf = open(args.outgdl, "w")
f.outGDL(outf, args)
outf.close()

