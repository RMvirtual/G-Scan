"""Module for creating a PDFWriter class."""

import io
from pathlib import Path

from PyPDF2.utils import PdfReadWarning
from app import file_system
from app.file_system import DirectoryItem
import os
import PyPDF2
import shutil
from PIL import Image as PILImage
from wand.image import Image as WandImage
from pdf.paperwork_types import CustomerPaperworkPage
from pdf.pdf_reader import PdfReader

def create_loading_list_pod(master_application, file, scan_dir,
        dest_dir, dest_file_name, dest_duplicate_check):
    """Moves a loading list or POD with correct naming convention
    without having to modify the document other than PDF conversion."""

    file_name, file_extension = os.path.splitext(file)
    temp_directory = file_system.get_temp_directory()

    # PDF files should be fine for a straight move
    if file_extension.lower() == ".pdf":
        shutil.copyfile(
            scan_dir + "/" + file, temp_directory + "result.pdf")

    # just image files need converting.
    if file_extension.lower() == ".jpeg" or file_extension.lower() == ".jpg" or file_extension.lower() == ".png":
        with PILImage.open(scan_dir + "/" + file) as img:
            output = PyPDF2.PdfFileWriter()
            temporary_image = temp_directory + file_name + ".png"
            img.save(temporary_image)
            img.close()

        final_image = temp_directory + "temp_image.png"

        # arrange page into portrait orientation
        with wand_image(filename = temporary_image, resolution = 200) as img_simulator:
            if img_simulator.width > img_simulator.height:
                img_simulator.rotate(270)
                img_simulator.save(filename = final_image)
            else:
                img_simulator.save(filename = final_image)

        packet = io.BytesIO()
        slab = canvas.Canvas(packet, pagesize = A4, pageCompression = 1)
        slab.setFillColorRGB(0,0,0)
        slab.drawImage(final_image, -110, 20, width = 815, height = 815, mask = None, preserveAspectRatio = True)
        slab.save()

        packet.seek(0)
        new_pdf = PyPDF2.PdfFileReader(packet)

        output.addPage(new_pdf.getPage(0))

        output_stream = open(temp_directory + "/" + "result.pdf", "wb")
        output.write(output_stream)
        output_stream.close()

def document_splitter(master_application, file, scan_dir,
        multi_page_handling):
    file_name, file_extension = os.path.splitext(file)
    split_file_list = [file]
    
    # split PDF into smaller PDFs
    if file_extension.lower() == ".pdf" and multi_page_handling == "Split":
        split_file_list = split_pdf_document(
            master_application, file, scan_dir)
        
    return split_file_list

def manual_document_splitter(master_application):
    file = master_application.file
    scan_dir = master_application.current_user.scan_directory
    multi_page_handling = "Split"

    split_file_list = document_splitter(
        master_application, file, scan_dir, multi_page_handling)

    del master_application.file_list[master_application.file_index]
    for file in reversed(split_file_list):
        master_application.file_list.insert(master_application.file_index, file)

    master_application.file = master_application.file_list[master_application.file_index]
    file_name, file_ext = os.path.splitext(master_application.file)

    master_application.pdf_viewer.show_image(master_application, master_application.file, master_application.current_user.scan_directory)
    
    master_application.insert_file_attributes(file_name, file_ext)
    master_application.user_input_entry_box.focus_set()

def split_pdf_document(master_application, file, scan_dir):
    split_file_list = [file]
    file_name, file_extension = os.path.splitext(file)
    
    with open(scan_dir + "/" + file, "rb") as current_file_pdf:
        current_file_pdf_reader = PyPDF2.PdfFileReader(current_file_pdf)
        
        current_file_page_amount = current_file_pdf_reader.getNumPages()

        if current_file_page_amount > 1:
            master_application.write_log("Splitting apart " + file)
            split_file_list.remove(file)
            page_counter = 0
            
            for page_number in range(current_file_page_amount):
                page_counter += 1
                split_pdf_holder = PyPDF2.PdfFileWriter()
                split_pdf_holder.addPage(current_file_pdf_reader.getPage(page_number))

                split_pdf_file_name = file_name + "_" + str(page_counter) + file_extension
                with open(scan_dir + "/" + split_pdf_file_name, "wb") as split_pdf_file:
                    split_pdf_holder.write(split_pdf_file)
                split_pdf_file.close()
                master_application.write_log("Created " + split_pdf_file_name)

                split_file_list.append(split_pdf_file_name)
                                    
            current_file_pdf.close()
            os.remove(scan_dir + "/" + file)
    
    return split_file_list

