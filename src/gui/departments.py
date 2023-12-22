import wx

from gui import fonts


class Operations(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(Operations, self).__init__(parent)

        self.options = OperationsOptions(self)
        self.back = wx.Button(parent=self, label="Back")
        self.back.SetFont(fonts.font(point_size=30, bold=True))

        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        sizer.Add(
            window=self.options, proportion=1, flag=wx.ALIGN_CENTRE_HORIZONTAL)

        sizer.Add(
            window=self.back, proportion=0, flag=wx.ALL|wx.ALIGN_RIGHT,
            border=15
        )

        self.SetSizer(sizer)


class OperationsOptions(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(OperationsOptions, self).__init__(parent)

        self._initialise_buttons()
        self._initialise_sizers()

    def _initialise_buttons(self) -> None:
        self.cust_pwork = wx.Button(parent=self, label="Customer\nPaperwork")
        self.loading_list = wx.Button(parent=self, label="Loading\nList")

        self.buttons = [self.cust_pwork, self.loading_list]
        self._initialise_fonts()

    def _initialise_fonts(self) -> None:
        font = fonts.font(point_size=30, bold=True)

        for button in self.buttons:
            button.SetFont(font)

    def _initialise_sizers(self) -> None:
        flags = wx.LEFT|wx.RIGHT|wx.ALIGN_TOP
        border = 15

        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)

        sizer.Add(
            window=self.cust_pwork, proportion=0, flag=flags, border=border)

        sizer.Add(
            window=self.loading_list, proportion=0, flag=flags, border=border)

        self.SetSizer(sizer)


class CreditControl(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent)

        self._initialise_widgets()
        self._initialise_sizer()

    def _initialise_widgets(self) -> None:
        self.options = CreditControlOptions(self)

        self.back = wx.Button(parent=self, label="Back")
        self.back.SetFont(fonts.font(point_size=30, bold=True))

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        options_flags = wx.ALIGN_CENTRE_HORIZONTAL
        sizer.Add(window=self.options, proportion=1, flag=options_flags)

        back_flags = wx.ALL|wx.ALIGN_RIGHT
        sizer.Add(window=self.back, proportion=0, flag=back_flags, border=15)

        self.SetSizer(sizer)


class CreditControlOptions(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent)

        self._initialise_widgets()
        self._initialise_sizers()

    def _initialise_widgets(self) -> None:
        self.signed_pod = wx.Button(
            parent=self, label="Standard\nDelivery Note")

        self.customer_paperwork_pod = wx.Button(
            parent=self, label="Customer\nPaperwork POD")

        self._buttons = [self.signed_pod, self.customer_paperwork_pod]
        self._initialise_fonts()

    def _initialise_fonts(self) -> None:
        font = fonts.font(point_size=30, bold=True)

        for button in self._buttons:
            button.SetFont(font)

    def _initialise_sizers(self) -> None:
        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        flags = wx.LEFT|wx.RIGHT|wx.ALIGN_TOP

        for button in self._buttons:
            sizer.Add(window=button, proportion=0, flag=flags, border=15)

        self.SetSizer(sizer)


class SettingsToolbar(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent=parent)

        self._initialise_buttons()
        self._initialise_sizer()

    def _initialise_buttons(self) -> None:
        self.settings = wx.Button(parent=self, label="Settings")
        self.exit = wx.Button(parent=self, label="Exit")

        font = fonts.font(point_size=30, bold=True)
        self.settings.SetFont(font)
        self.exit.SetFont(font)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        sizer.Add(
            window=self.settings, proportion=0,
            flag=wx.ALL|wx.ALIGN_RIGHT, border=15
        )

        sizer.Add(
            window=self.exit, proportion=0,
            flag=wx.ALL|wx.ALIGN_RIGHT, border=15
        )

        self.SetSizer(sizer)


class Departments(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super(Departments, self).__init__(parent)
        self._initialise_panels()
        self._initialise_sizer()

    def _initialise_panels(self) -> None:
        self.options = DepartmentOptions(self)
        self.toolbar = SettingsToolbar(self)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        sizer.Add(
            window=self.options, proportion=1, flag=wx.ALIGN_CENTRE_HORIZONTAL)

        sizer.Add(window=self.toolbar, proportion=0, flag=wx.ALIGN_RIGHT)

        self.SetSizer(sizer)


class DepartmentOptions(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent)

        self._initialise_buttons()
        self._initialise_sizer()

    def _initialise_buttons(self) -> None:
        self.ops = wx.Button(parent=self, label="Ops")
        self.pods = wx.Button(parent=self, label="PODs")
        self.quick_start = wx.Button(parent=self, label="Quick Start")

        self.buttons = [self.ops, self.pods, self.quick_start]

        self._initialise_fonts()

    def _initialise_fonts(self) -> None:
        font = fonts.font(point_size=30, bold=True)

        for button in self.buttons:
            button.SetFont(font)

    def _initialise_sizer(self) -> None:
        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)

        for button in self.buttons:
            sizer.Add(
                window=button, proportion=0,
                flag=wx.LEFT|wx.RIGHT|wx.ALIGN_TOP, border=15
            )

        self.SetSizer(sizer)
