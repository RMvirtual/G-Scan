import unittest
import src.main.job_references.references as job_refs
import src.main.date.calendar as calendar


class TestJobReferences(unittest.TestCase):
    def test_should_create_template_job_number(self):
        date = calendar.date(month=3, year=2022)
        job_number = job_refs.template_job_number(date)
        correct_job_number = "220300000"

        self.assertEqual(correct_job_number, job_number)

    def test_should_create_quick_job_number(self):
        date = calendar.date(month=3, year=2022)
        job_number = job_refs.job_number_from_brief("2300", date)
        correct_job_number = "220302300"

        self.assertEqual(correct_job_number, job_number)

    def test_should_create_full_job_reference(self):
        numbers = ["GR190100200", "190100200"]
        correct_reference = "GR190100200"

        for number in numbers:
            reference = job_refs.gr_reference(number)
            self.assertEqual(correct_reference, reference)

    def test_should_validate_full_numbers(self):
        valid_number = "190105255"
        self.assertTrue(job_refs.is_full_input_length(valid_number))

    def test_should_invalidate_full_numbers(self):
        invalid_numbers = [
            "1901052555", "19010525", "" "ABCDEFGHIJKLMNOPQRSTUVQXYZ"]

        for number in invalid_numbers:
            self.assertFalse(job_refs.is_full_input_length(number))

    def test_should_validate_quick_numbers(self):
        valid_numbers = [
            "190105255", "1234", "12345",
            "123456", "1234567", "12345678", "123456789"
        ]

        for number in valid_numbers:
            self.assertTrue(job_refs.is_quick_input_length(number))

    def test_should_invalidate_quick_numbers(self):
        invalid_numbers = [
            "0123456789", "OHNANANAAAAWHATSMANAME", "",
            "ABCDEFGHIJKLMNOPQRSTUVQXYZ"
        ]
        
        for number in invalid_numbers:
            self.assertFalse(job_refs.is_quick_input_length(number))


if __name__ == '__main__':
    unittest.main()