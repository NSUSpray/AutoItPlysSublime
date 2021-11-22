from __future__ import print_function
import sublime
import sublime_plugin
import AutoItPlysSublime.autoitbuild as autoitbuild


class PlysBuildCommand(sublime_plugin.WindowCommand):

	options = ["/ErrorStdOut", "/Rapid"]
	file_regex = r'[^"]*"?([a-zA-Z]:\\.+?\.aup)"? \(([0-9]*)()\) : ==> (.*)$'

	def run(self):
		filepath = self.window.active_view().file_name()
		settings = autoitbuild.autoit_settings()
		autoit_exe_path = settings.get("AutoItExePath")
		# plys_path = \
		# 	re.sub(r"(.*\\).*$", r"\1Plys\\plys.au3", autoit_exe_path)
		plys_path = settings.get("PlysAU3Path")
		cmd = [autoit_exe_path, plys_path] + self.options + [filepath]
		self.window.run_command("exec",
			{"cmd": cmd, "file_regex": self.file_regex})


class PlysRetranslateRunCommand(PlysBuildCommand):

	options = ["/ErrorStdOut"]


class PlysTranslateCommand(PlysBuildCommand):

	options = ["/Translate"]
	file_regex = r'"([a-zA-Z]:\\.+?\.aup\.au3)"$'


class PlysHelpCommand(autoitbuild.AutoitHelpCommand):

	def run(self):
		self.plys_help_path = autoitbuild.autoit_settings().get("PlysHelpPath")
		super().run()

	def make_args(self):
		return super().make_args() + ["Introduction", self.plys_help_path]


class PlysContexthelpCommand(autoitbuild.AutoitContexthelpCommand):

	def run(self, edit):
		self.plys_help_path = autoitbuild.autoit_settings().get("PlysHelpPath")
		super().run(edit)

	def make_args(self, query):
		return super().make_args(query) + [self.plys_help_path]


class PlysGetpathsCommand(sublime_plugin.WindowCommand):
	
	def __init__(self, window):
		super().__init__(window)
		if autoitbuild.autoit_settings().get("PlysStatus") == "installed":
			return

		try:
			exe_folder = autoitbuild.autoit_exe_folder()
		except WindowsError as e:
			sublime.active_window().run_command(
				"show_panel", {"panel": "console"}
			)
			print("[ERROR: Python exception trying to run following command]")
			print("Error " + str(e))
			return

		import json
		default_settings_path = \
			autoitbuild.PACKAGE_FOLDER + "\\AutoIt.sublime-settings"
		with open(default_settings_path) as f:
			settings = json.load(f)
		settings["PlysAU3Path"] = exe_folder + "\\Plys\\plys.au3"
		settings["PlysHelpPath"] = exe_folder + "\\Plys\\Plys.chm"
		settings["PlysStatus"] = "installed"
		with open(default_settings_path, "w") as f:
			json.dump(settings, f, indent="\t")

		import shutil
		shutil.move(
			autoitbuild.PACKAGE_FOLDER + "\\AutoIt Plys.sublime-settings",
			sublime.packages_path() + "\\User\\"
		)

	def run(self):
		pass
