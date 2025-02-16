import abc

from configuration import Configuration
from database import UserSettings

class ApplicationMediator(abc.ABC):
    @abc.abstractmethod
    def launch_settings(self) -> None:
        ...

    @abc.abstractmethod
    def launch_image_viewer(self, config: Configuration) -> None:
        ...

    @abc.abstractmethod
    def launch_main_menu(self) -> None:
        ...

    @abc.abstractmethod
    def update_user_settings(self, settings: UserSettings) -> None:
        ...

    @abc.abstractmethod
    def exit(self) -> None:
        ...
