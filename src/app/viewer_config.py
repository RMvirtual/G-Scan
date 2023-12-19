import database

from departments import Department, Departments
from documents import Document


class ViewerConfiguration:
    def __init__(self) -> None:
        self.scan_directory: str = ""
        self.dest_directory: str = ""
        self.department: Department = None
        self.document_type: Document = None
        self.all_departments: Departments = database.load_all_departments()

    def set_department(
            self, short_code: str = None, full_name: str = None) -> None:
        if short_code:
            self.department = self.all_departments.from_short_code(short_code)

        elif full_name:
            self.department = self.all_departments.from_full_name(full_name)

        else:
            raise ValueError("No department parameter provided.")

    def set_document_type(
            self, short_code: str = None, full_name: str = None) -> None:
        if short_code:
            self.document_type = \
                self.department.document_types.from_short_code(short_code)

        elif full_name:
            self.document_type = \
                self.department.document_types.from_full_name(full_name)

        else:
            raise ValueError("No document type paremeter provided.")


def load() -> ViewerConfiguration:
    result = ViewerConfiguration()
    result.all_departments = database.load_all_departments()

    return result


def load_default() -> ViewerConfiguration:
    user_defaults = database.load_user_settings()

    result = load()
    result.scan_directory = user_defaults.scan_dir
    result.dest_directory = user_defaults.dest_dir
    result.document_type = user_defaults.document_type
    result.department = user_defaults.department

    return result
