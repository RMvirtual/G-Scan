import unittest
import src.main.job_references.references as job_refs
from src.main.date.date import Date

class TestJobReferences(unittest.TestCase):
    """A class for testing the job references module."""

    def test_calculate_base_job_number(self):
        date = Date.from_month_number_and_year(3,2022)
        job_number = job_refs.base_job_number(date)
        correct_job_number = "220300000"

        self.assertEqual(correct_job_number, job_number)

    def test_create_quick_job_number(self):
        date = Date.from_month_number_and_year(3,2022)
        job_number = job_refs.create_quick_job_number("2300", date)
        correct_job_number = "220302300"

        self.assertEqual(correct_job_number, job_number)

    def test_create_job_reference(self):
        inputted_numbers = ["GR190100200", "190100200"]
        correct_reference = "GR190100200"

        for inputted_number in inputted_numbers:
            job_reference = job_refs.job_reference(inputted_number)
            self.assertEqual(correct_reference, job_reference)

    def test_full_number_input_length_check(self):
        correct_number = "190105255"
        length_okay = job_refs.check_full_number_input_length(correct_number)
        self.assertTrue(length_okay[0])

        false_tests = [
            "1901052555",
            "19010525",
            ""
            "ABCDEFGHIJKLMNOPQRSTUVQXYZ"
        ]

        for test in false_tests:
            is_correct_length = job_refs.check_full_number_input_length(test)
            self.assertFalse(is_correct_length[0])

    def test_quick_mode_input_length_check(self):
        pass_values = [
            "190105255", "1234", "12345",
            "123456", "1234567", "12345678", "123456789"
        ]

        for value in pass_values:
            length_okay = job_refs.check_quick_mode_input_length(value)
            self.assertTrue(length_okay[0])

        false_values = [
            "0123456789",
            "OHNANANAAAAWHATSMANAME",
            "",
            "ABCDEFGHIJKLMNOPQRSTUVQXYZ"
        ]

        for value in false_values:
            length_okay = job_refs.check_full_number_input_length(value)
            self.assertFalse(length_okay[0])

if __name__ == '__main__':
    unittest.main()