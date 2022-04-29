from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


class A4Document(canvas.Canvas):
    def __init__(self, file_name: str) -> None:
        super().__init__(filename=file_name, pagesize=A4, pageCompression=1)
        self.setFillColorRGB(0, 0, 0)

    def draw_image(self, image_path: str) -> None:
        self.drawImage(
            image=image_path,
            x=-85, y=25,
            width=730, height=730,
            mask=None, preserveAspectRatio=True
        )

    def next_page(self):
        self.showPage()
