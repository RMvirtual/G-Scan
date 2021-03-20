from app import file_system as filesystem
from gui.widgets.buttons import Button
from gui.widgets.panel import Panel
from gui.widgets.text import TextEntryBox, TextLabel
from gui.widgets.images import Image

class FilePanel(Panel):
    """A class modelling the file panel window found in the top panel
    of the main menu GUI.
    """

    def __init__(self, top_panel):
        """Creates a new file panel widget."""

        super().__init__(
            top_panel,
            size = (425, 255),
            position = (0, 0)
        )

        self.__create_widgets()

    def __create_widgets(self):
        """Creates the top-left panel containing the logo,
        file name and type, user input entry box, submit button,
        skip button and split document button."""

        self.__create_logo_widget()
        self.__create_file_detail_widgets()
        self.__create_user_input_widgets()

    def __create_logo_widget(self):
        """Creates the logo in the file panel."""

        gscan_logo_path = (
            filesystem.get_resources_directory() + "images\\g-scan_logo.png")
        
        self.__logo_image = Image(self, gscan_logo_path)

    def __create_file_detail_widgets(self):
        """Creates widgets related to displaying details about the
        current file being processed."""

        self.__file_name_label = TextLabel(
            self, "File Name:", (70, 20), (0, 130))

        self.__file_name_text_box = TextEntryBox(
            self, "I AM A FILE NAME", (285, 25), (100, 130))

        self.__file_extension_label = TextLabel(
            self, "File Type:", (70, 20), (0, 160))

        self.__file_extension_text_box = TextEntryBox(
            self, ".ext", (285, 25), (100, 160))

    def __create_user_input_widgets(self):
        """Creates widgets related to user input."""

        self.__input_instruction_label = TextLabel(
            self, "Please enter the job reference (excluding \"GR\")",
            (285, 25), (0, 195)
        )

        self.__user_input_entry_box = TextEntryBox(
            self, "", (140, 25), (0, 225))

        self.__submit_button = Button(
            self, "Submit", (60, 25), (140, 225))

        self.__submit_button.bindFunctionToClick(self.__submit_button_click)

        self.__skip_button = Button(
            self, "Skip", (60, 25), (208, 225))

        self.__split_document_button = Button(
            self, "Split Document", (120, 25), (270, 225))

    def __submit_button_click(self, event = None):
        """Defines the behaviour to follow when the submit button
        is clicked, activating the main application's submit
        workflow method."""

        print("Hello")

