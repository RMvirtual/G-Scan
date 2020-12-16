import os
import re
import userinputvalidation
from popupbox import PopupBox

"""Module for validating the users input within G-Scan."""

def check_user_input_length(master_application, user_input, input_mode):
    # Remove any alphabet characters in case Ops get carried away putting GR in front
    user_input = re.sub("[^0-9]", "", user_input)
    user_input_length = len(user_input)    
    
    if input_mode == "Normal":
        if user_input_length == 9:
            return True

        else:
            Popup_Box(
                master_application, "Numpty",
                "Too many/few digits for a GR number.", "215", "60")
            
            return False

    elif input_mode == "Quick":
        if user_input_length <= 9 and user_input_length >= 4:
            return True

        else:
            if user_input_length > 9:
                Popup_Box(
                    master_application, "Numpty",
                    "Too many digits for a GR number.", "215", "60")
            
            elif user_input_length < 4:
                Popup_Box(
                    master_application, "Numpty",
                    "Not enough digits for a GR number.", "215", "60")
        
            return False
        
def check_if_duplicate_file(file_name, directory_path):
    """Checks if a file already exists in a certain directory."""

    if os.path.exists(directory_path + "/" + file_name):
        return True
                        
    return False

def rename_file(user_input, input_mode, file_ext, user):
    job_ref = re.sub("[^0-9]", "", user_input)

    # If user input mode is set to Quick, will restructure the job ref
    # to fill in the missing digits from the user input.
    if input_mode == "Quick":
        working_year = self.year_choice.get()
        
        year_prefix = re.sub("[^0-9]", "", str(
            [year.short for year in YEARS if year.full == working_year]))

        working_month = self.month_choice.get()
        
        month_prefix = re.sub("[^0-9]", "", str(
            [month.short for month in MONTHS if month.full == working_month]))

        # Create the year + month job reference digits prefix,
        # add 5 zeroes to the template ref that will be overwritten
        # later.
        job_ref_prefix = year_prefix + month_prefix
        sacrificial_digits = str("00000")
        template_ref = job_ref_prefix + sacrificial_digits

        # Get the length of the job ref from the user input so we know
        # how many digits to knock off the template job reference.
        job_ref = template_ref[:-len(job_ref)] + job_ref

    paperwork_type = self.pw_setting.get()

    customer_pwork_flags_suffix = "++xShPaxIsVs0++OPSPWAT++Customer_Paperwork"
    loading_list_flags_suffix = "++xShxPaxIsVs0++OPSLDLST++Loading_List"
    POD_flags_suffix = "++xShxPaIsVs2++KPIPOD++Scanned_POD"

    if paperwork_type == "Cust PW":
        dest_flags_suffix = customer_pwork_flags_suffix

    elif paperwork_type == "Loading List":
        dest_flags_suffix = loading_list_flags_suffix

    elif paperwork_type == "POD":
        dest_flags_suffix = POD_flags_suffix

    backup_file_name = "GR" + job_ref + "_" + paperwork_type + file_ext

    backup_duplicate_check = userinputvalidation.check_if_duplicate_file(
        backup_file_name, user.backup_directory)

    if backup_duplicate_check == True:
        # If there is a duplicate named file in the backup directory,
        # append a paperwork counter to the backup filename, and loop
        # till there is no longer a duplicate file name
        pw_counter = 0
        
        while os.path.exists(user.backup_directory + "/" +  backup_file_name):
            if pw_counter == 0:
                pw_counter += 1
                backup_file_name = (
                    "GR" + job_ref + "_" + backup_suffix + "_" 
                    + str(pw_counter).zfill(3) + file_ext)
            else:
                pw_counter += 1
                backup_file_name = (
                    "GR" + job_ref + "_" + backup_suffix + "_"
                    + str(pw_counter).zfill(3) + file_ext)

    dest_file_name = "++GR" + job_ref + dest_flags_suffix + ".pdf"
    full_job_ref = "GR" + job_ref
    
    # Use the duplicate check method to append the correct page number
    # and not overwrite it in error.
    dest_duplicate_check = userinputvalidation.check_if_duplicate_file(
        dest_file_name, user.dest_directory)

    return full_job_ref, backup_file_name, dest_file_name, dest_duplicate_check

