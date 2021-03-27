import app.file_system
from datetime import datetime
import os
import shutil

def backup_file(file_name, backup_file_name, scan_dir, backup_dir):
    """Creates a backup copy of a file into a specified backup
    directory. Returns a Boolean value of whether the backup directory
    exists or not (could do with changing to copyfile success)."""

    backup_success = False

    try:
        backup_success = (
            __backup_file(file_name, backup_file_name, scan_dir, backup_dir))
    
    except Exception:
        backup_success = False

    return backup_success

def __backup_file(file_name, backup_file_name, scan_directory,
        backup_directory):
    """Private function for processing the backup file."""

    backup_success = False

    backup_directory_is_valid = (
        file_system.check_path_is_directory(backup_directory))

    if backup_directory_is_valid:
        backup_success = __copy_file(
            file_name, backup_file_name, scan_directory, backup_directory)

    return backup_success

def __append_file_to_path(file_name: str, directory_path: str):
    """Appends the file name to a directory path into one string."""

    full_path = directory_path + "/" + file_name

    return full_path

def __copy_file(file_name, backup_file_name, scan_directory,
        backup_directory):
    """Attempts to copy the file over."""

    copying_success = False

    try:
        scan_file_path = __append_file_to_path(file_name, scan_directory)
        backup_file_path = __append_file_to_path(
            backup_file_name, backup_directory)
        
        shutil.copyfile(scan_file_path, backup_file_path)

        copying_success = True

    except Exception:
        copying_success = False

    return copying_success

def start_housekeeping(backup_dir):
    """Checks the backup directory for any files over 30 days old and
    deletes them. I have removed this from being used in the code in
    case of issues arising from a user pointing their backup directory
    to the wrong folder, deleting potentially important files on a
    server directory."""

    backup_directory_exists = file_system.check_path_is_directory(backup_dir)

    if backup_directory_exists:
        __backup_housekeeping(backup_dir)

def __backup_housekeeping(backup_dir):
    """Does the backup housekeeping."""
    
    backup_folder = os.listdir(backup_dir)
    valid_extensions = (".pdf", ".tif", ".tiff", ".jpeg", ".jpg", ".png")

    for backup_file in backup_folder:
        backup_file_path = __append_file_to_path(backup_file, backup_dir)
        __housekeep_file(backup_file_path, valid_extensions)

def __housekeep_file(backup_file: str, valid_extensions):
    """Checks if a file in the backup folder is over 30 days old, and
    deletes it if so."""

    file_extension_valid = backup_file.lower().endswith(valid_extensions)
    file_over_thirty_days_old = __check_if_file_is_old(backup_file, 30)

    if file_extension_valid and file_over_thirty_days_old:
        os.remove(backup_file)

def __check_if_file_is_old(backup_file: str, maximum_age_in_days: int):
    """Checks whether a file is over a certain number of days old."""

    last_modified_time = __get_last_modified_date(backup_file)
    time_difference_in_days = __get_time_difference_in_days(
        last_modified_time)
    
    file_is_old = (time_difference_in_days > maximum_age_in_days)

    if file_is_old:
        return True

    return False

def __get_last_modified_date(backup_file: str):
    """Gets the last modified date from a file."""

    return datetime.fromtimestamp(os.path.getmtime(backup_file))

def __get_time_difference_in_days(last_modified_time):
    """Gets the time difference between the current time and a date in
    days."""

    current_time = datetime.now()
    time_difference_in_days = (current_time - last_modified_time).days

    return time_difference_in_days