import wx


def request_files_to_import() -> list[str]:
    browser_style = (wx.FD_MULTIPLE | wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

    with wx.FileDialog(parent=None, style=browser_style) as browser:
        if browser.ShowModal() == wx.ID_CANCEL:
            return []

        return browser.GetPaths()
