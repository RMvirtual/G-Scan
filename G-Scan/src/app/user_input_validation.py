import app.file_system as file_system

import re
from gui.popupbox import PopupBox
import app.validation.string_formatting as string_format
import app.validation.string_length_comparison as slc
import user

"""Module for validating the users input within G-Scan."""

def check_user_input_length(user_input: str, input_mode: str) -> bool:
    """Checks the length of the user's input (removing any alphabetic
    characters) to ensure it will create a valid job reference number
    depending on whether the program is in Normal or Quick Mode for
    inputting job numbers.
    
    Returns a tuple with Boolean value of whether the user input is
    the right length and an error message to be used."""

    user_input = string_format.remove_alphabetical_characters(user_input)
    
    if input_mode == "Normal":
        return check_normal_mode_input_length(user_input)

    elif input_mode == "Quick":
        return check_quick_mode_input_length(user_input)

def check_normal_mode_input_length(user_input: str) -> tuple:
    """Checks the string's length under normal mode conditions (i.e.
    string is 9 digits long.)"""

    is_nine_chars_long = slc.is_equal_to(user_input, 9)
    message = ""

    if not is_nine_chars_long:
        message = "Too many/few digits for a GR number."

    return (is_nine_chars_long, message)

def check_quick_mode_input_length(user_input: str) -> tuple:
    """Checks the string's length under quick mode conditions (i.e.
    the string is between 4 and 9 digits long)."""

    is_within_range = slc.is_between_range(user_input, 4, 9)
    message = ""

    if not is_within_range:
        is_greater_than_nine_chars = slc.is_greater_than(user_input, 9)
        is_less_than_four_chars = slc.is_less_than(user_input, 4)

        if is_greater_than_nine_chars:
            message = "Too many digits for a GR number."

        elif is_less_than_four_chars:
            message = "Not enough digits for a GR number."

    return (is_within_range, message)

def create_backup_file_name(job_reference, paperwork_type, file_extension,
        backup_directory):
    """Creates the backup file name including the job reference,
    paperwork counter (if applicable), paperwork type and file
    extension.
    
    Checks if there is a duplicately named file already in the backup
    directory and loops through appending increasing page numbers
    to the file name till it is no longer duplicate."""

    file_name = (
        "GR" + job_reference + "_" + paperwork_type + file_extension)

    is_file_name_duplicate = file_system.check_if_file_exists(
        file_name, backup_directory)
    
    page_counter = 1

    while is_file_name_duplicate:
        file_name = ("GR" + job_reference + "_" + paperwork_type + "_"
            + str(page_counter).zfill(3) + file_extension)
        
        is_file_name_duplicate = file_system.check_if_file_exists(
            file_name, backup_directory)
        
        page_counter += 1
    
    return file_name

def create_destination_file_name(job_reference, paperwork_type,
        file_extension):
    """Creates the full file name of a file intended for the
    destination directory (i.e. FCL server directory to be
    uploaded)."""

    # Dictionary of file name flags that FCL uses to differentiate
    # between different paperwork types. 
    paperwork_type_flags = {
        "Cust PW": "++xShPaxIsVs0++OPSPWAT++Customer_Paperwork",
        "Loading List": "++xShxPaxIsVs0++OPSLDLST++Loading_List",
        "POD": "++xShxPaIsVs2++KPIPOD++Scanned_POD"}

    file_name = (
        "++" + job_reference + paperwork_type_flags[paperwork_type]
        + file_extension)

    return file_name

def create_file_names(job_reference, paperwork_type, input_mode,
        file_extension, backup_directory):
    """Creates the file names required for processing."""

    backup_file_name = create_backup_file_name(
        job_reference, paperwork_type,
        file_extension, backup_directory
    )

    dest_file_name = create_destination_file_name(
        job_reference, paperwork_type, ".pdf")

    return job_reference, backup_file_name, dest_file_name