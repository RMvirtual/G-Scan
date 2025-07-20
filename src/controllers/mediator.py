import abc

from configuration import Configuration
from database import UserSettings


class ApplicationMediator(abc.ABC):
    @abc.abstractmethod
    def launch_editor(self, config: Configuration) -> None: ...

    @abc.abstractmethod
    def update_user_settings(self, settings: UserSettings) -> None: ...

    @abc.abstractmethod
    def exit(self) -> None: ...
