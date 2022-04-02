import src.main.file_system.file_system as file_system
import wand.image
import PyPDF2
import src.main.barcodes.reader as barcode_reader


class PdfReader:
    def __init__(self, source: str):
        with open(file=source, mode="rb") as pdf_stream:
            pdf_reader = PyPDF2.PdfFileReader(stream=pdf_stream)
            self._pages = []

            number_of_pages = pdf_reader.getNumPages()

            for page_no in range(number_of_pages):
                self._pages.append(pdf_reader.getPage(page_no))

    def number_of_pages(self) -> int:
        return len(self._pages)

def read_barcodes(file_name: str, directory: str):
    barcode_ref_list = []

    with open(directory + "/" + file_name, "rb") as current_file_pdf:
        current_file_pdf_reader = PdfReader(current_file_pdf)
        current_file_page_amount = current_file_pdf_reader.getNumPages()

        for page_number in range(current_file_page_amount):
            page_object = current_file_pdf_reader.getPage(page_number)
            temp_file_writer = PyPDF2.PdfFileWriter()
            temp_file_writer.addPage(page_object)

            temp_directory = file_system.temp_directory()
            temp_file_path = temp_directory + "temp.pdf"

            with open(temp_file_path, "wb") as temp_file:
                temp_file_writer.write(temp_file)

            scan_doc = temp_directory + "temp.pdf"
            cust_pw = temp_directory + "temp_image.png"

            with wand.image.Image(filename=scan_doc, resolution=300) as img:
                img.save(filename=cust_pw)

            refs = barcode_reader.read_job_references(cust_pw)
            barcode_ref_list.append(refs)

    return barcode_ref_list


def image_barcode_reader(self, file, scan_dir):
    return barcode_reader.read_job_references(scan_dir + "/" + file)