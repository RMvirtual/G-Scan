import io

import src.main.file_system.file_system as file_system
from src.main.file_system.file_system import DirectoryItem
import os
import PyPDF2
import shutil
import PIL
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, A3
import wand.image


def create_loading_list_pod(master_application, file, scan_dir,
                            dest_dir, dest_file_name, dest_duplicate_check):
    """Moves a loading list or POD with correct naming convention
    without having to modify the document other than PDF conversion.
    """
    file_name, file_extension = os.path.splitext(file)
    temp_directory = file_system.temp_directory()

    # PDF files should be fine for a straight move
    if file_extension.lower() == ".pdf":
        shutil.copyfile(scan_dir + "/" + file, temp_directory + "/result.pdf")

    # just image files need converting.
    if file_extension.lower() == ".jpeg" or file_extension.lower() == ".jpg"\
            or file_extension.lower() == ".png":
        with PIL.Image.open(scan_dir + "/" + file) as img:
            output = PyPDF2.PdfFileWriter()
            temporary_image = temp_directory + "/" + file_name + ".png"
            img.save(temporary_image)
            img.close()

        final_image = temp_directory + "/temp_image.png"

        # arrange page into portrait orientation
        with wand.image.Image(filename=temporary_image,
                              resolution=200) as img_simulator:
            if img_simulator.width > img_simulator.height:
                img_simulator.rotate(270)
                img_simulator.save(filename=final_image)
            else:
                img_simulator.save(filename=final_image)

        packet = io.BytesIO()
        slab = canvas.Canvas(packet, pagesize=A4, pageCompression=1)
        slab.setFillColorRGB(0, 0, 0)
        slab.drawImage(final_image, -110, 20, width=815, height=815, mask=None,
                       preserveAspectRatio=True)
        slab.save()

        packet.seek(0)
        new_pdf = PyPDF2.PdfFileReader(packet)

        output.addPage(new_pdf.getPage(0))

        output_stream = open(temp_directory + "/" + "result.pdf", "wb")
        output.write(output_stream)
        output_stream.close()
