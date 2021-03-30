from gui.widgets.widget import Attributes
from wx import Panel as wxPanel

class Panel(wxPanel):
    """A basic GUI panel (to be extended further into more concrete
    panels).
    """

    def __init__(self, frame, size:tuple, position:tuple) -> None:
        """Creates a new panel and attaches it to a frame."""

        super().__init__(
            frame,
            size = size,
            pos = position 
        )

        self.__frame = frame

    def create_empty_attributes(self) -> Attributes:
        """Creates an empty widget attributes data structure with only
        this panel assigned as the parent widget."""

        attributes = Attributes()
        attributes.parent_widget = self

        return attributes

    def get_main_application(self):
        """Gets the main application associated with the frame
        containing this object.
        """

        return self.__frame.get_main_application()

    def get_frame(self):
        return self.__frame