from abc import ABC, abstractmethod
import wx


class Display(ABC):
    @abstractmethod
    def frame(self) -> wx.Frame:
        ...
