import fitz
import wx

from rendering.input import MouseState
from rendering.scene import Scene


class RenderingContext:
    def __init__(self, canvas: wx.Panel) -> None:
        self.canvas = canvas
        self.working_buffer: wx.Bitmap = None
        self.final_buffer: wx.Bitmap = None
        self.document_bitmap: wx.Bitmap = None

    def render(self, scene: Scene, mouse_state: MouseState) -> None:
        self.working_buffer = wx.Bitmap(
            scene.bitmap_size.x, scene.bitmap_size.y
        )
        device_context = wx.MemoryDC(self.working_buffer)

        device_context.SetBrush(wx.Brush(wx.Colour(255, 0, 0)))
        device_context.Clear()

        if self.document_bitmap:
            bitmap = self.document_bitmap.GetSubBitmap(
                wx.Rect(scene.camera.x, scene.camera.y, 400, 400)
            )

            wx.Bitmap.Rescale(
                bitmap, wx.Size(scene.bitmap_size.x, scene.bitmap_size.y)
            )

            device_context.DrawBitmap(bitmap, 0, 0, False)

        if mouse_state.position is not None:
            # Black box signifying mouse motion.
            device_context.SetPen(wx.Pen(wx.Colour(0, 0, 0)))

            device_context.DrawRectangle(
                mouse_state.position.x - 25,
                mouse_state.position.y - 25,
                50,
                50,
            )

        device_context.SelectObject(wx.NullBitmap)

    def swap_buffers(self) -> None:
        self.final_buffer = self.working_buffer
        device_context = wx.PaintDC(self.canvas)
        device_context.DrawBitmap(self.final_buffer, 0, 0, useMask=False)


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
