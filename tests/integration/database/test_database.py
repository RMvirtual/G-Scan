from pathlib import Path
from database import Database
from file_system import DatabaseFiles


def test_should_load_departments() -> None:
    data_files_folder = Path(__file__).parent.joinpath("data")

    database_files = DatabaseFiles(
        data_files_folder.joinpath("departments.json"),
        data_files_folder.joinpath("document_types.json"),
        data_files_folder.joinpath("user_defaults.json")
    )

    database = Database(database_files)
    departments = database.all_departments()

    assert len(departments) == 2

    short_codes = set(department.short_code for department in  departments)
    assert short_codes == {"ops", "pods"}
