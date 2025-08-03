import wx

from rendering.camera import Camera


class Scene:
    def __init__(self, document: wx.Bitmap | None = None) -> None:
        self.camera = Camera()
        self.document = document
