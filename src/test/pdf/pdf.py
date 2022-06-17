import unittest
import src.main.file_system.file_system as file_system
import src.main.pdf.reader as pdf_reader


class TestPdfReader(unittest.TestCase):
    def test_should_read_one_page_pdf(self):
        pdf_file_path = (
            file_system.test_resources_directory() +
            "/correct_files/one_page.pdf"
        )

        page = pdf_reader.read_pdf(source=pdf_file_path)[0]

        dpi_300_pixel_dims = {
            "height": 3508,
            "width": 2481
        }

        self.assertEqual(dpi_300_pixel_dims["height"], page.height)
        self.assertEqual(dpi_300_pixel_dims["width"], page.width)


if __name__ == "__main__":
    unittest.main()
