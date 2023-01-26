import wx
from src.main.gui.menu.main import MainMenu
from src.main.app.pdf_viewer.controller import ImageViewerController


class MainMenuController:
    def __init__(self):
        self._menu = MainMenu("G-Scan")
        self._initialise_callbacks()
        self._menu.Show()
        self._paperwork_viewer = ImageViewerController()

    def _initialise_callbacks(self) -> None:
        self._menu.departments.ops.Bind(wx.EVT_BUTTON, self._menu.view_ops)

        self._menu.operations.back.Bind(
            wx.EVT_BUTTON, self._menu.view_departments)

        self._menu.departments.exit.Bind(wx.EVT_BUTTON, self._exit_btn_press)

        self._menu.operations.cust_pwork.Bind(
            wx.EVT_BUTTON, self._paperwork_viewer)

    def _exit_btn_press(self, event = None) -> None:
        self._menu.Close()

    def _paperwork_viewer(self, event = None) -> None:
        self._paperwork_viewer.launch()
