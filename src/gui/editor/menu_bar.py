import wx


class TopMenuBar(wx.MenuBar):
    def __init__(self) -> None:
        super().__init__()

        self.file = FileMenu()
        self.Append(self.file, "File")


class FileMenu(wx.Menu):
    def __init__(self) -> None:
        super().__init__()

        self.import_files = self.Append(
            id=wx.ID_ANY,
            item="&Import Files\tCTRL+I",
            helpString="Import Files",
        )

        self.import_prenamed_files = self.Append(
            id=wx.ID_ANY,
            item="&Import Prenamed Files\tCTRL+M",
            helpString="Import files prenamed as the reference to be used",
        )

        self.quit = self.Append(
            id=wx.ID_ANY,
            item="&Quit\tF4",
            helpString="Quit to Main Menu",
        )
