import wx


class DocumentSplitDialog(wx.Dialog):
    CANCEL = 0
    SPLIT_RANGE = 1
    SPLIT_ALL = 2

    def __init__(self, max_pages: int):
        super().__init__(parent=None, title="Split Document")
        self.max_pages = max_pages
        self._initialise_widgets()
        self._initialise_callbacks()
        self._initialise_sizer()

    def _initialise_widgets(self) -> None:
        self.from_label = wx.StaticText(
            parent=self, label="From", style=wx.TE_CENTRE)

        self.from_entry = wx.SpinCtrl(
            parent=self, initial=1, min=1, max=self.max_pages-1)

        self.to_label = wx.StaticText(
            parent=self, label="to", style=wx.TE_CENTRE)

        self.to_entry = wx.SpinCtrl(
            parent=self, initial=self.max_pages,
            min=2, max=self.max_pages
        )

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

    def _initialise_callbacks(self) -> None:
        self.from_entry.Bind(
            event=wx.EVT_SPINCTRL, handler=self._process_from_value_change)

        self.to_entry.Bind(
            event=wx.EVT_SPINCTRL, handler=self._process_to_value_change)

    def _process_from_value_change(self, event: wx.EVT_SPINCTRL) -> None:
        ...

    def _process_to_value_change(self, event: wx.EVT_SPINCTRL) -> None:
        ...

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