import wx
from app.controllers.root import RootApplication


def main() -> None:
    application = wx.App()
    controller = RootApplication()
    controller.show()
    controller.launch_main_menu()
    application.MainLoop()


if __name__ == '__main__':
    main()
