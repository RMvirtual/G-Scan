from src.main import file_system
from src.main import documents


class Department:
    def __init__(self) -> None:
        self.short_code = ""
        self.full_name = ""
        self.short_name = ""
        self.document_types = []


class Departments:
    def __init__(self):
        self.departments = []

    def __contains__(self, short_code: str) -> bool:
        for department in self.departments:
            if department.short_code == short_code:
                return True

        return False

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