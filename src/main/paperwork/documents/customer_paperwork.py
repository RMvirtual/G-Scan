from src.main.paperwork.documents.a4 import A4
from reportlab.graphics.barcode import code128
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("Calibri", "Calibri.ttf"))
pdfmetrics.registerFont(TTFont("Calibri-Bold", "Calibrib.ttf"))


class CustomerPaperwork(A4):
    def __init__(self, file_name, job_reference):
        super().__init__(file_name=file_name)
        self._job_reference = job_reference

    def draw_page(self, image):
        self.draw_title("Customer Paperwork")
        self.draw_barcode(self._job_reference)
        self.draw_job_reference(self._job_reference)
        self.draw_image(image)

        self.showPage()

    def draw_job_reference(self, job_reference: str) -> None:
        self.setFont("Calibri", 11)
        self.drawString(162 * mm, 275 * mm, job_reference)

    def draw_title(self, paperwork_type: str) -> None:
        self.setFont("Calibri-Bold", 22)
        self.drawString(5 * mm, 280 * mm, paperwork_type)

    def draw_barcode(self, job_reference: str) -> None:
        barcode = code128.Code128(
            job_reference, barHeight=10 * mm, barWidth=.5 * mm)

        barcode.drawOn(self, 135 * mm, 280 * mm)
