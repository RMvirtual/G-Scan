import numpy
import unittest
import src.main.file_system.file_system as file_system
import src.main.pdf.reader as pdf_reader


class TestPdfReader(unittest.TestCase):
    def test_should_read_300x300_pdf(self):
        self._populate_correct_pdf_values()

        pdf_path = (
            file_system.test_resources_directory() +
            "/correct_files/300x300.pdf"
        )

        page = pdf_reader.read_pdf(source=pdf_path)[0]

        dpi_300_pixel_dims = {
            "height": 300,
            "width": 300
        }

        self.assertEqual(dpi_300_pixel_dims["height"], page.height)
        self.assertEqual(dpi_300_pixel_dims["width"], page.width)

        for row in range(dpi_300_pixel_dims["height"]):
            for column in range(dpi_300_pixel_dims["width"]):
                pixel = page.pixel(row, column)
                correct_pixel = self.CORRECT_PDF_VALUES[column, row]

                for i in range(3):
                    self.assertEqual(pixel[i], correct_pixel[i], msg=(
                        "\nRow: " + str(row) + ", Column: " + str(column)
                    ))

    def _populate_correct_pdf_values(self):
        black_pixels = numpy.full(
            shape=(150, 300, 3),
            fill_value=(255, 255, 255)
        )

        white_pixels = numpy.full(
            shape=(150, 300, 3),
            fill_value=(0, 0, 0)
        )

        self.CORRECT_PDF_VALUES = numpy.concatenate(
            (white_pixels, black_pixels), axis=0)


if __name__ == "__main__":
    unittest.main()
