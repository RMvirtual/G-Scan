from abc import ABC, abstractmethod
from configuration import AppConfiguration


class RootInterface(ABC):
    @abstractmethod
    def exit(self) -> None:
        ...

    @abstractmethod
    def launch_settings(self) -> None:
        ...

    @abstractmethod
    def launch_image_viewer(self, config: AppConfiguration) -> None:
        ...

    @abstractmethod
    def launch_main_menu(self) -> None:
        ...
