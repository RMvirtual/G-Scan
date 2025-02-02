import wx


def request_directory() -> str|None:
    dialog = wx.DirDialog(parent=None)
    
    with dialog:
        return dialog.GetPath() if dialog.ShowModal() == wx.ID_OK else None


def request_files() -> list[str]:
    dialog = wx.FileDialog(
        parent=None, style=(wx.FD_MULTIPLE|wx.FD_OPEN|wx.FD_FILE_MUST_EXIST))

    with dialog:
        dialog.ShowModal()
        
        return dialog.GetPaths()
