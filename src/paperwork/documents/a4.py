from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm


class A4Document:
    def __init__(self, file_name: str) -> None:
        self._initialise_canvas(file_name)

    def _initialise_canvas(self, file_name):
        self.canvas = canvas.Canvas(
            filename=file_name,
            pagesize=A4,
            pageCompression=1
        )

        self.canvas.setFillColorRGB(0, 0, 0)

    def draw_page(self, image_path: str):
        self.draw_image(image_path=image_path, width_mm=210, height_mm=297)
        self.next_page()

    def draw_image(
            self, image_path: str, width_mm: int, height_mm: int,
            x: int = 0, y: int = 0) -> None:
        self.canvas.drawImage(
            image=image_path,
            x=x, y=y,
            width=width_mm*mm, height=height_mm*mm,
            mask=None, preserveAspectRatio=True
        )

    def next_page(self):
        self.canvas.showPage()

    def save(self):
        self.canvas.save()
