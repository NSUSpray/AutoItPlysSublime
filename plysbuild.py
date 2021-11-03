import sublime, sublime_plugin
import AutoItPlysSublime.autoitbuild as autoitbuild

class plysbuild(sublime_plugin.WindowCommand):
	def run(self):
		filepath = self.window.active_view().file_name()
		settings = sublime.load_settings("AutoIt.sublime-settings")
		autoit_exe_path = settings.get("AutoItExePath")
		# plys_path = re.sub(r"(.*\\).*$", r"\1Plys\\plys.au3", autoit_exe_path)
		plys_path = settings.get("PlysPath")
		cmd = [autoit_exe_path, plys_path, "/ErrorStdOut", filepath]
		self.window.run_command("exec", {"cmd": cmd})

class plystranslate(sublime_plugin.WindowCommand):
	def run(self):
		filepath = self.window.active_view().file_name()
		settings = sublime.load_settings("AutoIt.sublime-settings")
		autoit_exe_path = settings.get("AutoItExePath")
		# plys_path = re.sub(r"(.*\\).*$", r"\1Plys\\plys.au3", autoit_exe_path)
		plys_path = settings.get("PlysPath")
		cmd = [autoit_exe_path, plys_path, "/Translate", filepath]
		self.window.run_command("exec", {"cmd": cmd})

class plysgetpath(sublime_plugin.WindowCommand):
	def __init__(self, window):
		super().__init__(window)
		if sublime.load_settings("AutoIt.sublime-settings").get("PlysStatus") == "installed":
			return

		try:
			autoit_exe_folder = autoitbuild.get_autoit_exe_folder()
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
		settings["PlysPath"] = autoit_exe_folder + "\\Plys\\plys.au3"
		settings["PlysStatus"] = "installed"
		with open(default_settings_path, "w") as f:
			json.dump(settings, f, indent="\t")

	def run(self):
		pass
