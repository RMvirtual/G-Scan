import wx
from src.main import departments, documents, file_system, user
from src.main.app.interfaces import RootInterface
from src.main.departments import Department
from src.main.gui import Settings
from src.main.user import UserSettings


class SettingsController:
    def __init__(self, root_application: RootInterface):
        self._root = root_application
        self._initialise_gui()
        self._initialise_callbacks()
        self._load_settings_from_file()

    def _initialise_gui(self) -> None:
        self._gui = Settings(self._root.window)
        self._root.window.set_panel(self._gui)

    def _initialise_callbacks(self) -> None:
        self._gui.save.Bind(wx.EVT_BUTTON, self.on_save)
        self._gui.exit.Bind(wx.EVT_BUTTON, self.on_exit)

        self._gui.directories.scan_browse.Bind(
            wx.EVT_BUTTON, self.on_scan_dir_browse)

        self._gui.directories.dest_browse.Bind(
            wx.EVT_BUTTON, self.on_dest_dir_browse)

        self._gui.defaults.department_box.Bind(
            wx.EVT_COMBOBOX, self.on_department_box)

        self._gui.Bind(wx.EVT_CLOSE, self.on_close)

    def on_save(self, event = None) -> None:
        user.save_settings(settings=self._settings_from_gui())
        self._exit_to_main_menu()

    def on_exit(self, event = None) -> None:
        self._exit_to_main_menu()

    def on_scan_dir_browse(self, event = None) -> None:
        user_selection = self._directory_dialog()

        if user_selection:
            self._gui.directories.scan_directory = user_selection

    def on_dest_dir_browse(self, event = None) -> None:
        user_selection = self._directory_dialog()

        if user_selection:
            self._gui.directories.dest_directory = user_selection

    def on_department_box(self, event = None) -> None:
        self._refresh_document_options()

    def on_close(self, event = None) -> None:
        self._gui.Destroy()

    def _exit_to_main_menu(self) -> None:
        self._gui.Close()
        self._root.launch_main_menu()

    def _settings_from_gui(self) -> UserSettings:
        result = UserSettings()
        result.scan_dir = self._gui.directories.scan_directory
        result.dest_dir = self._gui.directories.dest_directory

        result.department = departments.load(
            full_name=self._gui.defaults.department_box)

        result.document_type = documents.load(
            full_name=self._gui.defaults.department_box)

        return result

    def _load_settings_from_file(self) -> None:
        self._set_from_user_settings(settings=user.load_settings())
        self._root.window.Layout()

    def _refresh_document_options(self) -> None:
        department = departments.load(full_name=self._gui.defaults.department_box)
        self._set_document_names(department)

    def _set_from_user_settings(self, settings: UserSettings) -> None:
        self._set_directories(settings)
        self._set_department(settings)
        self._set_document_type(settings)

    def _set_directories(self, settings: UserSettings) -> None:
        self._gui.directories.scan_directory = settings.scan_dir
        self._gui.directories.dest_directory = settings.dest_dir

    def _set_department(self, settings: UserSettings) -> None:
        department_names = departments.load_all().full_names()
        self._gui.defaults.department_options = department_names

        self._gui.defaults.department_box = settings.department.full_name

    def _set_document_type(self, settings: UserSettings) -> None:
        document_names = settings.department.document_types.full_names()
        self._gui.defaults.document_options = document_names

        self._gui.defaults.department_box = settings.document_type.full_name

    def _set_document_names(self, department: Department) -> None:
        document_names = department.document_types.full_names()

        self._gui.defaults.document_options = document_names
        self._gui.defaults.department_box = document_names[0]

    @staticmethod
    def _directory_dialog() -> str or None:
        with wx.DirDialog(None) as browser:
            if browser.ShowModal() == wx.ID_CANCEL:
                return None

            return browser.GetPath()