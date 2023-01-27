import wx
from src.main.app.controllers import ApplicationController


def main() -> None:
    application = wx.App()
    controller = ApplicationController()
    controller.launch_main_menu()
    # controller.launch_image_viewer()
    application.MainLoop()


if __name__ == '__main__':
    main()
