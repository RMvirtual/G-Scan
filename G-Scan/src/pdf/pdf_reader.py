"""A module containing functions for reading PDF files."""

from app import file_system
from gui.popupbox import PopupBox
from PIL import Image as pil_image
from pyzbar.pyzbar import decode
from wand.image import Image as wand_image
import PyPDF2
import os
import re

class PdfReader(PyPDF2.PdfFileReader):
    def __init__(self, stream):
        """Creates a new PDF Reader file."""

        super().__init__(stream)
        self.__stream = stream

    def get_number_of_pages(self):
        """Returns the number of pages in the pdf."""

        return self.getNumPages()

def read_barcodes(file_name, directory):
    """Reads barcodes on each page of a PDF file and returns them as
    a list."""
    barcode_ref_list = []

    with open(directory + "/" + file_name, "rb") as current_file_pdf:
        current_file_pdf_reader = PyPDF2.PdfFileReader(current_file_pdf)
        current_file_page_amount = current_file_pdf_reader.getNumPages()

        for page_number in range(current_file_page_amount):

            page_object = current_file_pdf_reader.getPage(page_number)
            temp_file_writer = PyPDF2.PdfFileWriter()
            temp_file_writer.addPage(page_object)
            
            temp_directory = file_system.get_temp_directory()
            temp_file_path = temp_directory + "temp.pdf"

            with open(temp_file_path, "wb") as temp_file:
                temp_file_writer.write(temp_file)

            scan_doc = temp_directory + "temp.pdf"
            cust_pw = temp_directory + "temp_image.png"

            with wand_image(filename = scan_doc, resolution = 300) as img:
                img.save(filename = cust_pw)

            barcode_reader = decode(pil_image.open(cust_pw, "r"))

            for barcode in barcode_reader:
                job_ref = re.sub("[^0-9GR]", "", str(barcode.data).upper())

                if (len(job_ref) == 11 and job_ref[:2].upper() == "GR"
                        and job_ref not in barcode_ref_list):
                    barcode_ref_list.append(job_ref)

    return barcode_ref_list

def image_barcode_reader(self, file, scan_dir):
    """Reads barcodes on PNG, JPEG, JPG image files. TIFs should
    already be pre-converted to PDF."""
    
    barcode_ref_list = []
    
    barcode_reader = decode(pil_image.open(scan_dir + "/" + file, "r"))

    for barcode in barcode_reader:
        job_ref = re.sub("[^0-9GR]", "", str(barcode.data).upper())

        if (len(job_ref) == 11 and job_ref[:2].upper() == "GR"
                and job_ref not in barcode_ref_list):
            barcode_ref_list.append(job_ref)

    return barcode_ref_list
