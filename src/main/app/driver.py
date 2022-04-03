from src.main.gui.app.app import GuiApplication
from src.main.gui.main_menu.main_menu import MainMenu
from src.main.gui.settings.settings_menu import SettingsMenu
from src.main.gui.image_viewer.viewer import ImageViewer
from src.main.pdf.reader import PdfReader

def main():
    gui_app = GuiApplication()
    # _main_menu = MainMenu()
    # _settings_menu = SettingsMenu()
    _image_viewer = ImageViewer((1000, 1000))

    pdf = (
        "C:/Users/rmvir/Desktop/gscan/resources/test/correct_files/one_page"
        ".pdf "
    )

    reader = PdfReader(pdf)
    _image_viewer.set_pixelmap(reader.page(0))

    gui_app.run()


if __name__ == '__main__':
    main()
