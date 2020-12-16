from datetime import datetime
from date import Date
from win32api import GetSystemMetrics
from tkinter import *
from tkinter import filedialog
from gui import Application

def main():
    #DEFAULT_PW_OPTIONS =("Cust PW", "Loading List", "POD")
    #DEFAULT_INPUT_OPTIONS = ("Normal", "Quick")
    #DEFAULT_MULTI_PAGE_OPTIONS = ("Split", "Do Not Split")

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

main()