def image_converter(master_application, file, scan_dir, multi_page_handling):
    """Converts image files into PDF format and returns the
    PDF file."""
    file_name, file_extension = os.path.splitext(file)
    pdf_file = file
    
    if file_extension.lower() == ".tif" or file_extension.lower() == ".tiff":
        master_application.write_log("Converting " + file)
        
        with pil_image.open(scan_dir + "/" + file) as img:
            img_page_amount = img.n_frames

            output = PyPDF2.PdfFileWriter()

            page_counter = 0

            for page_number in range(img_page_amount):
                img.seek(page_number)
                temporary_png = master_application.temp_dir + "/" + file_name + ".png"
                img.save(temporary_png)

                final_image = master_application.temp_dir + "/" + "temp_image.png"
                
                # ensures page is nearest thing possible to portrait orientation
                with wand_image(filename = temporary_png, resolution = 300) as img_simulator:
                    if img_simulator.width > img_simulator.height:
                        img_simulator.rotate(270)
                        img_simulator.save(filename = final_image)
                    else:
                        img_simulator.save(filename = final_image)

                packet = io.BytesIO()
                slab = canvas.Canvas(packet, pagesize = A4, pageCompression = 1)
                slab.setFillColorRGB(0,0,0)
                slab.drawImage(final_image, -110, 20, width = 815, height = 815, mask = None, preserveAspectRatio = True)
                slab.save()

                packet.seek(0)
                new_pdf = PyPDF2.PdfFileReader(packet)

                output.addPage(new_pdf.getPage(0))

            pdf_file = file_name + ".pdf"

            with open(scan_dir + "/" + pdf_file, "wb") as output_stream:
                output.write(output_stream)
            output_stream.close()
            master_application.write_log("Created " + pdf_file)
            img.close()
            os.remove(scan_dir + "/" + file)

    if file_extension.lower() == ".jpeg" or file_extension.lower() == ".jpg" or file_extension.lower() == ".png":
        master_application.write_log("Converting " + file)
        
        with pil_image.open(scan_dir + "/" + file) as img:
            output = PyPDF2.PdfFileWriter()
            temporary_image = master_application.temp_dir + "/" + file_name + ".png"
            img.save(temporary_image)

        final_image = master_application.temp_dir + "/" + "temp_image.png"
        # arrange page into portrait orientation
        with wand_image(filename = temporary_image, resolution = 300) as img_simulator:
            if img_simulator.width > img_simulator.height:
                img_simulator.rotate(270)
                img_simulator.save(filename = final_image)
            else:
                img_simulator.save(filename = final_image)

        packet = io.BytesIO()
        slab = canvas.Canvas(packet, pagesize = A4, pageCompression = 1)
        slab.setFillColorRGB(0,0,0)
        slab.drawImage(final_image, -110, 20, width = 815, height = 815, mask = None, preserveAspectRatio = True)
        slab.save()

        packet.seek(0)
        new_pdf = PyPDF2.PdfFileReader(packet)

        output.addPage(new_pdf.getPage(0))

        pdf_file = file_name + ".pdf"

        with open(scan_dir + "/" + pdf_file, "wb") as output_stream:
            output.write(output_stream)
        output_stream.close()
        master_application.write_log("Created " + pdf_file)
        os.remove(scan_dir + "/" + file)

    return pdf_file

def upload_doc(file, scan_dir, dest_dir,
        dest_file_name, dest_duplicate_check):
    """If duplicate file already exists in the destination directory,
    merge the pages together."""

    temp_directory = file_system.get_temp_directory()

    if dest_duplicate_check:
        temp_file_writer = PyPDF2.PdfFileWriter()

        dest_file_object = open(dest_dir + "/" + dest_file_name, "rb")
        dest_file_reader = PyPDF2.PdfFileReader(dest_file_object)

        for pageNum in range(0, dest_file_reader.numPages):
            page_object = dest_file_reader.getPage(pageNum)
            temp_file_writer.addPage(page_object)

        result = open(temp_directory + "result.pdf", "rb")
        result_reader = PyPDF2.PdfFileReader(result)

        for page_number in range(0, result_reader.numPages):
            result_page = result_reader.getPage(page_number)
            temp_file_writer.addPage(result_page)

        temp_file = open(temp_directory + "temp.pdf", "wb")
        temp_file_writer.write(temp_file)
        temp_file.close()
                        
        result.close()
        dest_file_object.close()
        
        shutil.move(
            temp_directory + "temp.pdf", dest_dir + "/" + dest_file_name)

        os.remove(scan_dir + "/" + file)

        return True
        
    # If duplicate file does not already exist, straightforward moves
    # the current file to the dest folder.
    elif not dest_duplicate_check:
        shutil.move(
            temp_directory + "result.pdf", dest_dir + "/" + dest_file_name)

        os.remove(scan_dir + "/" + file)

        return True

