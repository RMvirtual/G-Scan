import os
import filesystem
import backup
import userinputvalidation
import pdfreader
import pdfwriter
from settingswindow import SettingsWindow
from pdfviewer import PDFViewer
from user import User
import date
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

class GUI(Frame):
    """GUI Box for inputting a GR Number when viewing a page of paperwork"""

    def __init__(self, master, main_application):
        """ Initialise the frame, whatever that means."""

        super(GUI, self).__init__(master)
        self.main_application = main_application
        self.grid()
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.temp_dir = filesystem.get_temp_directory()
        self.create_widgets()
        self.activity_log_row_count = 1

    def create_widgets(self):
        """Creates all the widgets required for the main GUI window."""

        # Left master frame to contain the logo frame and the
        # file processing frame.
        left_master_frame = Frame(
            self, width = 390, height = 255,
            borderwidth = 0, highlightthickness = 0, bg = "white")

        left_master_frame.grid(row = 1, column = 0)
        left_master_frame.grid_rowconfigure(0, weight = 1)
        left_master_frame.grid_columnconfigure(0, weight = 1)

        self.create_left_master_frame_widgets(left_master_frame)

        # Right master frame.
        right_master_frame = Frame(
            self, width = 390, height = 255,
            borderwidth = 0, highlightthickness = 0, bg = "white")
        
        right_master_frame.grid(row = 1, column = 1, sticky = "nsew")
        right_master_frame.grid_rowconfigure(0, weight = 1)
        right_master_frame.grid_columnconfigure(0, weight = 1)
        
        self.create_right_master_frame_widgets(
            right_master_frame)

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

        self.create_bottom_widgets(activity_log_frame)

        for i in range(1,10):
            self.columnconfigure(i, weight = 1)

        for i in range(1,10):
            self.rowconfigure(1, weight = 1)

    def create_left_master_frame_widgets(self, left_master_frame):
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

        self.create_file_frame_widgets(self.file_frame)        

    def create_right_master_frame_widgets(self, right_master_frame):
        """Creates the right master frame's widgets."""

        # Frame for the settings panel inside the right master frame.
        settings_frame = Frame(
            right_master_frame, 
            bg = "white", highlightthickness=0, bd = 0)

        settings_frame.grid(row = 0, column = 0, sticky = S)
        settings_frame.grid_rowconfigure(0, weight = 1)
        settings_frame.grid_columnconfigure(0, weight = 1)

        self.create_settings_frame_widgets(settings_frame)

    def create_file_frame_widgets(self, file_frame):
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

        self.file_name_txt.config(
            font = ("Calibri", 16), bg = "light grey", state = DISABLED)

        # File extension label.
        self.file_ext_lbl = Label(file_frame, text = "File Type:\t")
        self.file_ext_lbl.grid(row = 1, column = 0, sticky = W, padx = 5)
        self.file_ext_lbl.config(font=("Calibri", 11), bg = "white")

        # File extension text field to display the file extension.
        self.file_ext_txt = Text(
            file_frame, width = 42, height = 1, wrap = WORD)
        
        self.file_ext_txt.grid(
            row = 1, column = 1, columnspan = 4, sticky = W)
        
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

    def create_bottom_widgets(self, file_frame):
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
            file_frame,
            image = self.michelin_logo,
            command = self.michelin_man)
        
        self.michelin_bttn.grid(row = 7, column = 1, sticky = E)

        # Settings button.
        self.settings_bttn = Button(
            file_frame,
            text = "Settings",
            command = lambda: self.open_settings(current_user))

        self.settings_bttn.grid(row = 7, column = 2, sticky = E, padx = 3)
        self.settings_bttn.bind("<Return>", self.settings_enter_key)
        self.settings_bttn.bind("<KP_Enter>", self.settings_enter_key)
        self.settings_bttn.config(font=("Calibri", 11))

        # Exit button.
        self.exit_bttn = Button(
            file_frame,
            text = "Exit",
            command = self.kill_program)
        
        self.exit_bttn.grid(row = 7, column = 3, columnspan = 2, sticky = W)
        self.exit_bttn.config(font=("Calibri", 11))
        self.exit_bttn.bind("<Return>", self.exit_enter_key)
        self.exit_bttn.bind("<KP_Enter>", self.exit_enter_key)

    def create_settings_frame_widgets(self, settings_frame):
        # Paperwork type heading for the radio dial to determine
        # the type of paperwork being processed.
        current_user = self.main_application.get_current_user()

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
            command = self.main_application.calculate_quick_mode_hint_message)
            
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
            command = self.main_application.calculate_quick_mode_hint_message)
        
        self.quick_mode_radio_bttn.grid(
            row = 3, column = 1, rowspan = 2, pady = 5, sticky = NW)

        # Dropdown box for selecting the month that quick mode uses.
        self.month_choice = StringVar(settings_frame)
        self.month_choice.set(date.get_current_month())
        
        self.month_dropdown_box = OptionMenu(
            settings_frame,
            self.month_choice,
            *date.get_months(),
            command = self.main_application.calculate_quick_mode_hint_message)

        self.month_dropdown_box.grid(
            row = 3, column = 2, columnspan = 2, padx = 10, sticky = NW)
        
        self.month_dropdown_box.config(
            font =("Calibri", 11), highlightthickness= 0, width = 13)
        
        # Dropdown box for selecting the year that quick mode uses.
        self.year_choice = StringVar(settings_frame)
        self.year_choice.set(date.get_current_year())

        self.year_dropdown_box = OptionMenu(
            settings_frame,
            self.year_choice,
            date.get_last_year(),
            date.get_current_year(),
            command = self.main_application.calculate_quick_mode_hint_message)
        
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

    def start(self):
        """Start the main application's workflow for processing
        paperwork based on the user's selected settings."""
        
        self.main_application.start()

    def get_current_input_mode(self):
        """Gets a string of the current input mode as set by the
        radio buttons for input mode (e.g. Quick or Normal)."""

        return self.current_input_mode.get()

    def get_current_paperwork_type(self):
        """Gets a string representing the current selection for
        paperwork type on the radio buttons for paperwork type
        (e.g. Cust PW, Loading List or POD)."""

        return self.pw_setting.get()
    
    def get_user_input(self):
        """Gets a string of the contents the user has entered
        into the user input box."""

        return self.user_input_entry_box.get()

    def get_autoprocessing_mode(self):
        """Gets a string representing whether autoprocessing mode
        is "on" or "off"."""

        return self.autoprocessing_mode.get()
    
    def get_multi_page_mode(self):
        """Gets a string representing whether multi-page handling
        is set to "Split" or "Do Not Split"."""

        return self.multi_page_mode.get()

    def get_current_year_choice(self):
        """Gets a string representing the value of the selection
        from the Year dropdown menu."""

        return self.year_choice.get()

    def get_current_month_choice(self):
        """Gets a string representing the value of the selection
        from the Month dropdown menu."""

        return self.month_choice.get()

    def move_cursor_to_user_input_box(self):
        """Focuses the cursor position in the GUI from the last thing
        it clicked back to the user input box for the user to start
        typing again."""

        self.user_input_entry_box.focus_set()

    def clear_user_input(self):
        """Clears the text in the user input box, making it appear
        as though it has been accepted."""

        self.user_input_entry_box.delete(0, END)

    def set_file_name(self, file_name):
        """Sets the file name text box value of the GUI."""

        self.file_name_txt.config(state = NORMAL)
        self.file_name_txt.delete(0.0, END)
        self.file_name_txt.insert(0.0, file_name)
        self.file_name_txt.config(state = DISABLED)

    def set_file_extension(self, file_extension):
        """Sets the file extension text box value of the GUI."""

        self.file_ext_txt.config(state = NORMAL)
        self.file_ext_txt.delete(0.0, END)
        self.file_ext_txt.insert(0.0, file_extension)
        self.file_ext_txt.config(state = DISABLED)

    def submit(self, barcode = None, manual_submission = True):
        self.main_application.submit(barcode, manual_submission)

    def michelin_man(self):
        """Autoprocesses all the files in the scan directory that are
        named as a GR number based on the paperwork type setting."""

        self.main_application.michelin_man()
            
    def skip(self):
        self.main_application.skip()
        
    def write_log(self, text):
        """Inserts text into the box and removes an extra line if
        it is too full."""
        row = str(self.activity_log_row_count) + ".0"
        self.activity_log_textbox.config(state = NORMAL)
        self.activity_log_textbox.insert(row, text + "\n")
        self.activity_log_textbox.see("end")
        self.activity_log_row_count += 1

    def set_quick_mode_hint_text(self, event = None):
        """Overwrites the text found in the quick mode hint text
        box."""
        
        self.quick_mode_notice_txt.config(state = NORMAL)
        self.quick_mode_notice_txt.delete(0.0, END)
        self.quick_mode_notice_txt.insert(0.0, END)
        self.quick_mode_notice_txt.config(state = DISABLED)

    def open_settings(self, current_user):
        """Opens a settings window to act as a user interface for
        amending the user settings data file to change default
        directories and user options."""

        SettingsWindow(
            self, current_user, filesystem.get_user_settings_data())

    def refresh_settings(self):
        current_user = self.main_application.get_current_user()

        self.pw_setting.set(current_user.pw_type)
        self.current_input_mode.set(current_user.input_mode)
        self.multi_page_mode.set(current_user.multi_page_handling)
        self.autoprocessing_mode.set(current_user.autoprocessing)
        self.quick_mode_hint_message()
        self.main_application.validate_user_directories()

    def kill_program(self):
        try:
            self.pdf_viewer.close()
            exit()

        except:
            exit()
