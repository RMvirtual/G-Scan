import fitz
import wx


def render_images(file_path: str) -> list[wx.Image]:
    result = []

    with fitz.open(file_path) as document_stream:
        for page in document_stream:
            pixel_buffer = page.get_pixmap(dpi=300)

            bitmap = wx.Bitmap.FromBuffer(
                pixel_buffer.width, pixel_buffer.height, pixel_buffer.samples)

            result.append(bitmap.ConvertToImage())

    return result

def render(image_path: str) -> wx.Image:
    document = fitz.open(image_path)
    _number_of_pages = document.page_count

    page = document[0]
    pixel_buffer = page.get_pixmap(dpi=300)

    bitmap = wx.Bitmap.FromBuffer(
        pixel_buffer.width, pixel_buffer.height, pixel_buffer.samples)

    return bitmap.ConvertToImage()
