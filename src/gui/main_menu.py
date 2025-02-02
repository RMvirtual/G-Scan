import wx

import file_system
from gui.departments import CreditControl, Departments, Operations


class Logo(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(parent)

        image = file_system.image_resources_directory().joinpath("logo.png")
        self.image = wx.Image(str(image), wx.BITMAP_TYPE_PNG)

        self.bitmap = wx.StaticBitmap(
            self, bitmap=self.image.ConvertToBitmap(depth=32))

        # Sizer layout.
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(window=self.bitmap, proportion=0, flag=wx.EXPAND, border=0)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_SIZE, self.on_resize)

    def on_resize(self, event: wx.Event) -> None:
        image_ratio = float(self.image.GetWidth()) / float(self.image.GetHeight())

        width, height = self.Size
        requested_ratio = float(width) / float(height)
        is_too_wide = requested_ratio > image_ratio

        if is_too_wide:
            new_width, new_height = (height*image_ratio, height)
        
        else:
            new_width, new_height = (width, width/image_ratio)
        
        scaled_image = self.image.Scale(
            int(new_width), int(new_height), wx.IMAGE_QUALITY_NORMAL)

        self.bitmap.SetBitmap(scaled_image.ConvertToBitmap())


class MainMenu(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        super().__init__(parent)

        self.logo = Logo(self)
        self.departments = Departments(self)
        self.operations = Operations(self)
        self.credit_control = CreditControl(self)

        self._subpanels = (
            self.departments, self.operations, self.credit_control)

        # Grid layout.
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(self.logo, proportion=2, flag=wx.EXPAND)

        for panel in self._subpanels:
            sizer.Add(panel, proportion=3, flag=wx.EXPAND)

        self.SetSizer(sizer)
        self.SetBackgroundColour(colour=wx.WHITE)
        self._switch_to(self.departments)

    def view_departments(self) -> None:
        self._switch_to(self.departments)

    def view_ops(self) -> None:
        self._switch_to(self.operations)

    def view_credit_control(self) -> None:
        self._switch_to(self.credit_control)

    def _switch_to(self, subpanel: wx.Panel) -> None:
        other_panels = filter(
            lambda panel: panel is not subpanel, self._subpanels)
        
        for panel in other_panels:
            panel.Hide()

        subpanel.Show()
        self.Layout()
