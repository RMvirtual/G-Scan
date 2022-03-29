import io

import src.main.file_system.file_system as file_system
from src.main.file_system.file_system import DirectoryItem
from src.main.paperwork.page_types.customer_paperwork import (
    CustomerPaperworkPage)

from src.main.pdf.reader import PdfReader
from src.main.pdf.extractor import PdfExtractor
from src.main.pdf.writer import PdfWriter

class CustomerPaperworkPDFWriter(PdfWriter):
    def __init__(self):
        super().__init__()

    def write_to_file(self, source:str, output:str, job_reference:str) -> None:
        file = DirectoryItem(source)
        
        if file.is_pdf():
            self.__pdf_to_customer_paperwork(file, output, job_reference)

        elif file.is_single_page_image_format():
            self.__png_to_customer_paperwork(file, output, job_reference)

    def __pdf_to_customer_paperwork(
            self, source:DirectoryItem, output: str, job_reference: str) -> str:
        self.__add_file_content(source, job_reference)
        self.__save_pdf(output)

    def __png_to_customer_paperwork(
            self, directory_item:DirectoryItem, output:str,
            job_reference:str) -> None:
        paperwork_image_path = self.save_image_as_png_to_temp_directory(
            directory_item)

        packet = self.__customer_paperwork_bytes(
            job_reference, paperwork_image_path)
        
        new_pdf_page = PdfReader(packet).getPage(0)
        self.addPage(new_pdf_page)
        self.__save_pdf(output)

    def __add_file_content(self, source:DirectoryItem, job_reference:str):
        with open(source.full_path(), "rb") as input_stream:
            self.__pdf_stream_to_page(input_stream, job_reference)

    def __pdf_stream_to_page(
            self, input_stream:io.BufferedReader, job_reference:str) -> None:
        temp_directory = str(file_system.temp_directory())
        pdf_reader = PdfReader(input_stream)
        number_of_pages = pdf_reader.get_number_of_pages()

        for page_number in range(number_of_pages):
            extracted_page_path = temp_directory + "/temp.pdf"
            extracted_page_as_png = temp_directory + "/temp_image.png"

            pdf_extractor = PdfExtractor(input_stream)
            pdf_extractor.extract_page(page_number, extracted_page_path)
            
            self.convert_single_page_pdf_to_png(
                extracted_page_path, extracted_page_as_png)
            
            packet = self.__customer_paperwork_bytes(
                job_reference, extracted_page_as_png)
            
            new_pdf_page = PdfReader(packet).getPage(0)
            self.addPage(new_pdf_page)

    def __customer_paperwork_bytes(
            self, job_reference:str, image_png:str) -> io.BytesIO:
        packet = io.BytesIO()
        CustomerPaperworkPage(packet, job_reference, image_png)
        packet.seek(0)

        return packet

    def __save_pdf(self, output_path:str):
        with open(output_path, "wb") as output_stream:
            self.write(output_stream)