import wx

from gui import fonts
from gui.settings.directories import Directories
from gui.settings.defaults import Defaults


BrowseWidgets = tuple[wx.StaticText, wx.TextCtrl, wx.Button]


class Directories(wx.Panel):
    def __init__(self, parent: wx.Window) -> None:
        super(Directories, self).__init__(parent=parent)

        self.title = wx.StaticText(parent=self, label="Folders")
        self.title.SetFont(fonts.font(point_size=20, bold=True))

        self.scan_label, self.scan_box, self.scan_browse = \
            self._browse_widgets("Scan Directory")

        self.dest_label, self.dest_box, self.dest_browse = \
            self._browse_widgets("Destination Directory")

        font = fonts.font(point_size=12)

        items = [
            self.scan_label, self.scan_box, self.scan_browse,
            self.dest_label, self.dest_box, self.dest_browse,
        ]

        for item in items:
            item.SetFont(font)

        sizer = wx.GridBagSizer(vgap=5, hgap=5)

        alignment = wx.ALIGN_LEFT|wx.ALIGN_CENTRE_VERTICAL
        align_and_expand = wx.EXPAND|alignment

        sizer.Add(window=self.title, pos=(0, 0), span=(1,3), flag=alignment)

        sizer.Add(window=self.scan_label, pos=(1, 0), flag=alignment)
        sizer.Add(window=self.scan_box, pos=(1, 1), flag=align_and_expand)
        sizer.Add(window=self.scan_browse, pos=(1, 2), flag=alignment)

        sizer.Add(window=self.dest_label, pos=(2, 0), flag=alignment)
        sizer.Add(window=self.dest_box, pos=(2, 1), flag=align_and_expand)
        sizer.Add(window=self.dest_browse, pos=(2, 2), flag=alignment)

        sizer.AddGrowableCol(1)
        self.SetSizer(sizer)

    @property
    def scan_directory(self) -> str:
        return self.scan_box.GetValue()

    @scan_directory.setter
    def scan_directory(self, directory: str) -> None:
        self.scan_box.SetValue(directory)

    @property
    def dest_directory(self) -> str:
        return self.dest_box.GetValue()

    @dest_directory.setter
    def dest_directory(self, directory: str) -> None:
        self.dest_box.SetValue(directory)

    def _browse_widgets(
            self, label: str, box_value: str = "NULL") -> BrowseWidgets:
        return (
            wx.StaticText(parent=self, label=label),
            wx.TextCtrl(parent=self, value=box_value),
            wx.Button(parent=self, label="...")
        )


class Settings(wx.Panel):
    def __init__(self, window: wx.Frame) -> None:
        super().__init__(parent=window)

        self.title = wx.StaticText(parent=self, label="Settings")
        self.title.SetFont(fonts.font(point_size=30, bold=True))

        self.directories = Directories(self)
        self.defaults = Defaults(self)

        self.save = wx.Button(parent=self, label="Save")
        self.exit = wx.Button(parent=self, label="Exit")

        font = fonts.font(point_size=12)
        self.save.SetFont(font)
        self.exit.SetFont(font)

        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        widget_to_flags = {
            self.title: wx.ALIGN_LEFT|wx.ALL,
            self.directories: wx.EXPAND|wx.ALL,
            self.defaults: wx.ALIGN_LEFT|wx.ALL,
            self.save: wx.ALIGN_RIGHT|wx.RIGHT|wx.BOTTOM,
            self.exit: wx.ALIGN_RIGHT|wx.RIGHT|wx.BOTTOM
        }

        for widget, flags in widget_to_flags.items():
            sizer.Add(window=widget, proportion=0, flag=flags, border=15)

        sizer.AddStretchSpacer()
        self.SetSizer(sizer)

        self.SetBackgroundColour(colour=wx.WHITE)
