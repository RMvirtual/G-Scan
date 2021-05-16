import unittest
import sys
import os
from pathlib import Path

main_src_path = str(Path(os.getcwd()).parent) + "\\src"
sys.path.append(main_src_path)

import app.validation.string_length_comparison as slc

class TestStringLengthComparison(unittest.TestCase):
    """A class for testing the string length comparison module."""

    def test_string_length_equal_to_operator(self):
        correct_tests = [
            slc.is_equal_to("190100100", 9),
            slc.is_equal_to("19010010", 8),
            slc.is_equal_to("LOLOLOLOLOL", 11)
        ]

        for test in correct_tests:
            self.assertTrue(test)
        
        fail_tests = [
            slc.is_equal_to("190100100", 6),
            slc.is_equal_to("19010010", 5),
            slc.is_equal_to("LOLOLOLOLOL", 50)
        ]

        for test in fail_tests:
            self.assertFalse(test)

    def test_string_length_less_than_operator(self):
        true_tests = [
            slc.is_less_than("190100100", 10),
            slc.is_less_than("19010010", 9),
            slc.is_less_than("LOLOLOLOLOL", 50)
        ]

        for test in true_tests:
            self.assertTrue(test)
        
        false_tests = [
            slc.is_less_than("190100100", 9),
            slc.is_less_than("19010010", 5),
            slc.is_less_than("LOLOLOLOLOL", 1)
        ]

        for test in false_tests:
            self.assertFalse(test)

    def test_string_length_less_than_equal_to_operator(self):
        true_tests = [
            slc.is_less_than_equal_to("190100100", 9),
            slc.is_less_than_equal_to("19010010", 15),
            slc.is_less_than_equal_to("LOLOLOLOLOL", 50)
        ]

        for test in true_tests:
            self.assertTrue(test)
        
        false_tests = [
            slc.is_less_than_equal_to("190100100", 8),
            slc.is_less_than_equal_to("19010010", 5),
            slc.is_less_than_equal_to("LOLOLOLOLOL", 1)
        ]

        for test in false_tests:
            self.assertFalse(test)

    def test_string_length_greater_than_operator(self):
        true_tests = [
            slc.is_greater_than("190100100", 8),
            slc.is_greater_than("19010010", 7),
            slc.is_greater_than("LOLOLOLOLOL", 1)
        ]

        for test in true_tests:
            self.assertTrue(test)
        
        false_tests = [
            slc.is_greater_than("190100100", 9),
            slc.is_greater_than("19010010", 8),
            slc.is_greater_than("LOLOLOLOLOL", 50)
        ]

        for test in false_tests:
            self.assertFalse(test)

    def test_string_length_greater_than_equal_to_operator(self):
        true_tests = [
            slc.is_greater_than_equal_to("190100100", 9),
            slc.is_greater_than_equal_to("19010010", 5),
            slc.is_greater_than_equal_to("LOLOLOLOLOL", 1)
        ]

        for test in true_tests:
            self.assertTrue(test)
        
        false_tests = [
            slc.is_greater_than_equal_to("190100100", 10),
            slc.is_greater_than_equal_to("19010010", 9),
            slc.is_greater_than_equal_to("LOLOLOLOLOL", 50)
        ]

        for test in false_tests:
            self.assertFalse(test)

    def test_string_length_in_range(self):
        true_tests = [
            slc.is_between_range("190100100", 0, 9),
            slc.is_between_range("19010010", 4, 9),
            slc.is_between_range("LOLOLOLOLOL", 5, 11)
        ]

        for test in true_tests:
            self.assertTrue(test)

        false_tests = [
            slc.is_between_range("190100100", 0, 8),
            slc.is_between_range("19010010", 3, 7),
            slc.is_between_range("LOLOLOLOLOL", 15, 59)
        ]

        for test in false_tests:
            self.assertFalse(test)
