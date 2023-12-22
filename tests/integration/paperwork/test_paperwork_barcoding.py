import shutil
import tempfile
import fitz
import pytest
import pdf.pdf

from pathlib import Path
from paperwork_types import A4Document, CustomerPaperwork


class TestPaperworkBarcoding:
    @pytest.fixture
    def setup_teardown(self) -> None:
        test_data_folder = Path(__file__).parent.joinpath("input_data")
        self.temp_directory = Path(tempfile.TemporaryDirectory().name)

        shutil.copytree(test_data_folder, self.temp_directory)

        yield

        shutil.rmtree(self.temp_directory)

    def test_should_read_page(self, setup_teardown) -> None:
        one_page_file = self.temp_directory.joinpath("one_page_A4.pdf")
        page_images = pdf.pdf.read_pdf(str(one_page_file))

        assert len(page_images) == 1

        page = page_images[0]
        assert (page.w, page.h) == (2481, 3508)

    @pytest.mark.skip
    def test_should_write_page(self, setup_teardown) -> None:
        test_data_folder = Path(__file__).parent.joinpath("input_data")

        one_page_file = self.temp_directory.joinpath("one_page_A4.pdf")
        page_images = pdf.pdf.read_pdf(str(one_page_file))

        out_file = test_data_folder.joinpath("attempt.pdf")
        doc = A4Document(str(out_file))

        page_image = page_images[0]
        page_image.save(test_data_folder.joinpath("attempt.png"))

        doc.draw_page(str(test_data_folder.joinpath("attempt.png")))
        doc.save()

        result_doc = fitz.Document(out_file)
        image = result_doc.get_page_images(0)[0]

        correct_folder = Path(__file__).parent.joinpath("expected_outputs")
        correct_doc = fitz.Document(correct_folder.joinpath("attempt.pdf"))
        correct_image = correct_doc.get_page_images(0)[0]

        assert image == correct_image

    @pytest.mark.skip
    def test_should_write_barcode_page(self, setup_teardown) -> None:
        test_data_folder = Path(__file__).parent.joinpath("input_data")

        one_page_file = self.temp_directory.joinpath("one_page_A4.pdf")
        page_images = pdf.pdf.read_pdf(str(one_page_file))

        out_file = test_data_folder.joinpath("attempt_b.pdf")
        doc = CustomerPaperwork(str(out_file), job_reference="GR230100000")

        page_image = page_images[0]
        page_image.save(test_data_folder.joinpath("attempt_b.png"))

        doc.draw_page(str(test_data_folder.joinpath("attempt_b.png")))
        doc.save()
