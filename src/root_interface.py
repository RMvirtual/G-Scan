import abc
from configuration import Configuration


class RootInterface(abc.ABC):
    @abc.abstractmethod
    def exit(self) -> None:
        ...

    @abc.abstractmethod
    def launch_settings(self) -> None:
        ...

    @abc.abstractmethod
    def launch_image_viewer(self, config: Configuration) -> None:
        ...

    @abc.abstractmethod
    def launch_main_menu(self) -> None:
        ...
