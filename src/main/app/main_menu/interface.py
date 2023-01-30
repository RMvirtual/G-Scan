from abc import ABC, abstractmethod


class RootMenu(ABC):
    @abstractmethod
    def exit(self) -> None:
        ...

    @abstractmethod
    def launch_settings(self) -> None:
        ...

    @abstractmethod
    def launch_image_viewer(self) -> None:
        ...

    @abstractmethod
    def launch_main_menu(self) -> None:
        ...
