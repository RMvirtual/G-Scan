import wx


class FileMenu(wx.MenuBar):
    def __init__(self):
        super().__init__()

        self._initialise_file_menu()
        self.Append(self.file_menu, "File")

    def _initialise_file_menu(self) -> None:
        self.file_menu = wx.Menu()

        self.import_files = self.file_menu.Append(
            id=wx.ID_ANY, item="&Import Files\tCTRL+I",
            helpString="Import Files"
        )

        self.import_prenamed_files = self.file_menu.Append(
            id=wx.ID_ANY, item="&Import Prenamed Files\tCTRL+M",
            helpString=(
                "Import files already named with the reference to be used")
        )

        self.quit = self.file_menu.Append(
            id=wx.ID_SAVE, item='&Quit\tF4', helpString="Quit to Main Menu")
