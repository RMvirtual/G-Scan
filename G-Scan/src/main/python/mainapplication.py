"""A module for the main application class."""

from datetime import datetime
from date import Date
from win32api import GetSystemMetrics
from tkinter import *
from tkinter import filedialog
from gui import GUI

class MainApplication():
    """A class for the main application of the program to run."""

    def __init__(self):
        x_axis = str(int(GetSystemMetrics(0) / 4))
        y_axis = str(int(GetSystemMetrics(1) / 4))

        root = Tk()
        root.title("GrayScan")
        root.geometry("850x500+" + x_axis + "+" + y_axis)
        root.grid_rowconfigure(0, weight = 1)
        root.grid_columnconfigure(0, weight = 1)
        root.configure(background = "white")

        gui = GUI(root)

        root.mainloop()