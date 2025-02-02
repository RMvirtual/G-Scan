import wx


def request_directory() -> str|None:
    dialog = wx.DirDialog(parent=None)
    
    with dialog:
        return dialog.GetPath() if dialog.ShowModal() == wx.ID_OK else None
