from src.main.pdf.reader import PdfReader
from src.main.pdf.writer import PdfWriter
from PyPDF2.pdf import PageObject

class PdfExtractor():
    def __init__(self, stream):
        self.__stream = stream

    def extract_page(self, page_number: int, output_path: str) -> None:
        page = self.__read_page(page_number)
        self.__page_to_pdf(page, output_path)

    def __read_page(self, page_number) -> PageObject:
        pdf_reader = PdfReader(self.__stream)
        
        return pdf_reader.getPage(page_number)

    def __page_to_pdf(self, page_object, output_path) -> None:
        page_writer = PdfWriter()
        page_writer.addPage(page_object)

        with open(output_path, "wb") as output_stream:
            page_writer.write(output_stream)