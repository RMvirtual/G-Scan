class Widget:
    """A class for a base widget."""


class Attributes:
    """A class acting as a data structure for holding widget attributes
    to be used with a widget's constructor."""

    def __init__(self) -> None:
        """Creates a new widget attributes data structure."""

        self.parent_widget = None
        self.names = []
        self.text = None
        self.size = None,
        self.position = None
        self.options = None
        self.callback_function = None
        self.image_path = None
        self.scaling_factor = None
