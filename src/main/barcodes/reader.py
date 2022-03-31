import PIL
from pyzbar.pyzbar import decode
import re


def read_job_references(image_path: str) -> tuple[str]:
    job_references = []
    barcodes = decode(PIL.Image.open(image_path, "r"))

    for barcode in barcodes:
        job_ref = re.sub("[^0-9GR]", "", str(barcode.data).upper())

        if (len(job_ref) == 11 and job_ref[:2].upper() == "GR"
                and job_ref not in job_references):
            job_references.append(job_ref)

    return job_references
