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
