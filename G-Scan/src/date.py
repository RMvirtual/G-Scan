from datetime import datetime

class Date(object):
    """A class representing a year and month with short and
    full displays."""
    
    def __init__(self, month_number, month_name, year):
        self.__month_number = month_number
        self.__month_name = month_name
        self.__year = year

    def get_month_number(self) -> int:
        """Returns the month number."""

        return self.__month_number

    def get_month_number_as_two_digits(self) -> str:
        """Returns the month number as string formatted to two digits
        (e.g. month 1 will be outputted as 01)."""

        formatted_month_number = str(self.__month_number).zfill(2)

        return formatted_month_number

    def get_month_name(self) -> str:
        """Returns the month name."""

        return self.__month_name

    def get_year(self) -> int:
        """Returns the year."""

        return self.__year

    def get_year_as_two_digits(self) -> str:
        """Returns the year as a string formatted to two digits (e.g.
        2021 will be "21")."""

        formatted_year = str(self.__year)[-2:]

        return formatted_year

    def get_month_name_and_number_string(self) -> str:
        """Returns a string representation of the month name,
        a hyphen with a space either side and the month number
        formatted to two digits (e.g. "January - 01")."""

        month_name = self.get_month_name()
        month_number = self.get_month_number_as_two_digits()
        month_string = month_name + " - " + month_number

        return month_string

def get_months(year: int):
    """Returns a tuple of the months of the year."""

    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    months = []
    month_number = 1

    for month_name in month_names:
        new_month = Date(month_number, month_name, year)
        months.append(new_month)

        month_number += 1

    return months

def get_months_as_strings():
    """Returns a list of the months as strings."""

    months = get_months()
    months_as_strings = []

    for month in months:
        months_as_strings.append(month.get_full_code())

    return months_as_strings

def get_years() -> tuple:
    """Returns a tuple containing the last year and the
    current year."""

    current_year = get_current_year()
    last_year = get_last_year()

    return (current_year, last_year)

def get_years_as_strings() -> tuple:
    """Returns a tuple containing the last year and the current year
    in string format rather than integers."""

    years = get_years()
    formatted_years = []

    for year in years:
        formatted_year = str(year)
        formatted_years.append(formatted_year)

    return formatted_years

def get_current_month():
    month_number = get_current_month_number()
    month_name = get_current_month_name()
    year = get_current_year()

    current_month = Date(month_number, month_name, year)
    
    return current_month

def get_current_month_name():
    current_month_name = datetime.now().strftime('%B')

    return current_month_name

def get_current_month_number() -> int:
    current_month_number = int(datetime.now().strftime("%m"))

    return current_month_number

def get_current_year() -> int:
    current_year = int(datetime.now().strftime('%Y'))

    return current_year

def get_current_year_as_two_digits() -> int:
    current_year = int(datetime.now().strftime('%y'))
    
    return current_year

def get_last_year() -> int:
    last_year = int(datetime.now().strftime('%Y')) - 1

    return last_year

def get_last_year_as_two_digits() -> int:
    last_year = int(datetime.now().strftime('%y')) - 1
    
    return last_year

def get_month_names_and_numbers() -> list:
    """Returns a list of strings of each month represented with a 
    month name, a hyphen with a space either side and the month number
    formatted to two digits."""

    months = get_months(get_current_year())
    month_names_and_numbers = []

    for month in months:
        month_string = month.get_month_name_and_number_string()
        month_names_and_numbers.append(month_string)
    
    return month_names_and_numbers