import wx

from maths import Vector2D
from rendering.camera import Camera


class Scene:
    def __init__(self) -> None:
        self.camera = Camera()
        self.document: wx.Bitmap = None
        self.bitmap_size: Vector2D = None
