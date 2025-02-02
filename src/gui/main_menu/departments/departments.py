import wx

from gui.main_menu.departments.settings_toolbar import SettingsToolbar


class Departments(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(parent)
        self.options = DepartmentOptions(self)
        self.toolbar = SettingsToolbar(self)

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(self.options, proportion=1, flag=wx.ALIGN_CENTRE_HORIZONTAL)
        sizer.Add(self.toolbar, proportion=0, flag=wx.ALIGN_RIGHT)
        self.SetSizer(sizer)


class DepartmentOptions(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(parent)

        font = wx.Font(wx.FontInfo(pointSize=30)).Bold()

        self.ops = wx.Button(self, label="Ops")
        self.ops.SetFont(font)
        
        self.pods = wx.Button(self, label="PODs")
        self.pods.SetFont(font)
        
        self.quick_start = wx.Button(self, label="Quick Start")
        self.quick_start.SetFont(font)

        # Sizer layout.        
        sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        alignment_flags = wx.LEFT|wx.RIGHT|wx.ALIGN_TOP
        sizer.Add(self.ops, proportion=0, flag=alignment_flags, border=15)
        sizer.Add(self.pods, proportion=0, flag=alignment_flags, border=15)
        sizer.Add(self.quick_start, proportion=0, flag=alignment_flags, border=15)
        self.SetSizer(sizer)
