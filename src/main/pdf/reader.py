import fitz
import src.main.pdf.pdf as pdf


def read_pdf(source: str):
    pdf_stream = fitz.Document(source)

    pages = pdf.Pdf()
    number_of_pages = pdf_stream.page_count

    for page_no in range(number_of_pages):
        page = pdf_stream.load_page(page_no)
        pixels = fitz.utils.get_pixmap(page, dpi=300)

        pages.append(pixels)

    pdf_stream.close()

    return pages
