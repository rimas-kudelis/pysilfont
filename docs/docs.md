# Pysilfont - utilities for font development

Pysilfont is a collection of tools to support font development, with an emphasis on [UFO](#ufo-support-in-pysilfont)-based workflows.

In addition to the UFO utilities, there is also support for testing using [FTML](#font-test-markup-language) and [Composite Definitions](#composite definitions).

Some scripts are written specifically to fit in with the approaches recommended in [Font Development Best Practices](https://silnrsi.github.io/FDBP/en-US/index.html)

# Documentation

Documentation is held in the following documents:

- docs.md: This document - the main document for users
- [scripts.md](scripts.md): User documentation for all command-line tools and other scripts
- [technical.md](technical.md): Technical details for those wanting write scripts or other development tasks
- Other sub-documents, with links from the above

Installation instructions are in [README.md](../README.md)

# Scripts and commands
Many Pysilfont scripts are installed to be used as command-line tools, and these are all listed, with usage instructions, in [scripts.md](scripts.md).  This also has details of some other example python scripts.

All scripts work using a standard framework designed to give users a consistent interface across scripts, and common features of these scripts are described in the following sections, so the documentation below needs to be read in conjunction with that in [scripts.md](scripts.md).

## Standard command line options

Nearly all scripts support these:

- `-h, --help`
  - Basic usage help for the command
- `-d, --defaults`
  - Display -h info with added info about default values
- `-q, --quiet`
  - Quiet mode - only display errors.  See reporting below
- `-l LOG, --log LOG`
  - Log file name (if not using default name)
- `-p PARAMS, --params PARAMS`
  - Other [parameters](#parameters)

The individual script documentation in scripts.md indicates if some don't apply for a particular script

## Default values

Most scripts have defaults for file names and other arguments - except for the main file the script is running against.

### Font/file name defaults

Once the initial input file (eg input font) has been given, most other font and file names will have defaults based on those.

This applies to other input font names, output font names, input file names and output file names and is done to minimise retyping repeated information like the path the files reside in.   For example, simply using:

```
psfsetpsnames path/font.ufo
```

will:

- open (and update)	`/path/font.ufo`
- backup the font to `/path/backups/font.ufo.nnn~`
- read its input from `/path/font_psnames.csv`
- write its log to `/path/font_psnames.log`

If only part of a file name is supplied, other parts will default. If only "test" is supplied for the output font name, the font would be output to `/path/test.ufo`.

If a full file name is supplied, but no path, the the current working directory will be used, so if “test.ufo” is supplied it won’t have `/path/` added.

### Other defaults

Other parameters will just have standard default values.

### Displaying defaults for a command

Use the `-d` option to see what defaults are for a given command. For example,

```
psfsetpsnames -d
```

will output its help text with the following appended:

```
Defaults for parameters/options

  Font/file names
    -i                  _PSnames.csv
    -l                  _PSnames.log
```

If the default value starts with “\_” (as with \_PSnames.csv above) then the input file name will be prepended to the default value; otherwise just the default value will be used.

## Reporting
Most scripts support standardised reporting, both to screen and a log file, with different levels of reporting set for each via loglevel and scrlevel parameters which can be set to one of:
- E	Errors
- P	Progress - Reports basic progress messages and all errors
- W	Warning - As P but with warning messages as well
- I	Info - As W but with information messages as well
- V	Verbose - even more messages!

For most scripts these default to W for loglevel and P for scrlevel and can be set using -p (eg to set screen reporting to verbose use -p scrlevel=v).

-q --quiet sets quiet mode where the scrlevel is set to E (and some additional messages suppressed) so only errors are reported on screen.

## Backups for fonts

If the output font name is the same as the input font name (which is the default behaviour for most scripts), then the original font is backed up prior to outputting the revised font.

By default, the last 5 copies of backups are kept in a sub-directory called “backups”.  These defaults can be changed using the following parameters:

- `backup` - if set to 0, no backups are done
- `backupdir` - alternative directory for backups
- `backupkeep` - number of backups to keep

# Parameters

There are many parameters that can be set to change the behaviour of scripts, either on the command line (using -p)  or via a config file.

To set a parameter on the command line, use -p <param name>=<param value>, eg
```
UFOconvert font.ufo -p backupkeep=3
```
-p can be used multiple times on a single command.

For a full list of parameters and how to set them via a config file (or in a UFO font) see [parameters.md](parameters.md).
# UFO support in Pysilfont
With some limitations, all UFO scripts in Pysilfont should work with UFO2 or UFO3 source files - and can convert from one format to the other.

In addition most scripts will output in a normalized form, designed to work with source control systems. Most aspects of the normalization can be set by parameters, so projects are not forced to use Pysilfont’s default normalization.

The simplest script is psfnormalize, which will normalize a UFO (and optionally convert between UFO 2 and UFO3 if -v is used to specify the alternative version)

Note that other scripts also normalize, so psfnormalize is usually only needed after fonts have been processed by external font tools.

## Normalization
Default normalization behaviours include:
- XML formatting
- - Use 2 spaces as indents
- - Don’t indent the <dict> for plists
- - Sort all <dicts>s in ascending key order
- - Where values can be “integer or float”, store integer values as <integer>
- - Limit <real> precision to 6
- glif file names - use the UFO 3 suggested algorithm
- order glif elements and attributes in the order they are described in the UFO spec

Most of the above can be overridden by parameters

## Known limitations
The following are known limitations that will be addressed in the future:
- UFO 3 specific folders (data and images) are not copied
- Converting from UFO 3 to UFO 2 only handles data that has a place in UFO 2, but does include converting UFO 3 anchors to the standard way of handling them in UFO 2
- If a project uses non-standard files within the UFO folder, they are deleted

# Font Test Markup Language

Font Test Markup Language (FTML) is a file format for specifying the content and structure of font test data. It is designed to support complex test data, such as strings with specific language tags or data that should presented with certain font features activated. It also allows for indication of what portions of test data are in focus and which are only present to provide context.

FTML is described in the [FTML github project](https://github.com/silnrsi/ftml).

Pysilfont includes some python scripts for working with FTML, and a python library, ftml.py, so that new scripts can be developed to read and write FTML files.

# Composite definitions

Pysilfont includes tools for automatically adding composite glyphs to fonts.  The syntax used for composite definitions is a subset of that used by RoboFont plus some extensions - see [Composite Tools](https://silnrsi.github.io/FDBP/en-US/Composite_Tools.html) in the Font Development Best Practices documentation for more details.

The current tools (psfbuildcomp, psfcomp2xml and psfxml2comp) are documented in [scripts.md](scripts.md).

The tools are based on a python module, cd.py.

# Contributing to the project

Pysilfont is developed and maintained by SIL International’s [Non-Roman Script Initiative team](http://scripts.sil.org), though contributions from anyone are welcome. Pysilfont is copyright (c) 2014-2017 [SIL International](http://www.sil.org) and licensed under the [MIT license](http://en.wikipedia.org/wiki/MIT_License). The project is hosted at [https://github.com/silnrsi/pysilfont](https://github.com/silnrsi/pysilfont).