import wx


class DocumentTreeCtrl(wx.TreeCtrl):
    def __init__(self, parent: wx.Window) -> None:
        style = (
            wx.TR_HIDE_ROOT|wx.TR_TWIST_BUTTONS|wx.TR_HAS_BUTTONS|
            wx.TR_NO_LINES|wx.TR_MULTIPLE
        )

        super().__init__(parent=parent, style=style)

