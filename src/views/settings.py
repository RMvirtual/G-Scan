import wx


class DirectoryBrowseBox:
    def __init__(
            self, parent: wx.Panel, label: str, initial_value: str|None = None
    ) -> None:
        self.label = wx.StaticText(parent, label=label)
        self.entry = wx.TextCtrl(parent, value=(initial_value or ""))
        self.button = wx.Button(parent, label="...")
    
    def set_font(self, font: wx.Font) -> None:
        for widget in (self.label, self.entry, self.button):
            widget.SetFont(font)


class Defaults(wx.Panel):
    def __init__(self, parent: wx.Window) -> None:
        super().__init__(parent)

        self.title = wx.StaticText(self, label="Defaults")
        self.departments_label = wx.StaticText(self, label="Departments")

        self.department_box = wx.ComboBox(
            self, value="", choices=[""], style=wx.CB_READONLY)

        self.doc_type_label = wx.StaticText(self, label="Document Type")

        self.doc_type_box = wx.ComboBox(
            self, value="", choices=[""], style=wx.CB_READONLY)

        self.title.SetFont(wx.Font(wx.FontInfo(pointSize=20)).Bold())

        text_widgets: list[wx.Window] = [
            self.doc_type_label, self.departments_label, self.department_box,
            self.doc_type_box
        ]

        for widget in text_widgets:
            widget.SetFont(wx.Font(wx.FontInfo(pointSize=12)))

        sizer = wx.GridBagSizer(vgap=15, hgap=30)

        sizer.Add(window=self.title, pos=(0,0), span=(1,2), flag=wx.ALIGN_LEFT)
        sizer.Add(window=self.departments_label, pos=(1,0), flag=wx.ALIGN_LEFT)
        sizer.Add(window=self.doc_type_label, pos=(1, 1), flag=wx.ALIGN_LEFT)

        align_centre = wx.ALIGN_CENTRE_HORIZONTAL
        sizer.Add(window=self.department_box, pos=(2, 0), flag=align_centre)
        sizer.Add(window=self.doc_type_box, pos=(2, 1), flag=align_centre)

        self.SetSizer(sizer)

    @property
    def department(self) -> str:
        return self.department_box.GetValue()

    @department.setter
    def department(self, new_department: str) -> None:
        self.department_box.SetValue(new_department)

    @property
    def department_options(self) -> str:
        return self.department_box.GetItems()

    @department_options.setter
    def department_options(self, options: list[str]) -> None:
        self.department_box.SetItems(options)

    @property
    def document_type(self) -> str:
        return self.doc_type_box.GetValue()

    @document_type.setter
    def document_type(self, new_document_type: str) -> None:
        self.doc_type_box.SetValue(new_document_type)

    @property
    def document_options(self) -> list[str]:
        return self.doc_type_box.GetItems()

    @document_options.setter
    def document_options(self, new_options: list[str]) -> None:
        self.doc_type_box.SetItems(new_options)




class Directories(wx.Panel):
    def __init__(self, parent: wx.Window) -> None:
        super().__init__(parent=parent)

        self.title = wx.StaticText(self, label="Folders")
        self.scan_box = DirectoryBrowseBox(self, "Scan Directory")
        self.dest_box = DirectoryBrowseBox(self, "Destination Directory")      

        self.title.SetFont(wx.Font(wx.FontInfo(pointSize=20)).Bold())

        for box in self.scan_box, self.dest_box:
            box.set_font(wx.Font(wx.FontInfo(pointSize=12)))

        flags = wx.ALIGN_LEFT|wx.ALIGN_CENTRE_VERTICAL
        sizer = wx.GridBagSizer(vgap=5, hgap=5)
        sizer.Add(window=self.title, pos=(0, 0), span=(1,3), flag=flags)

        for row_no, box in enumerate((self.scan_box, self.dest_box), start=1):
            sizer.Add(window=box.label, pos=(row_no, 0), flag=flags)
            sizer.Add(window=box.entry, pos=(row_no, 1), flag=wx.EXPAND|flags)
            sizer.Add(window=box.button, pos=(row_no, 2), flag=flags)

        sizer.AddGrowableCol(1)
        self.SetSizer(sizer)

    @property
    def scan_directory(self) -> str:
        return self.scan_box.entry.GetValue()

    @scan_directory.setter
    def scan_directory(self, directory: str) -> None:
        self.scan_box.entry.SetValue(directory)

    @property
    def dest_directory(self) -> str:
        return self.dest_box.entry.GetValue()

    @dest_directory.setter
    def dest_directory(self, directory: str) -> None:
        self.dest_box.entry.SetValue(directory)


class Settings(wx.Panel):
    def __init__(self, window: wx.Frame) -> None:
        super().__init__(window)

        self.title = wx.StaticText(self, label="Settings")
        self.directories = Directories(self)
        self.defaults = Defaults(self)
        self.save = wx.Button(self, label="Save")
        self.exit = wx.Button(self, label="Exit")

        self.title.SetFont(wx.Font(wx.FontInfo(pointSize=30)).Bold())
        self.save.SetFont(wx.Font(wx.FontInfo(pointSize=12)))
        self.exit.SetFont(wx.Font(wx.FontInfo(pointSize=12)))

        sizer = wx.BoxSizer(orient=wx.VERTICAL)

        widget_to_flags = {
            self.title: wx.ALIGN_LEFT|wx.ALL,
            self.directories: wx.EXPAND|wx.ALL,
            self.defaults: wx.ALIGN_LEFT|wx.ALL,
            self.save: wx.ALIGN_RIGHT|wx.RIGHT|wx.BOTTOM,
            self.exit: wx.ALIGN_RIGHT|wx.RIGHT|wx.BOTTOM
        }

        for widget, flags in widget_to_flags.items():
            sizer.Add(window=widget, proportion=0, flag=flags, border=15)

        sizer.AddStretchSpacer()
        self.SetSizer(sizer)

        self.SetBackgroundColour(colour=wx.WHITE)
