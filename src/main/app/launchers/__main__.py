import wx
from src.main.app.controllers import ApplicationController


def main() -> None:
    application = wx.App()
    controller = ApplicationController()
    controller.show_main_menu()

    application.MainLoop()


if __name__ == '__main__':
    main()
