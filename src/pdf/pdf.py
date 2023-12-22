import fitz.utils


from pathlib import Path
from fitz import Document, DocumentWriter, Page, Pixmap


def read_pdf(source: Path) -> list[Pixmap]:
    document = fitz.Document(source)

    result = []

    for page in document:
        result.insert(0, fitz.utils.get_pixmap(page, dpi=300))

    return result


def write_pdf(pdf_images: list[Pixmap], output_path: Path) -> None:
    document = fitz.Document()

    for page_image in pdf_images:
        page = fitz.utils.new_page(
            document, width=page_image.w, height=page_image.h)


    document.save(output_path)
