import wx

from rendering.input import MouseState
from rendering.scene import Scene


class RenderingContext:
    def __init__(self, canvas: wx.Panel) -> None:
        self.canvas = canvas
        self.working_buffer: wx.Bitmap = None
        self.final_buffer: wx.Bitmap = None

    def render(self, scene: Scene, mouse_state: MouseState) -> None:
        canvas_size = self.canvas.GetSize()
        self.working_buffer = wx.Bitmap(canvas_size)

        device_context = wx.MemoryDC(self.working_buffer)
        device_context.SetBrush(wx.Brush(wx.Colour(255, 0, 0)))
        device_context.Clear()

        if scene.document is not None:
            camera_rect = wx.Rect(
                int(scene.camera.position.x),
                int(scene.camera.position.y),
                int(scene.camera.dimensions.x),
                int(scene.camera.dimensions.y),
            )

            bitmap = scene.document.GetSubBitmap(camera_rect)

            device_context.DrawBitmap(bitmap, 0, 0, useMask=False)

        if mouse_state.position is not None:
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
