import wx

from gui.widgets.panel import Panel
from gui.widgets.buttons import Button

class ButtonsPanel(Panel):
    """A class representing the buttons panel."""

    def __init__(self, frame):
        super().__init__(
            frame, (860, 30), (10, 195))

        self.__frame = frame
        self.__create_buttons()

    def __create_buttons(self):
        """Creates widgets for the Save and Cancel buttons."""

        # Save button.
        self.__save_button = Button(
            self, "Save", (60, 25), (200, 0))
        
        self.__save_button.bind_function_to_click(self.__save_button_click)

        # Cancel button.
        self.__cancel_button = Button(
            self, "Cancel", (60, 25), (270, 0))
            
        self.__cancel_button.bind_function_to_click(self.__cancel_button_click)

    def __save_button_click(self, event = None):
        """Performs the behaviour required when the save button is
        clicked."""

        wx.CallAfter(self.__frame.Destroy)

    def __cancel_button_click(self, event = None):
        """Performs the behaviour required when the save button is
        clicked."""

        wx.CallAfter(self.__frame.Destroy)
