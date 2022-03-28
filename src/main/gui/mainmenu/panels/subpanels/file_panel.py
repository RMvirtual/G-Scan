from wx.core import EVT_TEXT
import app.file_system as filesystem
from gui.widgets.buttons import Button
from gui.widgets.panel import Panel
from gui.widgets.text import TextEntryBox, TextLabel
from gui.widgets.images import Image
from gui.widgets.widget import Attributes

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

    def __create_file_detail_widgets(self) -> None:
        """Creates widgets related to displaying details about the
        current file being processed."""

        self.__create_file_name_label()
        self.__create_file_name_text_box()
        self.__create_file_extension_label()
        self.__create_file_extension_text_box()

    def __create_user_input_widgets(self) -> None:
        """Creates widgets related to user input."""

        self.__create_input_instruction_label()
        self.__create_user_input_box()
        self.__create_submit_button()
        self.__create_skip_button()
        self.__create_split_document_button()

    def __create_logo_widget(self):
        """Creates the logo in the file panel."""

        gscan_logo_path = (
            filesystem.resources_directory() + "images\\g-scan_logo.png")
        
        self.__logo_image = Image(self, gscan_logo_path)

    def __create_file_name_label(self):
        """Creates the file name label."""

        attributes = self.__create_file_name_label_attributes()
        self.__file_name_label = TextLabel.from_attributes(attributes)

    def __create_file_name_label_attributes(self):
        """Creates the attributes required to instantiate the file_name
        label.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "File Name:"
        attributes.size = (70, 20)
        attributes.position = (0, 130)

        return attributes

    def __create_file_name_text_box(self):
        """Creates the file name text box."""

        attributes = self.__create_file_name_text_box_attributes()
        self.__file_name_text_box = TextEntryBox.from_attributes(attributes)

    def __create_file_name_text_box_attributes(self):
        """Creates the attributes required to instantiate the file name
        text box.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "I AM A FILE NAME"
        attributes.size = (285, 25)
        attributes.position = (100, 130)

        return attributes

    def __create_file_extension_label(self):
        """Creates the file extension label."""

        attributes = self.__create_file_extension_label_attributes()
        self.__file_extension_label = TextLabel.from_attributes(attributes)

    def __create_file_extension_label_attributes(self):
        """Creates the attributes required to instantiate the file
        extension label.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "File Type:"
        attributes.size = (70, 20)
        attributes.position = (0, 160)

        return attributes

    def __create_file_extension_text_box(self):
        """Creates the file extension text box."""

        attributes = self.__create_file_extension_text_box_attributes()
        self.__file_extension_text_box = (
            TextEntryBox.from_attributes(attributes))

    def __create_file_extension_text_box_attributes(self):
        """Creates the attributes required to instantiate the file
        extension textbox.
        """

        attributes = self.create_empty_attributes()

        attributes.text = ".ext"
        attributes.size = (285, 25)
        attributes.position = (100, 160)

        return attributes

    def __create_input_instruction_label(self):
        """Creates the input instruction label."""

        attributes = self.__create_input_instruction_label_attributes()
        self.__input_instruction_label = TextLabel.from_attributes(attributes)

    def __create_input_instruction_label_attributes(self):
        """Creates the attributes required to instantiate the input
        instruction label.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "Please enter the job reference (excluding \"GR\")"
        attributes.size = (285, 25)
        attributes.position = (0, 195)

        return attributes

    def __create_user_input_box(self):
        """Creates the user input entry box."""

        attributes = self.__create_user_input_box_attributes()
        self.__user_input_entry_box = TextEntryBox.from_attributes(attributes)

    def __create_user_input_box_attributes(self):
        """Creates the attributes required to instantiate the user
        input box.
        """

        attributes = self.create_empty_attributes()

        attributes.text = ""
        attributes.size = (140, 25)
        attributes.position = (0, 225)

        return attributes

    def __create_submit_button(self) -> None:
        """Creates the submit button."""

        attributes = self.__create_submit_button_attributes()
        self.__submit_button = Button.from_attributes(attributes)

    def __create_submit_button_attributes(self) -> Attributes:
        """Creates the attributes required to instantiate the submit
        button.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "Submit"
        attributes.size = (60, 25)
        attributes.position = (141, 225)
        # attributes.callback_function = self.__submit_button_click

        return attributes

    def __create_skip_button(self) -> None:
        """Creates the skip button."""

        attributes = self.__create_skip_button_attributes()
        self.__skip_button = Button.from_attributes(attributes)

    def __create_skip_button_attributes(self) -> Attributes:
        """Creates the attributes required to instantiate the skip
        button.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "Skip"
        attributes.size = (60, 25)
        attributes.position = (208, 225)

        return attributes

    def __create_split_document_button(self):
        """Creates the split document button."""

        attributes = self.__create_split_document_button_attributes()
        self.__split_document_button = Button.from_attributes(attributes)

    def __create_split_document_button_attributes(self) -> Attributes:
        """Creates the attributes required to instantiate the split
        document button.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "Split Document"
        attributes.size = (120, 25)
        attributes.position = (270, 225)

        return attributes

    def set_submit_button_function(self, callback_function) -> None:
        """Assigns a function to be run when the submit button is
        clicked.
        """

        self.__submit_button.bind_function_to_click(callback_function)
    
    def set_skip_button_function(self, callback_function) -> None:
        """Assigns a function to be run when the skip button is
        clicked.
        """

        self.__skip_button.bind_function_to_click(callback_function)

    def set_split_document_button_function(self, callback_function) -> None:
        """Assigns a function to be run when the split document button
        is clicked.
        """

        self.__split_document_button.bind_function_to_click(callback_function)

    def get_user_input_box_value(self) -> str:
        """Gets the value currently in the text box."""

        return self.__user_input_entry_box.get_value()

    def bind_event_handler_to_user_input_box(self, event_handler) -> None:
        """Adds something to something."""

        self.__user_input_entry_box.Bind(EVT_TEXT, event_handler)