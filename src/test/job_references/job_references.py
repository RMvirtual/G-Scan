import unittest
from src.main.job_references.references import GrReference
import src.main.date.calendar as calendar


class TestJobReferences(unittest.TestCase):
    def test_should_create_template_gr_reference(self):
        date = calendar.date(month=3, year=2022)
        gr_ref = GrReference.TemplateReference(date)
        correct_gr_ref = "GR220300000"

        self.assertEqual(correct_gr_ref, gr_ref.as_string())

    def test_should_create_full_gr_reference(self):
        numbers = ["GR190100200", "190100200"]
        correct_reference = "GR190100200"

        for number in numbers:
            reference = GrReference.FullReference(number)
            self.assertEqual(correct_reference, reference.as_string())

    def test_should_error_if_full_input_is_too_short(self):
        incorrect_input = "19010021"

        with self.assertRaises(ValueError):
            _ = GrReference.FullReference(incorrect_input)

    def test_should_error_if_full_input_is_too_long(self):
        incorrect_input = "1901002101"

        with self.assertRaises(ValueError):
            _ = GrReference.FullReference(incorrect_input)

    def test_should_error_if_full_input_is_wrong_format(self):
        incorrect_input = "ABCDEFGHI"

        with self.assertRaises(ValueError):
            _ = GrReference.FullReference(incorrect_input)

    def test_should_create_quick_job_number(self):
        date = calendar.date(month=3, year=2022)
        job_number = GrReference.TemplateReference(date)
        job_number.add_quick_reference("2300")
        correct_gr_ref = "GR220302300"

        self.assertEqual(correct_gr_ref, job_number.as_string())

    def test_should_error_if_quick_job_number_is_wrong_format(self):
        date = calendar.date(month=3, year=2022)
        job_number = GrReference.TemplateReference(date)
        incorrect_input = "ABCDE"

        with self.assertRaises(ValueError):
            job_number.add_quick_reference(incorrect_input)

    def test_should_error_if_quick_job_number_is_too_short(self):
        date = calendar.date(month=3, year=2022)
        job_number = GrReference.TemplateReference(date)
        incorrect_input = ""

        with self.assertRaises(ValueError):
            job_number.add_quick_reference(incorrect_input)

    def test_should_error_if_quick_job_number_is_too_long(self):
        date = calendar.date(month=3, year=2022)
        job_number = GrReference.TemplateReference(date)
        incorrect_input = "220302300"

        with self.assertRaises(ValueError):
            job_number.add_quick_reference(incorrect_input)


if __name__ == '__main__':
    unittest.main()