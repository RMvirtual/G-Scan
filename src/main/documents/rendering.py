import fitz
import wx


def render(image_path: str) -> wx.Image:
    document = fitz.open(image_path)
    _number_of_pages = document.page_count
    page = document[0]
    pixel_buffer = page.get_pixmap(dpi=600)

    bitmap = wx.Bitmap.FromBuffer(
        pixel_buffer.width, pixel_buffer.height, pixel_buffer.samples)

    return bitmap.ConvertToImage()

