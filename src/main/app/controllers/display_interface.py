from abc import ABC, abstractmethod
import wx


class Display(ABC):
    @property
    @abstractmethod
    def window(self) -> wx.Frame:
        ...


class DisplayController(ABC):
    @abstractmethod
    def close(self) -> None:
        ...

    @abstractmethod
    def hide(self) -> None:
        ...

    @abstractmethod
    def show(self) -> None:
        ...

    @property
    @abstractmethod
    def panel(self) -> wx.Panel:
        ...