import unittest
import sys
import os
from pathlib import Path
import shutil

main_src_path = Path.cwd().parent.joinpath("src")
sys.path.append(main_src_path)

import app.file_system as file_system

class TestPDFWriter(unittest.TestCase):
    """A class for testing the PDF writer module."""

    def test_creating_single_page_with_reference(self):
        dict = self.setup_customer_paperwork()

        

    def setup_customer_paperwork(self):
        current_directory = file_system.get_current_directory()
        
        original_page = file_system.get_test_directory().joinpath(
            "resources", "pdf", "p1testfile1.pdf")
        
        scans_directory = file_system.get_test_directory().joinpath(
            "resources", "scans")

        shutil.copy(original_page, scans_directory)

        dict = {
            "original": original_page,
            "scan": scans_directory.joinpath("p1testfile1.pdf")
        }

        return dict