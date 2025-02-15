import wx

from document_type import DocumentType


class DocumentSelectionPanel(wx.Panel):
    def __init__(
            self, parent: wx.Frame, document_types: list[DocumentType]
    ) -> None:
        super().__init__(parent)

        self.option_btns: dict[DocumentType, wx.Button] = {}

        for document in document_types:
            self.option_btns[document] = wx.Button(
                self, label=document.full_name)

        self.back = wx.Button(parent=self, label="Back")

        font = wx.Font(wx.FontInfo(pointSize=30)).Bold()

        for button in *self.option_btns.values(), self.back:
            button.SetFont(font)

        # Sizer layout.
        doc_row_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        flags = wx.LEFT|wx.RIGHT|wx.ALIGN_TOP
        
        for button in self.option_btns.values():
            doc_row_sizer.Add(button, proportion=0, flag=flags, border=15)

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(doc_row_sizer, proportion=1, flag=wx.ALIGN_CENTRE_HORIZONTAL)
        
        sizer.Add(
            self.back, proportion=0, flag=wx.ALL|wx.ALIGN_RIGHT, border=15)

        self.SetSizer(sizer)
