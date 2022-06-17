import fitz


class Page:
    def __init__(self, pixmap: fitz.Pixmap):
        self._pixmap = pixmap

    def width(self):
        return self._width

    def height(self):
        return self._height

    def to_pil_bytes(self):
        return self._pixmap.pil_tobytes(output="png")

    def save(self, output_path: str):
        self._pixmap.pil_save(output_path)