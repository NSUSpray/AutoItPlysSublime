# AutoItPlysSublime – Package for Sublime Text
AutoIt language and Plys dialect package for Sublime Text including syntax highlighting, comments toggling, auto-completions, build systems for run and compile, context help, Tidy and Include Helper command.

## Package Installation
* Manual method (without autoupdate):
	1. download ZIP from this repository
	1. extract the files to Sublime packages folder (Menu: `Preferences > Browse Packages…`)
	1. remove “-master” suffix from folder name
* Package control method (with autoupdate):
	1. open Sublime Text
	1. go to Command Palette (<kbd>Ctrl+Shift+P</kbd>) and enter “Add Repository”
	1. enter this repository address `https://github.com/NSUSpray/AutoItPlysSublime`
	1. in Command Palette again enter “Install Package”
	1. type “AutoItPlysSublime”, select appropriate item and press Enter

## Key Bindings
If you have the default Sublime keybindings intact, then:
* <kbd>Ctrl+B</kbd> will run the current file (with AutoIt3.exe)
* <kbd>Ctrl+Shift+B</kbd> will compile the current file (with Aut2Exe.exe)
* <kbd>Alt+T</kbd><kbd>I</kbd><kbd>I</kbd> will invoke Include Helper on the current file.
* <kbd>Alt+T</kbd><kbd>I</kbd><kbd>F</kbd> will invoke AutoIt Window Info.
* <kbd>Alt+T</kbd><kbd>I</kbd><kbd>H</kbd> will invoke AutoIt Help.
* <kbd>Alt+T</kbd><kbd>I</kbd><kbd>T</kbd> will invoke Tidy on the current file (only if SciTE4AutoIt is installed).
* <kbd>F1</kbd> will take you to AutoIt Help for word under cursor.

## Advanced Configuration
For the build systems and Tidy command, if you have a non-default installation you will need to set your specific path to AutoIt3.exe, Aut2Exe.exe, and Tidy.exe in a file named AutoIt.sublime-settings in your User folder. You can access the settings file from Menu `Preferences > Package Settings > AutoIt > Settings`. You should make a copy of left side panel at right side panel.

## Credits
* Syntax rules: http://sublime-text-community-packages.googlecode.com/svn/pages/AutoIt.html
* Snippets: http://www.autoitscript.com/forum/topic/148016-sublimetext/page-3#entry1080276
* Include Helper AZJIO: http://www.autoitscript.com/forum/topic/130468-constants-helper/#entry908064
