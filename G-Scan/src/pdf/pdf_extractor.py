from pdf.pdf_reader import PdfReader
from pdf.pdf_writer import PdfWriter

class PdfExtractor():
    def __init__(self):
        pass

    def extract_page(self, stream, page_number: int,
            output_path: str) -> None:
        """Extracts a single page from a pdf and saves
        it."""

        pdf_reader = PdfReader(stream)
        extracted_page = pdf_reader.getPage(page_number)

        page_writer = PdfWriter()
        page_writer.addPage(extracted_page)

        with open(output_path, "wb") as extracted_pdf_page:
            page_writer.write(extracted_pdf_page)