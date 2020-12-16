import filesystem
import os

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

    def overwrite_user(self, new_user, user_settings_file):
        user_settings_data = filesystem.get_user_settings_data()
        user_settings_data[self.name] = new_user
        user_settings_data.sync()

        user_settings_data.close()

    def validate_directories_check(self, master_application):
        scan_dir_check = os.path.isdir(self.scan_directory)
        dest_dir_check = os.path.isdir(self.dest_directory)
        backup_dir_check = os.path.isdir(self.backup_directory)

        if not scan_dir_check:
            master_application.write_log(
                "Scan folder is invalid. Please check the " +
                "folder exists and update it within your settings.")

        if not dest_dir_check:
            master_application.write_log(
                "Destination folder is invalid. Please check the " +
                "folder exists and update it within your settings.")
        
        if not backup_dir_check:
            master_application.write_log(
                "Backup folder is invalid. Please check the " +
                "folder exists and update it within your settings.")

        if(scan_dir_check and dest_dir_check and backup_dir_check):
            return True

        else:
            return False