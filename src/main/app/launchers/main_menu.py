import wx
from src.main.app.controllers import MainMenuController


def main() -> None:
    application = wx.App()
    _main_menu = MainMenuController()

    application.MainLoop()


if __name__ == '__main__':
    main()
