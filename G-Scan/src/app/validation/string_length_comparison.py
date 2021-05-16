import operator

"""A module for performing string comparison operations."""

def get_comparison_operators() -> dict:
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

def check_string_length_against_comparison_operator(string: str,
        comparison_operator: str, length_to_compare: int) -> bool:
    """Compares a string's length against a specific length amount and
    comparison operator in string format."""

    comparison_operators = get_comparison_operators()
    operation = comparison_operators.get(comparison_operator)

    length = len(string)
    is_operation_true = operation(length, length_to_compare)

    return is_operation_true

def is_equal_to(string: str, length_to_compare: int) -> bool:
    """Returns whether a string's length is equal to a specific
    amount."""

    is_equal = check_string_length_against_comparison_operator(
        string, "==", length_to_compare)

    return is_equal

def is_less_than(string: str, length_to_compare: int) -> bool:
    """Returns whether a string's length is less than a specific
    amount.""" 

    is_less_than = check_string_length_against_comparison_operator(
        string, "<", length_to_compare)

    return is_less_than

def is_less_than_equal_to(string: str,
        length_to_compare: int) -> bool:
    """Returns whether a string's length is less than or equal to a
    specific amount."""

    is_less_than_equal_to = check_string_length_against_comparison_operator(
            string, "<=", length_to_compare)
    
    return is_less_than_equal_to

def is_greater_than(string: str, length_to_compare: int) \
        -> bool:
    """Returns whether a string's length is greater than a specific
    amount."""

    is_greater_than = check_string_length_against_comparison_operator(
        string, ">", length_to_compare)

    return is_greater_than

def is_greater_than_equal_to(string: str,
        length_to_compare: int) -> bool:
    """Returns whether a string's length is greater than or equal to a
    specific amount."""

    is_greater_than_equal_to = (
        check_string_length_against_comparison_operator(
            string, ">=", length_to_compare)
    )

    return is_greater_than_equal_to

def is_between_range(string: str, minimum_length: int,
        maximimum_length: int) -> bool:
    """Returns whether a string's length is within a range."""

    is_within_minimum = is_greater_than_equal_to(string, minimum_length)
    is_within_maximum = is_less_than_equal_to(string, maximimum_length)

    is_within_range = is_within_minimum and is_within_maximum
    
    return is_within_range