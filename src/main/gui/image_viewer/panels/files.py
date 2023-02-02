import wx
from src.main.gui import fonts


class FilesPanel(wx.Panel):
    def __init__(self, parent: wx.Window):
        super(FilesPanel, self).__init__(parent=parent)
        self._initialise_widgets()
        self._initialise_sizer()
        self._create_dummy_data()
        self.files.ExpandAll()

    def _initialise_widgets(self) -> None:
        self._title = wx.StaticText(parent=self, label="Jobs")
        self._title.SetFont(fonts.font(point_size=30, bold=True))

        self.upload_to_fcl = wx.Button(parent=self, label="Upload to FCL")

        tree_style = (
            wx.TR_HIDE_ROOT|wx.TR_TWIST_BUTTONS|wx.TR_HAS_BUTTONS
            |wx.TR_NO_LINES|wx.TR_MULTIPLE
        )

        self.files = wx.TreeCtrl(parent=self, style=tree_style)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        sizer.Add(
            window=self._title, proportion=0,
            flag=wx.ALIGN_CENTRE_HORIZONTAL|wx.ALL, border=5
        )

        sizer.Add(
            window=self.upload_to_fcl, proportion=0,
            flag=wx.ALIGN_LEFT|wx.ALL, border=5
        )

        sizer.Add(
            window=self.files, proportion=1,
            flag=wx.EXPAND|wx.ALL, border=5
        )

        self.SetSizer(sizer)

    def _create_dummy_data(self) -> None:
        root_id = self.files.AddRoot(text="All Files")

        job_1 = self.files.AppendItem(parent=root_id, text="TestJob1")
        self.files.AppendItem(parent=job_1, text="Page 1")
        self.files.AppendItem(parent=job_1, text="Page 2")

        job_2 = self.files.AppendItem(parent=root_id, text="TestJob2")

        self.files.AppendItem(parent=job_2, text="DGN")
        self.files.AppendItem(parent=job_2, text="Customer Paperwork")
