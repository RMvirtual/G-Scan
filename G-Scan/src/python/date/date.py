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

    january = Date("01 - January", "01")
    february = Date("02 - February", "02")
    march = Date("03 - March", "03")
    april = Date("04 - April", "04")
    may = Date("05 - May", "05")
    june = Date("06 - June", "06")
    july = Date("07 - July", "07")
    august = Date("08 - August", "08")
    september = Date("09 - September", "09")
    october = Date("10 - October", "10")
    november = Date("11 - November", "11")
    december = Date("12 - December", "12")

    months = (
        january, february, march, april, may, june,
        july, august, september, october, november, december
    )

    return months

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

    current_year = Date(datetime.now().strftime('%Y'),
        datetime.now().strftime('%y'))

    last_year = Date(str(int(datetime.now().strftime('%Y')) - 1),
        str(int(datetime.now().strftime('%y')) - 1))

    years = (current_year, last_year)

    return years

def get_years_as_strings():
    """Returns a list of the months as strings."""

    years_as_strings = []
    years = get_years()

    for year in years:
        years_as_strings.append(year.get_full_code())

    return years_as_strings

def get_current_month():
    current_month = Date(
        datetime.now().strftime('%m') + " - " + datetime.now().strftime('%B'),
        datetime.now().strftime('%m'))
    
    return current_month

def get_current_year():
    current_year = Date(datetime.now().strftime('%Y'),
        datetime.now().strftime('%y'))

    return current_year

def get_last_year():
    last_year = Date(str(int(datetime.now().strftime('%Y')) - 1),
        str(int(datetime.now().strftime('%y')) - 1))

    return last_year