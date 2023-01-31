from src.main import file_system
from src.main import documents


class Department:
    def __init__(self) -> None:
        self.short_code: str = ""
        self.full_name: str = ""
        self.short_name: str = ""
        self.document_types = documents.DocumentTypes()


class Departments:
    def __init__(self):
        self.departments = []

    def __contains__(self, short_code: str) -> bool:
        return len(short_code == other for other in self.short_names())

    def __iter__(self):
        return self.departments.__iter__()

    def short_names(self) -> list[str]:
        return [document.short_code for document in self.departments]

    def full_names(self) -> list[str]:
        return [document.full_name for document in self.departments]


def load(short_code: str) -> Department:
    departments = _load_json()

    return _department(key=short_code, values=departments[short_code])


def load_all() -> Departments:
    result = Departments()

    result.departments = [
        _department(key=short_code, values=values)
        for short_code, values in _load_json().items()
    ]

    return result


def _department(key: str, values: dict[str, any]) -> Department:
    result = Department()
    result.short_code = key
    result.full_name = values["full_name"]
    result.short_name = values["short_name"]
    result.document_types = _document_types(values)

    return result


def _document_types(values: dict[str, any]) -> documents.DocumentTypes:
    result = documents.DocumentTypes()

    result.documents = [
        document for document in documents.load_all_types()
        if document.short_code in values["document_types"]
    ]

    return result


def _load_json() -> dict[str, any]:
    return file_system.load_json(file_system.departments_path())