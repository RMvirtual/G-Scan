import os
import filesystem
import backup
import userinputvalidation
import pdfreader
import pdfwriter
from settingswindow import SettingsWindow
from pdfviewer import PDFViewer
from user import User
from date import Date
from popupbox import PopupBox
import shelve
import shutil
import re
import PIL.ImageTk
from PIL import Image as pil_image
from wand.image import Image as wand_image
from pyzbar.pyzbar import decode
import PyPDF2
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, A3
from reportlab.lib.units import mm
from reportlab.graphics.barcode import code128
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime
from os import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
from tkinter import filedialog
from win32api import GetSystemMetrics

pdfmetrics.registerFont(TTFont("Calibri", "Calibri.ttf"))
pdfmetrics.registerFont(TTFont("Calibri-Bold", "Calibrib.ttf"))

class Application(Frame):
    """GUI Box for inputting a GR Number when viewing a page of paperwork"""

    def __init__(self, master):
        """ Initialise the frame, whatever that means."""
        super(Application, self).__init__(master)
        self.grid()
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.current_user = self.get_user_settings()
        self.temp_dir = filesystem.get_temp_directory()
        self.create_widgets(
            name = "", ext = "", job_ref = "", current_user = self.current_user)
        self.quick_mode_hint_message()
        self.activity_log_row_count = 1
        self.current_user.validate_directories_check(self)
        self.write_log("Awaiting input")
        
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

    def create_widgets(self, name, ext, job_ref, current_user):
        """Creates all the widgets required for the main GUI window."""

        # Left master frame to contain the logo frame and the
        # file processing frame.
        left_master_frame = Frame(
            self, width = 390, height = 255,
            borderwidth = 0, highlightthickness = 0, bg = "white")

        left_master_frame.grid(row = 1, column = 0)
        left_master_frame.grid_rowconfigure(0, weight = 1)
        left_master_frame.grid_columnconfigure(0, weight = 1)

        self.create_left_master_frame_widgets(
            left_master_frame, name, ext, job_ref)

        # Right master frame.
        right_master_frame = Frame(
            self, width = 390, height = 255,
            borderwidth = 0, highlightthickness = 0, bg = "white")
        
        right_master_frame.grid(row = 1, column = 1, sticky = "nsew")
        right_master_frame.grid_rowconfigure(0, weight = 1)
        right_master_frame.grid_columnconfigure(0, weight = 1)
        
        self.create_right_master_frame_widgets(
            right_master_frame, current_user)

        # Activity log frame along the bottom.
        activity_log_frame = Frame(
            self, width = 500, height = 250,
            borderwidth = 0, highlightthickness = 0, bg = "white")
        
        activity_log_frame.grid(
            row = 2, column = 0, columnspan = 2, sticky = N + W)
        
        activity_log_frame.grid_rowconfigure(0, weight = 1)
        activity_log_frame.grid_columnconfigure(0, weight = 1)
        
        # Text box for activity log to write into.
        self.activity_log_textbox = Text(
            activity_log_frame,
            width = 120, height = 11, wrap = WORD)
        
        self.activity_log_textbox.grid(
            row = 0, column = 0, sticky = W, padx = 7, pady = 5)

        # Scroll bar for the activity log.
        self.scroll_bar = Scrollbar(
            activity_log_frame,
            orient="vertical",
            command=self.activity_log_textbox.yview)
        
        self.scroll_bar.grid(row=0, column = 1, sticky = N + S + W)

        # Have to do config the activity log textbox here or the system
        # won't recognise the custom scroll bar being assigned to it.
        self.activity_log_textbox.config(
            font = ("Calibri", 11),
            bg = "light grey",
            state = DISABLED,
            yscrollcommand=self.scroll_bar.set)

        for i in range(1,10):
            self.columnconfigure(i, weight = 1)

        for i in range(1,10):
            self.rowconfigure(1, weight = 1)

    def create_left_master_frame_widgets(self, left_master_frame, name, ext,
            job_ref):
        """Creates the widgets for the left master frame."""

        # Logo frame inside the left master frame.
        self.logo_frame = Frame(
            left_master_frame,
            bg = "white", width = 390, height = 122,
            bd = 0, borderwidth = 0, highlightthickness=0)

        self.logo_frame.grid(row = 0, column = 0, sticky = N)
        self.logo_frame.grid_rowconfigure(0, weight = 1)
        self.logo_frame.grid_columnconfigure(0, weight = 1)

        # Create the the G-Scan logo image.
        gscan_logo_image_path = (
            filesystem.get_resources_directory() + "images\\g-scan_logo.png")

        logo = PIL.ImageTk.PhotoImage(pil_image.open(gscan_logo_image_path))
        logo_lbl = Label(self.logo_frame, image = logo)
        logo_lbl.image = logo
        logo_lbl.config(bg = "white")
        logo_lbl.grid()

        # Frame for the file processing panel inside the
        # left master frame.
        self.file_frame = Frame(
            left_master_frame,
            bg = "white", highlightthickness=0,
            width = 375, height = 350, bd = 0)

        self.create_file_frame_widgets(self.file_frame, name, ext, job_ref)        

    def create_right_master_frame_widgets(self, right_master_frame,
            current_user):
        """Creates the right master frame's widgets."""

        # Frame for the settings panel inside the right master frame.
        settings_frame = Frame(
            right_master_frame, 
            bg = "white", highlightthickness=0, bd = 0)

        settings_frame.grid(row = 0, column = 0, sticky = S)
        settings_frame.grid_rowconfigure(0, weight = 1)
        settings_frame.grid_columnconfigure(0, weight = 1)

        self.create_settings_frame_widgets(settings_frame, current_user)

    def create_file_frame_widgets(self, file_frame, name, ext, job_ref):
        """Creates widgets required for the file frame."""

        file_frame.grid(row = 1, column = 0, sticky = S)
        file_frame.grid_rowconfigure(0, weight = 1)
        file_frame.grid_columnconfigure(0, weight = 1)

        # File name label.
        self.file_name_lbl = Label(file_frame, text = "Filename:\t")
        self.file_name_lbl.grid(row = 0, column = 0, sticky = W, padx = 5)
        self.file_name_lbl.config(font=("Calibri", 11), bg = "white")

        # File name text field to display the name of the file.
        self.file_name_txt = Text(
            file_frame, width = 42, height = 1, wrap = WORD)
        
        self.file_name_txt.grid(
            row = 0, column = 1, columnspan = 4, sticky = W)
        
        self.file_name_txt.insert(0.0, name)
        self.file_name_txt.config(
            font = ("Calibri", 11), bg = "light grey", state = DISABLED)

        # File extension label.
        self.file_ext_lbl = Label(file_frame, text = "File Type:\t")
        self.file_ext_lbl.grid(row = 1, column = 0, sticky = W, padx = 5)
        self.file_ext_lbl.config(font=("Calibri", 11), bg = "white")

        # File extension text field to display the file extension.
        self.file_ext_txt = Text(
            file_frame, width = 42, height = 1, wrap = WORD)
        
        self.file_ext_txt.grid(
            row = 1, column = 1, columnspan = 4, sticky = W)
        
        self.file_ext_txt.insert(0.0, ext)
        self.file_ext_txt.config(
            font = ("Calibri", 11), bg = "light grey", state = DISABLED)

        # Input instruction label that provides text to aid the user
        # in discerning their next action.
        self.input_instruction_lbl = Label(
            file_frame,
            text = "Please enter the Job Reference (excluding \"GR\")")
        
        self.input_instruction_lbl.grid(
            row = 2, column = 0, columnspan = 5, sticky = W, padx = 5)
        self.input_instruction_lbl.config(font=("Calibri", 11), bg = "white")

        # User input entry box.
        self.user_input_entry_box = Entry(file_frame)
        self.user_input_entry_box.grid(
            row = 3, column = 0, columnspan = 2, sticky = W, padx = 5)

        self.user_input_entry_box.config(
            font=("Calibri", 11), bg = "light grey")
        
        self.user_input_entry_box.bind("<Return>", self.submit_enter_key)
        self.user_input_entry_box.bind("<KP_Enter>", self.submit_enter_key)

        # User input submission button.
        self.submit_bttn = Button(
            file_frame, text = "Submit",command = self.submit)
        
        self.submit_bttn.grid(row = 3, column = 1, sticky = E, ipadx = 28)
        self.submit_bttn.config(font=("Calibri", 11))
        self.submit_bttn.bind("<Return>", self.submit_enter_key)
        self.submit_bttn.bind("<KP_Enter>", self.submit_enter_key)

        # Skip file button.
        self.skip_bttn = Button(
            file_frame, text = "Skip", command = lambda: self.skip())
        
        self.skip_bttn.grid(row = 3, column = 3, sticky = E, padx = 5)
        self.skip_bttn.config(font=("Calibri", 11))
        self.skip_bttn.bind("<Return>", self.skip_enter_key)
        self.skip_bttn.bind("<KP_Enter>", self.skip_enter_key)

        # Document splitter button.
        self.split_multi_page_bttn = Button(
            file_frame,
            text = "Split Document",
            command = lambda: pdfwriter.manual_document_splitter(self))
        
        self.split_multi_page_bttn.grid(
            row = 3, column = 4, columnspan = 2, sticky = E)
        
        self.split_multi_page_bttn.config(font=("Calibri", 11))
        self.split_multi_page_bttn.bind("<Return>", self.split_pdf_enter_key)
        
        self.split_multi_page_bttn.bind(
            "<KP_Enter>", self.split_pdf_enter_key)

        # Start button.
        self.start_bttn = Button(
            file_frame, text = "Start", command = self.start)
        
        self.start_bttn.grid(
            row = 4, column = 0, sticky = W, padx = 5, pady = 3)
        
        self.start_bttn.config(font=("Calibri", 11))
        self.start_bttn.bind("<Return>", self.start_enter_key)
        self.start_bttn.bind("<KP_Enter>", self.start_enter_key)

        # GR Quick Mode setting text display notice informing the user
        # whether quick mode is switched on or not.
        self.quick_mode_notice_txt = Text(
            file_frame, width = 30, height = 1, wrap = WORD)
        
        self.quick_mode_notice_txt.grid(
            row = 4, column = 1, columnspan = 4, sticky = SE)
        
        self.quick_mode_notice_txt.config(
            font = ("Calibri", 11), bg = "White",
            highlightthickness = 0, borderwidth = 0,
            state = DISABLED)

    def create_settings_frame_widgets(self, settings_frame, current_user):
        # Paperwork type heading for the radio dial to determine
        # the type of paperwork being processed.

        self.pw_type_lbl = Label(settings_frame, text = "Paperwork Type")
        self.pw_type_lbl.config(font=("Calibri", 13), bg = "white")
        self.pw_type_lbl.grid(row = 0, column = 0, padx = 10, sticky = W)

        # Paperwork type radio buttons.
        # Initialise the paperwork type variable for the radio button options.
        self.pw_setting = StringVar()
        self.pw_setting.set(current_user.pw_type)
        
        # Customer Paperwork paperwork type radio button.
        self.cust_pw_radio_bttn = Radiobutton(
            settings_frame,
            text = "Customer PW",
            variable = self.pw_setting,
            value = "Cust PW",
            bg = "white",
            font = ("Calibri", 11),
            highlightthickness = 0)
        
        self.cust_pw_radio_bttn.grid(
            row = 1, column = 0,
            sticky = W, padx = 10, pady = 3)

        # Loading list paperwork type radio button.
        self.loading_list_radio_bttn = Radiobutton(
            settings_frame,
            text = "Loading List",
            variable = self.pw_setting,
            value = "Loading List",
            bg = "White",
            font = ("Calibri", 11),
            highlightthickness = 0
            )
        
        self.loading_list_radio_bttn.grid(
            row = 1, column = 1, sticky = W, pady = 3)

        # POD paperwork type radio button.
        self.pod_radio_bttn = Radiobutton(
            settings_frame,
            text = "POD",
            variable = self.pw_setting,
            value = "POD",
            bg = "White",
            font = ("Calibri", 11),
            highlightthickness = 0)
        
        self.pod_radio_bttn.grid(
            row = 1, column = 2,
            sticky = W, padx = 10, pady = 3)

        # POD autoprocessing mode checkbox to allow the user to
        # toggle this mode on and off.
        self.autoprocessing_mode = StringVar()
        self.autoprocessing_mode.set(current_user.autoprocessing)

        self.autoprocessing_checkbox = Checkbutton(
            settings_frame,
            text = "Autoprocess",
            variable = self.autoprocessing_mode,
            onvalue = "on",
            offvalue = "off",
            bg = "White",
            font = ("Calibri", 8),
            highlightthickness = 0)
        
        self.autoprocessing_checkbox.grid(
            row = 1, column = 3, sticky = W, pady = 3)

        # Input mode heading.
        self.input_mode_lbl = Label(settings_frame, text = "Input Mode")
        
        self.input_mode_lbl.grid(
            row = 2, column = 0, sticky = S + W, padx = 10, pady = 8)
        
        self.input_mode_lbl.config(font=("Calibri", 13), bg = "White")

        # Input mode radio buttons.
        # Initialise the input mode variable for input mode options.
        self.current_input_mode = StringVar()
        self.current_input_mode.set(current_user.input_mode)
        
        # Normal input mode radio button.
        self.normal_mode_radio_bttn = Radiobutton(
            settings_frame,
            text = "Normal Mode",
            variable = self.current_input_mode,
            value = "Normal",
            bg = "White",
            font = ("Calibri", 11),
            highlightthickness = 0,
            command = self.quick_mode_hint_message)
            
        self.normal_mode_radio_bttn.grid(
            row = 3, column = 0,
            rowspan = 2, padx = 10, pady = 5, sticky = NW)

        # Quick input mode radio button.
        self.quick_mode_radio_bttn = Radiobutton(
            settings_frame,
            text = "Quick Mode",
            variable = self.current_input_mode,
            value = "Quick",
            bg = "White",
            font = ("Calibri", 11),
            highlightthickness = 0,
            command = self.quick_mode_hint_message
            )
        
        self.quick_mode_radio_bttn.grid(
            row = 3, column = 1, rowspan = 2, pady = 5, sticky = NW)

        # Dropdown box for selecting the month that quick mode uses.
        self.month_choice = StringVar(settings_frame)
        self.month_choice.set(CURRENT_MONTH)
        
        self.month_dropdown_box = OptionMenu(
            settings_frame,
            self.month_choice,
            *MONTHS,
            command = self.quick_mode_hint_message)

        self.month_dropdown_box.grid(
            row = 3, column = 2, columnspan = 2, padx = 10, sticky = NW)
        
        self.month_dropdown_box.config(
            font =("Calibri", 11), highlightthickness= 0, width = 13)
        
        # Dropdown box for selecting the year that quick mode uses.
        self.year_choice = StringVar(settings_frame)
        self.year_choice.set(CURRENT_YEAR)

        self.year_dropdown_box = OptionMenu(
            settings_frame,
            self.year_choice,
            LAST_YEAR,
            CURRENT_YEAR,
            command = self.quick_mode_hint_message)
        
        self.year_dropdown_box.grid(
            row = 4, column = 2, columnspan = 2, padx = 10, sticky = NW)
        
        self.year_dropdown_box.config(
            font =("Calibri", 11), highlightthickness= 0, width = 13)

        ### Multi-Page Handling Section ###
        # Multi-page handling label.
        self.multi_page_lbl = Label(
            settings_frame, text = "Multi-Page Handling")
        
        self.multi_page_lbl.grid(
            row = 5, column = 0, padx = 10, sticky = S + W)
        
        self.multi_page_lbl.config(font=("Calibri", 13), bg = "white")

        # Multi-page handling radio buttons.
        # Initialise the multi-page handling variable on whether to
        # split multi-page pdfs or not.
        self.multi_page_mode = StringVar()
        self.multi_page_mode.set(current_user.multi_page_handling)

        # Split mode radio button to set multi-page handling to split
        # documents.
        self.split_mode_radio_bttn = Radiobutton(
            settings_frame,
            text = "Split Multi-Page\nDocuments",
            variable = self.multi_page_mode,
            value = "Split",
            bg = "White",
            font = ("Calibri", 11),
            highlightthickness = 0
            )
        
        self.split_mode_radio_bttn.grid(
            row = 6, column = 0, sticky = W, padx = 10, pady = 3)

        # Do not split mode radio button to set multi-page handling
        # not to split documents.
        self.do_not_split_mode_radio_bttn = Radiobutton(
            settings_frame,
            text = "Do Not Split",
            variable = self.multi_page_mode,
            value = "Do Not Split",
            bg = "White",
            font = ("Calibri", 11),
            highlightthickness = 0)
        
        self.do_not_split_mode_radio_bttn.grid(
            row = 6, column = 1, sticky = W, pady = 3)

        # Michelin button for performing the special michelin function
        # wherein paperwork processing is done based on using the
        # file name as a job reference without requiring user input
        # or document scanning.
        michelin_image_path = (filesystem.get_resources_directory()
            + "images\\michelin_logo.jpg")
        
        rendered_michelin_image = pil_image.open(michelin_image_path)
        rendered_michelin_image.thumbnail((25, 25), pil_image.ANTIALIAS)
        self.michelin_logo = PIL.ImageTk.PhotoImage(rendered_michelin_image)
        
        self.michelin_bttn = Button(
            settings_frame,
            image = self.michelin_logo,
            command = self.michelin_man)
        
        self.michelin_bttn.grid(row = 7, column = 1, sticky = E)

        # Settings button.
        self.settings_bttn = Button(
            settings_frame,
            text = "Settings",
            command = lambda: self.open_settings(current_user))

        self.settings_bttn.grid(row = 7, column = 2, sticky = E, padx = 3)
        self.settings_bttn.bind("<Return>", self.settings_enter_key)
        self.settings_bttn.bind("<KP_Enter>", self.settings_enter_key)
        self.settings_bttn.config(font=("Calibri", 11))

        # Exit button.
        self.exit_bttn = Button(
            settings_frame,
            text = "Exit",
            command = self.kill_program)
        
        self.exit_bttn.grid(row = 7, column = 3, columnspan = 2, sticky = W)
        self.exit_bttn.config(font=("Calibri", 11))
        self.exit_bttn.bind("<Return>", self.exit_enter_key)
        self.exit_bttn.bind("<KP_Enter>", self.exit_enter_key)

    def submit_enter_key(self, event = None):
        self.submit()

    def skip_enter_key(self, event = None):
        self.skip()

    def settings_enter_key(self, event = None):
        self.kill_program()

    def start_enter_key(self, event = None):
        self.start()

    def split_pdf_enter_key(self, event = None):
        self.split_current_doc()

    def exit_enter_key(self, event = None):
        self.kill_program()

    def start_browser(self):
        self.pdf_viewer = PDFViewer()

    def start(self):
        """ initialise looking for paperwork """
        if self.current_user.validate_directories_check(self) == True:
            scan_dir = self.current_user.scan_directory
            self.file_list = []
            self.file_index = 0

            # create a list of files in the scan folder that are either PDF, TIF, JPG, JPEG or PNG
            
            for file in os.listdir(scan_dir):
                if file.lower().endswith(".pdf") or file.lower().endswith(".tif") or file.lower().endswith(".tiff") or file.lower().endswith(".jpeg")or file.lower().endswith(".jpg") or file.lower().endswith(".png"):
                    self.file_list.append(file)
                    self.write_log("Adding " + file + " to list")

            if not self.file_list:
                PopupBox(self, "Failure", "No files found.", "200", "50")

            else:
                self.start_browser()
                self.get_file(self.file_index, self.file_list)
    
    def get_file(self, file_index, file_list):
        # directories
        scan_dir = self.current_user.scan_directory

        # user variables
        multi_page_handling = self.multi_page_mode.get()
        input_mode = self.current_input_mode.get()
        pw_type = self.pw_setting.get()
        autoprocessing = self.autoprocessing_mode.get()
        
        if not self.file_list:
            if self.file_index == 0:
                PopupBox(self, "Guess What", "No more files remaining.", "230", "75")
                self.pdf_viewer.close()
                
        else:
            self.file = self.file_list[self.file_index]

            pdf_file = pdfwriter.image_converter(
                self, self.file, scan_dir, multi_page_handling)
            
            split_file_list = pdfwriter.document_splitter(self, pdf_file, scan_dir, multi_page_handling)

            del self.file_list[self.file_index]
            for split_file in reversed(split_file_list):
                self.file_list.insert(self.file_index, split_file)

            self.file = self.file_list[self.file_index]
            file_name, file_ext = os.path.splitext(self.file)

            self.insert_file_attributes(file_name, file_ext)
            self.user_input_entry_box.focus_set()

            # Customer Paperwork/Loading List/Manual POD Processing Mode
            if pw_type == "Cust PW" or pw_type == "Loading List" or pw_type == "POD" and autoprocessing == "off":
                self.pdf_viewer.show_image(self, self.file, self.current_user.scan_directory)

            # POD Automatic Processing Mode
            elif pw_type == "POD" and autoprocessing == "on":
                pdfreader.barcode_scanner(
                    self, self.file_index, self.file_list)

    def submit(self, barcode = None, manual_submission = True):
        # user input variables
        input_mode = self.current_input_mode.get()
        pw_type = self.pw_setting.get()
        user_input = self.user_input_entry_box.get()
        auto_processing = self.autoprocessing_mode.get()

        # directory variables
        scan_dir = self.current_user.scan_directory
        dest_dir = self.current_user.dest_directory
        backup_dir = self.current_user.backup_directory

        # file variables
        file = self.file_list[self.file_index]
        file_name, file_extension = os.path.splitext(file)

        if pw_type == "Cust PW" or pw_type == "Loading List" or pw_type == "POD" and auto_processing == "off" or auto_processing == "on" and manual_submission == True:
            # check user has inputted correct amount of digits
            check = None
            check = userinputvalidation.check_user_input_length(
                self, user_input, input_mode)

            # if the check passes, start the renaming/move file method and get the next one
            if check == True:
                self.user_input_entry_box.delete(0, END)
                
                (full_job_ref, backup_file_name, dest_file_name,
                dest_duplicate_check) = userinputvalidation.rename_file(
                    self, user_input, input_mode, file_extension,
                    self.current_user)

                backup.backup_file(self, file, backup_file_name, scan_dir, backup_dir)
                
                if pw_type == "Cust PW":
                    pdfwriter.create_cust_pw(
                        self, file, scan_dir, dest_dir, 
                        full_job_ref, dest_file_name, dest_duplicate_check)

                elif pw_type == "Loading List" or pw_type == "POD":
                    pdfwriter.create_loading_list_pod(
                        self, file, scan_dir, dest_dir, dest_file_name,
                        dest_duplicate_check)
                    
                del self.file_list[self.file_index]

                pdfwriter.upload_doc(
                    self, file, scan_dir, dest_dir,
                    dest_file_name, dest_duplicate_check)

                self.get_file(self.file_index, self.file_list)

        # POD autoprocessing mode
        elif pw_type == "POD" and auto_processing == "on" and manual_submission == False:
                self.user_input_entry_box.delete(0, END)
                
                full_job_ref, backup_file_name, dest_file_name, dest_duplicate_check = userinputvalidation.rename_file(
                    self, barcode, input_mode, file_extension, self.current_user)

                backup.backup_file(self, file, backup_file_name, scan_dir, backup_dir)

                pdfwriter.create_loading_list_pod(
                    self, file, scan_dir, dest_dir,
                    dest_file_name, dest_duplicate_check)
                    
                del self.file_list[self.file_index]

                pdfwriter.upload_doc(
                    self, file, scan_dir, dest_dir,
                    dest_file_name, dest_duplicate_check)

                self.get_file(self.file_index, self.file_list)


    
    def michelin_man(self):
        """Autoprocesses all the files in the scan directory that are named as a GR number based on the paperwork type setting"""
        if self.current_user.validate_directories_check(self) == True:
            # user input variables
            pw_type = self.pw_setting.get()
            multi_page_handling = "Do Not Split"

            # directory variables
            scan_dir = self.current_user.scan_directory
            dest_dir = self.current_user.dest_directory
            backup_dir = self.current_user.backup_directory

            file_count = 0
            self.file_list = []

            for file in os.listdir(scan_dir):
                if file.lower().endswith(".pdf") or file.lower().endswith(".tif") or file.lower().endswith(".tiff") or file.lower().endswith(".jpeg") or file.lower().endswith(".jpg") or file.lower().endswith(".png"):
                    self.file_list.append(file)
                    self.write_log("Adding " + file + ".")

            # Converts all image files in the list into PDFs and
            # rebuilds a new list for later use.
            for file in self.file_list:
                self.file_index = self.file_list.index(file)
                
                pdf_file = pdfwriter.image_converter(
                    self, file, scan_dir, multi_page_handling)
                
                split_file_list = pdfwriter.document_splitter(self, pdf_file, scan_dir, "Do Not Split")

                for split_file in reversed(split_file_list):
                    self.file_list.insert(self.file_index, split_file) 

                self.file_list.remove(file)
                 
            # With all the TIF files converted, ready to start transforming files where the file name is a GR reference
            for file in self.file_list:
                if file.lower().endswith(".jpeg") or file.lower().endswith(".jpg") or file.lower().endswith(".png") or file.lower().endswith(".pdf") or file.lower().endswith(".tif") or file.lower().endswith(".tiff"):
                    file_name, file_extension = os.path.splitext(file)

                    job_ref = re.sub("[^0-9]", "", re.search("^[^_]*", file_name).group(0).upper())
                    self.write_log("\nJob reference is " + job_ref)
                    
                    if len(job_ref) == 9:
                        full_job_ref, backup_file_name, dest_file_name, dest_duplicate_check = userinputvalidation.rename_file(job_ref, "Normal", file_extension)

                        backup.backup_file(self, file, backup_file_name, scan_dir, backup_dir)
                        
                        if pw_type == "Cust PW":
                            pdfwriter.create_cust_pw(
                                self, file, scan_dir, dest_dir,
                                full_job_ref, dest_file_name, dest_duplicate_check)
                            
                        elif pw_type == "Loading List" or pw_type == "POD":
                            pdfwriter.create_loading_list_pod(
                                self, file, scan_dir, dest_dir,
                                dest_file_name, dest_duplicate_check)

                        pdfwriter.upload_doc(
                            self, file, scan_dir, dest_dir,
                            dest_file_name, dest_duplicate_check)
                        
                        self.write_log("Uploaded " + file + " as " + dest_file_name)
                        file_count += 1
                        self.user_input_entry_box.delete(0, END)
                        
                    else:
                        self.write_log("Ignoring" + file)
                        self.file_list.remove(file)

            PopupBox(self,
                "Michelin Man", str(file_count) + " files processed.",
                "215", "60")
            
    def skip(self):
        file_index = self.file_index
        file_list = self.file_list
        file = file_list[file_index]
        
        self.user_input_entry_box.delete(0, END)

        self.file_list.remove(self.file)
        self.write_log("Skipping " + self.file)
        
        self.get_file(file_index, file_list)
        
    def insert_file_attributes(self, file_name, file_ext):
        # make the name & ext text boxes writable
        self.file_name_txt.config(state = NORMAL)
        self.file_ext_txt.config(state = NORMAL)        

        # clear the current text and insert the file name and extension
        self.file_name_txt.delete(0.0, END)
        self.file_ext_txt.delete(0.0, END)
        self.file_name_txt.insert(0.0, file_name)
        self.file_ext_txt.insert(0.0, file_ext)

        # make the name and ext text boxes read only again
        self.file_name_txt.config(state = DISABLED)
        self.file_ext_txt.config(state = DISABLED)

    def write_log(self, text):
        """Inserts text into the box and removes an extra line if
        it is too full."""
        row = str(self.activity_log_row_count) + ".0"
        self.activity_log_textbox.config(state = NORMAL)
        self.activity_log_textbox.insert(row, text + "\n")
        self.activity_log_textbox.see("end")
        self.activity_log_row_count += 1

    def quick_mode_hint_message(self, event = None):
        """ Check the current input mode setting, and if switched on, provide a handy hint for what the template GR ref looks like """
        input_mode = self.current_input_mode.get()

        # if input mode is set to normal, set the hint box to be an empty string
        if input_mode == "Normal":
            self.quick_mode_notice_txt.config(font = ("Calibri", 11), bg = "White", highlightthickness = 0, borderwidth = 0, state = NORMAL)
            self.quick_mode_notice_txt.delete(0.0, END)
            self.quick_mode_notice_txt.config(font = ("Calibri", 11), bg = "White", highlightthickness = 0, borderwidth = 0, state = DISABLED)

        # if input mode is set to quick, get the year and month dropdown box variables and make a template ref.
        elif input_mode == "Quick":
            working_year = self.year_choice.get()
            year_prefix = re.sub("[^0-9]", "", str([year.short for year in YEARS if year.full == working_year]))

            working_month = self.month_choice.get()
            month_prefix = re.sub("[^0-9]", "", str([month.short for month in MONTHS if month.full == working_month]))

            template_ref = "GR" + year_prefix + month_prefix + "0"
            hint_message = "Current GR Number: " + template_ref

            # delete anything already in the hint box, and replace it with the new message
            self.quick_mode_notice_txt.config(font = ("Calibri", 11), bg = "White", highlightthickness = 0, borderwidth = 0, state = NORMAL)
            self.quick_mode_notice_txt.delete(0.0, END)
            self.quick_mode_notice_txt.insert(0.0, hint_message)
            self.quick_mode_notice_txt.config(font = ("Calibri", 11), bg = "White", highlightthickness = 0, borderwidth = 0, state = DISABLED)
            
    def open_settings(self, current_user):
        """Opens a settings window to act as a user interface for
        amending the user settings data file to change default
        directories and user options."""

        SettingsWindow(
            self, current_user, filesystem.get_user_settings_data())

    def refresh_settings(self, current_user):
        self.pw_setting.set(current_user.pw_type)
        self.current_input_mode.set(current_user.input_mode)
        self.multi_page_mode.set(current_user.multi_page_handling)
        self.autoprocessing_mode.set(current_user.autoprocessing)
        self.quick_mode_hint_message()

    def kill_program(self):
        try:
            self.pdf_viewer.close()
            exit()
        except:
            exit()

