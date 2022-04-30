import unittest
import os
import src.main.file_system.file_system as file_system
from src.main.paperwork.documents.a4 import A4Document
from src.main.paperwork.documents.customer_paperwork import CustomerPaperwork
import filecmp

class TestA4Document(unittest.TestCase):
    def test_should_create_a4_document_file(self):
        output_path = (
            file_system.test_resources_directory()
            + "/output/new_a4_document.pdf"
        )

        image = (
            file_system.test_resources_directory() + "/scans/p1testfile1.png")

        document = A4Document(output_path)
        document.draw_page(image_path=image)
        document.save()

        correct_file = (
                file_system.test_resources_directory()
                + "/correct_files/new_a4_document.pdf"
        )

        files_match = filecmp.cmp(
            f1=correct_file, f2=output_path, shallow=False)

        self.assertTrue(os.path.exists(image))
        self.assertTrue(files_match)

    def test_should_create_customer_paperwork_file(self):
        output_path = (
            file_system.test_resources_directory()
            + "/output/new_customer_paperwork.pdf"
        )

        image = (
            file_system.test_resources_directory() + "/scans/p1testfile1.png")

        document = CustomerPaperwork(
            file_name=output_path, job_reference="GR190100200")

        document.draw_page(image_path=image)
        document.save()

        self.assertTrue(os.path.exists(image))


if __name__ == '__main__':
    unittest.main()
