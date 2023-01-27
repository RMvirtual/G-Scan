import wx
from src.main.app.controllers import ApplicationController


def main() -> None:
    application = wx.App()
    controller = ApplicationController()

    application.MainLoop()


if __name__ == '__main__':
    main()
