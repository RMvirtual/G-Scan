import filesystem

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