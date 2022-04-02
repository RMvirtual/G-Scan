import PIL.Image
from pyzbar.pyzbar import decode
import re
import wand.image
import src.main.file_system.file_system as file_system
from src.main.pdf.reader import PdfReader
import PyPDF2


def read_job_references(source: str) -> list[str]:
    read_method = _read_pdf if source.endswith(".pdf") else _read_image

    return read_method(source)


def _read_pdf(source: str):
    barcode_ref_list = []

    pdf_reader = PdfReader(source)
    pages = pdf_reader.pages()

    for page in pages:
        temp_file_writer = PyPDF2.PdfFileWriter()
        temp_file_writer.addPage(page)

        staging_area = file_system.staging_area()
        extracted_pdf = staging_area + "/temp.pdf"

        with open(extracted_pdf, "wb") as pdf_extraction_stream:
            temp_file_writer.write(pdf_extraction_stream)

        extracted_image = staging_area + "/temp_image.png"

        with wand.image.Image(filename=extracted_pdf, resolution=300) as img:
            img.save(filename=extracted_image)

        refs = _read_image(extracted_image)

        for ref in refs:
            barcode_ref_list.append(ref)

    pdf_reader.close()

    return barcode_ref_list


def _read_image(source: str):
    job_references = []
    barcodes = decode(PIL.Image.open(source, "r"))

    for barcode in barcodes:
        job_ref = re.sub("[^0-9GR]", "", str(barcode.data).upper())

        if (len(job_ref) == 11 and job_ref[:2].upper() == "GR"
                and job_ref not in job_references):
            job_references.append(job_ref)

    return job_references
