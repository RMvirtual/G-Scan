import wx


class MenuBar(wx.MenuBar):
    def __init__(self):
        super(MenuBar, self).__init__()

        self.file_menu = wx.Menu()

        self.file_item = self.file_menu.Append(
            wx.ID_EXIT, 'Quit', 'Quit application')

        self.Append(self.file_menu, "&File")