import unittest
import sys
import os
from pathlib import Path
import shutil
from wand.image import Image

main_src_path = Path.cwd().parent.joinpath("src")
sys.path.append(main_src_path)

import app.file_system as file_system
import app.validation.file_naming as file_naming
from pdf.pdf_writer import create_cust_pw

class TestPDFWriter(unittest.TestCase):
    """A class for testing the PDF writer module."""

    def test_creating_single_page_with_reference(self):
        dict = self.setup_customer_paperwork()

        class MasterApplication():
            def __init__(self):
                self.temp_dir = file_system.get_temp_directory()

        master_application = MasterApplication()
        scan = dict.get("scan")

        scan_dir = file_system.get_test_directory().joinpath(
            "resources", "scans")

        dest_dir = file_system.get_test_directory().joinpath(
            "resources", "destination")

        job_ref = "GR190100200"

        file_name_attributes = file_naming.FileNamingAttributes()

        file_name_attributes.paperwork_type = "Cust PW"
        file_name_attributes.input_mode = "Normal"
        file_name_attributes.file_extension = ".pdf"
        file_name_attributes.page_number = 1
        file_name_attributes.job_reference = job_ref

        dest_file_name = file_naming.create_destination_file_name(file_name_attributes)

        result_file = create_cust_pw(
            master_application, str(scan), str(scan_dir), str(dest_dir), job_ref,
            dest_file_name, False
        )

        correct_pdf = file_system.get_test_directory().joinpath(
            "resources", "correct_files", "p1testfile1withbarcode.pdf")

        correct_image = Image(filename=str(correct_pdf), resolution=150)

        self.check_if_paperwork_pages_are_identical(
            correct_image, result_file)

    def setup_customer_paperwork(self) -> dict:
        current_directory = file_system.get_current_directory()
        
        original_page = file_system.get_test_directory().joinpath(
            "resources", "correct_files", "p1testfile1.pdf")
        
        scans_directory = file_system.get_test_directory().joinpath(
            "resources", "scans")

        shutil.copy(original_page, scans_directory)

        dict = {
            "original": original_page,
            "scan": scans_directory.joinpath("p1testfile1.pdf")
        }

        return dict

    def check_if_paperwork_pages_are_identical(self, correct_image: Image,
            result_file: Image):
        with Image(filename=result_file, resolution=150) as expected:
            difference = correct_image.compare(expected, metric="root_mean_square")
            self.assertLess(difference[1], 0.01)


    class CustomerPaperworkData():
        """A data structure to hold the necessary info."""

        def __init__(self):
            current_directory = file_system.get_current_directory()
            
            original_page = file_system.get_test_directory().joinpath(
                "resources", "pdf", "p1testfile1.pdf")
            
            scans_directory = file_system.get_test_directory().joinpath(
                "resources", "scans")
