from __future__ import print_function
import os
import subprocess
import sublime
import sublime_plugin

PACKAGE_FOLDER = os.path.abspath(os.path.dirname(__file__))


def autoit_settings():
	return sublime.load_settings("AutoIt.sublime-settings")


def install():
	try:
		exe_folder = autoit_exe_folder()
	except WindowsError as e:
		sublime.active_window().run_command(
			"show_panel", {"panel": "console"}
		)
		print("[ERROR: Python exception trying to run following command]")
		print("Error " + str(e))
		return

	import json
	default_settings_path = PACKAGE_FOLDER + "\\AutoIt.sublime-settings"
	with open(default_settings_path) as f:
		settings = json.load(f)
	settings["AutoItExePath"] = exe_folder + "\\AutoIt3.exe"
	settings["AutoItCompilerPath"] = exe_folder + "\\Aut2Exe\\Aut2exe.exe"
	settings["TidyExePath"] = exe_folder + "\\SciTE\\Tidy\\Tidy.exe"
	import platform
	is_os_64bit = platform.machine().endswith('64')
	suffix = "_x64" if is_os_64bit else ""
	settings["AutoItInfoPath"] = \
		exe_folder + "\\Au3Info" + suffix + ".exe"
	settings["AutoItHelpPath"] = exe_folder + "\\AutoIt3Help.exe"
	settings["Status"] = "installed"
	with open(default_settings_path, "w") as f:
		json.dump(settings, f, indent="\t")


def autoit_exe_folder():
	import winreg

	def get_in_branch(branch_bitness):
		registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
			r"SOFTWARE\AutoIt v3\AutoIt", 0,
			winreg.KEY_READ | branch_bitness)
		value, regtype = winreg.QueryValueEx(registry_key, "InstallDir")
		winreg.CloseKey(registry_key)
		return value

	try:
		return get_in_branch(winreg.KEY_WOW64_32KEY)
	except WindowsError:
		return get_in_branch(winreg.KEY_WOW64_64KEY)


# The autoitbuild command is called as target by AutoIt.sublime-build
class AutoitBuildCommand(sublime_plugin.WindowCommand):
	
	processor_path_key = "AutoItExePath"
	file_regex = \
		r'[^"]*"?([a-zA-Z]:\\.+?\.au3)"? \(([0-9]*)()\) : ==> (.*?)\.: ?$'
	syntax = "AutoIt Build.sublime-syntax"
	
	def run(self):
		processor_path = autoit_settings().get(self.processor_path_key)
		filepath = self.window.active_view().file_name() or " "
		cmd = [processor_path, "/ErrorStdOut", filepath]
		self.window.run_command("exec", {
			"cmd": cmd, "file_regex": self.file_regex, "syntax" : self.syntax
		})


class AutoitCompileCommand(AutoitBuildCommand):

	processor_path_key = "AutoItCompilerPath"
	file_regex = ""
	syntax = ""


class AutoitTidyCommand(sublime_plugin.WindowCommand):

	def run(self):
		self.window.run_command("save")
		filepath = self.window.active_view().file_name() or " "
		tidy_exe_path = autoit_settings().get("TidyExePath")
		tidycmd = [tidy_exe_path, filepath]
		try:
			tidyprocess = subprocess.Popen(
				tidycmd, shell=True, stdout=subprocess.PIPE,
				stderr=subprocess.STDOUT, universal_newlines=True
			)
			tidyoutput = tidyprocess.communicate()[0].rstrip()
			tidyoutputskipfirstline = "".join(tidyoutput.splitlines(True)[1:])
			self.window.run_command("revert")
			print("[Beginning AutoIt Tidy]")
			print(tidyoutput)
			if "Tidy Error" in tidyoutput:
				sublime.active_window().run_command(
					"show_panel", {"panel": "console"}
				)
				sublime.status_message("### Tidy Errors : Please See Console")
			else:
				sublime.status_message(tidyoutputskipfirstline)
		except Exception as e:
			sublime.active_window().run_command(
				"show_panel", {"panel": "console"}
			)
			print("[ERROR: Python exception trying to run Tidy]")
			print("TidyCmd was: " + " ".join(tidycmd))
			print("Error " + str(e))
			sublime.status_message("### EXCEPTION: " + str(e))


class AutoitIncludehelperCommand(sublime_plugin.WindowCommand):

	def run(self):
		self.window.run_command("save")

		filepath = self.window.active_view().file_name() or " "
		settings = autoit_settings()
		autoit_exe_path = settings.get("AutoItExePath")
		autoit_include_folder = os.path.dirname(autoit_exe_path) + "\\Include"

		include_helper_path = settings.get("IncludeHelperAU3Path")
		if include_helper_path is None:
			include_helper_path = PACKAGE_FOLDER + "\\Include_Helper.au3"
		else:
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
			sublime.active_window().run_command(
				"show_panel", {"panel": "console"}
			)
			print("[ERROR: Python exception trying to run following command]")
			print(autoit_include_cmd)
			print("Error " + str(e))


class AutoitWindowinfoCommand(sublime_plugin.WindowCommand):

	def run(self):
		autoit_info_path = autoit_settings().get("AutoItInfoPath")

		try:
			os.startfile(autoit_info_path)
		except Exception as e:
			sublime.active_window().run_command(
				"show_panel", {"panel": "console"}
			)
			print("[ERROR: Python exception trying to run following command]")
			print("Error " + str(e))


class AutoitHelpCommand(sublime_plugin.WindowCommand):

	def run(self):
		self.autoit_help_path = autoit_settings().get("AutoItHelpPath")

		try:
			subprocess.Popen(self.make_args())
		except Exception as e:
			sublime.active_window().run_command(
				"show_panel", {"panel": "console"}
			)
			print("[ERROR: Python exception trying to run following command]")
			print("Error " + str(e))

	def make_args(self):
		return [self.autoit_help_path]


class AutoitContexthelpCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		self.autoit_help_path = autoit_settings().get("AutoItHelpPath")
		for region in self.view.sel():
			location = False
			location = self.view.word(region) if region.empty() else region
			if location and not location.empty():
				query = self.view.substr(location)

				try:
					subprocess.Popen(self.make_args(query))
				except Exception as e:
					sublime.active_window().run_command(
						"show_panel", {"panel": "console"}
					)
					print("[ERROR: Python exception trying to run "
						"following command]")
					print("Error " + str(e))

	def make_args(self, query):
		return [self.autoit_help_path, query]


if autoit_settings().get("Status") != "installed":
	install()
