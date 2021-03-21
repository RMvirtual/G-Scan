import sys
import threading

sys.path.append("C:\\Users\\rmvir\\Desktop\\gscan\\G-Scan\\src\\python")

import wx

from app.main_application import MainApplication
from gui.widgets.frame import Frame
from gui.mainmenu.panels.toppanel.top_panel import TopPanel
from threading import Lock, Thread, Semaphore

def should_create_frame():
    app = wx.App(False)
    frame = Frame(None, (80,70), "Test Frame")

    frame.Show()

    input("Press any key to exit.")

def should_create_frame_with_top_panel():
    app = wx.App(False)

    frame = Frame(None, (500,500), "Test Frame")
    panel = TopPanel(frame)

    frame.Show()

    input("Press any key to exit")

def should_create_frame_as_thread():
    main_application = MainApplication()

def print1(lock):
    lock.acquire()

    for i in range(100):
        print("print1: ", i)

    lock.release()

def print2(lock):
    lock.acquire()

    for i in range(100):
        print("print2: ", i)

    lock.release()

def lock_test():
    mutex = Lock()

    thread1 = Thread(target=print1, args=(mutex,))
    thread2 = Thread(target=print2, args=(mutex,))

    mutex.acquire()

    for i in range(100):
        print("main thread: ", i)

    mutex.release()

    thread1.start()
    thread2.start()

lock_test()