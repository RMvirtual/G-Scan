"""Module for creating a PDFWriter class."""

from pathlib import Path
from app import file_system
import io
import os
import PyPDF2
import shutil
from PIL import Image as pil_image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, A3
from reportlab.lib.units import mm
from reportlab.graphics.barcode import code128
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from wand.image import Image as wand_image

pdfmetrics.registerFont(TTFont("Calibri", "Calibri.ttf"))
pdfmetrics.registerFont(TTFont("Calibri-Bold", "Calibrib.ttf"))

class PdfWriter(PyPDF2.PdfFileWriter):
    """Writes PDF files."""

    def __init__(self):
        """Creates a new PDF Writer object."""

        super().__init__()

    def create_cust_pw(self, pdf_file_path: str, scan_dir: str, dest_dir: str,
            job_ref: str):
        """Creates the customer paperwork page."""

        file_name, file_extension = os.path.splitext(pdf_file_path)
        is_pdf = (file_extension.lower() == ".pdf")

        image_file_extensions = (".jpeg", ".jpg", ".png")
        is_image_file = (file_extension.lower() in image_file_extensions)

        temp_dir = str(file_system.get_temp_directory())

        # Document generation for PDFs
        if is_pdf:
            output_file_path = self.convert_pdf_to_customer_paperwork(
                pdf_file_path, temp_dir, dest_dir, job_ref)
            
            return output_file_path

        # document generation for image files (excluding TIF as these will always be pre-processed into PDFs by the document splitter function)
        elif is_image_file:
            with pil_image.open(scan_dir + "/" + pdf_file_path) as img:
                output = PyPDF2.PdfFileWriter()
                temporary_png = temp_dir + "/" + file_name + ".png"
                img.save(temporary_png)
                img.close()

            working_image_path = temp_dir + "/temp_image.png"

            # arrange page into portrait orientation
            with wand_image(filename = temporary_png, resolution = 200) as img_simulator:
                if img_simulator.width > img_simulator.height:
                    img_simulator.rotate(270)
                    img_simulator.save(filename = working_image_path)
                else:
                    img_simulator.save(filename = working_image_path)

            packet = io.BytesIO()
            page = canvas.Canvas(packet, pagesize = A4, pageCompression = 1)
            page.setFillColorRGB(0,0,0)
            barcode = code128.Code128(job_ref, barHeight = 10*mm, barWidth = .5*mm)
            barcode.drawOn(page, 135*mm, 280*mm)

            page.setFont("Calibri", 11)
            page.drawString(162*mm, 275*mm, job_ref)
            page.setFont("Calibri-Bold", 22)
            page.drawString(5*mm, 280*mm, "Customer Paperwork")
            page.drawImage(working_image_path, -85, 25, width = 730, height = 730, mask = None, preserveAspectRatio = True)

            page.save()

            packet.seek(0)
            new_pdf = PyPDF2.PdfFileReader(packet)

            output.addPage(new_pdf.getPage(0))

            output_stream = open(temp_dir + "/" + "result.pdf", "wb")
            output.write(output_stream)
            output_stream.close()

            return (temp_dir + "/result.pdf")

    def convert_pdf_to_customer_paperwork(self, file_path: str,
            temporary_directory: str, destination_directory: str,
            job_reference: str) -> str:
        """Opens a pdf file as a file stream and converts it into
        customer paperwork format containing a heading and a barcoded
        job reference.
        """

        with open(file_path, "rb") as pdf_stream:     
            pdf_contents = self.convert_stream_to_customer_paperwork_file_writer_object(
                pdf_stream, temporary_directory, job_reference)
            
            output_stream = open(destination_directory + "/" + "result.pdf", "wb")
            pdf_contents.write(output_stream)
            output_stream.close()

        return destination_directory + "\\result.pdf"

    def convert_stream_to_customer_paperwork_file_writer_object(
            self, stream, temp_directory: str, job_reference: str) \
            -> PyPDF2.PdfFileWriter:
        """Converts all the pages in a PDF file into customer paperwork
        format."""

        pdf_reader = PyPDF2.PdfFileReader(stream)
        output = PyPDF2.PdfFileWriter()
        
        number_of_pages = pdf_reader.getNumPages()

        for page_number in range(number_of_pages):
            working_pdf_path = temp_directory + "/temp.pdf"

            self.extract_page_from_pdf_reader(
                pdf_reader, page_number, working_pdf_path)
            
            paperwork_image_path = temp_directory + "/temp_image.png"
            self.convert_single_page_pdf_to_png(working_pdf_path, paperwork_image_path)

            packet = self.create_customer_paperwork_bytes_packet(
                job_reference, paperwork_image_path)

            new_pdf_page = PyPDF2.PdfFileReader(packet).getPage(0)
            output.addPage(new_pdf_page)

        return output

    def convert_single_page_pdf_to_png(self, pdf_path: str, output_path: str):
        with wand_image(filename = pdf_path, resolution = 300) as image:
            self.rotate_image_to_portrait(image)
            image.save(filename = output_path)

    def rotate_image_to_portrait(self, image: wand_image):
        is_landscape = (image.width > image.height)

        if is_landscape:
            image.rotate(270)

    def create_customer_paperwork_bytes_packet(self, job_reference,
            paperwork_image_path) -> io.BytesIO:
        """Creates a bytes packet containing data required to write a
        customer paperwork page.
        """

        packet = io.BytesIO()
        page = CustomerPaperworkPage(packet, job_reference, paperwork_image_path)
        packet.seek(0)

        return packet

    def extract_page_from_pdf_reader(self, pdf_reader: PyPDF2.PdfFileReader,
            page_number: int, output_path: str):
        """Extracts a single page from a pdf reader object and saves it."""
        
        page = pdf_reader.getPage(page_number)

        extracted_page_writer = PyPDF2.PdfFileWriter()
        extracted_page_writer.addPage(page)

        extracted_pdf_page = open(output_path, "wb")
        extracted_page_writer.write(extracted_pdf_page)
        extracted_pdf_page.close()

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
        with pil_image.open(scan_dir + "/" + file) as img:
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

