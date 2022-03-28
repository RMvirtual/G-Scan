import os
import shelve
from pathlib import Path
from rules_python.python.runfiles import runfiles
from src.main.file_system.directory_item import DirectoryItem

def is_file_single_page_image_format(file: DirectoryItem):
    return file.matches_multiple_file_extensions((".jpeg", ".jpg", ".png"))

def item_directory(path):
    directory, _ = os.path.split(path)

    return directory

def full_path(path):
    return os.path.abspath(path)

def delete_file(path):
    os.remove(path)

def current_directory():
    return Path.cwd().resolve()

def directory_items(path):
    return os.listdir(path)

def root_directory():
    directory_path = ""

    for folder in current_directory().parts:
        if folder == "G-Scan":
            break
        
        directory_path += folder + "\\"
    
    if directory_path == "":
        return None

    return Path(directory_path + "G-Scan\\").resolve()

def base_name(path):
    """Returns the full file name (including the extension) of a
    file from a given path."""

    return os.path.basename(path) 

def file_name(path):
    file_name, _ = os.path.splitext(base_name(path))

    return file_name

def file_ext(path):
    _, file_ext = os.path.splitext(base_name(path))

    return file_ext

def data_directory():
    r = runfiles.Create()

    return r.Rlocation("data/user_settings.dat")

def user_settings_data_path():
    r = runfiles.Create()

    return r.Rlocation("data/user_settings.dat")

def user_settings_data():
    return shelve.open(user_settings_data_path())

def resources_directory():
    return root_directory().joinpath("resources")

def temp_directory():
    return root_directory().joinpath("temp")

def test_directory() -> Path:
    return root_directory().joinpath("test")
    
def is_path_directory(path):
    return os.path.isdir(path)

def path_exists(path) -> bool:
    return os.path.exists(path)

def file_exists(file_name, directory_path) -> bool:
    return path_exists(directory_path + "\\" + file_name)

def number_of_files_containing_substring(substring, directory_path) -> int:
    count = 0

    for item in directory_items(directory_path):
        if substring in item:
            count += 1

    return count