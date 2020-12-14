import os

# A static module for performing file system functions such as
# retrieving commonly used directories etc.

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

def get_current_path():
    """Gets the full current working path the file using this
    method resides in."""

    return os.getcwd()

def get_directory_items(path):
    """Returns a list of folders and files in a directory."""
    return os.listdir(path)

def get_directory_path():
    """Gets the directory path of the G-Scan folder that all the files
    and subfolders reside in."""

    current_path = get_current_path()

    directory_structure = current_path.split("\\")
    directory_path = ""

    for folder in directory_structure:
        directory_path += folder + "\\"

        if folder == "G-Scan":
            break
    
    return directory_path

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

    return get_directory_path() + "data\\"

def get_user_settings_data_path():
    """Returns the user settings .dat file containing all the
    user settings regarding directories and workspace defaults."""

    return get_data_directory() + "user_settings"

def get_resources_directory():
    """Returns the path of the resources folder that resides in
    the src\main directory of the program directory."""

    return get_directory_path() + "src\\main\\resources\\"

def check_path_is_directory(path):
    """Returns a boolean value describing whether the path provided
    is a directory or not."""

    return os.path.isdir(path)

def check_path_exists(path):
    """Returns a boolean value describing whether the path provided
    exists or not."""

    return os.path.exists(path)