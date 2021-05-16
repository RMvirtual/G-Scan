import re

def remove_alphabetical_characters(string_to_modify: str) -> str:
    reformatted_string = re.sub("[^0-9]", "", string_to_modify)

    return reformatted_string

