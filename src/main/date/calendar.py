from datetime import datetime
from src.main.date.date import Date

def months(year: int) -> list[Date]:
    names_and_numbers = {
        1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
        6: "June", 7: "July", 8: "August", 9: "September", 10: "October",
        11: "November", 12: "December"
    }
    
    return [
        Date(number, name, year) for number, name in names_and_numbers.items()]

def month_name_from_number(number: int) -> str:
    return months_as_strings()[number - 1]

def months_as_strings():
    return [month.month_name() for month in months(current_year())]

def years() -> tuple[int, int]:
    return (current_year(), last_year())

def years_as_strings() -> tuple:
    return [str(year) for year in years()]

def current_month():
    return Date(current_month_number(), current_month_name(), current_year())

def current_month_name() -> str:
    return __current_time_as_string("%B")

def current_month_number() -> int:
    return __current_time_as_int("%m")

def current_year() -> int:
    return __current_time_as_int("%Y")

def current_year_as_two_digits() -> int:
    return __current_time_as_int("%y")

def last_year() -> int:
    return __current_time_as_int("%Y") - 1

def last_year_as_two_digits() -> int:
    return __current_time_as_int("%y") - 1

def __current_time_as_string(format:str) -> str:
    return datetime.now().strftime(format)

def __current_time_as_int(format:str) -> int:
    return int(__current_time_as_string(format))

def month_names_and_numbers() -> list[str]:
    return [
        month.month_name_hyphen_number() for month in months(current_year())]
    
def months_as_xxx_mm_to_number() -> dict:
    months_dictionary = {}
    month_and_name_strings = month_names_and_numbers()
    month_number = 1

    for month_and_name in month_and_name_strings:
        months_dictionary[month_and_name] = month_number
        month_number += 1

    return months_dictionary

def date(month:int, year:int) -> Date:
    return months(year)[month-1]

def date_from_month_name_and_number(month_name_and_number: str, year) -> Date:
    month_names_and_numbers = months_as_xxx_mm_to_number()
    
    month_number = month_names_and_numbers[month_name_and_number]
    month_name = month_name_from_number(month_number)

    return Date(month_number, month_name, year)