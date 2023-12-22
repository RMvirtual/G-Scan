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

        self.cust_pwork = wx.Button(parent=self, label="Customer\nPaperwork")
        self.loading_list = wx.Button(parent=self, label="Loading\nList")

        for button in [self.cust_pwork, self.loading_list]:
            button.SetFont(fonts.font(point_size=30, bold=True))

        flags = wx.LEFT|wx.RIGHT|wx.ALIGN_TOP
        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)

        sizer.Add(self.cust_pwork, proportion=0, flag=flags, border=15)
        sizer.Add(self.loading_list, proportion=0, flag=flags, border=15)
        self.SetSizer(sizer)


class CreditControl(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent)

        self.options = CreditControlOptions(self)
    
        self.back = wx.Button(self, label="Back")
        self.back.SetFont(fonts.font(point_size=30, bold=True))

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(self.options, proportion=1, flag=wx.ALIGN_CENTRE_HORIZONTAL)
        
        sizer.Add(
            self.back, proportion=0, flag=wx.ALL|wx.ALIGN_RIGHT, border=15)

        self.SetSizer(sizer)


class CreditControlOptions(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent)

        self.signed_pod = wx.Button(self, label="Standard\nDelivery Note")

        self.customer_paperwork_pod = wx.Button(
            self, label="Customer\nPaperwork POD")

        self._buttons = [self.signed_pod, self.customer_paperwork_pod]

        for button in self._buttons:
            button.SetFont(fonts.font(point_size=30, bold=True))

        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)

        for button in self._buttons:
            sizer.Add(
                button, proportion=0, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_TOP, 
                border=15
            )

        self.SetSizer(sizer)


class SettingsToolbar(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent=parent)

        self.settings = wx.Button(parent=self, label="Settings")
        self.exit = wx.Button(parent=self, label="Exit")

        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        for widget in [self.settings, self.exit]:
            widget.SetFont(fonts.font(point_size=30, bold=True))

            sizer.Add(
                widget, proportion=0, flag=wx.ALL|wx.ALIGN_RIGHT, border=15)

        self.SetSizer(sizer)


class DepartmentOptions(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(parent)

        button_labels = ["Ops", "PODs", "Quick Start"]
        buttons = [wx.Button(self, label=label) for label in button_labels]

        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)

        for button in buttons:
            button.SetFont(fonts.font(point_size=30, bold=True))

            sizer.Add(
                button, proportion=0, flag=wx.LEFT|wx.RIGHT|wx.ALIGN_TOP,
                border=15
            )

        self.SetSizer(sizer)
        self.ops, self.pods, self.quick_start = buttons


class Departments(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(parent)
        self.options = DepartmentOptions(self)
        self.toolbar = SettingsToolbar(self)

        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        sizer.Add(
            window=self.options, proportion=1, flag=wx.ALIGN_CENTRE_HORIZONTAL)

        sizer.Add(window=self.toolbar, proportion=0, flag=wx.ALIGN_RIGHT)
        self.SetSizer(sizer)
