from abc import ABC, abstractmethod
import wx

from .app.configuration import ViewerConfiguration
from .gui.window import Window


class RootInterface(ABC):
    @property
    @abstractmethod
    def window(self) -> Window:
        ...

    @abstractmethod
    def exit(self) -> None:
        ...

    @abstractmethod
    def launch_settings(self) -> None:
        ...

    @abstractmethod
    def launch_image_viewer(self, config: ViewerConfiguration) -> None:
        ...

    @abstractmethod
    def launch_main_menu(self) -> None:
        ...
