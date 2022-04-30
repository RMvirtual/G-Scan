from src.main.paperwork.documents.a4 import A4Document
from reportlab.graphics.barcode import code128
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("Calibri", "Calibri.ttf"))
pdfmetrics.registerFont(TTFont("Calibri-Bold", "Calibrib.ttf"))


class CustomerPaperwork(A4Document):
    def __init__(self, file_name, job_reference):
        super().__init__(file_name=file_name)
        self._job_reference = job_reference

    def draw_page(self, image_path: str):
        self._draw_title("Customer Paperwork")
        self._draw_barcode(self._job_reference)
        self._draw_job_reference(self._job_reference)
        self._draw_scaled_image(image_path)

        self.next_page()

    def _draw_scaled_image(self, image_path):
        a4_width, bottom_padding, image_height = self._scaled_image_height()

        self.draw_image(
            image_path=image_path, width_mm=a4_width,
            height_mm=image_height, y=bottom_padding
        )

    def _scaled_image_height(self):
        a4_width = 210
        a4_height = 297
        top_padding = 20
        bottom_padding = 25
        image_height = a4_height - (top_padding + bottom_padding)

        return a4_width, bottom_padding, image_height

    def _draw_title(self, paperwork_type: str) -> None:
        self.canvas.setFont("Calibri-Bold", 22)
        self.canvas.drawString(x=20*mm, y=275*mm, text=paperwork_type)

    def _draw_barcode(self, job_reference: str) -> None:
        barcode = code128.Code128(
            value=job_reference, barHeight=10*mm, barWidth=.5*mm)

        barcode.drawOn(canvas=self.canvas, x=130*mm, y=270*mm)

    def _draw_job_reference(self, job_reference: str) -> None:
        self.canvas.setFont("Calibri", 11)
        self.canvas.drawString(x=155*mm, y=265*mm, text=job_reference)
