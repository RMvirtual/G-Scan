from src.main.pdf.reader import PdfReader
from src.main.pdf.writer import PdfWriter

class PdfExtractor():
    def __init__(self, stream):
        self.__stream = stream

    def extract_page(self, page_number: int, output_path: str) -> None:
        """Extracts a single page from a pdf and saves it."""

        extracted_page = self.__get_page_from_pdf_reader(page_number)
        self.__write_page_object_to_new_pdf(extracted_page, output_path)

    def __get_page_from_pdf_reader(self, page_number):
        """Gets a page object using a pdf reader."""

        pdf_reader = PdfReader(self.__stream)
        extracted_page = pdf_reader.getPage(page_number)

        return extracted_page

    def __write_page_object_to_new_pdf(
            self, page_object, output_path) -> None:
        """Writes a page object to an output path."""

        page_writer = PdfWriter()
        page_writer.addPage(page_object)

        with open(output_path, "wb") as output_stream:
            page_writer.write(output_stream)