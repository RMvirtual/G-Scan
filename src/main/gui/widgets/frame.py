from wx import Frame as wxFrame


class Frame(wxFrame):
    def __init__(self, size, title):
        super().__init__(None, size=size, title=title)
        self.SetBackgroundColour("WHITE")
