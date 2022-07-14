import unittest
import sys

print(sys.path)


class TestDate(unittest.TestCase):
    """A class for testing the date module."""

    CORRECT_MONTH_NAMES = (
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    )

    CORRECT_MONTH_NAME_AND_NUMBERS = (
        "January - 01", "February - 02", "March - 03",
        "April - 04", "May - 05", "June - 06",
        "July - 07", "August - 08", "September - 09",
        "October - 10", "November - 11", "December - 12"
    )

    def test_should_get_month_names(self):
        for month in calendar.months(2021):
            self.assertTrue(month.month_name() in self.CORRECT_MONTH_NAMES)

    def test_should_get_years_from_months(self):
        year = 2021

        for month in calendar.months(year):
            self.assertTrue(month.year() == year)

    def test_should_get_month_names_and_numbers(self):
        months = calendar.month_names_and_numbers()

        for month in self.CORRECT_MONTH_NAME_AND_NUMBERS:
            self.assertTrue(month in months)


if __name__ == '__main__':
    unittest.main()
