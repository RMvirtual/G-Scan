"""A module for the main application class."""

from datetime import datetime
from date import Date
import date
import backup
import userinputvalidation
from win32api import GetSystemMetrics
from tkinter import *
from tkinter import filedialog
from gui import GUI
import os
import filesystem
from user import User
import shelve
from popupbox import PopupBox
from pdfviewer import PDFViewer
import pdfreader
import pdfwriter
import re

class MainApplication():
    """A class for the main application of the program to run."""

    def __init__(self):
        """Constructor method."""
        self.current_user = self.get_user_settings()

        x_axis = str(int(GetSystemMetrics(0) / 4))
        y_axis = str(int(GetSystemMetrics(1) / 4))

        """root = Tk()
        root.title("GrayScan")
        root.geometry("850x500+" + x_axis + "+" + y_axis)
        root.grid_rowconfigure(0, weight = 1)
        root.grid_columnconfigure(0, weight = 1)
        root.configure(background = "white")

        self.gui = GUI(root, self)
        directories_valid = self.validate_user_directories()
        
        if not directories_valid:
            self.gui.write_log("\n")
        
        self.calculate_quick_mode_hint_message()
        self.gui.write_log("Awaiting user input.")
        root.mainloop()"""
        self.gui = GUI(self)
        
    
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

    def validate_user_directories(self):
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

    def calculate_quick_mode_hint_message(self):
        input_mode = self.gui.get_current_input_mode()

        # If input mode is set to normal, set the hint box to be an
        # empty string.
        if input_mode == "Normal":
            self.gui.set_quick_mode_hint_text("")

        # If input mode is set to quick, get the year and month
        # dropdown box variables and make a template ref.
        elif input_mode == "Quick":
            working_year = self.gui.get_current_year_choice()
            years = date.get_years()

            year_prefix = (
                [year.get_short_code() for year in years
                    if year.get_full_code() == working_year]
            )

            #year_prefix = working_year.get_short_code()

            # year_prefix = re.sub("[^0-9]", "",
            #    str([year.short for year in YEARS if year.full == working_year]))

            working_month = self.gui.get_current_month_choice()
            months = date.get_months()
            #month_prefix = working_month.get_short_code()

            month_prefix = (
                [month.get_short_code() for month in months
                    if month.get_full_code() == working_month]
            )

            #month_prefix = re.sub("[^0-9]", "",
            #    str([month.short for month in MONTHS if month.full == working_month]))

            template_ref = "GR" + year_prefix[0] + month_prefix[0] + "0"
            hint_message = "Current GR Number: " + template_ref

            # delete anything already in the hint box, and replace it with the new message
            self.gui.set_quick_mode_hint_text(hint_message)

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
    
    def start(self):
        """Starts the workflow of reading/viewing and writing from
        scan files."""

        all_directories_valid = self.validate_user_directories()
        
        if all_directories_valid:
            self.file_index = 0
            self.file_list = self.get_files_in_scan_folder()

            if not self.file_list:
                PopupBox(self.gui, "Failure", "No files found.", "200", "50")

            else:
                self.start_pdf_viewer()
                self.get_file(self.file_index, self.file_list)

    def start_pdf_viewer(self):
        self.pdf_viewer = PDFViewer()

    def get_file(self, file_index, file_list):
        # directories
        scan_dir = self.current_user.scan_directory

        # user variables
        multi_page_handling = self.gui.get_multi_page_mode()
        input_mode = self.gui.get_current_input_mode()
        pw_type = self.gui.get_current_paperwork_type()
        autoprocessing = self.gui.get_autoprocessing_mode()
        
        if not self.file_list:
            if self.file_index == 0:
                PopupBox(
                    self.gui, "Guess What", "No more files remaining.",
                    "230", "75")
                
                self.pdf_viewer.close()
                
        else:
            self.file = self.file_list[self.file_index]

            pdf_file = pdfwriter.image_converter(
                self, self.file, scan_dir, multi_page_handling)
            
            split_file_list = pdfwriter.document_splitter(
                self, pdf_file, scan_dir, multi_page_handling)

            del self.file_list[self.file_index]
            
            for split_file in reversed(split_file_list):
                self.file_list.insert(
                    self.file_index, split_file)

            self.file = self.file_list[self.file_index]
            file_name, file_ext = os.path.splitext(self.file)

            self.gui.set_file_name(file_name)
            self.gui.set_file_extension(file_ext)
            self.gui.move_cursor_to_user_input_box()

            # Customer Paperwork/Loading List/Manual POD Processing Mode
            if (pw_type == "Cust PW" or pw_type == "Loading List"
                    or pw_type == "POD" and autoprocessing == "off"):
                self.pdf_viewer.show_image(
                    self.gui, self.file, self.current_user.scan_directory)

            # POD Automatic Processing Mode
            elif pw_type == "POD" and autoprocessing == "on":
                pdfreader.barcode_scanner(
                    self.gui, self.file_index, self.file_list)

    def submit(self, barcode = None, manual_submission = True):
        """Runs the submission process workflow."""

        # User input variables.
        input_mode = self.gui.get_current_input_mode()
        paperwork_type = self.gui.get_current_paperwork_type()
        user_input = self.gui.get_user_input()
        auto_processing = self.gui.get_autoprocessing_mode()

        # Directory variables.
        current_user = self.get_current_user()

        scan_dir = current_user.scan_directory
        dest_dir = current_user.dest_directory
        backup_dir = current_user.backup_directory

        # File variables.
        current_file = self.file_list[
            self.file_index]

        file_name, file_extension = os.path.splitext(current_file)

        valid_paperwork_types = ("Cust PW", "Loading List", "POD")

        if (paperwork_type in valid_paperwork_types
                and auto_processing == "off"
                or auto_processing == "on" and manual_submission):
            # Check user has inputted correct amount of digits.
            user_input_check = userinputvalidation.check_user_input_length(
                user_input, input_mode)

            if not user_input_check[0]:
                PopupBox(self, "Numpty", user_input_check[1], 200, 50)

            # If the check passes, start the renaming/move file method
            # and get the next one.
            else:
                self.gui.clear_user_input()
                
                full_job_ref, backup_file_name, dest_file_name = (
                    userinputvalidation.rename_file(
                        self, user_input, input_mode, file_extension))

                # Check if there is a file already existing in the destination
                # directory with the same name so we know later that we need
                # to merge the two files.
                dest_duplicate_check = userinputvalidation.check_if_duplicate_file(
                    dest_file_name, current_user.dest_directory)

                backup_success = backup.backup_file(
                    current_file, backup_file_name, scan_dir, backup_dir)

                if backup_success:
                    self.write_log("Backed up " + file_name)
                
                else:
                    self.write_log(
                        "Backup directory not found. " +
                        "Please check your settings.")

                if paperwork_type == "Cust PW":
                    pdfwriter.create_cust_pw(
                        self, file, scan_dir, dest_dir, 
                        full_job_ref, dest_file_name, dest_duplicate_check)

                elif paperwork_type == "Loading List" or paperwork_type == "POD":
                    pdfwriter.create_loading_list_pod(
                        self, file, scan_dir, dest_dir, dest_file_name,
                        dest_duplicate_check)
                    
                del self.main_application.file_list[self.main_application.file_index]

                upload_success = pdfwriter.upload_doc(
                    file, scan_dir, dest_dir,
                    dest_file_name, dest_duplicate_check)

                if upload_success:
                    self.write_log(
                        dest_file_name + " uploaded successfully\n")

                else:
                    self.write_log(dest_file_name + " upload error.")

                self.get_file(self.main_application.file_index, self.main_application.file_list)

        # POD autoprocessing mode
        elif paperwork_type == "POD" and auto_processing == "on" and manual_submission:
                self.clear_user_input()
                
                full_job_ref, backup_file_name, dest_file_name = (
                    userinputvalidation.rename_file(
                        self.main_application, barcode, input_mode, file_extension))

                # Check if there is a file already existing in the destination
                # directory with the same name so we know later that we need
                # to merge the two files.
                dest_duplicate_check = (
                    userinputvalidation.check_if_duplicate_file(
                        dest_file_name, self.current_user.dest_directory))

                backup_success = backup.backup_file(
                    file, backup_file_name, scan_dir, backup_dir)

                if (backup_success):
                    self.gui.write_log("Backed up " + file_name)
                
                else:
                    self.gui.write_log(
                        "Backup directory not found. " +
                        "Please check your settings.")

                pdfwriter.create_loading_list_pod(
                    self.gui, current_file, scan_dir, dest_dir,
                    dest_file_name, dest_duplicate_check)
                    
                del self.file_list[self.file_index]

                upload_success = pdfwriter.upload_doc(
                    current_file, scan_dir, dest_dir,
                    dest_file_name, dest_duplicate_check)

                if upload_success:
                    self.gui.write_log(
                        dest_file_name + " uploaded successfully\n")

                else:
                    self.gui.write_log(dest_file_name + " upload error.")

                self.get_file(
                    self.file_index,
                    self.file_list)

    def michelin_man(self):
        """A workflow that autoprocesses all the files in the scan
        directory that are named as a GR number. The workflow takes
        this GR number as what would ordinarily be the user's input to
        define the job reference and proceeds through the workflow
        based on that."""
        
        directories_valid = self.validate_user_directories()
        
        if directories_valid:
            # user input variables
            pw_type = self.gui.get_current_paperwork_type()
            multi_page_handling = "Do Not Split"

            # directory variables
            current_user = self.get_current_user()

            scan_dir = current_user.scan_directory
            dest_dir = current_user.dest_directory
            backup_dir = current_user.backup_directory

            file_count = 0
            self.file_list = []

            valid_extensions = \
                (".pdf", ".tif", ".tiff", ".jpeg", ".jpg", ".png")

            for item in os.listdir(scan_dir):
                if item.lower().endswith(valid_extensions):
                    self.file_list.append(item)
                    self.gui.write_log("Adding " + item + ".")

            # Converts all image files in the list into PDFs and
            # rebuilds a new list for later use.
            for item in self.file_list:
                self.file_index = self.file_list.index(item)
                
                pdf_file = pdfwriter.image_converter(
                    self.gui, item, scan_dir, multi_page_handling)
                
                split_file_list = pdfwriter.document_splitter(
                    self.gui, pdf_file, scan_dir, "Do Not Split")

                for split_file in reversed(split_file_list):
                    self.file_list.insert(self.file_index, split_file)

                self.file_list.remove(item)

            # With all the TIF files converted, ready to start
            # transforming files where the file name is a GR reference.
            for item in self.file_list:
                valid_extensions.append(".pdf")
                if item.lower().endswith(valid_extensions):
                    file_name, file_extension = os.path.splitext(item)

                    job_ref = re.sub(
                        "[^0-9]", "",
                        re.search("^[^_]*", file_name).group(0).upper())

                    self.write_log("\nJob reference is " + job_ref)
                    
                    if len(job_ref) == 9:
                        full_job_ref, backup_file_name, dest_file_name = (
                            userinputvalidation.rename_file(
                                job_ref, "Normal", file_extension)
                        )

                        # Check if there is a file already existing in
                        # the destination directory with the same name
                        # so we know later that we need to merge the
                        # two files.
                        dest_duplicate_check = (
                            userinputvalidation.check_if_duplicate_file(
                                dest_file_name,
                                self.current_user.dest_directory)
                        )

                        backup_success = backup.backup_file(
                            item, backup_file_name, scan_dir, backup_dir)
                        
                        if (backup_success):
                            self.gui.write_log("Backed up " + file_name)
                
                        else:
                            self.gui.write_log(
                                "Backup directory not found. " +
                                "Please check your settings.")

                        if pw_type == "Cust PW":
                            pdfwriter.create_cust_pw(
                                self.gui, item, scan_dir, dest_dir,
                                full_job_ref, dest_file_name,
                                dest_duplicate_check)
                            
                        elif pw_type == "Loading List" or pw_type == "POD":
                            pdfwriter.create_loading_list_pod(
                                self.gui, item, scan_dir, dest_dir,
                                dest_file_name, dest_duplicate_check)

                        upload_success = pdfwriter.upload_doc(
                            item, scan_dir, dest_dir,
                            dest_file_name, dest_duplicate_check)
                        
                        if upload_success:
                            self.gui.write_log(
                                dest_file_name + " uploaded successfully\n")

                        else:
                            self.gui.write_log(
                                dest_file_name + " upload error.")

                        self.gui.write_log(
                            "Uploaded " + item + " as " + dest_file_name)
                        
                        file_count += 1
                        
                    else:
                        self.gui.write_log("Ignoring" + item)
                        self.file_list.remove(item)

            PopupBox(self,
                "Michelin Man", str(file_count) + " files processed.",
                "215", "60")

    def skip_file(self):
        """Skips over the current file in the list being processed."""

        current_file = self.file_list[self.file_index]
        
        self.gui.clear_user_input()

        self.file_list.remove(current_file)
        self.write_log("Skipping " + current_file)
        
        self.get_file(file_index, file_list)
