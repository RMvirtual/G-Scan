"""A module for calculating job references."""

import operator
import re
from src.main.date.date import Date

def base_job_number(date:Date):
    """Calculates a basic job number based on the year and month
    in a date object and pads out the rest of the job reference with
    remaining zeroes (e.g. 190800000)."""

    year_prefix = date.get_year_as_two_digits()
    month_prefix = date.get_month_number_as_two_digits()

    base_job_number = year_prefix + month_prefix + "00000"

    return base_job_number

def job_reference(user_input):
    """Creates a full FCL format job reference."""

    user_input = __remove_alphabetical_characters(user_input)
    complete_job_reference = __prefix_gr_to_job_number(user_input)
    
    return complete_job_reference

def quick_job_reference(user_input:str, date:Date):
    """Creates an FCL format job reference using a Date object to fill
    in any gaps with the user's input."""

    formatted_user_input = __remove_alphabetical_characters(user_input)
    job_number = create_quick_job_number(formatted_user_input, date)
    complete_job_reference = __prefix_gr_to_job_number(job_number)

    return complete_job_reference

def create_quick_job_number(user_input:str, date:Date):
    """Creates an FCL format job number using a date object to fill in
    the year and month prefixes."""
    
    job_number = base_job_number(date)
    overwritten_job_number = __overwrite_from_right(job_number, user_input)
    complete_job_number = overwritten_job_number
    
    return complete_job_number

def __prefix_gr_to_job_number(job_number:str) -> str:
    """Takes a 9-digit job number and prefixes "GR" to it."""

    gr_number = "GR" + job_number

    return gr_number

def check_full_number_input_length(user_input: str) -> tuple[bool, str]:
    """Checks if a string's length under normal mode conditions (i.e.
    string is 9 digits long.)"""

    is_nine_chars_long = __is_equal_to(user_input, 9)
    message = ""

    if not is_nine_chars_long:
        message = "Too many/few digits for a GR number."

    return (is_nine_chars_long, message)

def check_quick_mode_input_length(user_input:str) -> tuple[bool, str]:
    """Checks if a string's length under quick mode conditions (i.e.
    the string is between 4 and 9 digits long)."""

    is_within_range = __is_between_range(user_input, 4, 9)
    message = ""

    if not is_within_range:
        is_greater_than_nine_chars = __is_greater_than(user_input, 9)
        is_less_than_four_chars = __is_less_than(user_input, 4)

        if is_greater_than_nine_chars:
            message = "Too many digits for a GR number."

        elif is_less_than_four_chars:
            message = "Not enough digits for a GR number."

    return (is_within_range, message)

def __remove_alphabetical_characters(string_to_modify:str) -> str:
    """Creates a copy of a string with all alphabetical characters
    removed."""

    reformatted_string = re.sub("[^0-9]", "", string_to_modify)

    return reformatted_string

def __overwrite_from_right(original_string:str, string_to_append:str) -> str:
    """Creates a new string with the original string overwritten from
    the right by the contents of a new string. For example, GR190100000
    overwritten by 1234 would return "GR190101234"."""

    digits_to_overwrite = len(string_to_append)
    truncated_original_string = original_string[:-digits_to_overwrite]

    new_string = truncated_original_string + string_to_append

    return new_string

def __get_comparison_operators() -> dict:
    """Gets a dictionary of comparison operators to use, accessible
    by string representation as a key."""

    comparison_operators = {
        ">": operator.gt,
        ">=": operator.ge,
        "<": operator.lt,
        "<=": operator.le,
        "=": operator.eq,
        "==": operator.eq,
        "!=": operator.ne
    }

    return comparison_operators

def __check_string_length_against_comparison_operator(string:str,
        comparison_operator:str, length_to_compare:int) -> bool:
    """Compares a string's length against a specific length amount and
    comparison operator in string format."""

    comparison_operators = __get_comparison_operators()
    operation = comparison_operators.get(comparison_operator)

    length = len(string)
    is_operation_true = operation(length, length_to_compare)

    return is_operation_true

def __is_equal_to(string:str, length_to_compare:int) -> bool:
    """Returns whether a string's length is equal to a specific
    amount."""

    is_equal = __check_string_length_against_comparison_operator(
        string, "==", length_to_compare)

    return is_equal

def __is_less_than(string:str, length_to_compare:int) -> bool:
    """Returns whether a string's length is less than a specific
    amount.""" 

    is_less_than = __check_string_length_against_comparison_operator(
        string, "<", length_to_compare)

    return is_less_than

def __is_less_than_equal_to(string:str, length_to_compare:int) -> bool:
    is_less_than_equal_to = __check_string_length_against_comparison_operator(
            string, "<=", length_to_compare)
    
    return is_less_than_equal_to

def __is_greater_than(string:str, length_to_compare:int) -> bool:

    is_greater_than = __check_string_length_against_comparison_operator(
        string, ">", length_to_compare)

    return is_greater_than

def __is_greater_than_equal_to(string:str, length_to_compare:int) -> bool:
    is_greater_than_equal_to = (
        __check_string_length_against_comparison_operator(
            string, ">=", length_to_compare)
    )

    return is_greater_than_equal_to

def __is_between_range(string:str, minimum_length:int, 
        maximimum_length:int) -> bool:
    is_within_minimum = __is_greater_than_equal_to(string, minimum_length)
    is_within_maximum = __is_less_than_equal_to(string, maximimum_length)

    is_within_range = is_within_minimum and is_within_maximum
    
    return is_within_range