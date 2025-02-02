import wx


class PageRangeDialog(wx.Dialog):
    CANCEL = 0
    SPLIT_RANGE = 1
    SPLIT_ALL = 2

    def __init__(self, max_pages: int) -> None:
        super().__init__(None, title="Split Page Range")

        self.from_label = wx.StaticText(self, label="From", style=wx.TE_CENTRE)
        self.from_entry = wx.SpinCtrl(self, initial=1, min=1, max=max_pages-1)
        self.to_label = wx.StaticText(self, label="to", style=wx.TE_CENTRE)

        self.to_entry = wx.SpinCtrl(
            self, initial=max_pages, min=2, max=max_pages)

        self.split_all_btn = wx.Button(self, label="Split All")

        self.split_all_btn.Bind(
            event=wx.EVT_BUTTON,
            handler=lambda _evt: self.EndModal(self.SPLIT_ALL)
        )

        self.split_range_btn = wx.Button(self, label="Split Range")

        self.split_range_btn.Bind(
            event=wx.EVT_BUTTON,
            handler=lambda _event: self.EndModal(self.SPLIT_RANGE)
        )

        self.cancel_btn = wx.Button(self, label="Cancel")

        self.cancel_btn.Bind(
            event=wx.EVT_BUTTON,
            handler=lambda _event: self.EndModal(self.CANCEL)
        )

        # Bind callbacks.
        self.from_entry.Bind(
            event=wx.EVT_SPINCTRL,
            handler=lambda _event: (self.to_entry.SetMin(
                self.from_entry.GetValue() + 1))
        )

        self.to_entry.Bind(
            event=wx.EVT_SPINCTRL,
            handler=lambda _event: self.from_entry.SetMax(
                self.to_entry.GetValue() - 1)
        )

        # Sizer layout.
        top_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        top_sizer.Add(self.from_label, proportion=1, flag=wx.ALL, border=5)
        top_sizer.Add(self.from_entry, proportion=1, flag=wx.ALL, border=5)
        top_sizer.Add(self.to_label, proportion=1, flag=wx.ALL, border=5)
        top_sizer.Add(self.to_entry, proportion=1, flag=wx.ALL, border=5)

        btn_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        btn_sizer.Add(self.split_all_btn, proportion=1, flag=wx.ALL, border=5)
        btn_sizer.Add(self.split_range_btn, proportion=1, flag=wx.ALL, border=5)
        btn_sizer.Add(self.cancel_btn, proportion=1, flag=wx.ALL, border=5)

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(sizer=top_sizer, flag=wx.ALIGN_CENTRE_HORIZONTAL)
        sizer.Add(sizer=btn_sizer, flag=wx.ALIGN_CENTRE_HORIZONTAL)
        self.SetSizer(sizer)

    def page_range(self) -> tuple[int, int]:
        return int(self.from_entry.GetValue()), int(self.to_entry.GetValue())
    