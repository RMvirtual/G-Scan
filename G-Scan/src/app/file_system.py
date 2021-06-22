"""A module for performing file system functions such as retrieving
commonly used directories etc.
"""

import os
import shelve
from pathlib import Path

def get_item_directory(path):
    """Gets the directory of a path."""

    directory, item = os.path.split(path)

    return directory

def get_full_path(path):
    """Returns the absolute version of a path."""

    return os.path.abspath(path)

def delete_file(path):
    """Deletes a file in a path."""

    os.remove(path)

def get_current_directory():
    """Gets the full current working path the file using this
    method resides in."""

    return Path.cwd().resolve()

def get_directory_items(path):
    """Returns a list of folders and files in a directory."""

    return os.listdir(path)

def get_root_directory():
    """Gets the directory path of the G-Scan folder that all the files
    and subfolders reside in."""

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
    """Returns the name of a file (excluding the extension) of a
    file from a given path."""

    base_name = get_base_name(path)
    file_name, file_ext = os.path.splitext(base_name)

    return file_name

def get_file_ext(path):
    """Returns the name of a file (excluding the extension) of a
    file from a given path."""

    base_name = get_base_name(path)
    file_name, file_ext = os.path.splitext(base_name)

    return file_ext

def get_data_directory():
    """Returns the path of the data folder that resides in the
    main directory of the program. Contains things such as the
    user's settings etc."""

    return get_root_directory().joinpath("data")

def get_user_settings_data_path():
    """Returns the user settings .dat file containing all the
    user settings regarding directories and workspace defaults."""

    return get_data_directory().joinpath("user_settings")

def get_user_settings_data():
    """Returns an open shelf file of the user settings .data file
    containing all the user settings regarding directories and
    workspace defaults."""

    return shelve.open(get_user_settings_data_path())

def get_resources_directory():
    """Returns the path of the resources folder that resides in
    the src\main directory of the program directory."""

    return get_root_directory().joinpath("resources")

def get_temp_directory():
    """Returns the path of the temp directory that resides in the
    main directory. Used for file manipulation (pdf appending and
    copied etc)."""

    return get_root_directory().joinpath("temp")

def get_test_directory() -> Path:
    """Returns a Path object of the test directory."""

    return get_root_directory().joinpath("test")
    
def check_path_is_directory(path):
    """Returns a boolean value describing whether the path provided
    is a directory or not."""

    return os.path.isdir(path)

def check_path_exists(path) -> bool:
    """Returns a boolean value describing whether the path provided
    exists or not."""

    return os.path.exists(path)

def check_if_file_exists(file_name, directory_path) -> bool:
    """Checks if a file already exists in a certain directory."""

    return check_path_exists(directory_path + "\\" + file_name)

def get_number_of_files_containing_substring(substring, directory_path) \
        -> int:
    """Returns the number of files in a directory where the file name contains
    at least in part a matching substring."""
    
    directory_items = get_directory_items(directory_path)
    count = 0

    for item in directory_items:
        if substring in item:
            count += 1

    return count