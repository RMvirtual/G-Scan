import unittest
import src.main.job_references.references as job_refs
import src.main.date.date as date

class TestJobReferences(unittest.TestCase):
    """A class for testing the job references module."""

    def test_calculate_base_job_number(self):
        current_date = date.Date.from_month_number_and_year(3,2022)
        base_job_number = job_refs.calculate_base_job_number(current_date)
        self.assertTrue(base_job_number == "220300000", base_job_number)

        another_date = date.Date(1, "January", 2019)
        base_job_number = job_refs.calculate_base_job_number(another_date)
        self.assertTrue(base_job_number == "190100000")

    @unittest.skip("Pain testing dynamically changing dates.")
    def test_create_quick_job_number(self):
        current_date = date.get_current_month()
        job_number = job_refs.create_quick_job_number(
            "2300", current_date)

        correct_number = "210502300"
        self.assertTrue(job_number == correct_number, correct_number)

    def test_create_job_reference(self):
        correct_reference = "GR190100200"
        input_values = ["GR190100200", "190100200"]

        for value in input_values:
            job_reference = job_refs.create_job_reference(value)
            self.assertTrue(job_reference == correct_reference)

    def test_create_gr_number(self):
        job_number = "190105255"
        correct_job_number = "GR190105255"
        gr_number = job_refs.prefix_gr_to_job_number(job_number)

        self.assertTrue(gr_number == correct_job_number)

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