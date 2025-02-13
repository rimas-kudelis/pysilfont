#!/usr/bin/env python3
__doc__ = '''Export fonts in a GlyphsApp file to UFOs'''
__url__ = 'https://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2017-2025, SIL Global (https://www.sil.org)'
__license__ = 'Released under the MIT License (https://opensource.org/licenses/MIT)'
__author__ = 'Victor Gaultney'

from silfont.core import execute
from silfont.ufo import obsoleteLibKeys

import glyphsLib
import silfont.ufo
import silfont.etutil
from io import open
import os, shutil

argspec = [
    ('glyphsfont', {'help': 'Input font file'}, {'type': 'filename'}),
    ('masterdir', {'help': 'Output directory for masters'}, {}),
    ('--nofixes', {'help': 'Bypass code fixing data', 'action': 'store_true', 'default': False}, {}),
    ('--nofea', {'help': "Don't output features.fea", 'action': 'store_true', 'default': False}, {}),
    ('--preservefea', {'help': "Retain the original features.fea in the UFO", 'action': 'store_true', 'default': False}, {}),
    ('-l', '--log', {'help': 'Log file'}, {'type': 'outfile', 'def': '_glyphs2ufo.log'}),
    ('-r', '--restore', {'help': 'List of extra keys to restore to fontinfo.plist or lib.plist'}, {})]

def doit(args):
    logger = args.logger
    masterdir = args.masterdir
    logger.log("Creating UFO objects from GlyphsApp file", "I")
    with open(args.glyphsfont, 'r', encoding='utf-8') as gfile:
        gfont = glyphsLib.parser.load(gfile)
    ufos = glyphsLib.to_ufos(gfont, include_instances=False, family_name=None, propagate_anchors=False, generate_GDEF=False)

    keylists = {

        "librestorekeys": ["org.sil.pysilfontparams", "org.sil.altLineMetrics", "org.sil.lcg.toneLetters",
                   "org.sil.lcg.transforms", "public.glyphOrder", "public.postscriptNames", "public.unicodeVariationSequences",
                   "com.schriftgestaltung.disablesLastChange", "com.schriftgestaltung.disablesAutomaticAlignment",
                   "public.skipExportGlyphs"],
        "libdeletekeys": ("com.schriftgestaltung.customParameter.GSFont.copyright",
                          "com.schriftgestaltung.customParameter.GSFont.designer",
                          "com.schriftgestaltung.customParameter.GSFont.manufacturer",
                          "com.schriftgestaltung.customParameter.GSFont.note",
                          "com.schriftgestaltung.customParameter.GSFont.uniqueID",
                          "com.schriftgestaltung.customParameter.GSFont.Axes",
                          "com.schriftgestaltung.customParameter.GSFont.Axis Mappings",
                          "com.schriftgestaltung.customParameter.GSFontMaster.Master Name"),
        "libdeleteempty": ("com.schriftgestaltung.DisplayStrings",),
        "inforestorekeys": ["openTypeHeadCreated", "openTypeHeadFlags", "openTypeNamePreferredFamilyName", "openTypeNamePreferredSubfamilyName",
                       "openTypeNameUniqueID", "openTypeOS2WeightClass", "openTypeOS2WidthClass", "postscriptFontName",
                       "postscriptFullName", "styleMapFamilyName", "styleMapStyleName", "note",
                       "woffMetadataCredits", "woffMetadataDescription"],
        "integerkeys": ("openTypeOS2WeightClass", "openTypeOS2WidthClass"),
        "infodeletekeys": ("openTypeVheaVertTypoAscender", "openTypeVheaVertTypoDescender", "openTypeVheaVertTypoLineGap"),
 #       "infodeleteempty": ("openTypeOS2Selection",)
    }

    if args.restore: # Extra keys to restore.  Add to both lists, since should never be duplicated names
        keylist = args.restore.split(",")
        keylists["librestorekeys"] += keylist
        keylists["inforestorekeys"].append(keylist)

    loglists = []
    obskeysfound={}
    for ufo in ufos:
        loglists.append(process_ufo(ufo, keylists, masterdir, args, obskeysfound))
    for loglist in loglists:
        for logitem in loglist: logger.log(logitem[0], logitem[1])
    if obskeysfound:
        logmess = "The following obsolete keys were found. They may have been in the original UFO or you may have an old version of glyphsLib installed\n"
        for fontname in obskeysfound:
            keys = obskeysfound[fontname]
            logmess += "                    " + fontname + ": "
            for key in keys:
                logmess += key + ", "
            logmess += "\n"
        logger.log(logmess, "E")

