import unittest
from src.main.job_references.references import GrReference
import src.main.date.calendar as calendar


class TestJobReferences(unittest.TestCase):
    def test_should_create_template_gr_reference(self):
        date = calendar.date(month=3, year=2022)
        gr_ref = GrReference.TemplateReference(date)
        correct_gr_ref = "GR220300000"

        self.assertEqual(correct_gr_ref, gr_ref.as_string())

    def test_should_create_quick_job_number(self):
        date = calendar.date(month=3, year=2022)
        job_number = GrReference(date)
        job_number.pad_reference("2300")
        correct_gr_ref = "GR220302300"

        self.assertEqual(correct_gr_ref, job_number.as_string())

    def test_should_create_full_gr_reference(self):
        numbers = ["GR190100200", "190100200"]
        correct_reference = "GR190100200"

        for number in numbers:
            reference = GrReference.FromFullReference(number)
            self.assertEqual(correct_reference, reference)

    def test_should_error_if_wrong_length(self):
        self.fail(msg="Test not completed")

    def test_should_invalidate_full_numbers(self):
        invalid_numbers = [
            "1901052555", "19010525", "" "ABCDEFGHIJKLMNOPQRSTUVQXYZ"]

        self.fail(msg="Test not completed")

    def test_should_validate_quick_numbers(self):
        valid_numbers = [
            "190105255", "1234", "12345",
            "123456", "1234567", "12345678", "123456789"
        ]

        self.fail(msg="Test not completed")

    def test_should_invalidate_quick_numbers(self):
        invalid_numbers = [
            "0123456789", "OHNANANAAAAWHATSMANAME", "",
            "ABCDEFGHIJKLMNOPQRSTUVQXYZ"
        ]
        
        self.fail(msg="Test not completed")


if __name__ == '__main__':
    unittest.main()