class PdfWriter(PyPDF2.PdfFileWriter):
    """Writes PDF files."""

    def __init__(self):
        """Creates a new PDF Writer object."""

        super().__init__()

    def save_image_as_png_to_temp_directory(self,
            directory_item: DirectoryItem) -> str:
        file_name = directory_item.get_file_name()
        temp_dir = str(file_system.get_temp_directory())

        with WandImage(filename=str(directory_item), resolution=300) as img:
            temp_image_path = temp_dir + "/" + file_name + ".png"
            self.rotate_image_to_portrait(img)
            img.save(filename=temp_image_path)
            img.close()

        return temp_image_path

    def convert_single_page_pdf_to_png(self, pdf_path: str, output_path: str):
        with WandImage(filename = pdf_path, resolution = 300) as image:
            self.rotate_image_to_portrait(image)
            image.save(filename = output_path)

    def rotate_image_to_portrait(self, image: WandImage):
        is_landscape = (image.width > image.height)

        if is_landscape:
            image.rotate(270)

    def extract_page_from_pdf_reader(self, pdf_reader: PdfReader,
            page_number: int, output_path: str) -> None:
        """Extracts a single page from a pdf reader object and saves it."""
        
        page = pdf_reader.getPage(page_number)

        extracted_page_writer = PdfWriter()
        extracted_page_writer.addPage(page)

        with open(output_path, "wb") as extracted_pdf_page:
            extracted_page_writer.write(extracted_pdf_page)

class CustomerPaperworkPDFWriter(PdfWriter):
    def __init__(self):
        super().__init__()

    def create_pdf(
            self, source_path: str, destination_path: str,
            job_reference: str) -> None:
        """Creates a new customer paperwork PDF file."""
        
        directory_item = DirectoryItem(source_path)

        is_pdf = directory_item.check_if_file_extension_matches(".pdf")
        is_image_file = file_system.is_file_single_page_image_format(
            directory_item)
        
        if is_pdf:
            output_file_path = self.convert_pdf_to_customer_paperwork(
                source_path, destination_path, job_reference)
            
            return output_file_path

        # Image file extensions exclude TIF as these will always be
        # pre-processed into PDFs by the document splitter function.
        elif is_image_file:
            output_file_path = self.convert_png_to_customer_paperwork(
                directory_item, destination_path, job_reference)

            return output_file_path

    def convert_pdf_to_customer_paperwork(self, source_path: str,
            destination_directory: str,
            job_reference: str) -> str:
        """Opens a pdf file as a file stream and converts it into
        customer paperwork format containing a heading and a barcoded
        job reference.
        """

        with open(source_path, "rb") as pdf_stream:     
            self.convert_pdf_stream_to_customer_paperwork_file_writer_object(
                pdf_stream, job_reference)

        output_path = destination_directory + "\\result.pdf"

        with open(output_path, "wb") as output_stream:
            self.write(output_stream)

        return output_path

    def convert_png_to_customer_paperwork(
            self, directory_item, destination_directory, job_reference):

        paperwork_image_path = self.save_image_as_png_to_temp_directory(
            directory_item)

        packet = self.create_customer_paperwork_bytes_packet(
            job_reference, paperwork_image_path)
        
        new_pdf_page = PdfReader(packet).getPage(0)
        output = PdfWriter()
        output.addPage(new_pdf_page)

        with open(destination_directory + "\\result.pdf", "wb") \
                as output_stream:
            output.write(output_stream)

        return destination_directory + "\\result.pdf"

    def convert_pdf_stream_to_customer_paperwork_file_writer_object(
            self, stream, job_reference: str) -> None:
        """Converts all the pages in a PDF file into customer paperwork
        format."""

        temp_directory = str(file_system.get_temp_directory())
        pdf_reader = PdfReader(stream)        
        number_of_pages = pdf_reader.getNumPages()

        for page_number in range(number_of_pages):
            working_pdf_path = temp_directory + "/temp.pdf"

            self.extract_page_from_pdf_reader(
                pdf_reader, page_number, working_pdf_path)
            
            paperwork_image_path = temp_directory + "/temp_image.png"
            
            self.convert_single_page_pdf_to_png(
                working_pdf_path, paperwork_image_path)

            packet = self.create_customer_paperwork_bytes_packet(
                job_reference, paperwork_image_path)

            new_pdf_page = PdfReader(packet).getPage(0)
            self.addPage(new_pdf_page)

    def create_customer_paperwork_bytes_packet(self, job_reference,
            paperwork_image_path) -> io.BytesIO:
        """Creates a bytes packet containing data required to write a
        customer paperwork page.
        """

        packet = io.BytesIO()
        page = CustomerPaperworkPage(packet, job_reference, paperwork_image_path)
        packet.seek(0)

        return packet