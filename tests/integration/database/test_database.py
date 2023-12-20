from pathlib import Path
from database import JSONDatabase
from file_system import JSONDatabaseFiles
  

def database_files() -> JSONDatabaseFiles:
    data_files_folder = Path(__file__).parent.joinpath("data")

    return JSONDatabaseFiles(
        data_files_folder.joinpath("departments.json"),
        data_files_folder.joinpath("document_types.json"),
        data_files_folder.joinpath("user_defaults.json")
    )


def test_should_load_departments() -> None:
    database = JSONDatabase(database_files())
    departments = database.all_departments()

    assert len(departments) == 2

    short_codes = set(department.short_code for department in  departments)
    assert short_codes == {"ops", "pods"}


def test_should_load_document_types() -> None:
    database = JSONDatabase(database_files())
    document_types = database.all_documents()

    assert len(document_types) == 6

    short_codes = set(doc_type.short_code for doc_type in document_types)

    correct_short_codes = {
        "customer_paperwork_signed",  "standard_delivery_note",
        "customer_paperwork", "dgn", "loading_list", "commercial_invoice"
    }

    assert short_codes == correct_short_codes


def test_should_load_user_settings() -> None:
    database = JSONDatabase(database_files())


