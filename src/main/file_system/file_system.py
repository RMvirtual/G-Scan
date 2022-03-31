import os
import shelve
from rules_python.python.runfiles import runfiles
from src.main.file_system.directory_item import DirectoryItem


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
    file_name, _ = os.path.splitext(base_name(path))

    return file_name


def file_ext(path):
    _, file_ext = os.path.splitext(base_name(path))

    return file_ext


def test_resources_directory() -> str:
    r = runfiles.Create()

    return r.Rlocation("gscan/resources/test")


def image_resources_directory() -> str:
    r = runfiles.Create()

    return r.Rlocation("gscan/resources/images")


def data_directory() -> str:
    r = runfiles.Create()

    return r.Rlocation("data/user_settings.dat")


def user_settings_data_path() -> str:
    r = runfiles.Create()

    return r.Rlocation("data/user_settings.dat")


def temp_directory() -> str:
    r = runfiles.Create()

    return r.Rlocation("gscan/data/temp")


def user_settings_data():
    return shelve.open(user_settings_data_path())


def is_path_directory(path):
    return os.path.isdir(path)


def path_exists(path) -> bool:
    return os.path.exists(path)


def file_exists(file_name: str, directory_path) -> bool:
    return path_exists(directory_path + "\\" + file_name)


def matching_file_names(file_name: str, directory_path: str) -> int:
    count = 0

    for item in directory_items(directory_path):
        if file_name in item:
            count += 1

    return count
