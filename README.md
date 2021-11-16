# AutoIt Plys package for Sublime Text
[AutoIt language](https://www.autoitscript.com/site/autoit/) and [Plys dialect](https://github.com/NSUSpray/Plys) package for [Sublime Text](https://www.sublimetext.com/) including syntax highlighting, auto-completions, build systems for run and compile, context help, “goto” feature, comments toggling, Tidy and Include Helper command.

## Requirements
* [AutoIt](https://www.autoitscript.com/site/autoit/downloads/) (minimum)
* [Tidy or AutoIt Script Editor full set](https://www.autoitscript.com/site/autoit-script-editor/downloads/) for Tidy feature (optional)
* [AutoIt Plys translator](https://github.com/NSUSpray/Plys) for Plys language multiset features (optional)

## Installation
* Package control method (with autoupdate):
	1. open Sublime Text
	1. go to Command Palette (<kbd>Ctrl+Shift+P</kbd>) and enter “Add Repository”
	1. enter this repository address `https://github.com/NSUSpray/AutoItPlysSublime`
	1. in Command Palette again enter “Install Package”
	1. type “AutoItPlysSublime”, select appropriate item and press Enter
* Manual method (without autoupdate):
	1. clone this repository or download ZIP with source files
	1. extract package folder to the Sublime packages folder (Menu: `Preferences > Browse Packages…`)
	1. remove “-master” suffix from folder name

## Key Bindings
If you have the default Sublime keybindings intact, then:
* <kbd>Ctrl+B</kbd> will run/compile/translate the current file (with AutoIt3.exe, Aut2Exe.exe or plys.au3)
* <kbd>Ctrl+Shift+B</kbd> will change the build mode (between run/compile/translate)
* <kbd>F12</kbd> will go to definition of the function by its name under cursor
* <kbd>Ctrl+R</kbd> will show list of the all functions in current file
* <kbd>Alt</kbd><kbd>T</kbd><kbd>I</kbd><kbd>I</kbd> will invoke Include Helper on the current file
* <kbd>Alt</kbd><kbd>T</kbd><kbd>I</kbd><kbd>F</kbd> will invoke AutoIt Window Info
* <kbd>Alt</kbd><kbd>T</kbd><kbd>I</kbd><kbd>H</kbd> will invoke AutoIt Help
* <kbd>Alt</kbd><kbd>T</kbd><kbd>I</kbd><kbd>P</kbd> will invoke Plys Help
* <kbd>Alt</kbd><kbd>T</kbd><kbd>I</kbd><kbd>T</kbd> will invoke Tidy on the current file (if it’s installed).
* <kbd>F1</kbd> will take you to AutoIt Help for word under cursor (context help)

## Advanced Configuration
For the build systems and Tidy command, if you have a non-default installation you will need to set your specific path to AutoIt3.exe, Aut2Exe.exe, and Tidy.exe in a file named AutoIt.sublime-settings in your User folder. You can access the settings file from Menu `Preferences > Package Settings > AutoIt Plys > Settings`. You should make a copy of left side panel at right side panel.

## Credits
* Syntax rules: http://sublime-text-community-packages.googlecode.com/svn/pages/AutoIt.html
* Snippets: http://www.autoitscript.com/forum/topic/148016-sublimetext/page-3#entry1080276
* Include Helper AZJIO: http://www.autoitscript.com/forum/topic/130468-constants-helper/#entry908064
