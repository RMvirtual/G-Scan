from src.main.gui.widgets.panel import Panel
from src.main.gui.widgets.text import TextLabel, TextEntryBox
from src.main.gui.widgets.buttons import Button
from src.main.gui.widgets.widget import Attributes


class TextValuesPanel(Panel):
    def __init__(self, frame):
        super().__init__(frame, (860, 125), (10, 10))
        self.__create_all_widgets()

    def __create_all_widgets(self):
        self.__create_user_name_widgets()
        self.__create_scan_directory_widgets()
        self.__create_destination_directory_widgets()
        self.__create_backup_directory_widgets()

    def __create_user_name_widgets(self):
        self.__create_user_name_label()
        self.__create_user_name_entry_box()

    def __create_scan_directory_widgets(self):
        self.__create_scan_directory_label()
        self.__create_scan_directory_entry_box()
        self.__create_browse_scan_directory_button()

    def __create_destination_directory_widgets(self):
        self.__create_destination_directory_label()
        self.__create_destination_directory_entry_box()
        self.__create_browse_destination_directory_button()

    def __create_backup_directory_widgets(self):
        self.__create_backup_directory_label()
        self.__create_backup_directory_entry_box()
        self.__create_browse_backup_directory_button()

    def __create_user_name_label(self) -> None:
        attributes = self.__create_user_name_label_attributes()
        self.__user_name_label = TextLabel.from_attributes(attributes)

    def __create_user_name_label_attributes(self) -> Attributes:
        attributes = self.create_empty_attributes()

        attributes.text = "User Name:"
        attributes.size = (200, 20)
        attributes.position = (0, 0)

        return attributes

    def __create_user_name_entry_box(self) -> None:
        attributes = self.__create_user_name_entry_box_attributes()
        self.__user_name_entry_box = TextEntryBox.from_attributes(attributes)

    def __create_user_name_entry_box_attributes(self) -> Attributes:
        attributes = self.create_empty_attributes()

        attributes.text = ""
        attributes.size = (285, 25)
        attributes.position = (200, 0)

        return attributes

    def __create_scan_directory_label(self) -> None:
        attributes = self.__create_scan_directory_label_attributes()
        self.__scan_directory_label = TextLabel.from_attributes(attributes)

    def __create_scan_directory_label_attributes(self) -> Attributes:
        attributes = self.create_empty_attributes()

        attributes.text = "Scan Directory:"
        attributes.size = (200, 20)
        attributes.position = (0, 30)

        return attributes

    def __create_scan_directory_entry_box(self) -> None:
        attributes = self.__create_scan_directory_entry_box_attributes()
        
        self.__scan_directory_entry_box = (
            TextEntryBox.from_attributes(attributes))

    def __create_scan_directory_entry_box_attributes(self) -> Attributes:
        attributes = self.create_empty_attributes()

        attributes.text = ""
        attributes.size = (625, 25)
        attributes.position = (200, 30)

        return attributes

    def __create_browse_scan_directory_button(self) -> None:
        attributes = (
            self.__create_browse_scan_directory_button_attributes())
        
        self.__browse_scan_directory_button = (
            Button.from_attributes(attributes))

    def __create_browse_scan_directory_button_attributes(self) -> Attributes:
        attributes = self.create_empty_attributes()

        attributes.text = "..."
        attributes.size = (25, 25)
        attributes.position = (826, 30)

        return attributes

    def __create_destination_directory_label(self) -> None:
        attributes = self.__create_destination_directory_label_attributes()
        self.__destination_directory_label = TextLabel.from_attributes(attributes)

    def __create_destination_directory_label_attributes(self) -> Attributes:
        attributes = self.create_empty_attributes()

        attributes.text = "Destination Directory:"
        attributes.size = (200, 20)
        attributes.position = (0, 60)

        return attributes

    def __create_destination_directory_entry_box(self) -> None:
        attributes = (
            self.__create_destination_directory_entry_box_attributes())

        self.__destination_directory_entry_box = TextEntryBox.from_attributes(attributes)

    def __create_destination_directory_entry_box_attributes(self) -> Attributes:
        attributes = self.create_empty_attributes()

        attributes.text = ""
        attributes.size = (625, 25)
        attributes.position = (200, 60)

        return attributes

    def __create_browse_destination_directory_button(self) -> None:
        attributes = (
            self.__create_browse_destination_directory_button_attributes())
        
        self.__browse_destination_directory_button = (
            Button.from_attributes(attributes))

    def __create_browse_destination_directory_button_attributes(self) \
            -> Attributes:
        attributes = self.create_empty_attributes()

        attributes.text = "..."
        attributes.size = (25, 25)
        attributes.position = (826, 60)

        return attributes

    def __create_backup_directory_label(self) -> None:
        attributes = self.__create_backup_directory_label_attributes()
        self.__backup_directory_label = TextLabel.from_attributes(attributes)

    def __create_backup_directory_label_attributes(self) -> Attributes:
        attributes = self.create_empty_attributes()

        attributes.text = "Backup Directory:"
        attributes.size = (200, 20)
        attributes.position = (0, 90)

        return attributes

    def __create_backup_directory_entry_box(self) -> None:
        attributes = self.__create_backup_directory_entry_box_attributes()
        
        self.__backup_directory_entry_box = (
            TextEntryBox.from_attributes(attributes))

    def __create_backup_directory_entry_box_attributes(self) -> Attributes:
        attributes = self.create_empty_attributes()

        attributes.text = ""
        attributes.size = (625, 25)
        attributes.position = (200, 90)

        return attributes

    def __create_browse_backup_directory_button(self) -> None:
        attributes = (
            self.__create_browse_backup_directory_button_attributes())
        
        self.__browse_backup_directory_button = (
            Button.from_attributes(attributes))

    def __create_browse_backup_directory_button_attributes(self) \
            -> Attributes:
        attributes = self.create_empty_attributes()

        attributes.text = "..."
        attributes.size = (25, 25)
        attributes.position = (826, 90)

        return attributes

    def get_user_name(self):
        self.__user_name_entry_box.get_value()

    def get_scan_directory(self):
        return self.__scan_directory_entry_box.GetValue()

    def get_destination_directory(self):
        return self.__destination_directory_entry_box.get_value()

    def get_backup_directory(self):
        return self.__backup_directory_entry_box.get_value()

    def set_user_name(self, user_name):
        self.__user_name_entry_box.SetValue(user_name)

    def set_scan_directory(self, directory):
        self.__scan_directory_entry_box.SetValue(directory)

    def set_destination_directory(self, directory):
        self.__destination_directory_entry_box.SetValue(directory)

    def set_backup_directory(self, directory):
        self.__backup_directory_entry_box.SetValue(directory)

    def set_browse_backup_directory_button_function(self, callback_function):
        self.__browse_backup_directory_button.bind_function_to_click(
            callback_function)

    def set_browse_scan_directory_button_function(self, callback_function):
        self.__browse_scan_directory_button.bind_function_to_click(
            callback_function)

    def set_browse_destination_directory_button_function(
            self, callback_function) -> None:
        self.__browse_destination_directory_button.bind_function_to_click(
            callback_function)