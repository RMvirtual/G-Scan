from abc import ABC, abstractmethod
import wx


class Display(ABC):
    @abstractmethod
    def frame(self) -> wx.Frame:
        ...

    @abstractmethod
    def close(self) -> None:
        ...

    @abstractmethod
    def hide(self) -> None:
        ...

    @abstractmethod
    def show(self) -> None:
        ...

    @abstractmethod
    def panel(self) -> wx.Panel:
        ...

    @abstractmethod
    def set_panel(self, panel: wx.Panel) -> None:
        ...

    @abstractmethod
    def set_menu_bar(self, menu_bar: wx.MenuBar) -> None:
        ...
