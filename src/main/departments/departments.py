from src.main import file_system
from src.main import documents


class Department:
    def __init__(self) -> None:
        self.short_code = ""
        self.full_name = ""
        self.short_name = ""
        self.document_types = []


def load(short_code: str) -> Department:
    departments = _load_json()

    return _department(key=short_code, values=departments[short_code])


def load_all() -> list[Department]:
    departments = _load_json()

    result = []

    for short_code, values in departments.items():
        result.append(_department(key=short_code, values=values))

    return result


def _department(key: str, values: dict[str, any]) -> Department:
    result = Department()
    result.short_code = key
    result.full_name = values["full_name"]
    result.short_name = values["short_name"]
    raw_document_types = values["document_types"]

    all_types = documents.load_all_types()
    document_types = []

    for document in all_types:
        if document.short_code in raw_document_types:
            document_types.append(document)

    result.document_types = document_types

    return result



def _load_json() -> dict[str, any]:
    return file_system.load_json(file_system.departments_path())