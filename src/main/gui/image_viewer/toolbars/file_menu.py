import wx


class FileMenu(wx.MenuBar):
    def __init__(self):
        super().__init__()

        self.file_menu = wx.Menu()

        self.quit = self.file_menu.Append(
            wx.ID_SAVE, '&Save\tCTRL+S', "Save File")

        self.Append(self.file_menu, "File")
