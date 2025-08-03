from maths import Vector2D


class Camera:
    def __init__(
        self,
        position: Vector2D | None = None,
        dimensions: Vector2D | None = None,
        zoom: float = 1.0,
    ) -> None:
        self.position = (
            position if position is not None else Vector2D(0.0, 0.0)
        )

        self.dimensions = (
            dimensions if dimensions is not None else Vector2D(0.0, 0.0)
        )

        self.zoom = zoom
