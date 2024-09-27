# Pysilfont parameters

In addition to normal command-line arguments (see [scripts.md](scripts.md) and [Standard Command-line Options](docs.md#standard-command-line-options)), Pysilfont supports many other parameters that can be changed either on the command-line or by settings in a config file.  For UFO fonts there is also an option to set parameters within the UFO.

See [List of Parameters](#list-of-parameters) for a full list, which includes the default values for each parameter.

# Setting parameters

Parameters can be set in multiple ways
1. Default values are set by the core.py Pysilfont module - see [List of Parameters](#list-of-parameters)
1. Standard values for a project can be set in a pysilfont.cfg [config file](#config-file)
1. For UFO fonts, font-specific values can be set within the [lib.plist](#lib-plist) file
1. On the command line \- see next section

Values set by later methods override those set by earlier methods.

(Scripts can also change some values, but they would normally be written to avoid overwriting command-line values)

## Command line

For script users, parameters can be set on the command line with -p, for example:
```
psfnormalize test.ufo -p scrlevel=V -p indentIncr="    "
```
would increase the screen reporting level to Verbose and change the xml indent from 2 spaces to 4 spaces.

If a parameter has multiple values, enter them separated with commas but no spaces, eg:

`-p glifElemOrder=unicode,advance,note,image,guideline,anchor,outline,lib`



## Config file
If pysilfont.cfg exists in the same directory as the first file specified on the command line (typically the font being processed) then parameters will be read from there.

The format is a [ConfigParser](https://docs.python.org/2/library/configparser.html) config file, which is similar structure to a Windows .ini file.

Lines starting with # are ignored, as are any blank lines.

Example:
```
# Config file

[logging]
scrlevel: I

[outparams]
indentIncr: '  '
glifElemOrder: unicode,advance,note,image,guideline,anchor,outline,lib
```
The section headers are backups, logging, outparams and ufometadata.

In a font project with multiple UFO fonts in the same folder, all would use a single config file.

## lib plist

If, with a UFO font, org.sil.pysilfontparams exists in lib.plist, parameter values held in an array will be processed, eg
```
<key>org.sil.pysilfontparams</key>
<array>
  <indentIncr>\t</indentIncr>  
  <glifElemOrder>lib,unicode,note,image,guideline,anchor,outline,advance</glifElemOrder>
</array>
```
Currently only font output parameters can be changed via lib.plist

## List of parameters

| Parameter | Default | Description | Notes |
| -------- | -------- | --------------------------------------------- | ------------------------------------- |
| **Reporting** | | | To change within a script use <br>`logger.<parameter> = <value>`|
| scrlevel | P | Reporting level to screen. See [Reporting](docs.md#reporting) for more details | -q, --quiet option sets this to S |
| loglevel | W | Reporting level to log file |  |
| **Backup** (font scripts only) |  |  |  |  
| backup | True | Backup font to subdirectory | If the original font is being updated, make a backup first |
| backupdir | backups | Sub-directory name for backups |  |
| backupkeep |  5 | Number of backups to keep |  |
| **Output** (UFO scripts only) |  |  | To change in a script use <br>`font.outparams[<parameter>] = <value>` |
| indentFirst | 2 spaces | Increment for first level in xml |  |
| indentIncr | 2 spaces | Amount to increment xml indents |  |
| indentML | False | Indent multi-line text items | (indenting really messes some things up!) |
| plistIndentFirst | Empty string | Different initial indent for plists | (dict is commonly not indented) |
| sortDicts | True | sort all plist dicts |  |
| precision | 6 | decimal precision |  |
| updateTimestamps | True | Update font timestamps if other changes occur | Controls handling of the `openTypeHeadCreated` field in UFO fontinfo. |
| renameGlifs | True | Name glifs with standard algorithm |  |
| UFOversion | (existing) |  | Defaults to the version of the UFO when opened |
| format1Glifs | False| Force output of format 1 glifs | Includes UFO2-style anchors; for use with FontForge |
| floatAttribs | (list of attributes in the spec that hold numbers and are handled as float) | Used to know if precision needs setting. | May need items adding for lib data |
| intAttribs | (list of attributes in the spec that hold numbers and handled as integer) |  | May need items adding for lib data |
| glifElemOrder | (list of elements in the order defined in spec) | Order for outputting elements in a glif |  |
| attribOrders | (list of attribute orders defined in spec) | Order for outputting attributes in an element.  One list per element type | When setting this, the parameter name is `attribOrders.<element type>`.  Currently only used with attribOrders.glif |
| **ufometadata** (ufo scripts only) |  |  |  |
| checkfix | check | Metadata check & fix action | If set to "fix", some values updated (or deleted).  Set to "none" for no metadata checking |
| More may be added... | |

## Within basic scripts
### Accessing values
If you need to access values of parameters or to see what values have been set on the command line you can look at:
- args.paramsobj.sets[“main”]
  - This is a dictionary containing the values for **all** parameters listed above.  Where they have been specified in a config file, or overwritten on the command line, those values will be used.  Otherwise the default values listed above will be used
- args.params
  - This is a dictionary containing any parameters specified on the command line with -p.

Within a UFO Ufont object, use font.paramset, since this will include any updates as a result parameter values set in lib.plist.

In addition to the parameters in the table above, two more read-only parameters can be accessed by scripts - “version” and “copyright” - which give the pysilfont library version and copyright info, based on values in core.py headers.

### Updating values
Currently only values under Output can be set via scripts, since Backup and Reporting parameters are processed by execute() prior to the script being called.  For example:
```python
font.paramset[“precision”] = 9
```
would set the precision parameter to 9.

Note that, whilst reporting _parameters_ can’t be set in scripts, _reporting levels_ can be updated by setting values in the args.logger() object, eg `args.logger.scrlevel = “W”.`

# Technical

_Note the details below are probably not needed just for developing scripts..._

## Basics
The default for all parameters are set in core.py as part of the parameters() object.  Those for **all** pysilfont library modules need to be defined in core.py so that execute() can process command-line arguments without needing information from other modules.

Parameters are passed to scripts via a parameters() object as args.paramsobj.  This contains several parameter sets, with “main” being the standard one for scripts to use since that contains the default parameters updated with those (if any) from the config file then the same for any command-line values.

Parameters can be accessed from the parameter set by parameter name, eg paramsobj.sets[“main”][“loglevel”].

Although parameters are split into classes (eg backup, logging), parameter names need to be unique across all groups to allow simple access by name.

If logging set set to I or V, changes to parameter values (eg config file values updating default values) are logged.

There should only be ever a single parameters() object used by a script.

## Paramobj
In addition to the paramsets, the paramobj also contains
- classes:
  - A dictionary keyed on class, returning a list of parameter names in that class
- paramclass:
  - A dictionary keyed on parameter name, returning the class of that parameter
- lcase:
  - A dictionary keyed on lowercase version of parameter name returning the parameter name
- type:
  - A dictionary keyed on parameter name, returning the type of that parameter (eg str, boolean, list)
- listtype:
  - For list parameters, a dictionary keyed on parameter name, returning the type of that parameters in the list
- logger:
  - The logger object for the script

## Parameter sets
These serve two purposes:
1. To allow multiple set of parameter values to be used - eg two different fonts might have different values in the lib.plist
1. To keep track of the original sets of parameters (“default”, “config file” and “command line”) if needed.  See UFO specific for an example of this need.

Additional sets can be added with addset() and one set can be updated with values from another using updatewith(), for example, to create the “main” set, the following code is used:
```
params.addset("main",copyset = "default")       # Make a copy of the default set
params.sets["main"].updatewith("config file")   # Update with config file values
params.sets["main"].updatewith("command line")  # Update with command-line values
```
## UFO-specific
The parameter set relevant to a UFO font can be accessed by font.paramset, so font.paramset[“loglevel"] would access the loglevel.

In ufo.py there is code to cope with two complications:
1. If a script is opening multiple fonts, in they could have different lib.plist values so font-specific parameter sets are needed
1. The parameters passed to ufo.py include the “main” set which has already had command-line parameters applied.   Any in lib.plist also need to be applied, but can’t simply be applied to “main” since command-line parameters should take precedence over lib.plist ones

To ensure unique names, the parameter sets are created using the full path name of the UFO.  Then font.paramset is set to point to this, so scripts do not need to know the underlying set name.

To apply the parameter sets updates in the correct order, ufo.py does:

1. Create a new paramset from any lib parameters present
1. Update this with any command line parameters
1. Create the paramset for the font by copying the “main” paramset
1. Update this with the lib paramset (which has already been updated with command line values in step 2)

## Adding another parameter or class
If there was a need to add another parameter or class, all that should be needed is to add that to defparams in the \_\_init\_\_() of parameters() in core.py.  Ensure the new parameter is case-insensitively unique.

If a class was Ufont-specific and needed to be supported within lib.plist, then ufo.py would also need updating to handle that similarly to how it now handles outparams and ufometadata.
