from database import JSONDatabase


class AppConfiguration:
    def __init__(self, database: JSONDatabase, username: str) -> None:
        self.database = database

        self.settings = (
            database.create_user(username) if not database.user_exists(username)
            else database.load_user_settings(username)
        )

        self.scan_directory = self.settings.scan_dir
        self.dest_directory = self.settings.dest_dir
        self.department = self.settings.department
        self.document_type = self.settings.document_type

        self.departments = database.all_departments()

    def set_department(
            self, short_code: str = None, full_name: str = None) -> None:
        if short_code:
            self.department = self.database.department(short_code=short_code)

        elif full_name:
            self.department = self.database.department(full_name=full_name)

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
