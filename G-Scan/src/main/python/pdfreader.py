"""A module containing functions for reading PDF files."""

import filesystem
import os
import pdfwriter
import PyPDF2
import re
from PIL import Image as pil_image
from popupbox import PopupBox
from pyzbar.pyzbar import decode
from wand.image import Image as wand_image

def barcode_scanner(master_application, file_index, file_list):
    scan_dir = master_application.current_user.scan_directory
    multi_page_handling = master_application.multi_page_mode.get()
    barcode_ref_list = []
    
    if not master_application.file_list:
        if master_application.file_index == 0:
            PopupBox(master_application, "Guess What",
                "No more files remaining.",
                "230", "75")
            
            master_application.pdf_viewer.close()
    else:
        file = master_application.file_list[master_application.file_index]
        file_name, file_extension = os.path.splitext(master_application.file)
        master_application.insert_file_attributes(file_name, file_extension)

        if file_extension.lower() == ".pdf":
            barcode_ref_list = read_barcodes(master_application.file, scan_dir)

        elif file_extension.lower() == ".jpeg" or file_extension.lower() == ".jpg" or file_extension.lower() == ".png":
            barcode_ref_list = image_barcode_reader(master_application.file, scan_dir)

        # if no GR reference obtained, display the image for user to manually type in the reference
        if not barcode_ref_list:
            master_application.write_log("No barcode found")
            master_application.pdf_viewer.show_image(master_application, master_application.file, master_application.current_user.scan_directory)

        # if more than 1 GR reference obtained, split it apart and show the image
        elif len(barcode_ref_list) > 1:
            master_application.write_log("Too many conflicting barcodes?")
            
            split_file_list = pdfwriter.document_splitter(
                master_application, file, scan_dir, "Split")
            
            if split_file_list:
                del master_application.file_list[master_application.file_index]
                for file in reversed(split_file_list):
                    master_application.file_list.insert(master_application.file_index, file)

            file = master_application.file_list[master_application.file_index]
            
            master_application.pdf_viewer.show_image(
                master_application, master_application.file, master_application.current_user.scan_directory)

        # if 1 GR reference obtained, use this as the user input
        elif len(barcode_ref_list) == 1:
            job_ref = barcode_ref_list[0]
            
            master_application.write_log(
                "Barcode " + job_ref + " found successfully")
            
            master_application.submit(job_ref, manual_submission = False)

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
            
            temp_directory = filesystem.get_temp_directory()
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
