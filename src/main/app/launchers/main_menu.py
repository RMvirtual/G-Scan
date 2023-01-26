import sys
from src.main.app.controllers.main_menu import MainMenuController
from src.main.gui.app.app import GuiApplication


def main() -> None:
    application = GuiApplication()
    _main_menu = MainMenuController()

    application.run()


if __name__ == '__main__':
    main()
