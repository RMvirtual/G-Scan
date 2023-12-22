import shutil
import tempfile
import pytest

from pathlib import Path
from database import JSONDatabase
from file_system import JSONDatabaseFiles
  

class TestJSONDatabase:
    @pytest.fixture
    def setup_teardown(self) -> None:
        test_data_folder = Path(__file__).parent.joinpath("data")

        self.temp_directory = Path(tempfile.TemporaryDirectory().name)
        shutil.copytree(test_data_folder, self.temp_directory)

        self.database_files = JSONDatabaseFiles(
            self.temp_directory.joinpath("departments.json"),
            self.temp_directory.joinpath("document_types.json"),
            self.temp_directory.joinpath("user_settings.json")
        )

        yield

        shutil.rmtree(self.temp_directory)

    def test_should_load_departments(self, setup_teardown) -> None:
        database = JSONDatabase(self.database_files)
        departments = database.all_departments()

        assert len(departments) == 2

        short_codes = set(department.short_code for department in  departments)
        assert short_codes == {"ops", "pods"}

    def test_should_load_document_types(self, setup_teardown) -> None:
        database = JSONDatabase(self.database_files)
        document_types = database.all_documents()

        assert len(document_types) == 6

        short_codes = set(doc_type.short_code for doc_type in document_types)

        correct_short_codes = {
            "customer_paperwork_signed", "standard_delivery_note",
            "customer_paperwork", "dgn", "loading_list", "commercial_invoice"
        }

        assert short_codes == correct_short_codes

    def test_should_load_all_user_settings_json(self, setup_teardown) -> None:
        database = JSONDatabase(self.database_files)
    
        correct_settings = {
            "GSCAN_DEFAULT": {
                "scan_directory": "",
                "dest_directory": "//office/edocs",
                "department": "ops",
                "document_type": "customer_paperwork"
            },
            "rmvir": {
                "scan_directory": "myshare/lol",
                "dest_directory": "//does_not_matter/share",
                "department": "ops",
                "document_type": "customer_paperwork"
            }
        }

        assert database.user_settings_json() == correct_settings

    def test_should_load_user_settings(self, setup_teardown) -> None:
        database = JSONDatabase(self.database_files)
        settings = database.load_user_settings(username="rmvir")

        assert settings.username == "rmvir"
        assert settings.department.short_code == "ops"

    def test_should_overwrite_user_settings(self, setup_teardown) -> None:
        database = JSONDatabase(self.database_files)

        settings = database.load_user_settings(username="rmvir")
        settings.department = database.department(short_code="pods")
        
        database.save_user_settings(settings)

        updated_settings = database.load_user_settings(username="rmvir")
        assert updated_settings.department.short_code == "pods"
