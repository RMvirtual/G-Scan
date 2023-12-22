import json

from departments import Department 
from documents import Document
from file_system import JSONDatabaseFiles
from user import UserSettings


JSONFormat = dict[str, dict[str, str|list[str]]]


class JSONDatabase:
    def __init__(self, files: JSONDatabaseFiles) -> None:
        self.files = files

    def department(
            self, short_code: str = "", full_name: str = "") -> Department:
        if not (short_code or full_name):
            raise ValueError("Department parameter not selected.")

        departments = self.all_departments()

        if full_name:
            filtered = [
                dept for dept in departments if dept.full_name == full_name]
        
            if not filtered:
                raise ValueError(f"Invalid department: {full_name}")

            return filtered[0]

        else:
            filtered = [
                dept for dept in departments if dept.short_code == short_code]

            if not filtered:
                raise ValueError(f"Invalid department: {short_code}")

            return filtered[0]

    def all_departments(self) -> list[Department]:
        with open(self.files.departments) as file_stream:
            json_contents: JSONFormat = json.load(file_stream)
        
        return [
            Department(
                short_code,
                values["full_name"],
                values["short_name"], 
                list(filter(
                    lambda doc: doc.short_code in values["document_types"], 
                    self.all_documents())
                )
            ) for short_code, values in json_contents.items()
        ]

    def document(
            self, short_code: str = None, full_name: str = None) -> Document:
        documents = self.all_documents()

        if not (short_code or full_name):
            raise ValueError("Document Type parameter not selected.")

        if full_name:
            filtered = [
                doc for doc in documents if doc.full_name == full_name]
        
            if not filtered:
                raise ValueError(f"Invalid Document Type: {full_name}")

            return filtered[0]

        else:
            filtered = [
                dept for dept in documents if dept.short_code == short_code]

            if not filtered:
                raise ValueError(f"Invalid Document Type: {short_code}")

            return filtered[0]

    def all_documents(self) -> list[Document]:
        with open(self.files.document_types) as file_stream:
            json_contents: JSONFormat = json.load(file_stream)
        
        return [
            Document(short_code, values["full_name"], values["analysis_code"])
            for short_code, values in json_contents.items()
        ]

    def load_user_settings(self, username: str) -> UserSettings:
        contents = self.user_settings_json()

        if username not in contents:
            raise ValueError(f"Could not find settings for user {username}.")

        return self._deserialise_user_settings(
            {username: contents[username]})[0]

    def user_exists(self, username: str) -> bool:
        return username in self.user_settings_json()

    def create_user(self, username: str) -> UserSettings:
        contents = self.user_settings_json()

        if username in contents:        
            raise ValueError(f"User {username} already exists.")
        
        result = self._deserialise_individual_user_settings(
            username, contents["GSCAN_DEFAULT"])

        self.save_user_settings(result)

        return result

    def save_user_settings(self, settings: UserSettings) -> None:
        json_contents = self.user_settings_json()
        json_contents.update(self._serialise_user_settings(settings))

        with open(self.files.user_settings, mode="w") as user_settings:
            user_settings.write(json.dumps(json_contents, indent=2))

    def user_settings_json(self) -> JSONFormat:
        with open(self.files.user_settings) as file_stream:
            return json.load(file_stream)

    @staticmethod
    def _serialise_user_settings(settings: UserSettings) -> JSONFormat:
        return {
            settings.username: {
                "scan_directory": settings.scan_dir,
                "dest_directory": settings.dest_dir,
                "department": settings.department.short_code,
                "document_type": settings.document_type.short_code
            }
        }

    def _deserialise_user_settings(
            self, settings: JSONFormat) -> list[UserSettings]:
        return [
            self._deserialise_individual_user_settings(username, user_settings)
            for username, user_settings in settings.items()
        ]

    def _deserialise_individual_user_settings(
            self, username: str, values: dict[str, str|list[str]]
    ) -> UserSettings:
        return UserSettings(
            username,
            values["scan_directory"],
            values["dest_directory"],
            self.department(short_code=values["department"]),
            self.document(short_code=values["document_type"])
        )
