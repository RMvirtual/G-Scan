class WidgetAttributes():
    """A class acting as a data structure for holding widget attributes
    to be used with a widget's constructor."""

    def __init__(self) -> None:
        """Creates a new widget attributes data structure."""

        self.parent_widget = None
        self.text = None
        self.size = None,
        self.position = None
        self.callback_function = None

