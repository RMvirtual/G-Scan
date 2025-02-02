import wx

from configuration import Configuration
from controllers.document_editor.editor import DocumentEditorController
from controllers.main_menu import MainMenuController
from controllers.settings import SettingsController
from gui.window import Window
from root_interface import RootInterface


class RootApplication(RootInterface):
    def __init__(self, config: Configuration):
        display_width, display_height = wx.DisplaySize()
        size = (int(display_width/2), int(display_height/1.1))
        self.window = Window(size, position=wx.Point(size[0],0))
        self._config = config

    def launch_main_menu(self) -> None:
        MainMenuController(self, self._config, self.window)

    def launch_settings(self) -> None:
        SettingsController(self, self._config, self.window)

    def launch_image_viewer(self, config: Configuration) -> None:
        DocumentEditorController(self, config, self.window)

    def show(self) -> None:
        self.window.Show()

    def close(self, event: wx.Event = None) -> None:
        self.window.Close()

    def exit(self) -> None:
        self.close()
