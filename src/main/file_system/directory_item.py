import os
from pathlib import Path

class DirectoryItem():
    def __init__(self, path: str) -> None:
        self.__path = Path(path)
        self.__full_file_name =  self.__path.name
        self.__file_name, self.__file_extension = os.path.splitext(
            self.__full_file_name)

    def __str__(self):
        return str(self.__path)

    def file_name(self) -> str:
        return self.__file_name

    def file_extension(self) -> str:
        return self.__file_extension

    def full_file_name(self) -> str:
        return self.__full_file_name

    def full_path(self) -> str:
        return str(self.__path)

    def matches_file_extension(self, extension: str) -> bool:
        return self.__file_extension.lower() == extension.lower()

    def matches_multiple_file_extensions(self, extensions: tuple[str]) -> bool:
        return self.__file_extension.lower() in extensions

    def is_single_page_image_format(self):
        return self.matches_multiple_file_extensions((".jpeg", ".jpg", ".png"))

    def is_pdf(self):
        return self.matches_file_extension(".pdf")