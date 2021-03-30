import app.backup
from datetime import datetime
from gui.mainmenu.main_menu import MainMenu
from gui.popupbox import PopupBox
from gui.settings.settings_menu import SettingsMenu
from pdf.pdf_viewer import PDFViewer
import pdf.pdf_reader
import pdf.pdf_writer
from user import User, UserDefaults
import wx

import app.file_system as file_system
import app.user_input_validation as user_input_validation
import date.date
import os
import re
import shelve

class Model():
    """A class for the model."""

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
        except Exception as exception:
            print(exception)
            current_user = User(current_username)
            user_settings_data[current_username] = current_user
            user_settings_data.sync()

            print("Created user: ", current_user.get_name())
            
        user_settings_data.close()

        return current_user

class Controller():
    """A class for the main controller."""

    def __init__(self):
        self.__model = Model()
        self.__current_user = self.__model.get_user_settings()
        self.__create_main_menu()
        directories_valid = self.validate_user_directories()

        if not directories_valid:
            self.__main_menu.write_log("\n")

        self.calculate_quick_mode_hint_message()
        self.__main_menu.write_log("Awaiting user input.")
        self.__assign_main_menu_button_functions()
        user_defaults = self.get_default_settings_from_user()
        self.__set_main_menu_values_from_user_defaults(user_defaults)

    def __create_main_menu(self):
        """Creates the main menu."""

        self.__main_menu = MainMenu()
        self.__assign_main_menu_button_functions()

    def __assign_main_menu_button_functions(self):
        """Assigns functions to the main menu's buttons."""

        self.__main_menu.set_submit_button_function(self.submit_click)
        self.__main_menu.set_skip_button_function(self.skip_button_click)
        
        self.__main_menu.set_split_document_button_function(
            self.split_document_button_click)

        self.__main_menu.set_start_button_function(self.start_button_click)
        self.__main_menu.set_exit_button_function(self.exit_button_click)
        
        self.__main_menu.set_settings_button_function(
            self.settings_button_click)

        self.__main_menu.set_michelin_man_button_function(
            self.michelin_man_button_click)

    def submit_click(self, event = None):
        print("Submit button clicked.")

    def skip_button_click(self, event = None):
        print("Skip button clicked.")

    def split_document_button_click(self, event = None):
        print("Split Document button clicked.")

    def exit_button_click(self, event = None):
        self.exit()

    def start_button_click(self, event = None):
        print("Start button clicked.")

    def settings_button_click(self, event = None):
        print("Settings button clicked.")

        self.__create_settings_menu()

    def michelin_man_button_click(self, event = None):
        print("Michelin Man button clicked.")

    def exit(self):
        """Exits the program."""

        exit()

    def validate_user_directories(self) -> bool:
        """Checks whether all the working directories of a user are
        valid and accessible. Prints to the GUI's log if not and
        returns an overall Boolean at the end on whether all
        directories are valid or not."""

        directory_checks = self.__current_user.validate_directories_check()
        all_directories_valid = True

        for directory in directory_checks:
            is_directory_valid = directory_checks[directory]
            
            if not is_directory_valid:
                all_directories_valid = False
                
                self.__main_menu.write_log(
                    directory + " folder is invalid. Please check the " +
                    "folder exists and update it within your settings.\n")
        
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

    def __create_settings_menu(self):
        """Creates and launches the user settings menu."""

        self.__settings_menu = SettingsMenu()
        self.__assign_settings_menu_button_functions()
        self.__load_settings_menu_values()

    def __load_settings_menu_values(self):
        """Does stuff and things."""

        values = self.get_default_settings_from_user()
        self.__set_settings_menu_values_from_values(values)

    def __set_settings_menu_values_from_values(self, defaults: UserDefaults):
        """Sets the settings menu fields based on values data
        structure.
        """

        menu = self.__settings_menu

        menu.set_user_name(defaults.user_name)
        menu.set_scan_directory(defaults.scan_directory)
        menu.set_destination_directory(defaults.destination_directory)
        menu.set_backup_directory(defaults.backup_directory)
        menu.set_paperwork_type(defaults.paperwork_type)
        menu.set_input_mode_dropdown_box(defaults.input_mode)
        menu.set_multi_page_handling(defaults.multi_page_handling)
        menu.set_autoprocessing_checkbox(defaults.autoprocessing_mode)

    def __set_main_menu_values_from_user_defaults(self,
            defaults: UserDefaults):
        """Sets the main menu's default options from a User Defaults
        data structure.
        """

        menu = self.__main_menu

        menu.set_paperwork_type(defaults.paperwork_type)
        # menu.set_input_mode(defaults.input_mode)
        # menu.set_multi_page_handling(defaults.multi_page_handling)
        # menu.set_autoprocessing_mode(defaults.autoprocessing_mode)
        

    def get_default_settings_from_user(self) -> UserDefaults:
        """Returns the default values from the current user."""

        user = self.__current_user
        values = UserDefaults.from_user(user)

        return values

    def __save_settings_menu_values(self, event = None):
        """Saves the current settings menu values to the current user's
        state.
        """
 
        values = self.get_user_defaults_from_settings_menu()
        self.__set_user_defaults_from_values(values)
        self.__close_settings_menu()

    def __set_user_defaults_from_values(self, values: UserDefaults):
        """Sets the user's default settings from a user values data
        structure.
        """

        user = self.__current_user
        
        user.set_scan_directory(values.scan_directory)
        user.set_destination_directory(values.destination_directory)
        user.set_backup_directory(values.backup_directory)
        user.set_paperwork_type(values.paperwork_type)
        user.set_multi_page_handling(values.multi_page_handling)
        user.set_input_mode(values.input_mode)
        user.set_auto_processing_mode(values.autoprocessing_mode)

        user.sync()

    def __assign_settings_menu_button_functions(self):
        """Assigns functions to the settings menu's buttons."""

        menu = self.__settings_menu

        menu.set_save_button_function(self.__save_settings_menu_values)
        menu.set_cancel_button_function(self.__close_settings_menu)
        
        menu.set_browse_scan_directory_button_function(
            self.browse_scan_directory_path)
        
        menu.set_browse_destination_directory_button_function(
            self.browse_destination_directory_path)
        
        menu.set_browse_backup_directory_button_function(
            self.browse_backup_directory_path)

    def get_path_from_folder_browser(self) -> str:
        """Launches a folder browser."""

        path = ""

        with wx.DirDialog(
                None, "Select a directory", style=wx.DD_DEFAULT_STYLE
                ) as file_dialog:
            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return None

            path = file_dialog.GetPath()

        return path

    def browse_path_and_use_with_function(self, callback_function):
        """Launches a directory dialog window to get a path and then
        feeds it as the only parameter into a function.
        """

        path = self.get_path_from_folder_browser()
        callback_function(path)

    def browse_scan_directory_path(self, event = None):
        self.browse_path_and_use_with_function(
            self.__settings_menu.set_scan_directory)

    def browse_destination_directory_path(self, event = None):
        self.browse_path_and_use_with_function(
            self.__settings_menu.set_destination_directory)

    def browse_backup_directory_path(self, event = None):
        self.browse_path_and_use_with_function(
            self.__settings_menu.set_backup_directory)

    def __close_settings_menu(self, event = None):
        self.__settings_menu.close()

    def get_current_user(self):
        """Returns the current user of the program as a User object."""

        return self.__current_user

    def get_files_in_scan_folder(self):
        """Gets a list of all files in the current user's scan folder
        that have a valid extension for the program to handle."""

        scan_directory = self.__current_user.scan_directory

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
        scan_directory = self.__current_user.scan_directory
        multi_page_handling = self.__main_menu.get_multi_page_handling_mode()

        current_file = self.file_list[self.file_index]

        # If file is an image format rather than PDF, convert it to
        # PDF.
        if not current_file.lower().endswith(".pdf"):    
            pdf_file = pdf_writer.image_converter(
                self, current_file, scan_directory, multi_page_handling)

        # If the multi page handling setting is set to split multiple
        # pages of paperwork apart, split it and return them as an
        # array of new pdf files.
        if multi_page_handling:
            split_files = pdf_writer.document_splitter(
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

        scan_directory = self.__current_user.scan_directory
        multi_page_handling = self.__main_menu.get_multi_page_handling_mode()
        barcode_ref_list = []

        current_file = self.file_list[self.file_index]
        file_name, file_extension = os.path.splitext(current_file)
        self.__main_menu.insert_file_attributes(file_name, file_extension)

        valid_image_extensions = (".jpeg", ".jpg", ".png")

        if file_extension.lower() == ".pdf":
            barcode_ref_list = pdf_reader.read_barcodes(
                current_file, scan_directory)

        elif file_extension.lower() in valid_image_extensions:
            barcode_ref_list = pdf_reader.image_barcode_reader(
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
            
            split_file_list = pdf_writer.document_splitter(
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

        job_reference = app.user_input_validation.create_job_reference(
            self.__main_menu,
            barcode_reference,
            "Normal"
        )

        backup_directory = self.__current_user.backup_directory
        paperwork_type = self.__main_menu.get_current_paperwork_type()

        backup_file_name = app.user_input_validation.create_backup_file_name(
            job_reference, paperwork_type, file_extension, backup_directory)
        
        scan_directory = self.__current_user.scan_directory

        backup_success = backup.backup_file(
            current_file, backup_file_name, scan_directory, backup_directory)

        if backup_success:
            self.__main_menu.write_log("Backed up " + file_name)
        
        else:
            self.__main_menu.write_log(
                "Backup directory not found. " +
                "Please check your settings.")
            
            return

        dest_file_name = app.user_input_validation.create_destination_file_name(
            job_reference, paperwork_type, file_extension)

        dest_directory = self.__current_user.destination_directory

        # Check if there is a file already existing in the
        # destination directory with the same name so we know later
        # that we need to merge the two files.
        dest_duplicate_check = (
            app.user_input_validation.check_if_duplicate_file(
                dest_file_name, dest_directory))

        scan_directory = self.__current_user.scan_directory

        pdf_writer.create_loading_list_pod(
            self.__main_menu, current_file, scan_directory, dest_directory,
            dest_file_name, dest_duplicate_check)

        upload_success = pdf_writer.upload_doc(
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
            user_input_check = app.user_input_validation.check_user_input_length(
                user_input, input_mode)

            if not user_input_check[0]:
                PopupBox(self, "Numpty", user_input_check[1], 200, 50)

            # If the check passes, start the renaming/move file method
            # and get the next one.
            else:
                self.__main_menu.clear_user_input()
                
                full_job_ref = app.user_input_validation.create_job_reference(
                    self.__main_menu,
                    user_input,
                    input_mode
                )

                backup_file_name, dest_file_name = (
                    app.user_input_validation.create_file_names(
                        self, user_input, input_mode, file_extension))

                # Check if there is a file already existing in the destination
                # directory with the same name so we know later that we need
                # to merge the two files.
                dest_duplicate_check = app.user_input_validation.check_if_duplicate_file(
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
                    pdf_writer.create_cust_pw(
                        self, current_file, scan_dir, dest_dir, 
                        full_job_ref, dest_file_name, dest_duplicate_check)

                elif paperwork_type == "Loading List" or paperwork_type == "POD":
                    pdf_writer.create_loading_list_pod(
                        self, current_file, scan_dir, dest_dir,
                        dest_file_name, dest_duplicate_check)
                    
        # POD autoprocessing mode
        elif (paperwork_type == "POD" and auto_processing == "on" 
                and manual_submission):
            self.__main_menu.clear_user_input()
            
            full_job_ref = app.user_input_validation.create_job_reference(
                self.__main_menu,
                user_input,
                input_mode
            )

            backup_file_name, dest_file_name = (
                app.user_input_validation.create_file_names(
                    self, barcode, input_mode, file_extension))

            # Check if there is a file already existing in the
            # destination directory with the same name so we know later
            # that we need to merge the two files.
            dest_duplicate_check = (
                app.user_input_validation.check_if_duplicate_file(
                    dest_file_name, self.__current_user.dest_directory))

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

        upload_success = pdf_writer.upload_doc(
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
                
                pdf_file = pdf_writer.image_converter(
                    self.__main_menu, item, scan_dir, multi_page_handling)
                
                split_file_list = pdf_writer.document_splitter(
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
                            app.user_input_validation.create_file_names(
                                job_ref, "Normal", file_extension)
                        )

                        # Check if there is a file already existing in
                        # the destination directory with the same name
                        # so we know later that we need to merge the
                        # two files.
                        dest_duplicate_check = (
                            app.user_input_validation.check_if_duplicate_file(
                                dest_file_name,
                                self.__current_user.dest_directory)
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
                            pdf_writer.create_cust_pw(
                                self.__main_menu, item, scan_dir, dest_dir,
                                full_job_ref, dest_file_name,
                                dest_duplicate_check)
                            
                        elif pw_type == "Loading List" or pw_type == "POD":
                            pdf_writer.create_loading_list_pod(
                                self.__main_menu, item, scan_dir, dest_dir,
                                dest_file_name, dest_duplicate_check)

                        upload_success = pdf_writer.upload_doc(
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

    def get_user_defaults_from_settings_menu(self) -> UserDefaults:
        """Creates a set of values from a settings menu object."""

        values = UserDefaults()
        menu = self.__settings_menu

        values.scan_directory = menu.get_scan_directory()
        values.destination_directory = menu.get_destination_directory()
        values.backup_directory = menu.get_backup_directory()
        values.paperwork_type = menu.get_paperwork_type()
        values.input_mode = menu.get_input_mode()
        values.multi_page_handling = menu.get_multi_page_handling()
        values.autoprocessing_mode = menu.get_autoprocessing_mode()

        return values

class MainApplication():
    """A class for the main application of the program to run."""

    def __init__(self):
        """Constructor method."""

        self.__app = wx.App()
        self.__controller = Controller()
        self.__app.MainLoop()
