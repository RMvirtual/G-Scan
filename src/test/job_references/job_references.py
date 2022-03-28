import unittest
import src.main.job_references.references as job_refs
from src.main.date.date import Date

class TestJobReferences(unittest.TestCase):
    def test_should_get_template_job_number(self):
        date = Date.from_month_number_and_year(3,2022)
        job_number = job_refs.template_job_number(date)
        correct_job_number = "220300000"

        self.assertEqual(correct_job_number, job_number)

    def test_should_get_quick_job_number(self):
        date = Date.from_month_number_and_year(3,2022)
        job_number = job_refs.job_number_from_brief("2300", date)
        correct_job_number = "220302300"

        self.assertEqual(correct_job_number, job_number)

    def test_should_get_full_job_number(self):
        inputted_numbers = ["GR190100200", "190100200"]
        correct_reference = "GR190100200"

        for inputted_number in inputted_numbers:
            job_reference = job_refs.gr_reference(inputted_number)
            self.assertEqual(correct_reference, job_reference)

    def test_should_validate_full_number_length(self):
        correct_length = "190105255"

        incorrect_lengths = [
            "1901052555", "19010525", "" "ABCDEFGHIJKLMNOPQRSTUVQXYZ"]

        self.assertTrue(job_refs.is_full_input_length(correct_length))

        (self.assertFalse(job_refs.is_full_input_length(value))
            for value in incorrect_lengths)

    def test_should_validate_quick_number_length(self):
        correct_values = [
            "190105255", "1234", "12345",
            "123456", "1234567", "12345678", "123456789"
        ]
            
        incorrect_values = [
            "0123456789", "OHNANANAAAAWHATSMANAME", "",
            "ABCDEFGHIJKLMNOPQRSTUVQXYZ"
        ]

        (self.assertTrue(job_refs.is_quick_input_length(value))
            for value in correct_values)

        (self.assertFalse(job_refs.is_quick_input_length(value))
            for value in incorrect_values)

if __name__ == '__main__':
    unittest.main()