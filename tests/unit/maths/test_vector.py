import wx

from maths.vector import Vector2D


class TestVector2D:
    def test_should_add_vectors(self) -> None:
        result = Vector2D(1, 2) + Vector2D(3, 4)
        assert result.x == 4
        assert result.y == 6

    def test_should_subtract_vectors(self) -> None:
        result = Vector2D(4, 6) - Vector2D(1, 2)
        assert result.x == 3
        assert result.y == 4

    def test_should_construct_from_wx_point(self) -> None:
        result = Vector2D.fromPoint(wx.Point(10, 20))
        assert result.x == 10
        assert result.y == 20
