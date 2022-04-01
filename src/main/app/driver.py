from src.main.gui.app.app import GuiApplication
from src.main.gui.main_menu.main_menu import MainMenu
from src.main.gui.settings.settings_menu import SettingsMenu


def main():
    gui_app = GuiApplication()
    _main_menu = MainMenu()
    _settings_menu = SettingsMenu()
    gui_app.run()


if __name__ == '__main__':
    main()
