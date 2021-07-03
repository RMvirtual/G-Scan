import unittest
import sys
import os
from pathlib import Path

main_src_path = str(Path(os.getcwd()).parent) + "\\src"
sys.path.append(main_src_path)

import date
from date import Date

class TestDate(unittest.TestCase):
    """A class for testing the date module."""

    def test_month_names_in_get_months(self):
        months = date.get_months(2021)
        month_names_to_test = self.get_month_names_strings()

        for month in months:
            self.assertTrue(month.get_month_name() in month_names_to_test)

    def test_years_pull_through_in_get_months(self):
        months = date.get_months(2021)
        
        for month in months:
            self.assertTrue(month.get_year() == 2021)

        months = date.get_months(2022)
        
        for month in months:
            self.assertTrue(month.get_year() == 2022)

    def test_get_current_year_is_2021(self):
        current_year = date.get_current_year()
        current_year_in_two_digits = date.get_current_year_as_two_digits()
        
        self.assertTrue(current_year == 2021)
        self.assertTrue(current_year_in_two_digits == 21)

    def test_get_last_year_is_2020(self):
        last_year = date.get_last_year()
        last_year_in_two_digits = date.get_last_year_as_two_digits()
        
        self.assertTrue(last_year == 2020)
        self.assertTrue(last_year_in_two_digits == 20)

    @unittest.skip("Pain checking dynamically changing dates.")
    def test_current_month_number_is_five(self):
        month_number = date.get_current_month_number()

        self.assertTrue(month_number == 6)

    def test_get_month_names_and_numbers(self):
        months = date.get_month_names_and_numbers()
        strings_to_test = self.get_month_name_and_numbers_as_strings()

        for month in months:
            self.assertTrue(month in strings_to_test) 

    @unittest.skip("Pain checking dynamically changing dates.")
    def test_get_current_month_is_june(self):
        month = date.get_current_month()

        self.assertTrue(month.get_month_name() == "June")
        self.assertTrue(month.get_month_number() == 6)
        self.assertTrue(month.get_month_number_as_two_digits() == "06")
        self.assertTrue(month.get_year() == 2021)
        self.assertTrue(month.get_year_as_two_digits() == "21")

    def test_get_years(self):
        years_to_test = (2021, 2020)
        years = date.get_years()

        for year in years:
            self.assertTrue(year in years_to_test)

    def get_month_names_strings(self):
        month_names = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]

        return month_names

    def get_month_name_and_numbers_as_strings(self):
        months = [
            "January - 01", "February - 02", "March - 03",
            "April - 04", "May - 05", "June - 06",
            "July - 07", "August - 08", "September - 09",
            "October - 10", "November - 11", "December - 12"
        ]

        return months