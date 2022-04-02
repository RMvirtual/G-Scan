import unittest
import os
import shutil
from wand.image import Image
import src.main.file_system.file_system as file_system
import src.main.file_names.name_scheme as file_naming
from src.main.paperwork.writer.customer_paperwork import (
    CustomerPaperworkPDFWriter)

@unittest.SkipTest
class TestCustomerPaperworkPDFWriter(unittest.TestCase):
    """A class for testing the PDF writer module."""

    def check_if_paperwork_pages_are_identical(
            self, correct_image: Image, result_file_path: str):
        with Image(filename=result_file_path, resolution=150) as expected:
            difference = correct_image.compare(
                expected, metric="root_mean_square")

            self.assertLess(difference[1], 0.01)

    def get_folder_from_test_resources(self, folder):
        test_dir = file_system.test_resources_directory()
        full_path = test_dir + "/" + folder

        return full_path

    def teardown_customer_paperwork_pdf(self, path):
        os.remove(path)


class TestSinglePagePDFCustomerPaperworkWriter(
    TestCustomerPaperworkPDFWriter):

    def setup_file_name_attributes(self, job_ref):
        file_name_attributes = file_naming.FileNamingAttributes()

        file_name_attributes.paperwork_type = "Cust PW"
        file_name_attributes.input_mode = "Normal"
        file_name_attributes.file_extension = ".pdf"
        file_name_attributes.page_number = 1
        file_name_attributes.job_reference = job_ref

        return file_name_attributes

    def setup_customer_paperwork_pdf(self) -> dict:
        original_page = file_system.test_resources_directory() + (
            "/correct_files/p1testfile1.pdf")

        scans_directory = file_system.test_resources_directory() + "/scans"
        shutil.copy(original_page, scans_directory)

        dict = {
            "original": original_page,
            "scan": scans_directory + "/p1testfile1.pdf"
        }

        return dict

    def test_creating_single_page_pdf_with_reference(self):
        dict = self.setup_customer_paperwork_pdf()

        scan_file = dict.get("scan")
        output_directory = self.get_folder_from_test_resources("output")
        output_path = output_directory + "/single_page_pdf_test.pdf"
        job_ref = "GR190100200"

        writer = CustomerPaperworkPDFWriter()
        writer.write_to_file(scan_file, output_path, job_ref)

        correct_pdf = file_system.test_resources_directory() + (
            "/correct_files/p1testfile1_pdf_with_barcode.pdf")

        correct_image = Image(filename=str(correct_pdf), resolution=150)

        self.check_if_paperwork_pages_are_identical(
            correct_image, output_path)

        self.teardown_customer_paperwork_pdf(output_path)


class TestSinglePagePNGCustomerPaperworkWriter(
    TestCustomerPaperworkPDFWriter):
    def setup_file_name_attributes(self, job_ref):
        file_name_attributes = file_naming.FileNamingAttributes()

        file_name_attributes.paperwork_type = "Cust PW"
        file_name_attributes.input_mode = "Normal"
        file_name_attributes.file_extension = ".pdf"
        file_name_attributes.page_number = 1
        file_name_attributes.job_reference = job_ref

        return file_name_attributes

    def setup_customer_paperwork_png(self) -> dict:
        page_to_copy = file_system.test_resources_directory() + (
            "/correct_files/p1testfile1.png")

        scans_directory = file_system.test_resources_directory() + (
            "/scans")

        with Image(filename=page_to_copy, resolution=300) as image:
            image.save(filename=str(scans_directory + "/p1testfile1.png"))

        dict = {
            "original": page_to_copy,
            "scan": scans_directory + "/p1testfile1.png"
        }

        return dict

    def test_creating_single_page_png_with_reference(self):
        dict = self.setup_customer_paperwork_png()

        scan_file = str(dict.get("scan"))
        output_directory = self.get_folder_from_test_resources("output")
        output_path = output_directory + "/single_page_pdf_test.pdf"

        job_ref = "GR190100200"

        writer = CustomerPaperworkPDFWriter()
        writer.write_to_file(scan_file, output_path, job_ref)

        correct_pdf = file_system.test_resources_directory() + (
            "/correct_files/p1testfile1_png_with_barcode.pdf")

        correct_image = Image(filename=str(correct_pdf), resolution=150)

        self.check_if_paperwork_pages_are_identical(correct_image, output_path)
        self.teardown_customer_paperwork_pdf(output_path)


class TestMultiplePagePDFCustomerPaperwork(TestCustomerPaperworkPDFWriter):
    def setup_multiple_page_pdf(self):
        pdf_to_copy = file_system.test_resources_directory() + (
            "/correct_files/testfile2_with_5_pages.pdf")

        scans_directory = file_system.test_resources_directory() + "/scans"
        output_path = scans_directory + "/testfile2_with_5_pages.pdf"

        shutil.copy(pdf_to_copy, output_path)

        dict = {
            "original": pdf_to_copy,
            "scan": output_path
        }

        return dict

    def test_creating_multiple_page_pdf(self):
        dict = self.setup_multiple_page_pdf()

        scan_file = dict.get("scan")
        output_directory = self.get_folder_from_test_resources("output")
        output_path = output_directory + "/multiple_page_pdf_test.pdf"
        job_ref = "GR190100200"

        writer = CustomerPaperworkPDFWriter()
        writer.write_to_file(scan_file, output_path, job_ref)

        correct_pdf = (
                file_system.test_resources_directory() +
                "/correct_files/test_file_2_with_5_pages_with_barcodes.pdf"
        )

        correct_image = Image(filename=str(correct_pdf), resolution=150)

        self.check_if_paperwork_pages_are_identical(
            correct_image, output_path)

        self.teardown_customer_paperwork_pdf(output_path)


if __name__ == '__main__':
    unittest.main()
