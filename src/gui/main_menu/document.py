import wx

from documents import DocumentType


class DocumentsPanel(wx.Panel):
    def __init__(
        self, parent: wx.Panel, document_types: list[DocumentType]
    ) -> None:
        super().__init__(parent)

        self.document_type_btns: dict[DocumentType, wx.Button] = {}

        for document_type in document_types:
            new_btn = wx.Button(
                self, label=document_type.full_name, style=wx.BU_EXACTFIT
            )

            self.document_type_btns[document_type] = new_btn

        self.back = wx.Button(parent=self, label="Back")

        # Fonts.
        font = wx.Font(wx.FontInfo(pointSize=16)).Bold()

        for button in *self.document_type_btns.values(), self.back:
            button.SetFont(font)

        # Sizer layout.
        border = 15
        document_types_sizer = wx.WrapSizer()

        for button in self.document_type_btns.values():
            document_types_sizer.Add(button, 1, wx.ALL, border)

        main_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        main_sizer.Add(document_types_sizer, 1, wx.ALIGN_CENTRE_HORIZONTAL)
        main_sizer.Add(self.back, 0, wx.ALL | wx.ALIGN_RIGHT, border)
        self.SetSizer(main_sizer)
