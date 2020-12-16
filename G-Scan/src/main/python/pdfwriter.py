"""Module for creating a PDFWriter class."""
import io
import os
import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, A3
from reportlab.lib.units import mm
from reportlab.graphics.barcode import code128
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from wand.image import Image as wand_image

pdfmetrics.registerFont(TTFont("Calibri", "Calibri.ttf"))
pdfmetrics.registerFont(TTFont("Calibri-Bold", "Calibrib.ttf"))

def create_cust_pw(master_application, file, scan_dir, dest_dir, job_ref, dest_file_name, dest_duplicate_check):
    file_name, file_extension = os.path.splitext(file)

    # document generation for PDFs
    if file_extension.lower() == ".pdf":
        with open(scan_dir + "/" + file, "rb") as current_file_pdf:
            current_file_pdf_reader = PyPDF2.PdfFileReader(current_file_pdf)
            
            current_file_page_amount = current_file_pdf_reader.getNumPages()

            output = PyPDF2.PdfFileWriter()
            
            for page_number in range(current_file_page_amount):
                page_object = current_file_pdf_reader.getPage(page_number)
                temp_file_writer = PyPDF2.PdfFileWriter()
                temp_file_writer.addPage(page_object)
                temp_file = open(master_application.temp_dir + "/" + "temp.pdf", "wb")
                temp_file_writer.write(temp_file)
                temp_file.close()
                
                scan_doc = master_application.temp_dir + "/" + "temp.pdf"
                cust_pw = master_application.temp_dir + "/temp_image.png"
                
                with wand_image(filename = scan_doc, resolution = 300) as img:
                    if img.width > img.height:
                        img.rotate(270)
                        img.save(filename = cust_pw)
                    else:
                        img.save(filename = cust_pw)

                packet = io.BytesIO()
                slab = canvas.Canvas(packet, pagesize = A4, pageCompression = 1)
                slab.setFillColorRGB(0,0,0)
                barcode = code128.Code128(job_ref, barHeight = 10*mm, barWidth = .5*mm)
                barcode.drawOn(slab, 135*mm, 280*mm)

                slab.setFont("Calibri", 11)
                slab.drawString(162*mm, 275*mm, job_ref)
                slab.setFont("Calibri-Bold", 22)
                slab.drawString(5*mm, 280*mm, "Customer Paperwork")
                slab.drawImage(cust_pw, -85, 25, width = 730, height = 730, mask = None, preserveAspectRatio = True)

                slab.save()

                packet.seek(0)
                new_pdf = PyPDF2.PdfFileReader(packet)

                output.addPage(new_pdf.getPage(0))

            current_file_pdf.close()
        
        output_stream = open(master_application.temp_dir + "/" + "result.pdf", "wb")
        output.write(output_stream)
        output_stream.close()

    # document generation for image files (excluding TIF as these will always be pre-processed into PDFs by the document splitter function)
    elif file_extension.lower() == ".jpeg" or file_extension.lower() == ".jpg" or file_extension.lower() == ".png":
        with pil_image.open(scan_dir + "/" + file) as img:
            output = PyPDF2.PdfFileWriter()
            temporary_png = master_application.temp_dir + "/" + file_name + ".png"
            img.save(temporary_png)
            img.close()

        cust_pw = master_application.temp_dir + "/temp_image.png"

        # arrange page into portrait orientation
        with wand_image(filename = temporary_png, resolution = 200) as img_simulator:
            if img_simulator.width > img_simulator.height:
                img_simulator.rotate(270)
                img_simulator.save(filename = cust_pw)
            else:
                img_simulator.save(filename = cust_pw)

        packet = io.BytesIO()
        slab = canvas.Canvas(packet, pagesize = A4, pageCompression = 1)
        slab.setFillColorRGB(0,0,0)
        barcode = code128.Code128(job_ref, barHeight = 10*mm, barWidth = .5*mm)
        barcode.drawOn(slab, 135*mm, 280*mm)

        slab.setFont("Calibri", 11)
        slab.drawString(162*mm, 275*mm, job_ref)
        slab.setFont("Calibri-Bold", 22)
        slab.drawString(5*mm, 280*mm, "Customer Paperwork")
        slab.drawImage(cust_pw, -85, 25, width = 730, height = 730, mask = None, preserveAspectRatio = True)

        slab.save()

        packet.seek(0)
        new_pdf = PyPDF2.PdfFileReader(packet)

        output.addPage(new_pdf.getPage(0))

        output_stream = open(master_application.temp_dir + "/" + "result.pdf", "wb")
        output.write(output_stream)
        output_stream.close()
