from src.main.gui.app.app import GuiApplication
from src.main.gui.main_menu.main_menu import MainMenu


def main():
    gui_app = GuiApplication()
    _main_menu = MainMenu()
    gui_app.run()


if __name__ == '__main__':
    main()
