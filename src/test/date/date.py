import unittest
import src.main.date.calendar as calendar

class TestDate(unittest.TestCase):
    """A class for testing the date module."""

    def test_should_get_month_names(self):
        months = calendar.months(2021)
        month_names_to_test = self.correct_month_names()

        for month in months:
            self.assertTrue(month.month_name() in month_names_to_test)

    def test_should_get_years_from_months(self):
        months = calendar.months(2021)
        
        for month in months:
            self.assertTrue(month.year() == 2021)

        months = calendar.months(2022)
        
        for month in months:
            self.assertTrue(month.year() == 2022)

    def test_should_get_month_names_and_numbers(self):
        months = calendar.month_names_and_numbers()
        correct_months = self.correct_month_names_and_numbers()

        (self.assertTrue(month in correct_months) for month in months)

    def test_should_get_current_month(self):
        month = calendar.current_month()
    
        self.assertTrue(month.month_name() == "March")
        self.assertTrue(month.month_number() == 3)
        self.assertTrue(month.month_number_as_two_digits() == "03")
        self.assertTrue(month.year() == 2022)
        self.assertTrue(month.year_as_two_digits() == "22")

    def test_should_get_past_two_years(self):
        correct_years = (2022, 2021)
        years = calendar.years()

        (self.assertTrue(year in years) for year in correct_years)

    def correct_month_names(self) -> list[str]:
        return [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]

    def correct_month_names_and_numbers(self) -> list[str]:
        return [
            "January - 01", "February - 02", "March - 03",
            "April - 04", "May - 05", "June - 06",
            "July - 07", "August - 08", "September - 09",
            "October - 10", "November - 11", "December - 12"
        ]

if __name__ == '__main__':
    unittest.main()