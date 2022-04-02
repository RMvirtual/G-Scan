import unittest
import src.main.file_system.file_system as file_system
from src.main.barcodes.reader import read_job_references


class TestBarcodeReader(unittest.TestCase):
    def test_should_read_barcode(self):
        pdf_file = (
            file_system.test_resources_directory() +
            "/correct_files/p1testfile1_pdf_with_barcode.pdf"
        )

        barcodes = read_job_references(pdf_file)
        correct_barcode = "GR190100200"

        self.assertEqual(correct_barcode, barcodes[0])


if __name__ == '__main__':
    unittest.main()
