import shutil
import tempfile
import pytest

from pathlib import Path


class TestPaperworkBarcoding:
    @pytest.fixture
    def setup_teardown(self) -> None:
        test_data_folder = Path(__file__).parent.joinpath("data")
        self.temp_directory = Path(tempfile.TemporaryDirectory().name)

        shutil.copytree(test_data_folder, self.temp_directory)

        yield

        # shutil.rmtree(self.temp_directory)


    def test_should_barcode_page(self, setup_teardown) -> None:
        one_page_file = self.temp_directory.joinpath("one_page_A4.pdf")

        