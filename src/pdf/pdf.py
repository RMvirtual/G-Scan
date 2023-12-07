import pdf.page

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