def process_ufo(ufo, keylists, masterdir, args, obskeysfound):
    loglist=[]
#    sn = ufo.info.styleName  # )
#    sn = sn.replace("Italic Italic", "Italic")  # ) Temp fixes due to glyphLib incorrectly
#    sn = sn.replace("Italic Bold Italic", "Bold Italic")  # ) forming styleName
#    sn = sn.replace("Extra Italic Light Italic", "Extra Light Italic")  # )
#    ufo.info.styleName = sn  # )
    fontname = ufo.info.familyName.replace(" ", "") + "-" + ufo.info.styleName.replace(" ", "")

    # Fixes to the data
    if not args.nofixes:
        loglist.append(("Fixing data in " + fontname, "P"))
        # lib.plist processing
        loglist.append(("Checking lib.plist", "P"))

        # Restore values from original UFOs, assuming named as <fontname>.ufo in the masterdir

        ufodir = os.path.join(masterdir, fontname + ".ufo")
        try:
            origlibplist = silfont.ufo.Uplist(font=None, dirn=ufodir, filen="lib.plist")
        except Exception as e:
            loglist.append(("Unable to open lib.plist in " + ufodir + "; values will not be restored", "E"))
            origlibplist = None

        if origlibplist is not None:

            for key in keylists["librestorekeys"]:
                current = None if key not in ufo.lib else ufo.lib[key]
                if key in origlibplist:
                    new = origlibplist.getval(key)
                    if current == new:
                        continue
                    else:
                        ufo.lib[key] = new
                        logchange(loglist, " restored from backup ufo. ", key, current, new)
                elif current:
                    ufo.lib[key] = None
                    logchange(loglist, " removed since not in backup ufo. ", key, current, None)

        # Delete unneeded keys

        for key in keylists["libdeletekeys"]:
            if key in ufo.lib:
                current = ufo.lib[key]
                del ufo.lib[key]
                logchange(loglist, " deleted. ", key, current, None)

        for key in keylists["libdeleteempty"]:
            if key in ufo.lib and (ufo.lib[key] == "" or ufo.lib[key] == []):
                current = ufo.lib[key]
                del ufo.lib[key]
                logchange(loglist, " empty field deleted. ", key, current, None)

        # Check for obsolete keys
        for key in obsoleteLibKeys:
            if key in ufo.lib:
                if fontname not in obskeysfound: obskeysfound[fontname] = []
                obskeysfound[fontname].append(key)

        # Special processing for Axis Mappings
        #key = "com.schriftgestaltung.customParameter.GSFont.Axis Mappings"
        #if key in ufo.lib:
        #    current =ufo.lib[key]
        #    new = dict(current)
        #    for x in current:
        #        val = current[x]
        #        k = list(val.keys())[0]
        #        if k[-2:] == ".0": new[x] = {k[0:-2]: val[k]}
        #    if current != new:
        #        ufo.lib[key] = new
        #        logchange(loglist, " key names set to integers. ", key, current, new)

        # Special processing for ufo2ft filters
        key = "com.github.googlei18n.ufo2ft.filters"
        if key in ufo.lib:
            current = ufo.lib[key]
            new = list(current)
            for x in current:
                if x["name"] == "eraseOpenCorners":
                    new.remove(x)

            if current != new:
                if new == []:
                    del ufo.lib[key]
                else:
                    ufo.lib[key] = new
                logchange(loglist, " eraseOpenCorners filter removed ", key, current, new)

        # fontinfo.plist processing

        loglist.append(("Checking fontinfo.plist", "P"))

        try:
            origfontinfo = silfont.ufo.Uplist(font=None, dirn=ufodir, filen="fontinfo.plist")
        except Exception as e:
            loglist.append(("Unable to open fontinfo.plist in " + ufodir + "; values will not be restored", "E"))
            origfontinfo = None

        if origfontinfo is not None:
            for key in keylists["inforestorekeys"]:
                current = None if not hasattr(ufo.info, key) else getattr(ufo.info, key)
                if key in origfontinfo:
                    new = origfontinfo.getval(key)
                    if key in keylists["integerkeys"]: new = int(new)
                    if current == new:
                        continue
                    else:
                        setattr(ufo.info, key, new)
                        logchange(loglist, " restored from backup ufo. ", key, current, new)
                elif current:
                    setattr(ufo.info, key, None)
                    logchange(loglist, " removed since not in backup ufo. ", key, current, None)

        if getattr(ufo.info, "italicAngle") == 0:  # Remove italicAngle if 0
            setattr(ufo.info, "italicAngle", None)
            logchange(loglist, " removed", "italicAngle", 0, None)

        # Delete unneeded keys

        for key in keylists["infodeletekeys"]:
            if hasattr(ufo.info, key):
               current = getattr(ufo.info, key)
               setattr(ufo.info, key, None)
               logchange(loglist, " deleted. ", key, current, None)

