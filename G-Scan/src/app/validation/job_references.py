import date
import re
import app.validation.string_formatting as string_format

"""A module for calculating job references."""

def calculate_base_job_reference(date: date.Date):
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

    user_input = string_format.remove_alphabetical_characters(user_input)

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