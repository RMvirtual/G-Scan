from gui.widgets.panel import Panel
from gui.widgets.text import TextLabel, TextEntryBox
from gui.widgets.buttons import Button
from gui.widgets.widgetattributes import WidgetAttributes

class TextValuesPanel(Panel):
    """A class representing the text values panel in the gettings
    window GUI."""

    def __init__(self, frame):
        """Creates a new text values panel."""

        super().__init__(frame, (860, 125), (10, 10))
        self.__create_all_widgets()

    def __create_all_widgets(self):
        """Creates all the widgets in the current panel."""

        self.__create_user_name_widgets()
        self.__create_scan_directory_widgets()
        self.__create_destination_directory_widgets()
        self.__create_backup_directory_widgets()

    def __create_user_name_widgets(self):
        """Creates widgets related to the name of the current user."""

        self.__create_user_name_label()
        self.__create_user_name_entry_box()

    def __create_scan_directory_widgets(self):
        """Creates widgets related to the current specified
        scan directory."""

        self.__create_scan_directory_label()
        self.__create_scan_directory_entry_box()
        self.__create_scan_directory_file_dialog_button()

    def __create_destination_directory_widgets(self):
        """Creates widgets related to the current specified
        destination directory."""

        self.__create_destination_directory_label()
        self.__create_destination_directory_entry_box()
        self.__create_destination_directory_file_dialog_button()

    def __create_backup_directory_widgets(self):
        """Creates widgets related to the current specified backup
        directory."""

        self.__create_backup_directory_label()
        self.__create_backup_directory_entry_box()
        self.__create_backup_directory_file_dialog_button()

    def __create_user_name_label(self) -> None:
        """Creates the user name label."""

        attributes = self.__create_user_name_label_attributes()
        self.__user_name_label = TextLabel.from_attributes(attributes)

    def __create_user_name_label_attributes(self) -> WidgetAttributes:
        """Creates the attributes required to instantiate the user
        name label.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "User Name:"
        attributes.size = (200, 20)
        attributes.position = (0, 0)

        return attributes

    def __create_user_name_entry_box(self) -> None:
        """Creates the user name entry box."""

        attributes = self.__create_user_name_entry_box_attributes()
        self.__user_name_entry_box = TextEntryBox.from_attributes(attributes)

    def __create_user_name_entry_box_attributes(self) -> WidgetAttributes:
        """Creates the attributes required to instantiate the user
        name entry box.
        """

        attributes = self.create_empty_attributes()

        attributes.text = ""
        attributes.size = (285, 25)
        attributes.position = (200, 0)

        return attributes

    def __create_scan_directory_label(self) -> None:
        """Creates the scan directory label."""

        attributes = self.__create_scan_directory_label_attributes()
        self.__scan_directory_label = TextLabel.from_attributes(attributes)

    def __create_scan_directory_label_attributes(self) -> WidgetAttributes:
        """Creates the attributes required to instantiate the scan
        directory label.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "Scan Directory:"
        attributes.size = (200, 20)
        attributes.position = (0, 30)

        return attributes

    def __create_scan_directory_entry_box(self) -> None:
        """Creates the scan directory entry box."""

        attributes = self.__create_scan_directory_entry_box_attributes()
        
        self.__scan_directory_entry_box = (
            TextEntryBox.from_attributes(attributes))

    def __create_scan_directory_entry_box_attributes(self) -> WidgetAttributes:
        """Creates the attributes required to instantiate the scan
        directory entry box.
        """

        attributes = self.create_empty_attributes()

        attributes.text = ""
        attributes.size = (625, 25)
        attributes.position = (200, 30)

        return attributes

    def __create_scan_directory_file_dialog_button(self) -> None:
        """Creates the scan directory file dialog button."""

        attributes = (
            self.__create_scan_directory_file_dialog_button_attributes())
        
        self.__scan_directory_file_dialog_button = (
            Button.from_attributes(attributes))

    def __create_scan_directory_file_dialog_button_attributes(self) \
            -> WidgetAttributes:
        """Creates the attributes required to instantiate the scan
        directory file dialog button.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "..."
        attributes.size = (25, 25)
        attributes.position = (826, 30)

        return attributes

    def __create_destination_directory_label(self) -> None:
        """Creates the destination directory label."""

        attributes = self.__create_destination_directory_label_attributes()
        self.__destination_directory_label = TextLabel.from_attributes(attributes)

    def __create_destination_directory_label_attributes(self) -> WidgetAttributes:
        """Creates the attributes required to instantiate the
        destination directory label.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "Destination Directory:"
        attributes.size = (200, 20)
        attributes.position = (0, 60)

        return attributes

    def __create_destination_directory_entry_box(self) -> None:
        """Creates the destination directory entry box."""

        attributes = (
            self.__create_destination_directory_entry_box_attributes())

        self.__destination_directory_entry_box = TextEntryBox.from_attributes(attributes)

    def __create_destination_directory_entry_box_attributes(self) -> WidgetAttributes:
        """Creates the attributes required to instantiate the
        destination directory entry box.
        """

        attributes = self.create_empty_attributes()

        attributes.text = ""
        attributes.size = (625, 25)
        attributes.position = (200, 60)

        return attributes

    def __create_destination_directory_file_dialog_button(self) -> None:
        """Creates the destination directory file dialog button."""

        attributes = (
            self.__create_destination_directory_file_dialog_button_attributes())
        
        self.__destination_directory_file_dialog_button = (
            Button.from_attributes(attributes))

    def __create_destination_directory_file_dialog_button_attributes(self) \
            -> WidgetAttributes:
        """Creates the attributes required to instantiate the
        destination directory file dialog button.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "..."
        attributes.size = (25, 25)
        attributes.position = (826, 60)

        return attributes

    def __create_backup_directory_label(self) -> None:
        """Creates the backup directory label."""

        attributes = self.__create_backup_directory_label_attributes()
        self.__backup_directory_label = TextLabel.from_attributes(attributes)

    def __create_backup_directory_label_attributes(self) -> WidgetAttributes:
        """Creates the attributes required to instantiate the backup
        directory label.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "Backup Directory:"
        attributes.size = (200, 20)
        attributes.position = (0, 90)

        return attributes

    def __create_backup_directory_entry_box(self) -> None:
        """Creates the backup directory entry box."""

        attributes = self.__create_backup_directory_entry_box_attributes()
        
        self.__backup_directory_entry_box = (
            TextEntryBox.from_attributes(attributes))

    def __create_backup_directory_entry_box_attributes(self) -> WidgetAttributes:
        """Creates the attributes required to instantiate the backup
        directory entry box.
        """

        attributes = self.create_empty_attributes()

        attributes.text = ""
        attributes.size = (625, 25)
        attributes.position = (200, 90)

        return attributes

    def __create_backup_directory_file_dialog_button(self) -> None:
        """Creates the backup directory file dialog button."""

        attributes = (
            self.__create_backup_directory_file_dialog_button_attributes())
        
        self.__backup_directory_file_dialog_button = (
            Button.from_attributes(attributes))

    def __create_backup_directory_file_dialog_button_attributes(self) \
            -> WidgetAttributes:
        """Creates the attributes required to instantiate the backup
        directory file dialog button.
        """

        attributes = self.create_empty_attributes()

        attributes.text = "..."
        attributes.size = (25, 25)
        attributes.position = (826, 90)

        return attributes

    def get_user_name(self):
        """Gets the user name."""

        self.__user_name_entry_box.get_value()

    def get_scan_directory(self):
        """Gets the scan directory text field."""

        return self.__scan_directory_entry_box.GetValue()

    def get_destination_directory(self):
        """Gets the destination directory text field."""

        return self.__destination_directory_entry_box.get_value()

    def get_backup_directory(self):
        """Gets the backup directory text field."""

        return self.__backup_directory_entry_box.get_value()

    def set_user_name(self, user_name):
        """Sets the user name."""

        self.__user_name_entry_box.SetValue(user_name)

    def set_scan_directory(self, directory):
        """Sets the scan directory text field."""

        self.__scan_directory_entry_box.SetValue(directory)

    def set_destination_directory(self, directory):
        """Sets the destination directory text field."""

        self.__destination_directory_entry_box.SetValue(directory)

    def set_backup_directory(self, directory):
        """Sets the backup directory text field."""

        self.__backup_directory_entry_box.SetValue(directory)
