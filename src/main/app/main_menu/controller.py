from src.main.gui.menu.main import MainMenu


class MainMenuController:
    def __init__(self):
        self._menu = MainMenu("G-Scan")
        self._menu.Show()
