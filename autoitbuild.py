from __future__ import print_function
import sublime, sublime_plugin
import subprocess
import os

# The autoitbuild command is called as target by AutoIt.sublime-build
class autoitbuild(sublime_plugin.WindowCommand):
	def run(self):
		filepath = self.window.active_view().file_name()
		autoit_exe_path = \
			sublime.load_settings("AutoIt.sublime-settings").get("AutoItExePath")
		cmd = [autoit_exe_path, "/ErrorStdOut", filepath]
		self.window.run_command("exec", {"cmd": cmd})

class autoitcompile(sublime_plugin.WindowCommand):
	def run(self):
		filepath = self.window.active_view().file_name()
		autoit_compiler_path = \
			sublime.load_settings("AutoIt.sublime-settings").get("AutoItCompilerPath")
		cmd = [autoit_compiler_path, "/in", filepath]
		self.window.run_command("exec", {"cmd": cmd})

class autoittidy(sublime_plugin.WindowCommand):
	def run(self):
		self.window.run_command("save")
		filepath = self.window.active_view().file_name()
		tidy_exe_path = \
			sublime.load_settings("AutoIt.sublime-settings").get("TidyExePath")
		tidycmd = [tidy_exe_path, filepath]
		try:
			tidyprocess = subprocess.Popen(
				tidycmd, shell=True, stdout=subprocess.PIPE,
				stderr=subprocess.STDOUT, universal_newlines=True
			)
			tidyoutput = tidyprocess.communicate()[0].rstrip()
			tidyoutputskipfirstline = "".join(tidyoutput.splitlines(True)[1:])
			self.window.run_command("revert")
			print("------------ Beginning AutoIt Tidy ------------")
			print(tidyoutput)
			if "Tidy Error" in tidyoutput:
				sublime.active_window().run_command("show_panel", {"panel": "console"})
				sublime.status_message("### Tidy Errors : Please See Console")
			else:
				sublime.status_message(tidyoutputskipfirstline)
		except Exception as e:
			sublime.active_window().run_command("show_panel", {"panel": "console"})
			print("------------ ERROR: Python exception trying to run Tidy ------------")
			print("TidyCmd was: " + " ".join(tidycmd))
			print("Error " + str(e))
			sublime.status_message("### EXCEPTION: " + str(e))

class autoitincludehelper(sublime_plugin.WindowCommand):
	def run(self):
		self.window.run_command("save")

		filepath = self.window.active_view().file_name()
		autoit_exe_path = \
			sublime.load_settings("AutoIt.sublime-settings").get("AutoItExePath")
		autoit_include_folder = os.path.dirname(autoit_exe_path) + "\\Include"

		include_helper_path = \
			sublime.load_settings("AutoIt.sublime-settings").get("IncludeHelperAU3Path")
		if include_helper_path is None:
			include_helper_path = \
				"{PACKAGE_PATH}\\AutoItPlysSublime\\Include_Helper.au3"
		include_helper_path = include_helper_path.replace(
			"{PACKAGE_PATH}", sublime.packages_path()
		)

		autoit_include_cmd = [autoit_exe_path, include_helper_path, filepath,
			autoit_include_folder]

		try:
			subprocess.call(autoit_include_cmd)
			self.window.run_command("revert")
			sublime.status_message("AutoIt IncludeHelper Finished")
		except Exception as e:
			sublime.active_window().run_command("show_panel", {"panel": "console"})
			print("------------ ERROR: Python exception trying to run following command ------------")
			print(autoit_include_cmd)
			print("Error " + str(e))

class autoitwindowinfo(sublime_plugin.WindowCommand):
	def run(self):
		autoit_info_path = \
			sublime.load_settings("AutoIt.sublime-settings").get("AutoItInfoPath")

		try:
			os.startfile(autoit_info_path)
		except Exception as e:
			sublime.active_window().run_command("show_panel", {"panel": "console"})
			print("------------ ERROR: Python exception trying to run following command ------------")
			print("Error " + str(e))

class autoithelp(sublime_plugin.WindowCommand):
	def run(self):
		autoit_help_path = \
			sublime.load_settings("AutoIt.sublime-settings").get("AutoItHelpPath")

		try:
			os.startfile(autoit_help_path)
		except Exception as e:
			sublime.active_window().run_command("show_panel", {"panel": "console"})
			print("------------ ERROR: Python exception trying to run following command ------------")
			print("Error " + str(e))

class autoitgetpaths(sublime_plugin.WindowCommand):
	def __init__(self, window):
		super().__init__(window)

		import winreg
		def get_au3_exe_folder(bitness):
			registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, \
				r"SOFTWARE\AutoIt v3\AutoIt", 0, \
				winreg.KEY_READ | winreg.KEY_WOW64_32KEY)
			value, regtype = winreg.QueryValueEx(registry_key, "InstallDir")
			winreg.CloseKey(registry_key)
			return value
		try:
			au3_exe_folder = get_au3_exe_folder(winreg.KEY_WOW64_32KEY)
		except WindowsError as e:
			try:
				au3_exe_folder = get_au3_exe_folder(winreg.KEY_WOW64_64KEY)
			except WindowsError as e:
				sublime.active_window().run_command("show_panel", {"panel": "console"})
				print("------------ ERROR: Python exception trying to run following command ------------")
				print("Error " + str(e))
				return

		import json
		default_settings_path = sublime.packages_path() + \
			"\\AutoItPlysSublime\\AutoIt.sublime-settings"
		with open(default_settings_path) as f:
			settings = json.load(f)
		if not settings.get("AutoItExePath"):
			settings["AutoItExePath"] = au3_exe_folder + "\\AutoIt3.exe"
		if not settings.get("AutoItCompilerPath"):
			settings["AutoItCompilerPath"] = \
				au3_exe_folder + "\\Aut2Exe\\Aut2exe.exe"
		if not settings.get("TidyExePath"):
			settings["TidyExePath"] = au3_exe_folder + "\\SciTE\\Tidy\\Tidy.exe"
		if not settings.get("AutoItInfoPath"):
			import platform
			is_os_64bit = platform.machine().endswith('64')
			suffix = "_x64" if is_os_64bit else ""
			settings["AutoItInfoPath"] = \
				au3_exe_folder + "\\Au3Info" + suffix + ".exe"
		if not settings.get("AutoItHelpPath"):
			settings["AutoItHelpPath"] = au3_exe_folder + "\\AutoIt3Help.exe"
		with open(default_settings_path, "w") as f:
			json.dump(settings, f, indent="\t")

	def run(self):
		pass
