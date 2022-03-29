import io
from reportlab.graphics.barcode import code128
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("Calibri", "Calibri.ttf"))
pdfmetrics.registerFont(TTFont("Calibri-Bold", "Calibrib.ttf"))

class A4Page(canvas.Canvas):
    def __init__(self, packet: io.BytesIO) -> None:
        super().__init__(packet, pagesize=A4, pageCompression=1)
        self.setFillColorRGB(0,0,0)        

    def draw_job_reference_on_page(self, job_reference: str) -> None:
        self.setFont("Calibri", 11)
        self.drawString(162*mm, 275*mm, job_reference)

    def draw_paperwork_type_on_page(self, paperwork_type: str) -> None:
        self.setFont("Calibri-Bold", 22)
        self.drawString(5*mm, 280*mm, paperwork_type)

    def draw_image_on_page(self, image_path: str) -> None:
        self.drawImage(
            image_path, -85, 25, 
            width = 730, height = 730, 
            mask = None, preserveAspectRatio = True
        )

    def draw_barcode_on_page(self, job_reference: str) -> None:
        barcode = code128.Code128(
            job_reference, barHeight = 10*mm, barWidth = .5*mm)
        
        barcode.drawOn(self, 135*mm, 280*mm)
