import app.file_system as file_system
import os
import shelve

def get_user_settings():
    """Opens the user settings file for the user's directory and
    workspace settings."""

    user_settings_data = get_user_settings_file_connection()
    current_username = os.getlogin()

    try:
        user = user_settings_data[current_username]

    except Exception as exception:
        user = create_new_user(current_username, user_settings_data)

    user_settings_data.close()

    return user

def get_current_user_name():
    user_name = os.getlogin()

    return user_name

def get_user_settings_file_connection():
    user_settings_path = file_system.get_user_settings_data_path() 
    user_settings_data = shelve.open(user_settings_path)

    return user_settings_data

def create_new_user(user_name, user_settings_data):
    new_user = User(user_name)

    user_settings_data[user_name] = new_user
    user_settings_data.sync()

    print("Created user: ", new_user.get_name())

    return new_user

class User(object):
    """A user of the application. Contains their default settings and
    directory paths.
    """

    def __init__(self, name) -> None:
        """Creates a new User."""

        self.__name = name
        self.__backup_directory = ""
        self.__scan_directory = ""
        self.__destination_directory = ""
        self.__paperwork_type = "Customer PW"
        self.__multi_page_handling = "Split"
        self.__input_mode = "Normal"
        self.__autoprocessing = True

    def sync(self) -> None:
        user_settings_data = file_system.get_user_settings_data()
        user_settings_data[self.__name] = self
        user_settings_data.sync()

        user_settings_data.close()

    def validate_directories_check(self) -> dict:
        """Returns an a dictionary (hash map) with the keys as the
        directory type (scan, dest, backup) and the values as Boolean
        type denoting whether the directory exists.
        """

        directories_to_check = (
            self.__scan_directory,
            self.__destination_directory,
            self.__backup_directory
        )

        checks = []

        for directory in directories_to_check:
            checks.append(file_system.check_path_is_directory(directory))

        valid_directory_checks = {
            "Scan": checks[0],
            "Destination": checks[1],
            "Backup": checks[2]
        }

        return valid_directory_checks

    def get_name(self) -> str:
        """Returns a string representing the user's login name."""
        
        return self.__name

    def get_scan_directory(self) -> str:
        """Returns a string representing the user's scan directory
        path.
        """
        
        return self.__scan_directory

    def get_destination_directory(self) -> str:
        """Returns a string representing the user's destination
        directory path.
        """
        
        return self.__destination_directory

    def get_backup_directory(self) -> str:
        """Returns a string representing the user's backup directory
        path.
        """
        
        return self.__backup_directory

    def get_paperwork_type(self) -> str:
        """Returns a string representing the user's default paperwork
        type.
        """
        
        return self.__paperwork_type

    def get_multi_page_handling(self) -> str:
        """Returns a string representing the user's default multi-page
        handling value.
        """
        
        return self.__multi_page_handling

    def get_input_mode(self) -> str:
        """Returns a string representing the user's default input
        mode.
        """
        
        return self.__input_mode

    def get_autoprocessing_mode(self) -> bool:
        """Returns a boolean representing whether autoprocessing mode
        is active by default.
        """

        return self.__autoprocessing

    def set_scan_directory(self, path: str) -> None:
        """Sets the user's default scan directory."""

        self.__scan_directory = path

    def set_destination_directory(self, path: str) -> None:
        """Sets the user's default destination directory."""

        self.__destination_directory = path

    def set_backup_directory(self, path: str) -> None:
        """Sets the user's default backup directory."""

        self.__backup_directory = path

    def set_paperwork_type(self, paperwork_type: str) -> None:
        """Sets the user's default paperwork type."""

        self.__paperwork_type = paperwork_type

    def set_multi_page_handling(self, multi_page_handling: str) -> None:
        """Sets the user's default multi-page handling setting."""

        self.__multi_page_handling = multi_page_handling

    def set_input_mode(self, input_mode: str) -> None:
        """Sets the user's default input mode."""

        self.__input_mode = input_mode

    def set_auto_processing_mode(self, autoprocessing_mode: bool) -> None:
        """Sets the user's default value for autoprocessing mode."""

        self.__autoprocessing = autoprocessing_mode

class UserDefaults():
    """A data structure containing fields relevant to a user's
    default values. Can be created either from a User or from the
    values in a Settings Window.
    """

    def __init__(self):
        """Creates a new data structure containing user values
        obtained from the settings menu."""

        self.user_name = ""
        self.scan_directory = ""
        self.destination_directory = ""
        self.backup_directory = ""
        self.paperwork_type = ""
        self.multi_page_handling = ""
        self.input_mode = ""
        self.autoprocessing_mode = False

    @staticmethod
    def from_user(user: User) -> "UserDefaults":
        """Creates a set of values from a user object."""

        values = UserDefaults()

        values.user_name = user.get_name()
        values.scan_directory = user.get_scan_directory()
        values.destination_directory = user.get_destination_directory()
        values.backup_directory = user.get_backup_directory()
        values.paperwork_type = user.get_paperwork_type()
        values.input_mode = user.get_input_mode()
        values.multi_page_handling = user.get_multi_page_handling()
        values.autoprocessing_mode = user.get_autoprocessing_mode()

        return values
    