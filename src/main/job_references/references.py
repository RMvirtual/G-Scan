"""A module for calculating job references."""

import re
from src.main.date.date import Date

def job_reference(user_input:str):
    """Creates a full FCL format job reference by extracting the full
    number from a string of characters.
    """    
    return "GR" + __remove_alphabetical_characters(user_input)
    
def quick_job_reference(user_input:str, date:Date):
    """Creates an FCL format job reference using a Date object to fill
    in any gaps with the user's input.
    """
    formatted_user_input = __remove_alphabetical_characters(user_input)
    job_number = quick_job_number(formatted_user_input, date)
    
    return "GR" + job_number

def quick_job_number(user_input:str, date:Date):
    """Creates an FCL format job number using a date object to fill in
    the year and month prefixes.
    """
    job_number = base_job_number(date)

    return __overwrite_from_right(job_number, user_input)

def base_job_number(date:Date):
    """Calculates a basic job number based on the year and month
    in a date object and pads out the rest of the job reference with
    remaining zeroes (e.g. 190800000).
    """
    year = date.get_year_as_two_digits()
    month = date.get_month_number_as_two_digits()

    return year + month + "00000"

def is_input_correct_full_length(user_input: str) -> tuple[bool, str]:
    """Checks if a string's length under normal mode conditions (i.e.
    string is 9 digits long.).
    """
    return (True, "") if len(user_input) == 9 else (
        False, "Too many/few digits for a GR Number")

def is_input_correct_short_length(user_input:str) -> tuple[bool, str]:
    """Checks if a string's length under quick mode conditions
    (i.e. the string is between 4 and 9 digits long).
    """
    input_length = len(user_input)
    within_range = 4 <= input_length <= 9
    message = ""

    if not within_range:
        is_greater_than_nine_chars = input_length > 9
        is_less_than_four_chars = input_length < 4

        if is_greater_than_nine_chars:
            message = "Too many digits for a GR number."

        elif is_less_than_four_chars:
            message = "Not enough digits for a GR number."

    return (within_range, message)

def __remove_alphabetical_characters(string_to_modify:str) -> str:
    return re.sub("[^0-9]", "", string_to_modify)

def __overwrite_from_right(original_string:str, new_characters:str) -> str:
    """Creates a new string with the original string overwritten from
    the right by the contents of a new string. For example, GR190100000
    overwritten by 1234 would return "GR190101234".
    """
    digits_to_overwrite = len(new_characters)
    truncated_original_string = original_string[:-digits_to_overwrite]

    return truncated_original_string + new_characters