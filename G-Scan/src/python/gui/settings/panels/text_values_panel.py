import wx

from gui.widgets.panel import Panel
from gui.widgets.text import TextLabel, TextEntryBox
from gui.widgets.buttons import Button

class TextValuesPanel(Panel):
    """A class representing the text values panel in the gettings
    window GUI."""

    def __init__(self, frame):
        """Constructor method."""

        super().__init__(
            frame, (860, 125), (10, 10)
        )

        self.__create_user_name_widgets()
        self.__create_scan_directory_widgets()
        self.__create_destination_directory_widgets()
        self.__create_backup_directory_widgets()

    def __create_user_name_widgets(self):
        """Creates widgets related to the name of the current user."""

        # User Name label.
        self.__user_name_label = TextLabel(
            self, "User Name:", (200, 20), (0, 0))

        # User Name value label.
        self.__user_name_field = TextEntryBox(
            self, "", (285, 25), (200, 0))

    def __create_scan_directory_widgets(self):
        """Creates widgets related to the current specified
        scan directory."""

        # Scan Directory label.
        self.__scan_directory_label = TextLabel(
            self, "Scan Directory:", (200, 20), (0, 30))

        # Scan Directory value text box.
        self.__scan_directory_field = TextEntryBox(
            self, "", (625, 25), (200, 30))

        # Scan Directory file dialog button.
        self.__scan_directory_file_dialog_button = Button(
            self, "...", (25, 25), (826, 30))

    def __create_destination_directory_widgets(self):
        """Creates widgets related to the current specified
        destination directory."""

        # Destination Directory label.
        self.__destination_directory_label = TextLabel(
            self, "Destination Directory:", (200, 20), (0, 60))

        # Destination Directory text field.
        self.__destination_directory_field = TextEntryBox(
            self, "", (625, 25), (200, 60))

        # Destination Directory file dialog button.
        self.__destination_directory_file_dialog_button = Button(
            self, "...", (25, 25), (826, 60))

    def __create_backup_directory_widgets(self):
        """Creates widgets related to the current specified backup
        directory."""

        # Backup Directory label.
        self.__backup_directory_label = TextLabel(
            self, "Backup Directory:", (200, 20), (0, 90))

        # Backup Directory value text box.
        self.__backup_directory_field = TextEntryBox(
            self, "", (625, 25), (200, 90))

        # Backup Directory file dialog button.
        self.__backup_directory_file_dialog_button = Button(
            self, "...", (25, 25), (826, 90))

    def get_user_name(self):
        """Gets the user name."""

        self.__user_name_field.GetLabel()

    def get_scan_directory(self):
        """Gets the scan directory text field."""

        self.__scan_directory_field.GetLabel()

    def get_destination_directory(self):
        """Gets the destination directory text field."""

        self.__destination_directory_field.GetLabel()

    def get_backup_directory(self):
        """Gets the backup directory text field."""

        self.__backup_directory_field.GetLabel()

    def set_user_name(self, user_name):
        """Sets the user name."""

        self.__user_name_field.SetLabel(user_name)

    def set_scan_directory(self, directory):
        """Sets the scan directory text field."""

        self.__scan_directory_field.SetLabel(directory)

    def set_destination_directory(self, directory):
        """Sets the destination directory text field."""

        self.__destination_directory_field.SetLabel(directory)

    def set_backup_directory(self, directory):
        """Sets the backup directory text field."""

        self.__backup_directory_field.SetLabel(directory)
