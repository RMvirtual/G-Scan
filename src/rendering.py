import fitz
import wx

from maths import Vector2D


class RenderingContext:
    def __init__(self) -> None:
        self.buffer: wx.Bitmap = None
        self.page_bitmap: wx.Bitmap = None
        self.document_bitmap: wx.Bitmap = None
        self.camera_xy = Vector2D(0, 0)


def load_images(file_path: str) -> list[wx.Bitmap]:
    result = []

    with fitz.open(file_path) as document_stream:
        for page in document_stream:
            pixel_buffer = page.get_pixmap(dpi=300)

            bitmap = wx.Bitmap.FromBuffer(
                pixel_buffer.width, pixel_buffer.height, pixel_buffer.samples
            )

            result.append(bitmap)

    return result
