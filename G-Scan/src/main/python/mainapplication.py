"""A module for the main application class."""

from datetime import datetime
from date import Date
from win32api import GetSystemMetrics
from tkinter import *
from tkinter import filedialog
from gui import GUI
import os
import filesystem
from user import User
import shelve

class MainApplication():
    """A class for the main application of the program to run."""

    def __init__(self):
        """Constructor method."""
        self.current_user = self.get_user_settings()

        x_axis = str(int(GetSystemMetrics(0) / 4))
        y_axis = str(int(GetSystemMetrics(1) / 4))

        root = Tk()
        root.title("GrayScan")
        root.geometry("850x500+" + x_axis + "+" + y_axis)
        root.grid_rowconfigure(0, weight = 1)
        root.grid_columnconfigure(0, weight = 1)
        root.configure(background = "white")

        self.gui = GUI(root, self)

        root.mainloop()
    
    def get_user_settings(self):
        """Opens the user settings file for the user's directory and
        workspace settings."""

        current_username = os.getlogin()

        # If the user already exists in the user settings data file,
        # load the user up as the current user and pass it back as a
        # user object.
        user_settings_data = shelve.open(
            filesystem.get_user_settings_data_path())
        
        if current_username in user_settings_data:
            current_user = user_settings_data[current_username]

        # If the user does not exist, creates a new user and adds it to
        # the user settings data file, passing back the user object.
        else:
            current_user = User(current_username)
            user_settings_data[current_username] = current_user
            user_settings_data.sync()
        
        user_settings_data.close()

        return current_user

    def get_current_user(self):
        """Returns the current user of the program as a User object."""

        return self.current_user

    def check_user_directories_are_valid(self):
        """Checks whether all the working directories of a user are
        valid and accessible. Prints to the GUI's log if not and
        returns an overall Boolean at the end on whether all
        directories are valid or not."""

        directory_checks = self.current_user.validate_directories_check()
        all_directories_valid = True

        for directory in directory_checks:
            is_directory_valid = directory_checks[directory]
            
            if not is_directory_valid:
                all_directories_valid = False
                
                self.gui.write_log(
                    directory + " folder is invalid. Please check the " +
                    "folder exists and update it within your settings.")
        
        return all_directories_valid

    def get_files_in_scan_folder(self):
        """Gets a list of all files in the current user's scan folder
        that have a valid extension for the program to handle."""

        scan_directory = self.current_user.scan_directory

        valid_file_extensions = (
            ".pdf", ".tif", ".tiff", ".tiff", ".jpeg", ".jpg", ".png")
        
        file_list = []

        for scan_file in filesystem.get_directory_items(scan_directory):
            if scan_file.lower().endswith(valid_file_extensions):
                file_list.append(scan_file)

                self.gui.write_log("Adding " + scan_file + " to list.")
        
        return file_list