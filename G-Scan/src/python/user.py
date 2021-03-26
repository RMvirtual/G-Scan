from app import file_system

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
        self.__paperwork_type = "Cust PW"
        self.__multi_page_handling = "Split"
        self.__input_mode = "Normal"
        self.__autoprocessing = True

    def overwrite_user(self, new_user) -> None:
        user_settings_data = file_system.get_user_settings_data()
        user_settings_data[self.__name] = new_user
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