#        for key in keylists["infodeleteempty"]:
#            if hasattr(ufo.info, key) and getattr(ufo.info, key) == "":
#                setattr(ufo.info, key, None)
#                logchange(loglist, " empty field deleted. ", key, current, None)
    if args.nofea or args.preservefea: ufo.features.text = ""  # Suppress output of features.fea

    # Now check for glyph level changes needed
    heightchanges = 0
    vertorichanges = 0
    for layer in ufo.layers:
        for glyph in layer:
            if glyph.height != 0:
                loglist.append((f'Advance height of {str(glyph.height)} removed for {glyph.name}', "V"))
                glyph.height = 0
                heightchanges += 1
            lib = glyph.lib
            if "public.verticalOrigin" in lib:
                del lib["public.verticalOrigin"]
                vertorichanges += 1
    if heightchanges: loglist.append((f"{str(heightchanges)} advance heights removed from glyphs", "I"))
    if vertorichanges: loglist.append((f"{str(vertorichanges)} public.verticalOrigins removed from lib in glyphs", "I"))

    # Write ufo out
    ufopath = os.path.join(masterdir, fontname + ".ufo")
    if args.preservefea:  # Move features.fea out of the ufo so that it can be restored afterward
        origfea = os.path.join(ufopath, "features.fea")
        hiddenfea = os.path.join(masterdir, fontname + "features.tmp")
        if os.path.exists(origfea):
            loglist.append((f'Renaming {origfea} to {hiddenfea}', "I"))
            os.rename(origfea, hiddenfea)
        else:
            loglist.append((f"{origfea} does not exists so can't be restored", "E"))
            origfea = None
    loglist.append(("Writing out " + ufopath, "P"))
    if os.path.exists(ufopath): shutil.rmtree(ufopath)
    ufo.save(ufopath)
    if args.preservefea and origfea:
        loglist.append((f'Renaming {hiddenfea} back to {origfea}', "I"))
        os.rename(hiddenfea, origfea)

    # Now correct the newly-written fontinfo.plist with changes that can't be made via glyphsLib
    if not args.nofixes:
        fontinfo = silfont.ufo.Uplist(font=None, dirn=ufopath, filen="fontinfo.plist")
        changes = False
        for key in ("guidelines", "postscriptBlueValues", "postscriptFamilyBlues", "postscriptFamilyOtherBlues",
                    "postscriptOtherBlues"):
            if key in fontinfo and fontinfo.getval(key) == []:
                fontinfo.remove(key)
                changes = True
                logchange(loglist, " empty list deleted", key, None, [])
        if changes:
            # Create outparams.  Just need any valid values, since font will need normalizing later
            params = args.paramsobj
            paramset = params.sets["main"]
            outparams = {"attribOrders": {}}
            for parn in params.classes["outparams"]: outparams[parn] = paramset[parn]
            loglist.append(("Writing updated fontinfo.plist", "I"))
            silfont.ufo.writeXMLobject(fontinfo, params=outparams, dirn=ufopath, filen="fontinfo.plist", exists=True,
                                       fobject=True)
    return loglist

def logchange(loglist, logmess, key, old, new):
    oldstr = str(old) if len(str(old)) < 22 else str(old)[0:20] + "..."
    newstr = str(new) if len(str(new)) < 22 else str(new)[0:20] + "..."
    logmess = key + logmess
    if old is None:
        logmess = logmess + " New value: " + newstr
    else:
        if new is None:
            logmess = logmess + " Old value: " + oldstr
        else:
            logmess = logmess + " Old value: " + oldstr + ", new value: " + newstr
    loglist.append((logmess, "I"))
    # Extra verbose logging
    if len(str(old)) > 21 :
        loglist.append(("Full old value: " + str(old), "V"))
    if len(str(new)) > 21 :
        loglist.append(("Full new value: " + str(new), "V"))
    loglist.append(("Types: Old - " + str(type(old)) + ", New - " + str(type(new)), "V"))

def cmd(): execute(None, doit, argspec)
if __name__ == "__main__": cmd()
