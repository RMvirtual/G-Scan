from date import Date
import app.validation.string_manipulation as sm
import app.validation.string_length_comparison as slc

"""A module for calculating job references."""

def calculate_base_job_number(date: Date):
    """Calculates a basic job number based on the year and month
    in a date object and pads out the rest of the job reference with
    remaining zeroes (e.g. 190800000)."""

    year_prefix = date.get_year_as_two_digits()
    month_prefix = date.get_month_number_as_two_digits()

    base_job_number = year_prefix + month_prefix + "00000"

    return base_job_number

def create_job_reference(user_input):
    """Creates a full FCL format job reference."""

    user_input = sm.remove_alphabetical_characters(user_input)
    complete_job_reference = prefix_gr_to_job_number(user_input)
    
    return complete_job_reference

def create_quick_job_reference(user_input: str, date: Date):
    """Creates an FCL format job reference using a Date object to fill
    in any gaps with the user's input."""

    formatted_user_input = sm.remove_alphabetical_characters(user_input)
    job_number = create_quick_job_number(formatted_user_input, date)
    complete_job_reference = prefix_gr_to_job_number(job_number)

    return complete_job_reference

def create_quick_job_number(user_input: str, date: Date):
    """Creates an FCL format job number using a date object to fill in
    the year and month prefixes."""
    
    base_job_number = calculate_base_job_number(date)
    overwritten_job_number = sm.overwrite_from_right(base_job_number, user_input)
    complete_job_number = overwritten_job_number
    
    return complete_job_number

def prefix_gr_to_job_number(job_number: str) -> str:
    """Takes a 9-digit job number and prefixes "GR" to it."""

    gr_number = "GR" + job_number

    return gr_number

def check_full_number_input_length(user_input: str) -> tuple:
    """Checks if a string's length under normal mode conditions (i.e.
    string is 9 digits long.)"""

    is_nine_chars_long = slc.is_equal_to(user_input, 9)
    message = ""

    if not is_nine_chars_long:
        message = "Too many/few digits for a GR number."

    return (is_nine_chars_long, message)

def check_quick_mode_input_length(user_input: str) -> tuple:
    """Checks if a string's length under quick mode conditions (i.e.
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