"""A module for the main application class."""

from backup import backup
from date.date import Date
from datetime import datetime
from gui.main_menu import MainMenu
from gui.main_menu_thread import MainMenuThread
from gui.popupbox import PopupBox
from gui.settings_window import SettingsWindow
from pdf.pdf_viewer import PDFViewer
from pdf import pdf_reader
from pdf import pdf_writer
from user.user import User
from win32api import GetSystemMetrics

import app.file_system
import app.user_input_validation
import os
import re
import shelve
import threading
import time

class MainApplication():
    """A class for the main application of the program to run."""

    def __init__(self):
        """Constructor method."""

        self.current_user = self.get_user_settings()

        self.__main_menu_semaphore = threading.Semaphore()
        self.__main_menu = MainMenu(self, self.__main_menu_semaphore)
        self.__main_menu_thread = MainMenuThread(self.__main_menu)
        self.__main_menu_thread.start()

        x_axis = str(int(GetSystemMetrics(0) / 4))
        y_axis = str(int(GetSystemMetrics(1) / 4))

        self.__main_menu_semaphore.acquire() 
        directories_valid = self.validate_user_directories()
            
        if not directories_valid:
            self.__main_menu.write_log("\n")

        self.calculate_quick_mode_hint_message()
        self.__main_menu.write_log("Awaiting user input.")
        
        self.__main_menu_semaphore.release()
            
    def get_user_settings(self):
        """Opens the user settings file for the user's directory and
        workspace settings."""

        current_username = os.getlogin()

        # If the user already exists in the user settings data file,
        # load the user up as the current user and pass it back as a
        # user object.
        user_settings_data = shelve.open(
            app.file_system.get_user_settings_data_path())
       
        try:
            current_user = user_settings_data[current_username]
    
        # If the user does not exist, creates a new user and adds it to
        # the user settings data file, passing back the user object.
        except Exception:
            current_user = User(current_username)
            user_settings_data[current_username] = current_user
            user_settings_data.sync()
            
        user_settings_data.close()

        return current_user

    def get_current_user(self):
        """Returns the current user of the program as a User object."""

        return self.current_user

    def validate_user_directories(self) -> bool:
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
                
                self.__main_menu.write_log(
                    directory + " folder is invalid. Please check the " +
                    "folder exists and update it within your settings.")
        
        return all_directories_valid

    def calculate_quick_mode_hint_message(self):
        """Calculates the message to be displayed in the GUI's quick
        mode hint box."""

        # Saving status strings for later.
        possible_status_strings = (
            "Quick Mode Preview: GR190506111",
            "Too many digits",
            "Not enough digits",
            "Should not contain letters/symbols"
        )

        input_mode = self.__main_menu.get_current_input_mode()

        # If input mode is set to normal, set the hint box to be an
        # empty string.
        if input_mode == "Normal":
            self.__main_menu.set_quick_mode_hint_text("")

        # If input mode is set to quick, get the year and month
        # dropdown box variables and make a template ref.
        elif input_mode == "Quick":
            working_year = self.__main_menu.get_current_year_choice()
            years = date.get_years()

            year_prefix = (
                [year.get_short_code() for year in years
                    if year.get_full_code() == working_year]
            )

            #year_prefix = working_year.get_short_code()

            # year_prefix = re.sub("[^0-9]", "",
            #    str([year.short for year in YEARS if year.full == working_year]))

            working_month = self.__main_menu.get_current_month_choice()
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
            self.__main_menu.set_quick_mode_hint_text(hint_message)

    def get_files_in_scan_folder(self):
        """Gets a list of all files in the current user's scan folder
        that have a valid extension for the program to handle."""

        scan_directory = self.current_user.scan_directory

        valid_file_extensions = (
            ".pdf", ".tif", ".tiff", ".tiff", ".jpeg", ".jpg", ".png")
        
        file_list = []

        for scan_file in app.file_system.get_directory_items(scan_directory):
            if scan_file.lower().endswith(valid_file_extensions):
                file_list.append(scan_file)

                self.__main_menu.write_log("Adding " + scan_file + " to list.")
        
        return file_list
    
    def start(self):
        """Starts the workflow of reading/viewing and writing from
        scan files."""

        if not self.validate_user_directories():
            return

        self.file_list = self.get_files_in_scan_folder()

        if not self.file_list:
            PopupBox(
                self.__main_menu, 
                "Failure",
                "No files found.",
                "200", "50"
            )
            
            return

        autoprocessing_mode = self.__main_menu.get_autoprocessing_mode()
        paperwork_type = self.__main_menu.get_current_paperwork_type()
        self.file_index = 0
        self.start_pdf_viewer()
        
        if paperwork_type == "POD" and autoprocessing_mode:
            self.submit_by_barcode(self.file_index, self.file_list)

        else:
            self.get_file(self.file_index, self.file_list)

    def start_pdf_viewer(self):
        self.pdf_viewer = PDFViewer()

    def get_next_file(self):
        """Gets the next file in the scan directory, determining
        the behaviour dependent on the paperwork type and whether
        autoprocessing is on or not."""

        # If the scan folder is empty and the current file index is 0
        # indicating no skipped files remain.
        if not self.file_list:
            PopupBox(
                self.__main_menu, "Guess What",
                "No available files found in scan directory.",
                230, 75)
            
            self.pdf_viewer.close()

            return

        paperwork_type = self.__main_menu.get_current_paperwork_type()
        autoprocessing = self.__main_menu.get_autoprocessing_mode()

        # If the paperwork type is a POD and the system is set to scan
        # the paperwork by barcode number, scan the next file for barcode
        # readings.
        if paperwork_type == "POD" and autoprocessing:
            self.get_file_with_barcode_scanner()

        # If the paperwork type is either Customer Paperwork or
        # Loading List, or autoprocessing is switched off, load up the
        # next scan with the PDF viewer for the user to check for a
        # job number manually rather than automatic barcode scanning.
        else:
            self.get_file_with_pdf_viewer()

    def get_file_with_pdf_viewer(self):
        # Directories
        scan_directory = self.current_user.scan_directory
        multi_page_handling = self.__main_menu.get_multi_page_handling_mode()

        current_file = self.file_list[self.file_index]

        # If file is an image format rather than PDF, convert it to
        # PDF.
        if not current_file.lower().endswith(".pdf"):    
            pdf_file = pdfwriter.image_converter(
                self, current_file, scan_directory, multi_page_handling)

        # If the multi page handling setting is set to split multiple
        # pages of paperwork apart, split it and return them as an
        # array of new pdf files.
        if multi_page_handling:
            split_files = pdfwriter.document_splitter(
                self, pdf_file, scan_directory, multi_page_handling)

            del self.file_list[self.file_index]
            
            # Insert the split PDF files into the current index
            # position of the list of files to be processed.
            # Reverse order to maintain the ordering of the files
            # as they would be end up added as 3rd, 2nd, 1st rather
            # than 1st, 2nd, 3rd.
            for new_file in reversed(split_files):
                self.file_list.insert(
                    self.file_index, new_file)

            current_file = self.file_list[self.file_index]

        self.pdf_viewer.show_image(current_file, scan_directory)
        file_name, file_ext = os.path.splitext(current_file)

        self.__main_menu.set_file_name(file_name)
        self.__main_menu.set_file_extension(file_ext)
        self.__main_menu.write_log("Displaying " + current_file)
        self.__main_menu.move_cursor_to_user_input_box()

    def get_file_with_barcode_scanner(self):
        """Gets the next file by scanning it's barcode contents first,
        submitting it immediately if a valid barcode is found with
        no other conflicting conditions."""

        scan_directory = self.current_user.scan_directory
        multi_page_handling = self.__main_menu.get_multi_page_handling_mode()
        barcode_ref_list = []

        current_file = self.file_list[self.file_index]
        file_name, file_extension = os.path.splitext(current_file)
        self.__main_menu.insert_file_attributes(file_name, file_extension)

        valid_image_extensions = (".jpeg", ".jpg", ".png")

        if file_extension.lower() == ".pdf":
            barcode_ref_list = pdfreader.read_barcodes(
                current_file, scan_directory)

        elif file_extension.lower() in valid_image_extensions:
            barcode_ref_list = pdfreader.image_barcode_reader(
                current_file, scan_directory)

        # If no GR reference obtained, get the file using the PDF
        # viewer instead to manually type in the reference.
        if not barcode_ref_list:
            self.__main_menu.write_log("No barcode found")
            self.get_file_with_pdf_viewer()

        # If more than 1 GR reference obtained, split it apart and
        # show the image.
        elif len(barcode_ref_list) > 1:
            self.__main_menu.write_log("Too many conflicting barcodes?")
            
            split_file_list = pdfwriter.document_splitter(
                self, current_file, scan_directory, "Split")
            
            if split_file_list:
                del self.file_list[self.file_index]

                for file_name in reversed(split_file_list):
                    self.file_list.insert(self.file_index, file_name)
          
            self.get_file_with_pdf_viewer()

        # If 1 GR reference obtained, use this as the user input.
        elif len(barcode_ref_list) == 1:
            job_reference = barcode_ref_list[0]
            
            self.__main_menu.write_log(
                "Barcode " + job_reference + " found successfully")
            
            self.submit_by_barcode(job_reference)

    def submit_by_barcode(self, barcode_reference):
        """Submits a file based on the job reference that has been 
        read from a barcode."""
        
        input_mode = self.__main_menu.get_current_input_mode()
        current_file = self.file_list[self.file_index]
        file_name = app.file_system.get_file_name(current_file)
        file_extension = app.file_system.get_file_ext(current_file)

        job_reference = user_input_validation.create_job_reference(
            self.__main_menu,
            barcode_reference,
            "Normal"
        )

        backup_directory = self.current_user.backup_directory
        paperwork_type = self.__main_menu.get_current_paperwork_type()

        backup_file_name = user_input_validation.create_backup_file_name(
            job_reference, paperwork_type, file_extension, backup_directory)
        
        scan_directory = self.current_user.scan_directory

        backup_success = backup.backup_file(
            current_file, backup_file_name, scan_directory, backup_directory)

        if backup_success:
            self.__main_menu.write_log("Backed up " + file_name)
        
        else:
            self.__main_menu.write_log(
                "Backup directory not found. " +
                "Please check your settings.")
            
            return

        dest_file_name = user_input_validation.create_destination_file_name(
            job_reference, paperwork_type, file_extension)

        dest_directory = self.current_user.destination_directory

        # Check if there is a file already existing in the
        # destination directory with the same name so we know later
        # that we need to merge the two files.
        dest_duplicate_check = (
            user_input_validation.check_if_duplicate_file(
                dest_file_name, dest_directory))

        scan_directory = self.current_user.scan_directory

        pdfwriter.create_loading_list_pod(
            self.__main_menu, current_file, scan_directory, dest_directory,
            dest_file_name, dest_duplicate_check)

        upload_success = pdfwriter.upload_doc(
            current_file, scan_directory, dest_directory,
            dest_file_name, dest_duplicate_check)

        if upload_success:
            self.__main_menu.write_log(
                dest_file_name + " uploaded successfully\n")

            del self.file_list[self.file_index]

        else:
            self.__main_menu.write_log(dest_file_name + " upload error.")

            return

        # If no more files remaining (whether skipped or empty).
        if self.file_index >= len(self.file_list):
            message = "No more files remaining."

            if self.file_index > 0:
                message += "\n" + self.file_index + " files skipped."

            PopupBox(self.__main_menu, "Job Complete", message, 300, 300)
        
        else:
            self.get_next_file()

    def submit(self):
        """Runs the submission process workflow."""

        # User input variables.
        user_input = self.__main_menu.get_user_input()
        input_mode = self.__main_menu.get_current_input_mode()
        paperwork_type = self.__main_menu.get_current_paperwork_type()
        auto_processing = self.__main_menu.get_autoprocessing_mode()

        # Directory variables.
        current_user = self.get_current_user()

        scan_dir = current_user.scan_directory
        dest_dir = current_user.dest_directory
        backup_dir = current_user.backup_directory

        # File variables.
        current_file = self.file_list[self.file_index]
        file_name, file_extension = os.path.splitext(current_file)

        valid_paperwork_types = ("Cust PW", "Loading List", "POD")

        if (paperwork_type in valid_paperwork_types
                and auto_processing == "off"
                or auto_processing == "on" and manual_submission):
            # Check user has inputted correct amount of digits.
            user_input_check = user_input_validation.check_user_input_length(
                user_input, input_mode)

            if not user_input_check[0]:
                PopupBox(self, "Numpty", user_input_check[1], 200, 50)

            # If the check passes, start the renaming/move file method
            # and get the next one.
            else:
                self.__main_menu.clear_user_input()
                
                full_job_ref = user_input_validation.create_job_reference(
                    self.__main_menu,
                    user_input,
                    input_mode
                )

                backup_file_name, dest_file_name = (
                    user_input_validation.create_file_names(
                        self, user_input, input_mode, file_extension))

                # Check if there is a file already existing in the destination
                # directory with the same name so we know later that we need
                # to merge the two files.
                dest_duplicate_check = user_input_validation.check_if_duplicate_file(
                    dest_file_name, current_user.dest_directory)

                backup_success = backup.backup_file(
                    current_file, backup_file_name, scan_dir, backup_dir)

                if backup_success:
                    self.__main_menu.write_log("Backed up " + file_name)
                
                else:
                    self.__main_menu.write_log(
                        "Backup directory not found. " +
                        "Please check your settings.")

                if paperwork_type == "Cust PW":
                    pdfwriter.create_cust_pw(
                        self, current_file, scan_dir, dest_dir, 
                        full_job_ref, dest_file_name, dest_duplicate_check)

                elif paperwork_type == "Loading List" or paperwork_type == "POD":
                    pdfwriter.create_loading_list_pod(
                        self, current_file, scan_dir, dest_dir,
                        dest_file_name, dest_duplicate_check)
                    
        # POD autoprocessing mode
        elif (paperwork_type == "POD" and auto_processing == "on" 
                and manual_submission):
            self.__main_menu.clear_user_input()
            
            full_job_ref = user_input_validation.create_job_reference(
                self.__main_menu,
                user_input,
                input_mode
            )

            backup_file_name, dest_file_name = (
                user_input_validation.create_file_names(
                    self, barcode, input_mode, file_extension))

            # Check if there is a file already existing in the
            # destination directory with the same name so we know later
            # that we need to merge the two files.
            dest_duplicate_check = (
                userinputvalidation.check_if_duplicate_file(
                    dest_file_name, self.current_user.dest_directory))

            backup_success = backup.backup_file(
                current_file, backup_file_name, scan_dir, backup_dir)

            if (backup_success):
                self.__main_menu.write_log("Backed up " + file_name)
            
            else:
                self.__main_menu.write_log(
                    "Backup directory not found. " +
                    "Please check your settings.")

            pdf_writer.create_loading_list_pod(
                self.__main_menu, current_file, scan_dir, dest_dir,
                dest_file_name, dest_duplicate_check)
                
        del self.file_list[self.file_index]

        upload_success = pdfwriter.upload_doc(
            current_file, scan_dir, dest_dir,
            dest_file_name, dest_duplicate_check)

        if upload_success:
            self.__main_menu.write_log(
                dest_file_name + " uploaded successfully\n")

        else:
            self.__main_menu.write_log(dest_file_name + " upload error.")

        self.get_file(self.file_index, self.file_list)

    def michelin_man(self):
        """A workflow that autoprocesses all the files in the scan
        directory that are named as a GR number. The workflow takes
        this GR number as what would ordinarily be the user's input to
        define the job reference and proceeds through the workflow
        based on that."""
        
        directories_valid = self.validate_user_directories()
        
        if directories_valid:
            # user input variables
            pw_type = self.__main_menu.get_current_paperwork_type()
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
                    self.__main_menu.write_log("Adding " + item + ".")

            # Converts all image files in the list into PDFs and
            # rebuilds a new list for later use.
            for item in self.file_list:
                self.file_index = self.file_list.index(item)
                
                pdf_file = pdfwriter.image_converter(
                    self.__main_menu, item, scan_dir, multi_page_handling)
                
                split_file_list = pdfwriter.document_splitter(
                    self.__main_menu, pdf_file, scan_dir, "Do Not Split")

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
                            userinputvalidation.create_file_names(
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
                            self.__main_menu.write_log("Backed up " + file_name)
                
                        else:
                            self.__main_menu.write_log(
                                "Backup directory not found. " +
                                "Please check your settings.")

                        if pw_type == "Cust PW":
                            pdfwriter.create_cust_pw(
                                self.__main_menu, item, scan_dir, dest_dir,
                                full_job_ref, dest_file_name,
                                dest_duplicate_check)
                            
                        elif pw_type == "Loading List" or pw_type == "POD":
                            pdfwriter.create_loading_list_pod(
                                self.__main_menu, item, scan_dir, dest_dir,
                                dest_file_name, dest_duplicate_check)

                        upload_success = pdfwriter.upload_doc(
                            item, scan_dir, dest_dir,
                            dest_file_name, dest_duplicate_check)
                        
                        if upload_success:
                            self.__main_menu.write_log(
                                dest_file_name + " uploaded successfully\n")

                        else:
                            self.__main_menu.write_log(
                                dest_file_name + " upload error.")

                        self.__main_menu.write_log(
                            "Uploaded " + item + " as " + dest_file_name)
                        
                        file_count += 1
                        
                    else:
                        self.__main_menu.write_log("Ignoring" + item)
                        self.file_list.remove(item)

            PopupBox(self,
                "Michelin Man", str(file_count) + " files processed.",
                "215", "60")

    def skip_file(self):
        """Skips over the current file in the list being processed."""

        current_file = self.file_list[self.file_index]
        
        self.__main_menu.clear_user_input()

        self.file_list.remove(current_file)
        self.write_log("Skipping " + current_file)
        
        self.get_file(file_index, file_list)

    def exit(self):
        """Exits the program."""

        try:
            self.pdf_viewer.close()
            exit()

        except:
            exit()

    def open_settings_menu(self):
        """Opens the settings menu."""

        self.__settings_menu = SettingsWindow(self)