class A4Page(canvas.Canvas):
    """An A4 Page canvas class."""

    def __init__(self, packet: io.BytesIO) -> None:
        """Creates a new A4 Page canvas."""

        super().__init__(packet, pagesize=A4, pageCompression=1)
        self.setFillColorRGB(0,0,0)        

    def draw_job_reference_on_page(self, job_reference: str) -> None:
        """Draws a job reference onto the page."""

        self.setFont("Calibri", 11)
        self.drawString(162*mm, 275*mm, job_reference)

    def draw_paperwork_type_on_page(self, paperwork_type: str) -> None:
        """Draws the paperwork type subheading on the page."""

        self.setFont("Calibri-Bold", 22)
        self.drawString(5*mm, 280*mm, paperwork_type)

    def draw_image_on_page(self, image_path: str) -> None:
        """Draws the image of the customer_paperwork on the page."""

        self.drawImage(
            image_path, -85, 25, 
            width = 730, height = 730, 
            mask = None, preserveAspectRatio = True
        )

    def draw_barcode_on_page(self, job_reference: str):
        barcode = code128.Code128(
            job_reference, barHeight = 10*mm, barWidth = .5*mm)
        
        barcode.drawOn(self, 135*mm, 280*mm)

class CustomerPaperworkPage(A4Page):
    """A page of customer paperwork."""

    def __init__(self, packet, job_reference, paperwork_image):
        """Creates a new customer paperwork page."""

        super().__init__(packet)

        self.draw_barcode_on_page(job_reference)
        self.draw_job_reference_on_page(job_reference)
        self.draw_paperwork_type_on_page("Customer Paperwork")
        self.draw_image_on_page(paperwork_image)
        self.save()

class Directories():
    """A data structure holding directories."""

    def __init__(self):
        self.scan_file = ""
        self.thing = ""