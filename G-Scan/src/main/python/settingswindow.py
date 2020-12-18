from tkinter import *
from tkinter import filedialog
from win32api import GetSystemMetrics

class SettingsWindow(Frame):
    """A class representing a Settings window to act as a
    user interface for amending the user settings data file."""
    
    def __init__(self, main_application, current_user, user_settings_data):
        """Constructor method."""
        self.root = Tk()
        self.root.grid()
        self.root.grid_rowconfigure(0, weight = 1)
        self.root.grid_columnconfigure(0, weight = 1)
        self.root.configure(background = "white")
        self.create_widgets(
            main_application, current_user, user_settings_data)

        x_axis = str(int(GetSystemMetrics(0) / 4))
        y_axis = str(int(GetSystemMetrics(1) / 4))

        self.root.geometry("820x220+" + x_axis + "+" + y_axis)
        self.root.title("User Settings: " + current_user.name)

    def create_widgets(self, main_application, current_user, user_settings_file):
        # frame for the settings widgets
        main_frame = Frame(self.root, width = 600, height = 250, borderwidth = 0, highlightthickness = 0, bg = "white")
        main_frame.grid(sticky = N + W)

        # username label
        user_lbl = Label(main_frame, text = "User:")
        user_lbl.config(font = ("Calibri", 11), bg = "white")
        user_lbl.grid(row = 0, column = 0, sticky = W)

        # username field
        user_txt = Text(main_frame, width = 30, height = 1, wrap = WORD)
        user_txt.config(font = ("Calibri", 11), bg = "light grey")
        user_txt.grid(row = 0, column = 1, columnspan = 5, sticky = W)
        user_txt.insert(0.0, current_user.name)

        # scan directory label
        scan_dir_lbl = Label(main_frame, text = "Scan Directory:")
        scan_dir_lbl.config(font = ("Calibri", 11), bg = "white")
        scan_dir_lbl.grid(row = 1, column = 0, sticky = W)

        # scan directory location entry field  
        self.scan_dir_ent = Entry(main_frame)
        self.scan_dir_ent.grid(row = 1, column = 1, columnspan = 5, sticky = W)
        self.scan_dir_ent.config(font = ("Calibri", 11), width = 91, bg = "light grey")
        self.scan_dir_ent.insert(0, current_user.scan_directory)

        # scan directory folder browser button
        scan_dir_bttn = Button(main_frame, text = "...", command = lambda: self.find_folder(self.scan_dir_ent))
        scan_dir_bttn.grid(row = 1, column = 5, sticky = E)

        # destination directory label
        dest_dir_lbl = Label(main_frame, text = "Destination Directory:")
        dest_dir_lbl.config(font = ("Calibri", 11), bg = "white")
        dest_dir_lbl.grid(row = 2, column = 0, sticky = W)

        # destination directory location entry field
        self.dest_dir_ent = Entry(main_frame)
        self.dest_dir_ent.config(font = ("Calibri", 11), width = 91, bg = "light grey")
        self.dest_dir_ent.grid(row = 2, column = 1, columnspan = 5, sticky = W)
        self.dest_dir_ent.insert(0, current_user.dest_directory)

        # destination directory folder browser button
        dest_dir_bttn = Button(main_frame, text = "...", command = lambda: self.find_folder(self.dest_dir_ent))
        dest_dir_bttn.grid(row = 2, column = 5, sticky = E)

        # backup directory label
        backup_dir_lbl = Label(main_frame, text = "Backup Directory:")
        backup_dir_lbl.config(font = ("Calibri", 11), bg = "white")
        backup_dir_lbl.grid(row = 3, column = 0, sticky = W)
        
        # backup directory entry field
        self.backup_dir_ent = Entry(main_frame)
        self.backup_dir_ent.config(font = ("Calibri", 11), width = 91, bg = "light grey")
        self.backup_dir_ent.grid(row = 3, column = 1, columnspan = 5, sticky = W)
        self.backup_dir_ent.insert(0, current_user.backup_directory)

        # backup directory folder browser button
        backup_dir_bttn = Button(main_frame, text = "...", command = lambda: self.find_folder(self.backup_dir_ent))
        backup_dir_bttn.grid(row = 3, column = 5, sticky = E)

        # default paperwork type label
        pw_type_lbl = Label(main_frame, text = "Default Paperwork Type:")
        pw_type_lbl.config(font = ("Calibri", 11), bg = "white")
        pw_type_lbl.grid(row = 4, column = 0, sticky = W)

        # default paperwork type dropdown box (what's in the boooooooooxxxxxx)
        self.default_pw_type = StringVar(main_frame)
        self.default_pw_type.set(current_user.pw_type)
        
        default_pw_options =("Cust PW", "Loading List", "POD")

        default_pw_menu = OptionMenu(main_frame,
                                self.default_pw_type,
                                *default_pw_options
                                )
        default_pw_menu.grid(row = 4, column = 1, sticky = NW)
        default_pw_menu.config(font =("Calibri", 11), highlightthickness= 0, width = 10)

        # default Multi-Page handling label
        multi_page_handling_lbl = Label(main_frame, text = "Default Multi-Page Handling:")
        multi_page_handling_lbl.config(font = ("Calibri", 11), bg = "white")
        multi_page_handling_lbl.grid(row = 4, column = 2, sticky = W)

        # default Multi-Page handling dropdown box (what's in the boooooooooxxxxxx)
        self.default_multi_page = StringVar(main_frame)
        self.default_multi_page.set(current_user.multi_page_handling)
        
        default_multi_page_options = ("Split", "Do Not Split")

        default_multi_page_menu = OptionMenu(main_frame,
                               self.default_multi_page,
                                *default_multi_page_options
                                )
        default_multi_page_menu.grid(row = 4, column = 3, sticky = NW)
        default_multi_page_menu.config(font =("Calibri", 11), highlightthickness= 0, width = 10)

        # default input mode label
        default_input_lbl = Label(main_frame, text = "Default Input Mode:")
        default_input_lbl.config(font = ("Calibri", 11), bg = "white")
        default_input_lbl.grid(row = 4, column = 4, sticky = W)

        # default input mode dropdown box (what's in the boooooooooxxxxxx)
        self.default_input_mode = StringVar(main_frame)
        self.default_input_mode.set(current_user.input_mode)
        
        default_input_options = ("Normal", "Quick")

        default_input_menu = OptionMenu(main_frame,
                                self.default_input_mode,
                                *default_input_options
                                )
        default_input_menu.grid(row = 4, column = 5, sticky = NW)
        default_input_menu.config(font =("Calibri", 11), highlightthickness= 0, width = 8)
       
        # Autoprocessing variable on PODs
        self.default_autoprocess = StringVar(main_frame)
        self.default_autoprocess.set(current_user.autoprocessing)

        # Autoprocessing checkbox
        Checkbutton(main_frame,
                    text = "POD Autoprocessing",
                    variable = self.default_autoprocess,
                    onvalue = "on",
                    offvalue = "off",
                    bg = "White",
                    font = ("Calibri", 8),
                    highlightthickness = 0
                    ).grid(row = 5, column = 1, columnspan = 3, sticky = W, padx = 0, pady = 3)
        
        # save button (saves the current settings)
        save_bttn = Button(main_frame, text = "Save", command = lambda: self.save_settings(main_application, current_user, user_settings_file))
        save_bttn.grid(row = 6, column=1, sticky = W, pady = 15)
        save_bttn.config(font=("Calibri", 11))

        # cancel button (exits the settings menu)
        cancel_bttn = Button(main_frame, text = "Cancel", command = self.root.destroy)
        cancel_bttn.grid(row = 6, column=1, sticky = E, padx = 15, pady = 15)
        cancel_bttn.config(font=("Calibri", 11))

    def save_settings(self, main_application, current_user, user_settings_file):
        current_user.pw_type = self.default_pw_type.get()
        current_user.multi_page_handling = self.default_multi_page.get()
        current_user.input_mode = self.default_input_mode.get()
        current_user.scan_directory = self.scan_dir_ent.get()
        current_user.dest_directory = self.dest_dir_ent.get()
        current_user.backup_directory = self.backup_dir_ent.get()
        current_user.autoprocessing = self.default_autoprocess.get()
        current_user.overwrite_user(current_user)
        main_application.gui.refresh_settings(current_user)
        self.root.destroy()

    def find_folder(self, directory):
        path = filedialog.askdirectory()
        directory.delete(0,END)
        directory.insert(0, path)
        self.root.lift()