import io

import src.main.app.file_system as file_system
from src.main.app.file_system import DirectoryItem
from src.main.paperwork.types import CustomerPaperworkPage
from src.main.pdf.reader import PdfReader
from src.main.pdf.extractor import PdfExtractor
from src.main.pdf.writer import PdfWriter

class CustomerPaperworkPDFWriter(PdfWriter):
    def __init__(self):
        super().__init__()

    def create_pdf(
            self, source_path: str, output_path: str,
            job_reference: str) -> None:
        """Creates a new customer paperwork PDF file."""
        
        directory_item = DirectoryItem(source_path)

        is_pdf = directory_item.check_if_file_extension_matches(".pdf")
        is_image_file = file_system.is_file_single_page_image_format(
            directory_item)
        
        if is_pdf:
            self.__convert_pdf_to_customer_paperwork(
                source_path, output_path, job_reference)

        # Image file extensions exclude TIF as these will always be
        # pre-processed into PDFs by the document splitter function.
        elif is_image_file:
            self.__convert_png_to_customer_paperwork(
                directory_item, output_path, job_reference)

    def __convert_pdf_to_customer_paperwork(self, source_path: str,
            output_path: str, job_reference: str) -> str:
        """Opens a pdf file as a file stream and converts it into
        customer paperwork format containing a heading and a barcoded
        job reference.
        """

        self.__add_file_content_to_buffer(
            source_path, job_reference)
        
        self.__write_buffered_content(output_path)

    def __add_file_content_to_buffer(
            self, source_path, job_reference):
        """Takes a source path to a pdf file and converts it into
        customer paperwork format, writing it to this objects buffer
        to be outputted to a pdf file later.
        """

        with open(source_path, "rb") as pdf_stream:     
            self.__convert_pdf_stream_to_content_buffer(
                pdf_stream, job_reference)

    def __write_buffered_content(self, output_path):
        """Takes the content written to this object's buffer and writes
        it to an output path."""

        with open(output_path, "wb") as output_stream:
            self.write(output_stream)

    def __convert_png_to_customer_paperwork(
            self, directory_item, output_path, job_reference) -> None:
        """Converts a png into customer paperwork format."""

        paperwork_image_path = self.save_image_as_png_to_temp_directory(
            directory_item)

        packet = self.__create_customer_paperwork_bytes_packet(
            job_reference, paperwork_image_path)
        
        new_pdf_page = PdfReader(packet).getPage(0)
        output = PdfWriter()
        output.addPage(new_pdf_page)

        with open(output_path, "wb") as output_stream:
            output.write(output_stream)

    def __convert_pdf_stream_to_content_buffer(
            self, stream, job_reference: str) -> None:
        """Converts all the pages in a PDF file into customer paperwork
        format."""

        temp_directory = str(file_system.get_temp_directory())
        pdf_reader = PdfReader(stream)        
        number_of_pages = pdf_reader.get_number_of_pages()

        for page_number in range(number_of_pages):
            working_pdf_path = temp_directory + "/temp.pdf"

            pdf_extractor = PdfExtractor(stream)
            pdf_extractor.extract_page(page_number, working_pdf_path)
            
            paperwork_image_path = temp_directory + "/temp_image.png"
            
            self.convert_single_page_pdf_to_png(
                working_pdf_path, paperwork_image_path)

            packet = self.__create_customer_paperwork_bytes_packet(
                job_reference, paperwork_image_path)

            new_pdf_page = PdfReader(packet).getPage(0)
            self.addPage(new_pdf_page)

    def __create_customer_paperwork_bytes_packet(self, job_reference,
            paperwork_image_path) -> io.BytesIO:
        """Creates a bytes packet containing data required to write a
        customer paperwork page.
        """

        packet = io.BytesIO()
        page = CustomerPaperworkPage(
            packet, job_reference, paperwork_image_path)
        
        packet.seek(0)

        return packet