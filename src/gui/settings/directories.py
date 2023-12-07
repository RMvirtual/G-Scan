import wx
from gui import fonts

BrowseWidgets = tuple[wx.StaticText, wx.TextCtrl, wx.Button]


class Directories(wx.Panel):
    def __init__(self, parent: wx.Window) -> None:
        super(Directories, self).__init__(parent=parent)

        self._initialise_widgets()
        self._initialise_sizer()

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

    def _initialise_widgets(self) -> None:
        self._initialise_title()
        self._initialise_body_widgets()

    def _initialise_body_widgets(self) -> None:
        self._initialise_scan_widgets()
        self._initialise_dest_widgets()
        self._initialise_fonts()

    def _initialise_scan_widgets(self) -> None:
        self.scan_label, self.scan_box, self.scan_browse = \
            self._browse_widgets("Scan Directory")

    def _initialise_dest_widgets(self) -> None:
        self.dest_label, self.dest_box, self.dest_browse = \
            self._browse_widgets("Destination Directory")

    def _initialise_fonts(self) -> None:
        font = fonts.font(point_size=12)

        items = [
            self.scan_label, self.scan_box, self.scan_browse,
            self.dest_label, self.dest_box, self.dest_browse,
        ]

        for item in items:
            item.SetFont(font)

    def _browse_widgets(
            self, label: str, box_value: str = "NULL") -> BrowseWidgets:
        return (
            wx.StaticText(parent=self, label=label),
            wx.TextCtrl(parent=self, value=box_value),
            wx.Button(parent=self, label="...")
        )

    def _initialise_title(self) -> None:
        self.title = wx.StaticText(parent=self, label="Folders")
        self.title.SetFont(fonts.font(point_size=20, bold=True))

    def _initialise_sizer(self) -> None:
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

