

class Page:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._contents = []

    def width(self):
        return self._width

    def height(self):
        return self._height

    def contents(self):
        return self._contents

