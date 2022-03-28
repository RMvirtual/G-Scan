"""A module for calculating job references."""

import re
from src.main.date.date import Date

def gr_reference(full_job_no:str):
    return "GR" + __strip_alphabet(full_job_no)
    
def quick_gr_reference(brief_job_no:str, date:Date):
    full_job_no = job_number_from_brief(brief_job_no, date)

    return gr_reference(full_job_no)

def job_number_from_brief(brief_job_no:str, date:Date):
    clean_brief_job_no = __strip_alphabet(brief_job_no)

    template_job_no = template_job_number(
        date=date, digits_to_exclude=len(brief_job_no))
   
    return template_job_no + clean_brief_job_no

def template_job_number(date:Date, digits_to_exclude:int=0):
    year = date.get_year_as_two_digits()
    month = date.get_month_number_as_two_digits()
    zeroes_padding = (5 - digits_to_exclude)*"0"

    return year + month + zeroes_padding

def is_full_input_length(inputted_reference: str) -> tuple[bool, str]:
    is_nine_digits = len(inputted_reference) == 9
    message = "" if is_nine_digits else "Too many/few digits for a GR Number"

    return is_nine_digits, message

def is_quick_input_length(inputted_reference:str) -> tuple[bool, str]:
    """Checks if a string's length under quick mode conditions
    (i.e. the string is between 4 and 9 digits long).
    """
    input_length = len(inputted_reference)
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

def __strip_alphabet(string_to_modify:str) -> str:
    return re.sub("[^0-9]", "", string_to_modify)