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


class Pdf:
    def __init__(self, page_images: list = None):
        self._initialise_pages(page_images)

    def _initialise_pages(self, page_images: list):
        if not page_images:
            page_images = []

        self._page_images = page_images

    def number_of_pages(self) -> int:
        return len(self._page_images)

    def page(self, page_no: int):
        return self._page_images[page_no]

    def pages(self):
        return self._page_images

    def append(self, pixmap):
        self._page_images.append(pixmap)
