import fitz


class PdfReader:
    def __init__(self, source: str):
        self._pdf_stream = fitz.Document(source)
        self._pages = []

        number_of_pages = self._pdf_stream.page_count

        for page_no in range(number_of_pages):
            page = self._pdf_stream.load_page(page_no)
            pixels = fitz.utils.get_pixmap(page, dpi=300)
            self._pages.append(pixels)

        self._pdf_stream.close()

    def number_of_pages(self) -> int:
        return len(self._pages)

    def page(self, page_no: int):
        return self._pages[page_no]

    def pages(self) :
        return self._pages

    def close(self) -> None:
        self._pdf_stream.close()
