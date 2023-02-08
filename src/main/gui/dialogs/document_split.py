import wx


class DocumentSplitDialog(wx.Dialog):
    CANCEL = 0
    SPLIT_RANGE = 1
    SPLIT_ALL = 2

    def __init__(self, total_pages: int):

        super().__init__(
            parent=None, title="Split Document")

        self.total_pages = total_pages
        self._initialise_widgets()
        self._initialise_sizer()

    def _initialise_widgets(self) -> None:
        self.from_label = wx.StaticText(parent=self, label="From")
        self.from_entry = wx.TextCtrl(parent=self, value="1")

        self.to_label = wx.StaticText(parent=self, label="to")
        self.to_entry = wx.TextCtrl(parent=self, value=f"{self.total_pages}")

        self.split_all_button = wx.Button(parent=self, label="Split All")

        self.split_all_button.Bind(
            event=wx.EVT_BUTTON,
            handler=lambda _evt: self.EndModal(self.SPLIT_ALL)
        )

        self.split_range_button = wx.Button(parent=self, label="Split Range")

        self.split_range_button.Bind(
            event=wx.EVT_BUTTON,
            handler=lambda _evt: self.EndModal(self.SPLIT_RANGE)
        )

        self.cancel_button = wx.Button(parent=self, label="Cancel")

        self.cancel_button.Bind(
            event=wx.EVT_BUTTON,
            handler=lambda _evt: self.EndModal(self.CANCEL)
        )

    def _initialise_sizer(self) -> None:
        border = 5
        flags = wx.ALL

        top_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        top_sizer.Add(
            window=self.from_label, proportion=1, flag=flags, border=border)

        top_sizer.Add(
            window=self.from_entry, proportion=1,flag=flags, border=border)

        top_sizer.Add(
            window=self.to_label, proportion=1, flag=flags, border=border)

        top_sizer.Add(
            window=self.to_entry, proportion=1, flag=flags, border=border)

        button_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)

        button_sizer.Add(
            window=self.split_all_button, proportion=1, flag=flags, border=border)

        button_sizer.Add(
            window=self.split_range_button, proportion=1, flag=flags, border=border)

        button_sizer.Add(
            window=self.cancel_button, proportion=1, flag=flags, border=border)

        vertical_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        vertical_sizer.Add(sizer=top_sizer, flag=wx.ALIGN_CENTRE_HORIZONTAL)
        vertical_sizer.Add(sizer=button_sizer, flag=wx.ALIGN_CENTRE_HORIZONTAL)

        self.SetSizer(vertical_sizer)

    def page_range(self) -> tuple[int, int]:
        return int(self.from_entry.GetValue()), int(self.to_entry.GetValue())