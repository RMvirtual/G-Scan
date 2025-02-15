from database import JSONDatabase
from departments import Department
from documents import DocumentType


class Configuration:
    def __init__(self, database: JSONDatabase, username: str) -> None:
        self.database = database

        self.settings = (
            database.create_user(username) if not database.user_exists(username)
            else database.load_user_settings(username)
        )

        self.dest_directory = self.settings.dest_dir
        self.department = self.settings.department
        self.document_type = self.settings.document_type
        self.departments = database.all_departments()

    def set_department(
            self, short_code: str = None, full_name: str = None) -> None:
        self._assert_one_parameter_used(short_code, full_name)

        if short_code:
            self.department = self.database.department(short_code=short_code)

        elif full_name:
            self.department = self.database.department(full_name=full_name)

    def set_document_type(
            self, short_code: str = None, full_name: str = None) -> None:
        self._assert_one_parameter_used(short_code, full_name)

        if short_code:
            self.document_type = \
                self.department.document_types.from_short_code(short_code)

        elif full_name:
            self.document_type = self.department.document_types.from_full_name(
                full_name)

    def _assert_one_parameter_used(
            short_code: str|None, full_name: str|None) -> None:
        if not (short_code or full_name):
            raise ValueError("Neither short code or full name parameter used.")
        
        if short_code and full_name:
            raise ValueError(
                "Only one of short code or full name parameter should be used."
            )
