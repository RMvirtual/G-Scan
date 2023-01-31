import os
import shelve
import src.main.file_system.runfiles
from src.main.file_system.directory_item import DirectoryItem


def app_data_directory():
    return os.environ["LOCALAPPDATA"] + "\\G-Scan"


def item_directory(path):
    directory, _ = os.path.split(path)

    return directory


def full_path(path):
    return os.path.abspath(path)


def delete_file(path):
    os.remove(path)


def directory_items(path):
    return os.listdir(path)


def base_name(path):
    return os.path.basename(path)


def file_name(path):
    return name_and_extension(path)[0]


def file_ext(path) -> str:
    return name_and_extension(path)[1]


def name_and_extension(path: str) -> tuple[str, str]:
    return os.path.splitext(base_name(path))[0:2]


def user_settings_data():
    return shelve.open(runfiles.user_settings_data_path())


def is_path_directory(path):
    return os.path.isdir(path)


def path_exists(path) -> bool:
    return os.path.exists(path)


def file_exists(name: str, directory_path) -> bool:
    return path_exists(directory_path + "\\" + name)


def matching_file_names(name: str, directory_path: str) -> int:
    return len([
        item for item in directory_items(directory_path) if name in item])
