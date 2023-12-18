import io

import file_system
from file_system import DirectoryItem
from pdf.extractor import PdfExtractor
from pdf.writer_old import PdfWriter


class CustomerPaperworkPDFWriter(PdfWriter):
    def __init__(self):
        super().__init__()

    def write_to_file(
            self, source: str, output: str, job_reference: str) -> None:
        file = DirectoryItem(source)

        if file.is_pdf():
            self._pdf_to_customer_paperwork(file, output, job_reference)

        elif file.is_single_page_image_format():
            self._png_to_customer_paperwork(file, output, job_reference)

    def _pdf_to_customer_paperwork(
            self, source: DirectoryItem, output: str,
            job_reference: str) -> str:
        self._add_file_content(source, job_reference)
        self._save_pdf(output)

    def _png_to_customer_paperwork(
            self, source: DirectoryItem, output: str,
            job_reference: str) -> None:
        extracted_image = self.save_image_as_png_to_temp_directory(source)

        paperwork_bytes = self._customer_paperwork_bytes(
            job_reference, extracted_image)

        new_page = PdfReader(paperwork_bytes).getPage(0)
        self.addPage(new_page)
        self._save_pdf(output)

    def _add_file_content(self, source: DirectoryItem, job_reference: str):
        with open(source.full_path(), "rb") as input_stream:
            self._stream_to_pages(input_stream, job_reference)

    def _stream_to_pages(
            self, input_stream: io.BufferedReader, job_reference: str) -> None:
        temp_directory = file_system.temp_directory()
        reader = PdfReader(input_stream)
        number_of_pages = reader.number_of_pages()

        for page_number in range(number_of_pages):
            self._extract_page_from_pdf(input_stream, page_number)

            extracted_pdf = temp_directory + "/temp.pdf"
            extracted_png = temp_directory + "/temp_image.png"

            self.convert_single_page_pdf_to_png(
                extracted_pdf, extracted_png)

            packet = self._customer_paperwork_bytes(
                job_reference, extracted_png)

            new_pdf_page = PdfReader(packet).getPage(0)
            self.addPage(new_pdf_page)

    def _extract_page_from_pdf(
            self, input_stream: io.BufferedReader, page_number: int) -> None:
        temp_directory = file_system.temp_directory()
        extracted_page_as_pdf = temp_directory + "/temp.pdf"
        pdf_extractor = PdfExtractor(input_stream)
        pdf_extractor.extract_page(page_number, extracted_page_as_pdf)

    def _save_pdf(self, output_path: str):
        with open(output_path, "wb") as output_stream:
            self.write(output_stream)

    def _customer_paperwork_bytes(
            self, job_reference: str, image_png: str) -> io.BytesIO:
        packet = io.BytesIO()
        CustomerPaperworkPage(packet, job_reference, image_png)
        packet.seek(0)

        return packet
