from wx.core import EVT_TEXT
import src.main.file_system.paths as filesystem
from src.main.gui.widgets.buttons import Button
from src.main.gui.widgets.panel import Panel
from src.main.gui.widgets.text import TextEntryBox, TextLabel
from src.main.gui.widgets.images import Image
from src.main.gui.widgets.widget import Attributes


class FilePanel(Panel):
    def __init__(self, top_panel):
        super().__init__(top_panel, size=(425, 255), position=(0, 0))
        self.__create_widgets()

    def __create_widgets(self):
        self.__create_logo_widget()
        self.__create_file_detail_widgets()
        self.__create_user_input_widgets()

    def __create_file_detail_widgets(self) -> None:
        self.__create_file_name_label()
        self.__create_file_name_text_box()
        self.__create_file_extension_label()
        self.__create_file_extension_text_box()

    def __create_user_input_widgets(self) -> None:
        self.__create_input_instruction_label()
        self.__create_user_input_box()
        self.__create_submit_button()
        self.__create_skip_button()
        self.__create_split_document_button()

    def __create_logo_widget(self):
        gscan_logo_path = (
                filesystem.image_resources_directory() + "\\g-scan_logo.png")

        self.__logo_image = Image(self, gscan_logo_path)

    def __create_file_name_label(self):
        attributes = self.__create_file_name_label_attributes()
        self.__file_name_label = TextLabel.from_attributes(attributes)

    def __create_file_name_label_attributes(self):
        attributes = self.create_empty_attributes()

        attributes.text = "File Name:"
        attributes.size = (70, 20)
        attributes.position = (0, 130)

        return attributes

    def __create_file_name_text_box(self):
        attributes = self.__create_file_name_text_box_attributes()
        self.__file_name_text_box = TextEntryBox.from_attributes(attributes)

    def __create_file_name_text_box_attributes(self):
        attributes = self.create_empty_attributes()

        attributes.text = "I AM A FILE NAME"
        attributes.size = (285, 25)
        attributes.position = (100, 130)

        return attributes

    def __create_file_extension_label(self):
        attributes = self.__create_file_extension_label_attributes()
        self.__file_extension_label = TextLabel.from_attributes(attributes)

    def __create_file_extension_label_attributes(self):
        attributes = self.create_empty_attributes()

        attributes.text = "File Type:"
        attributes.size = (70, 20)
        attributes.position = (0, 160)

        return attributes

    def __create_file_extension_text_box(self):
        attributes = self.__create_file_extension_text_box_attributes()
        self.__file_extension_text_box = (
            TextEntryBox.from_attributes(attributes))

    def __create_file_extension_text_box_attributes(self):
        attributes = self.create_empty_attributes()

        attributes.text = ".ext"
        attributes.size = (285, 25)
        attributes.position = (100, 160)

        return attributes

    def __create_input_instruction_label(self):
        attributes = self.__create_input_instruction_label_attributes()
        self.__input_instruction_label = TextLabel.from_attributes(attributes)

    def __create_input_instruction_label_attributes(self):
        attributes = self.create_empty_attributes()

        attributes.text = "Please enter the job reference (excluding \"GR\")"
        attributes.size = (285, 25)
        attributes.position = (0, 195)

        return attributes

    def __create_user_input_box(self):
        attributes = self.__create_user_input_box_attributes()
        self.__user_input_entry_box = TextEntryBox.from_attributes(attributes)

    def __create_user_input_box_attributes(self):
        attributes = self.create_empty_attributes()

        attributes.text = ""
        attributes.size = (140, 25)
        attributes.position = (0, 225)

        return attributes

    def __create_submit_button(self) -> None:
        attributes = self.__create_submit_button_attributes()
        self.__submit_button = Button.from_attributes(attributes)

    def __create_submit_button_attributes(self) -> Attributes:
        attributes = self.create_empty_attributes()

        attributes.text = "Submit"
        attributes.size = (60, 25)
        attributes.position = (141, 225)
        # attributes.callback_function = self.__submit_button_click

        return attributes

    def __create_skip_button(self) -> None:
        attributes = self.__create_skip_button_attributes()
        self.__skip_button = Button.from_attributes(attributes)

    def __create_skip_button_attributes(self) -> Attributes:
        attributes = self.create_empty_attributes()

        attributes.text = "Skip"
        attributes.size = (60, 25)
        attributes.position = (208, 225)

        return attributes

    def __create_split_document_button(self):
        attributes = self.__create_split_document_button_attributes()
        self.__split_document_button = Button.from_attributes(attributes)

    def __create_split_document_button_attributes(self) -> Attributes:
        attributes = self.create_empty_attributes()

        attributes.text = "Split Document"
        attributes.size = (120, 25)
        attributes.position = (270, 225)

        return attributes

    def set_submit_button_function(self, callback_function) -> None:
        self.__submit_button.bind_function_to_click(callback_function)

    def set_skip_button_function(self, callback_function) -> None:
        self.__skip_button.bind_function_to_click(callback_function)

    def set_split_document_button_function(self, callback_function) -> None:
        self.__split_document_button.bind_function_to_click(callback_function)

    def get_user_input_box_value(self) -> str:
        return self.__user_input_entry_box.get_value()

    def bind_event_handler_to_user_input_box(self, event_handler) -> None:
        self.__user_input_entry_box.Bind(EVT_TEXT, event_handler)
