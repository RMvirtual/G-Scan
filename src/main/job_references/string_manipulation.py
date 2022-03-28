import re

def remove_alphabetical_characters(string_to_modify: str) -> str:
    """Creates a copy of a string with all alphabetical characters
    removed."""

    reformatted_string = re.sub("[^0-9]", "", string_to_modify)

    return reformatted_string

def overwrite_from_right(original_string: str, string_to_append: str):
    """Creates a new string with the original string overwritten from
    the right by the contents of a new string. For example, GR190100000
    overwritten by 1234 would return "GR190101234"."""

    digits_to_overwrite = len(string_to_append)
    truncated_original_string = original_string[:-digits_to_overwrite]

    new_string = truncated_original_string + string_to_append

    return new_string