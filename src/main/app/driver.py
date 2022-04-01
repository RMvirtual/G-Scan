from src.main.gui.app.app import GuiApplication
from src.main.gui.main_menu.main_menu import MainMenu
from src.main.gui.settings.settings_menu import SettingsMenu
from src.main.gui.image_viewer.viewer import ImageViewer


def main():
    gui_app = GuiApplication()
    # _main_menu = MainMenu()
    # _settings_menu = SettingsMenu()
    _image_viewer = ImageViewer((200, 200))
    _image_viewer.set_image(
        "C:/Users/rmvir/Desktop/gscan/resources/images/g-scan_logo.png")

    gui_app.run()


if __name__ == '__main__':
    main()
