import wx

from maths import Vector2D
from rendering.input import MouseState
from rendering.scene import Scene


class RenderingContext:
    def __init__(self, canvas: wx.Panel) -> None:
        self.canvas = canvas
        self.working_buffer: wx.Bitmap = None
        self.final_buffer: wx.Bitmap = None

    def render(self, scene: Scene, mouse_state: MouseState) -> None:
        self.working_buffer = wx.Bitmap(self.canvas.GetSize())
        device_context = wx.MemoryDC(self.working_buffer)
        device_context.SetBrush(wx.Brush(wx.Colour(255, 0, 0)))
        device_context.Clear()

        if scene.document is not None:
            self.render_scene(scene, device_context)

        if mouse_state.position is not None:
            self.render_mouse_reticle(mouse_state.position, device_context)

        device_context.SelectObject(wx.NullBitmap)

    def render_scene(self, scene: Scene, device_context: wx.MemoryDC) -> None:
        camera_box = scene.camera.rect()
        document_box = wx.Rect(scene.document.GetSize())

        if not document_box.Intersects(camera_box):
            return

        document_box.Intersect(camera_box)
        document_bitmap = scene.document.GetSubBitmap(document_box)

        document_top_left = Vector2D(document_box.x, document_box.y)
        camera_top_left = Vector2D(camera_box.x, camera_box.y)
        relative_top_left = document_top_left - camera_top_left

        device_context.DrawBitmap(
            document_bitmap,
            int(relative_top_left.x),
            int(relative_top_left.y),
            useMask=False,
        )

    def render_mouse_reticle(
        self, position: Vector2D, device_context: wx.MemoryDC
    ) -> None:
        device_context.SetPen(wx.Pen(wx.Colour(0, 0, 0)))
        size = 50

        square = wx.Rect(
            int(position.x - size / 2),
            int(position.y - size / 2),
            size,
            size,
        )

        device_context.DrawRectangle(square)

    def swap_buffers(self) -> None:
        self.final_buffer = self.working_buffer
        device_context = wx.PaintDC(self.canvas)
        device_context.DrawBitmap(self.final_buffer, 0, 0, useMask=False)
