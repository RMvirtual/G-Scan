import app.file_system as file_system
import os
import re
from gui.popupbox import PopupBox

"""Module for validating the users input within G-Scan."""

def check_user_input_length(user_input, input_mode):
    """Checks the length of the user's input (removing any alphabetic
    characters) to ensure it will create a valid job reference number
    depending on whether the program is in Normal or Quick Mode for
    inputting job numbers.
    
    Returns a tuple with Boolean value of whether the user input is
    the right length and an error message to be used."""

    user_input = re.sub("[^0-9]", "", user_input)
    user_input_length = len(user_input)    
    
    if input_mode == "Normal":
        if user_input_length == 9:
            return (True, "")

        else:
            return (False, "Too many/few digits for a GR number.")

    elif input_mode == "Quick":
        if user_input_length <= 9 and user_input_length >= 4:
            return (True, "")

        else:
            if user_input_length > 9:
                return (False, "Too many digits for a GR number.")

            elif user_input_length < 4:
                return (False, "Not enough digits for a GR number.")
        
def check_if_duplicate_file(file_name, directory_path):
    """Checks if a file already exists in a certain directory."""

    if file_system.check_path_exists(directory_path + "/" + file_name):
        return True
 
    return False

def calculate_base_job_reference(month, year):
    """Calculates a basic job reference based on the year and month
    and pads out the rest of the job reference with remaining zeroes
    (e.g. GR190800000).
    
    Takes Date objects as the year and month parameters so it can
    use their short attributes."""

    year_prefix = re.sub("[^0-9]", "", str(year.get_short_code()))
    month_prefix = re.sub("[^0-9]", "", str(month.get_short_code()))

    # Create the year + month job reference digits prefix,
    # add 5 zeroes to the template ref that will be overwritten
    # later.
    job_ref_prefix = year_prefix + month_prefix
    sacrificial_digits = str("00000")
    template_ref = job_ref_prefix + sacrificial_digits

def create_job_reference(master_application, user_input, input_mode):
    """Creates a full FCL format job reference based on the user's
    input and the inputting mode the program is currently running
    in."""

    user_input = re.sub("[^0-9]", "", user_input)

    # If user input mode is set to Quick, will restructure the job ref
    # to fill in the missing digits from the user input.
    if input_mode == "Quick":
        working_year = master_application.year_choice.get()
        working_month = master_application.month_choice.get()
        
        base_job_reference = calculate_base_job_reference(
            working_month, working_year)

        # Overwrites the base job reference from the right with
        # the digits the user has inputted.
        user_input_length = len(user_input)

        complete_job_reference = (
            base_job_reference[:-user_input_length] + user_input)

    else:
        complete_job_reference = "GR" + user_input
    
    return complete_job_reference

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

    is_file_name_duplicate = check_if_duplicate_file(
        file_name, backup_directory)
    
    page_counter = 1

    while is_file_name_duplicate:
        file_name = ("GR" + job_reference + "_" + paperwork_type + "_"
            + str(page_counter).zfill(3) + file_extension)
        
        is_file_name_duplicate = check_if_duplicate_file(
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