from pathlib import Path
from database import JSONDatabase
from file_system import JSONDatabaseFiles
  

def database_files() -> JSONDatabaseFiles:
    # Could do with a setup method here to create a temp folder
    # for the data files each test.
    data_files_folder = Path(__file__).parent.joinpath("data")

    return JSONDatabaseFiles(
        data_files_folder.joinpath("departments.json"),
        data_files_folder.joinpath("document_types.json"),
        data_files_folder.joinpath("user_settings.json")
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
        "customer_paperwork_signed", "standard_delivery_note",
        "customer_paperwork", "dgn", "loading_list", "commercial_invoice"
    }

    assert short_codes == correct_short_codes


def test_should_load_user_settings() -> None:
    database = JSONDatabase(database_files())
    settings = database.load_user_settings(username="rmvir")

    assert settings.username == "rmvir"
    assert settings.department.short_code == "ops"


def test_should_overwrite_user_settings() -> None:
    database = JSONDatabase(database_files())

    settings = database.load_user_settings(username="rmvir")
    settings.department = database.department(short_code="pods")
    
    database.save_user_settings(settings)

    updated_settings = database.load_user_settings(username="rmvir")
    assert updated_settings.department.short_code == "pods"
