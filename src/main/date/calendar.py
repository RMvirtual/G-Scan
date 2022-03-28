from datetime import datetime
from src.main.date.date import Date

def months(year: int) -> list[Date]:
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    dates = []
    month_number = 1

    for month_name in month_names:
        new_month = Date(month_number, month_name, year)
        dates.append(new_month)

        month_number += 1

    return dates

def month_name_from_number(month_number: int) -> str:
    months = {}
    month_names = months_as_strings()

    for month_number in range(1, 12):
        months[month_number] = month_names[month_number - 1]

    month_name = months[month_number]

    return month_name

def months_as_strings():
    return [month.month_name() for month in months(current_year())]

def years() -> tuple[int, int]:
    return (current_year(), last_year())

def years_as_strings() -> tuple:
    return [str(year) for year in years()]

def current_month():
    return Date(current_month_number(), current_month_name(), current_year())

def current_month_name():
    return datetime.now().strftime('%B')

def current_month_number() -> int:
    return int(datetime.now().strftime("%m"))

def current_year() -> int:
    return int(datetime.now().strftime('%Y'))

def current_year_as_two_digits() -> int:
    return int(datetime.now().strftime('%y'))

def last_year() -> int:
    return int(datetime.now().strftime('%Y')) - 1

def last_year_as_two_digits() -> int:
    return int(datetime.now().strftime('%y')) - 1

def month_names_and_numbers() -> list[str]:
    """Returns a list of strings of each month represented with a 
    month name, a hyphen with a space either side and the month number
    formatted to two digits.
    """
    return [
        month.month_name_hyphen_number() for month in months(current_year())]
    
def month_names_and_numbers_as_dictionary() -> dict:
    """Returns a dictionary of the month numbers as keys and their
    longform string representation of "month_name - month_number" as
    values.
    """
    months_dictionary = {}
    month_and_name_strings = month_names_and_numbers()
    month_number = 1

    for month_and_name in month_and_name_strings:
        months_dictionary[month_and_name] = month_number
        month_number += 1

    return months_dictionary

def date_from_month_name_number(month_name_and_number: str, year) -> Date:
    """Creates a Date object using the full "month_name - number"
    string representation and year to create it.
    """
    month_names_and_numbers = month_names_and_numbers_as_dictionary()
    
    month_number = month_names_and_numbers[month_name_and_number]
    month_name = month_name_from_number(month_number)

    return Date(month_number, month_name, year)