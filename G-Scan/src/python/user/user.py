from app import file_system

class User(object):
    """ A user with a couple of values to store """
    def __init__(self, name):
        self.name = name
        self.backup_directory = ""
        self.scan_directory = ""
        self.dest_directory = ""
        self.pw_type = "Cust PW"
        self.multi_page_handling = "Split"
        self.input_mode = "Normal"
        self.autoprocessing = "on"

    def __str__(self):
        return self.name

    def overwrite_user(self, new_user):
        user_settings_data = file_system.get_user_settings_data()
        user_settings_data[self.name] = new_user
        user_settings_data.sync()

        user_settings_data.close()

    def validate_directories_check(self):
        """Returns an a dictionary (hash map) with the keys
        as the directory type (scan, dest, backup) and the values
        as Boolean type denoting whether the directory exists."""

        directories_to_check = (
            self.scan_directory, self.dest_directory, self.backup_directory)

        checks = []

        for directory in directories_to_check:
            checks.append(file_system.check_path_is_directory(directory))

        valid_directory_checks = {
            "Scan": checks[0],
            "Destination": checks[1],
            "Backup": checks[2]}

        return valid_directory_checks

    def get_name(self):
        """Returns a string of the current user's name."""
        
        return self.name