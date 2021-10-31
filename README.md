# AutoItPlysSublime - Package for Sublime Text 2–4
AutoIt language and Plys dialect package for Sublime Text including syntax highlighting, comments toggling, auto-completions, build systems for run and compile, Tidy command, Include Helper command.

## Package Installation
* Manual method:
	1. download ZIP from this repository
	2. extract the files to Sublime packages folder (Menu: `Preferences > Browse Packages…`)
* Package control method:
	1. open Sublime Text
	2. go to Command Palette (<kbd>Ctrl+Shift+P</kbd>) and enter “Add Repository”
	3. enter this repository address `https://github.com/NSUSpray/AutoItPlysSublime`
	4. in Command Palette again enter “Install Package”
	5. type “AutoItPlysSublime”, select appropriate item and press Enter

## Key Bindings
If you have the default Sublime keybindings intact, then:
* <kbd>Ctrl+B</kbd> will run the current file (with AutoIt3.exe)
* <kbd>Ctrl+Shift+B</kbd> will compile the current file (with Aut2Exe.exe)
* <kbd>Alt+T</kbd><kbd>T</kbd> will invoke Tidy on the current file (with Tidy.exe).
* <kbd>Alt+T</kbd><kbd>I</kbd> will invoke Include Helper on the current file.
* <kbd>Alt+T</kbd><kbd>F</kbd> will invoke AutoIt Window Info.
* <kbd>Alt+T</kbd><kbd>H</kbd> will invoke AutoIt Help.

## Advanced Configuration
For the build systems and Tidy command, if you have a non-default installation you will need to set your specific path to AutoIt3.exe, Aut2Exe.exe, and Tidy.exe in a file named AutoIt.sublime-settings in your User folder. You can access the settings file from Menu `Preferences > Package Settings > AutoIt`. You should make a copy of `AutoIt Settings - Default` at `AutoIt Settings - User` since then your settings file in your User folder will not get overwritten when this package updates.

## Goto-documentation Integration
Instructions on how to configure goto-documentation plugin for AutoIt (F1 Hotkey will take you to documentation for word under cursor):
* https://github.com/AutoIt/AutoItScript/blob/master/goto-documentation_instructions.md

## Credits
* Syntax rules: http://sublime-text-community-packages.googlecode.com/svn/pages/AutoIt.html
* Snippets: http://www.autoitscript.com/forum/topic/148016-sublimetext/page-3#entry1080276
* Include Helper AZJIO: http://www.autoitscript.com/forum/topic/130468-constants-helper/#entry908064
