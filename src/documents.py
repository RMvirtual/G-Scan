import dataclasses

import fitz
import wx


@dataclasses.dataclass(frozen=True)
class DocumentType:
    short_code: str = ""
    full_name: str = ""
    analysis_code: str = ""


def load_images(file_path: str) -> list[wx.Bitmap]:
    result = []

    with fitz.open(file_path) as document_stream:
        for page in document_stream:
            pixel_buffer: fitz.Pixmap = page.get_pixmap(dpi=300)

            bitmap = wx.Bitmap.FromBuffer(
                pixel_buffer.width, pixel_buffer.height, pixel_buffer.samples
            )

            result.append(bitmap)

    return result
