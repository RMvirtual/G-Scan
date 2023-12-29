import wx


class PageRangeDialog(wx.Dialog):
    CANCEL = 0
    SPLIT_RANGE = 1
    SPLIT_ALL = 2

    def __init__(self, max_pages: int) -> None:
        super().__init__(None, title="Split Page Range")

        self.max_pages = max_pages
        self._initialise_widgets()
        self._initialise_callbacks()
        self._initialise_sizer()

    def _initialise_widgets(self) -> None:
        self.from_label = wx.StaticText(self, label="From", style=wx.TE_CENTRE)

        self.from_entry = wx.SpinCtrl(
            self, initial=1, min=1, max=self.max_pages-1)

        self.to_label = wx.StaticText(self, label="to", style=wx.TE_CENTRE)

        self.to_entry = wx.SpinCtrl(
            self, initial=self.max_pages, min=2, max=self.max_pages)

        self.split_all_button = wx.Button(self, label="Split All")

        self.split_all_button.Bind(
            event=wx.EVT_BUTTON,
            handler=lambda _evt: self.EndModal(self.SPLIT_ALL)
        )

        self.split_range_button = wx.Button(self, label="Split Range")

        self.split_range_button.Bind(
            event=wx.EVT_BUTTON,
            handler=lambda _evt: self.EndModal(self.SPLIT_RANGE)
        )

        self.cancel_button = wx.Button(self, label="Cancel")

        self.cancel_button.Bind(
            event=wx.EVT_BUTTON,
            handler=lambda _evt: self.EndModal(self.CANCEL)
        )

    def _initialise_callbacks(self) -> None:
        self.from_entry.Bind(
            event=wx.EVT_SPINCTRL,
            handler=lambda _evt: self.to_entry.SetMin(
                self.from_entry.GetValue()+1)
        )

        self.to_entry.Bind(
            event=wx.EVT_SPINCTRL,
            handler=lambda _evt: self.from_entry.SetMax(
                self.to_entry.GetValue()-1)
        )

    def _process_from_value_change(self, event: wx.EVT_SPINCTRL) -> None:
        self.to_entry.SetMin(self.from_entry.GetValue() + 1)

    def _process_to_value_change(self, event: wx.EVT_SPINCTRL) -> None:
        self.from_entry.SetMax(self.to_entry.GetValue() - 1)

    def _initialise_sizer(self) -> None:
        top_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        button_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)

        sizer_arrangements = {
            top_sizer: [
                self.from_label,
                self.from_entry,
                self.to_label,
                self.to_entry
            ],
            button_sizer: [
                self.split_all_button,
                self.split_range_button, 
                self.cancel_button
            ]
        }

        for sizer, buttons in sizer_arrangements.items():
            for button in buttons:
                sizer.Add(button, proportion=1, flag=wx.ALL, border=5)

        vertical_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        vertical_sizer.Add(sizer=top_sizer, flag=wx.ALIGN_CENTRE_HORIZONTAL)
        vertical_sizer.Add(sizer=button_sizer, flag=wx.ALIGN_CENTRE_HORIZONTAL)

        self.SetSizer(vertical_sizer)

    def page_range(self) -> tuple[int, int]:
        return int(self.from_entry.GetValue()), int(self.to_entry.GetValue())