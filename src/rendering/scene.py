import wx

from rendering.camera import Camera


class Scene:
    def __init__(self) -> None:
        self.camera = Camera()
        self.document: wx.Bitmap = None
