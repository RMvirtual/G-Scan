import PyPDF2


class PdfReader:
    def __init__(self, source: str):
        self._pdf_stream = open(file=source, mode="rb")
        pdf_reader = PyPDF2.PdfFileReader(stream=self._pdf_stream)
        self._pages = []

        number_of_pages = pdf_reader.getNumPages()

        for page_no in range(number_of_pages):
            self._pages.append(pdf_reader.getPage(page_no))

    def number_of_pages(self) -> int:
        return len(self._pages)

    def page(self, page_no: int) -> PyPDF2.pdf.PageObject:
        return self._pages[page_no]

    def pages(self) -> list[PyPDF2.pdf.PageObject]:
        return self._pages

    def close(self) -> None:
        self._pdf_stream.close()