import shutil
import tempfile
from pathlib import Path
from typing import Any, Generator

import pytest

from database import JSONDatabase, JSONDatabaseFiles


INPUT_DATA = Path(__file__).parent.joinpath("input_data")


class TestJSONDatabase:
    @pytest.fixture(autouse="function")
    def setup_teardown(self) -> Generator[Any, Any, Any]:
        temp_dir = Path(tempfile.TemporaryDirectory().name)
        shutil.copytree(INPUT_DATA, temp_dir)

        file_paths = [
            temp_dir.joinpath(f"{file_}.json") 
            for file_ in ["departments", "document_types", "user_settings"]
        ]

        self.database_files = JSONDatabaseFiles(*file_paths)

        yield
        shutil.rmtree(temp_dir)

    def test_should_load_departments(self) -> None:
        database = JSONDatabase(self.database_files)
        departments = database.all_departments()

        assert len(departments) == 2

        short_codes = set(department.short_code for department in  departments)
        assert short_codes == {"ops", "pods"}

    def test_should_load_document_types(self) -> None:
        database = JSONDatabase(self.database_files)
        document_types = database.all_documents()

        assert len(document_types) == 6
        short_codes = set(doc.short_code for doc in document_types)

        correct_short_codes = {
            "customer_paperwork_signed", "standard_delivery_note",
            "customer_paperwork", "dgn", "loading_list", "commercial_invoice"
        }

        assert short_codes == correct_short_codes

    def test_should_load_all_user_settings_json(self) -> None:
        database = JSONDatabase(self.database_files)
    
        correct_settings = {
            "GSCAN_DEFAULT": {
                "output_directory": "//office/edocs",
                "department": "ops",
                "document_type": "customer_paperwork"
            },
            "rmvir": {
                "output_directory": "//does_not_matter/share",
                "department": "ops",
                "document_type": "customer_paperwork"
            }
        }

        assert database.user_settings_json() == correct_settings

    def test_should_load_user_settings(self) -> None:
        database = JSONDatabase(self.database_files)
        settings = database.load_user_settings(username="rmvir")

        assert settings.username == "rmvir"
        assert settings.department.short_code == "ops"

    def test_should_overwrite_user_settings(self) -> None:
        database = JSONDatabase(self.database_files)

        settings = database.load_user_settings(username="rmvir")
        settings.department = database.department(short_code="pods")
        database.save_user_settings(settings)

        updated_settings = database.load_user_settings(username="rmvir")
        assert updated_settings.department.short_code == "pods"

    def test_overwrite_preserves_other_entries(self) -> None:
        database = JSONDatabase(self.database_files)

        settings = database.load_user_settings(username="rmvir")
        settings.department = database.department(short_code="pods")
        database.save_user_settings(settings)

        correct_settings = {
            "GSCAN_DEFAULT": {
                "output_directory": "//office/edocs",
                "department": "ops",
                "document_type": "customer_paperwork"
            },
            "rmvir": {
                "output_directory": "//does_not_matter/share",
                "department": "pods",
                "document_type": "customer_paperwork"
            }
        }

        assert database.user_settings_json() == correct_settings
