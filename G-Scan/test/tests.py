import unittest
import sys
import os
from pathlib import Path

path = Path(os.getcwd()).parent
sys.path.append(str(path) + "\\src\\python")

import app.validation.string_length_comparison as sl

class TestStringLengthComparison(unittest.TestCase):
    """A class for testing the string length comparison module."""

    def test_string_length_equal_to_operator(self):
        correct_tests = [
            sl.is_string_length_equal_to("190100100", 9),
            sl.is_string_length_equal_to("19010010", 8),
            sl.is_string_length_equal_to("LOLOLOLOLOL", 11)
        ]

        for test in correct_tests:
            self.assertTrue(test)
        
        fail_tests = [
            sl.is_string_length_equal_to("190100100", 6),
            sl.is_string_length_equal_to("19010010", 5),
            sl.is_string_length_equal_to("LOLOLOLOLOL", 50)
        ]

        for test in fail_tests:
            self.assertFalse(test)

    def test_string_length_less_than_operator(self):
        true_tests = [
            sl.is_string_length_less_than("190100100", 10),
            sl.is_string_length_less_than("19010010", 9),
            sl.is_string_length_less_than("LOLOLOLOLOL", 50)
        ]

        for test in true_tests:
            self.assertTrue(test)
        
        false_tests = [
            sl.is_string_length_less_than("190100100", 9),
            sl.is_string_length_less_than("19010010", 5),
            sl.is_string_length_less_than("LOLOLOLOLOL", 1)
        ]

        for test in false_tests:
            self.assertFalse(test)

    def test_string_length_less_than_equal_to_operator(self):
        true_tests = [
            sl.is_string_length_less_than_equal_to("190100100", 9),
            sl.is_string_length_less_than_equal_to("19010010", 15),
            sl.is_string_length_less_than_equal_to("LOLOLOLOLOL", 50)
        ]

        for test in true_tests:
            self.assertTrue(test)
        
        false_tests = [
            sl.is_string_length_less_than_equal_to("190100100", 8),
            sl.is_string_length_less_than_equal_to("19010010", 5),
            sl.is_string_length_less_than_equal_to("LOLOLOLOLOL", 1)
        ]

        for test in false_tests:
            self.assertFalse(test)

    def test_string_length_greater_than_operator(self):
        true_tests = [
            sl.is_string_length_greater_than("190100100", 8),
            sl.is_string_length_greater_than("19010010", 7),
            sl.is_string_length_greater_than("LOLOLOLOLOL", 1)
        ]

        for test in true_tests:
            self.assertTrue(test)
        
        false_tests = [
            sl.is_string_length_greater_than("190100100", 9),
            sl.is_string_length_greater_than("19010010", 8),
            sl.is_string_length_greater_than("LOLOLOLOLOL", 50)
        ]

        for test in false_tests:
            self.assertFalse(test)

    def test_string_length_greater_than_equal_to_operator(self):
        true_tests = [
            sl.is_string_length_greater_than_equal_to("190100100", 9),
            sl.is_string_length_greater_than_equal_to("19010010", 5),
            sl.is_string_length_greater_than_equal_to("LOLOLOLOLOL", 1)
        ]

        for test in true_tests:
            self.assertTrue(test)
        
        false_tests = [
            sl.is_string_length_greater_than_equal_to("190100100", 10),
            sl.is_string_length_greater_than_equal_to("19010010", 9),
            sl.is_string_length_greater_than_equal_to("LOLOLOLOLOL", 50)
        ]

        for test in false_tests:
            self.assertFalse(test)

unittest.main()