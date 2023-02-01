from abc import ABC, abstractmethod
import wx
from src.main.app.configurations import ImageViewerConfiguration


class RootInterface(ABC):
    @abstractmethod
    def frame(self) -> wx.Frame:
        ...

    @abstractmethod
    def exit(self) -> None:
        ...

    @abstractmethod
    def launch_settings(self) -> None:
        ...

    @abstractmethod
    def launch_image_viewer(self, config: ImageViewerConfiguration) -> None:
        ...

    @abstractmethod
    def launch_main_menu(self) -> None:
        ...