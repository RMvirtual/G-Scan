from maths import Vector2D


class Scene:
    def __init__(self) -> None:
        self.camera: Vector2D = Vector2D(0, 0)
        self.bitmap_size: Vector2D = None
