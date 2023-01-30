import wx
from src.main.app.application.controller import ApplicationController


def main() -> None:
    application = wx.App()
    controller = ApplicationController()
    controller.show()
    controller.launch_main_menu()
    application.MainLoop()


if __name__ == '__main__':
    main()
