from win32api import GetSystemMetrics
from tkinter import *
from tkinter import filedialog

class Popup_Box():
    """A class representing a pop up notification window."""

    def __init__(self, master_application, title, popup_text, length, height):
        self.master_application = master_application
        
        self.master_application.win = Toplevel()
        self.master_application.win.wm_title(title)

        x_axis = str(int(GetSystemMetrics(0) / 4))
        y_axis = str(int(GetSystemMetrics(1) / 4))

        master_application.win.geometry(
            length + "x" + height + "+" + x_axis + "+" + y_axis)

        label = Label(master_application.win, text = popup_text)
        label.grid(row = 0, column = 0)

        button = Button(
            master_application.win,
            text = "Okay",
            command = master_application.win.destroy)
        
        button.grid(row=1, column=0)
        button.focus_set()
        button.bind("<Return>", self.popup_close)
        button.bind("<KP_Enter>", self.popup_close)

    def popup_close(self, event = None):
        self.master_application.win.destroy()
