from datetime import datetime

class Date(object):
    """A class representing a year or month with short and
    full displays."""
    
    def __init__(self, full, short):
        self.full = full
        self.short = short

    def __str__(self):
        return str(self.full)

    def get_short_code(self):
        """Returns the short string representation of the date
        (e.g. 02 for "02 - February" or 19 for "2019")."""

        return self.short

    def get_full_code(self):
        """Returns the full string representation of the date
        (e.g. "02 - February" or "2019")."""

        return self.full

def get_months():
    """Returns a tuple of the months of the year."""

    JANUARY = Date("01 - January", "01")
    FEBRUARY = Date("02 - February", "02")
    MARCH = Date("03 - March", "03")
    APRIL = Date("04 - April", "04")
    MAY = Date("05 - May", "05")
    JUNE = Date("06 - June", "06")
    JULY = Date("07 - July", "07")
    AUGUST = Date("08 - August", "08")
    SEPTEMBER = Date("09 - September", "09")
    OCTOBER = Date("10 - October", "10")
    NOVEMBER = Date("11 - November", "11")
    DECEMBER = Date("12 - December", "12")

    MONTHS = (
        JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE,
        JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER
    )

    return MONTHS

def get_months_as_strings():
    """Returns a list of the months as strings."""

    months_as_strings = []
    months = get_months()

    for month in months:
        months_as_strings.append(month.get_full_code())

    return months_as_strings

def get_years():
    """Returns a tuple containing the last year and the
    current year."""

    CURRENT_YEAR = Date(datetime.now().strftime('%Y'),
        datetime.now().strftime('%y'))

    LAST_YEAR = Date(str(int(datetime.now().strftime('%Y')) - 1),
        str(int(datetime.now().strftime('%y')) - 1))

    YEARS = (CURRENT_YEAR, LAST_YEAR)

    return YEARS

def get_current_month():
    CURRENT_MONTH = Date(
        datetime.now().strftime('%m') + " - " + datetime.now().strftime('%B'),
        datetime.now().strftime('%m'))
    
    return CURRENT_MONTH

def get_current_year():
    CURRENT_YEAR = Date(datetime.now().strftime('%Y'),
        datetime.now().strftime('%y'))

    return CURRENT_YEAR

def get_last_year():
    LAST_YEAR = Date(str(int(datetime.now().strftime('%Y')) - 1),
        str(int(datetime.now().strftime('%y')) - 1))