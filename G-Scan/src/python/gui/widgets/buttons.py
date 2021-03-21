from gui.widgets.panel import Panel
from gui.widgets import fonts
from gui.widgets.widgetattributes import WidgetAttributes

import wx

class Button(wx.Button):
    """A class for a button."""

    def __init__(self, panel: Panel, text: str, size: tuple, position: tuple):
        """Creates a new button."""

        super().__init__(
            panel,
            label = text,
            size = size,
            pos = position
        )

        self.SetFont(fonts.getCalibriFont(11))

    def bind_function_to_click(self, callbackFunction) -> None:
        """Assigns a callback function to run when the button is
        clicked.
        """

        self.Bind(
            wx.EVT_BUTTON,
            callbackFunction,
            self
        )

    @staticmethod
    def from_attributes(attributes:WidgetAttributes):
        """Creates a new button."""

        new_button = Button(
            attributes.parent_widget, attributes.text,
            attributes.size, attributes.position
        )

        if attributes.callback_function:
            new_button.bind_function_to_click(attributes.callback_function)

        return new_button

class ImageButton(wx.BitmapButton):
    """A class for a button containing an image icon rather than text.
    """

    def __init__(self, panel: Panel, image_path: str, size: tuple,
            position: tuple, scaling_factor):
        """Creates a new image button."""

        bitmap_image = self.convert_image_path_to_bitmap(
            image_path, scaling_factor)

        super().__init__(
            panel,
            bitmap = bitmap_image,
            size = size,
            pos = position
        )

    def bind_function_to_click(self, callbackFunction) -> None:
        """Assigns a callback function to run when the button is
        clicked.
        """

        self.Bind(wx.EVT_BUTTON, callbackFunction, self)

    @staticmethod
    def from_attributes(attributes:WidgetAttributes):
        """Creates a new image button."""

        new_button = ImageButton(
            attributes.parent_widget, attributes.image_path,
            attributes.size, attributes.position, attributes.scaling_factor
        )

        if attributes.callback_function:
            new_button.bind_function_to_click(attributes.callback_function)

        return new_button

    def convert_image_path_to_bitmap(self, image_path: str,
            scaling_factor: tuple):
        """Converts a path to an image into a bitmap image."""

        image = wx.Image(
            image_path, wx.BITMAP_TYPE_ANY).Scale(
                scaling_factor[0], scaling_factor[1])

        bitmap_image = image.ConvertToBitmap()

        return bitmap_image