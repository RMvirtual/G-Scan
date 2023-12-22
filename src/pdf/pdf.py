import fitz.utils


from pathlib import Path
from fitz import Pixmap


def read_pdf(source: Path) -> list[Pixmap]:
    result = [
        fitz.utils.get_pixmap(page, dpi=300) for page in fitz.Document(source)]
    
    result.reverse()

    return result


def write_pdf(pdf_images: list[Pixmap], output_path: Path) -> None:
    document = fitz.Document()

    for page_image in pdf_images:
        fitz.utils.new_page(document, width=page_image.w, height=page_image.h)

    document.save(output_path)
