"""A module for performing file system functions such as retrieving
commonly used directories etc.
"""

import os
import shelve
from pathlib import Path
from rules_python.python.runfiles import runfiles

class DirectoryItem():
    """A class for a directory item."""

    def __init__(self, path: str) -> None:
        self.__path = Path(path)
        self.__full_file_name =  self.__path.name
        self.__file_name, self.__file_extension = os.path.splitext(
            self.__full_file_name)

    def __str__(self):
        return str(self.__path)

    def get_file_name(self) -> str:
        return self.__file_name

    def get_file_extension(self) -> str:
        return self.__file_extension

    def get_full_file_name(self) -> str:
        return self.__full_file_name

    def get_full_path(self) -> str:
        return str(self.__path)

    def check_if_file_extension_matches(
            self, extension_to_check: str) -> bool:
        return (self.__file_extension.lower() == extension_to_check)

    def check_if_file_extension_matches_in_tuple(
            self, extensions_to_check: tuple) -> bool:
        return (self.__file_extension.lower() in extensions_to_check)

def is_file_single_page_image_format(file: DirectoryItem):
    image_file_extensions = (".jpeg", ".jpg", ".png")

    is_image_file = file.check_if_file_extension_matches_in_tuple(
        image_file_extensions)

    return is_image_file

def get_item_directory(path):
    directory, item = os.path.split(path)

    return directory

def get_full_path(path):
    return os.path.abspath(path)

def delete_file(path):
    os.remove(path)

def get_current_directory():
    return Path.cwd().resolve()

def get_directory_items(path):
    return os.listdir(path)

def get_root_directory():
    current_directory = get_current_directory()
    directory_path = ""

    for folder in current_directory.parts:
        if folder == "G-Scan":
            break
        
        directory_path += folder + "\\"
    
    if directory_path == "":
        return None

    return Path(directory_path + "G-Scan\\").resolve()

def get_base_name(path):
    """Returns the full file name (including the extension) of a
    file from a given path."""

    return os.path.basename(path) 

def get_file_name(path):
    base_name = get_base_name(path)
    file_name, file_ext = os.path.splitext(base_name)

    return file_name

def get_file_ext(path):
    base_name = get_base_name(path)
    file_name, file_ext = os.path.splitext(base_name)

    return file_ext

def get_data_directory():
    r = runfiles.Create()

    dataPath = r.Rlocation("data/user_settings.dat")

    return dataPath

def get_user_settings_data_path():
    r = runfiles.Create()

    dataPath = r.Rlocation("data/user_settings.dat")

    return dataPath

def get_user_settings_data():
    return shelve.open(get_user_settings_data_path())

def get_resources_directory():
    return get_root_directory().joinpath("resources")

def get_temp_directory():
    return get_root_directory().joinpath("temp")

def get_test_directory() -> Path:
    return get_root_directory().joinpath("test")
    
def check_path_is_directory(path):
    return os.path.isdir(path)

def check_path_exists(path) -> bool:
    return os.path.exists(path)

def check_if_file_exists(file_name, directory_path) -> bool:
    return check_path_exists(directory_path + "\\" + file_name)

def get_number_of_files_containing_substring(substring, directory_path) \
        -> int:   
    directory_items = get_directory_items(directory_path)
    count = 0

    for item in directory_items:
        if substring in item:
            count += 1

    return count