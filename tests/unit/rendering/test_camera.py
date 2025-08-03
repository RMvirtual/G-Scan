from maths import Vector2D
from rendering.camera import Camera


class TestCamera:
    def test_should_create_rectangle(self) -> None:
        camera = Camera(position=Vector2D(30, 40), dimensions=Vector2D(30, 40))
        result = camera.rect()

        assert result.Left == 15
        assert result.Right == 44
        assert result.Top == 20
        assert result.Bottom == 59

    def test_should_create_zoomed_rectangle(self) -> None:
        camera = Camera(position=Vector2D(30, 40), dimensions=Vector2D(30, 40))
        camera.zoom = 2.0

        zoomed_in = camera.rect()
        assert zoomed_in.Left == 22
        assert zoomed_in.Right == 36
        assert zoomed_in.Top == 30
        assert zoomed_in.Bottom == 49