CURRENT_YEAR = Date(datetime.now().strftime('%Y'),
                    datetime.now().strftime('%y'))

LAST_YEAR = Date(str(int(datetime.now().strftime('%Y')) - 1),
                str(int(datetime.now().strftime('%y')) - 1))

CURRENT_MONTH = Date(datetime.now().strftime('%m') + " - " + datetime.now().strftime('%B'),
                     datetime.now().strftime('%m'))

JANUARY = Date("01 - January", "01")
FEBRUARY = Date("02 - February", "02")
MARCH = Date("03 - March", "03")
APRIL = Date("04 - April", "04")
MAY = Date("05 - May", "05")
JUNE = Date("06 - June", "06")
JULY = Date("07 - July", "07")
AUGUST = Date("08 - August", "08")
SEPTEMBER = Date("09 - September", "09")
OCTOBER = Date("10 - October", "10")
NOVEMBER = Date("11 - November", "11")
DECEMBER = Date("12 - December", "12")

MONTHS = (JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER)
YEARS = (CURRENT_YEAR, LAST_YEAR)

DEFAULT_PW_OPTIONS =("Cust PW", "Loading List", "POD")
DEFAULT_INPUT_OPTIONS = ("Normal", "Quick")
DEFAULT_MULTI_PAGE_OPTIONS = ("Split", "Do Not Split")

customer_pwork_flags_suffix = "++xShPaxIsVs0++OPSPWAT++Customer_Paperwork"
loading_list_flags_suffix = "++xShxPaxIsVs0++OPSLDLST++Loading_List"
POD_flags_suffix = "++xShxPaIsVs2++KPIPOD++Scanned_POD"

x_axis = str(int(GetSystemMetrics(0) / 4))
y_axis = str(int(GetSystemMetrics(1) / 4))

root = Tk()
root.title("GrayScan")
root.geometry("850x500+" + x_axis + "+" + y_axis)
root.grid_rowconfigure(0, weight = 1)
root.grid_columnconfigure(0, weight = 1)
root.configure(background = "white")

app = Application(root)

root.mainloop()