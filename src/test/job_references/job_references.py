import unittest
import src.main.job_references.references as job_refs
import src.main.date.calendar as calendar


class TestJobReferences(unittest.TestCase):
    def test_should_get_template_job_number(self):
        date = calendar.date(month=3, year=2022)
        job_number = job_refs.template_job_number(date)
        correct_job_number = "220300000"

        self.assertEqual(correct_job_number, job_number)

    def test_should_get_quick_job_number(self):
        date = calendar.date(month=3, year=2022)
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
        valid_number = "190105255"

        invalid_numbers = [
            "1901052555", "19010525", "" "ABCDEFGHIJKLMNOPQRSTUVQXYZ"]

        self.assertTrue(job_refs.is_full_input_length(valid_number))

        for number in invalid_numbers:
            self.assertFalse(job_refs.is_full_input_length(number))

    def test_should_validate_quick_number_length(self):
        valid_numbers = [
            "190105255", "1234", "12345",
            "123456", "1234567", "12345678", "123456789"
        ]
            
        invalid_numbers = [
            "0123456789", "OHNANANAAAAWHATSMANAME", "",
            "ABCDEFGHIJKLMNOPQRSTUVQXYZ"
        ]

        for number in valid_numbers:
            self.assertTrue(job_refs.is_quick_input_length(number))
            
        for number in invalid_numbers:
            self.assertFalse(job_refs.is_quick_input_length(number))


if __name__ == '__main__':
    unittest.main()