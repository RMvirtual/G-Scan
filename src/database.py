from __future__ import annotations

import dataclasses
import json
from pathlib import Path

from departments import Department
from documents import DocumentType


@dataclasses.dataclass
class UserSettings:
    username: str = ""
    output_dir: str = ""
    department: Department | None = None
    document: DocumentType | None = None

    def update(self, settings: UserSettings) -> None:
        self.username = settings.username
        self.output_dir = settings.output_dir
        self.department = settings.department
        self.document = settings.document


JSONFormat = dict[str, dict[str, str | list[str]]]


@dataclasses.dataclass
class JSONDatabaseFiles:
    departments: Path
    document_types: Path
    user_settings: Path


class JSONDatabase:
    def __init__(self, files: JSONDatabaseFiles) -> None:
        self.files = files

    def department(
        self, short_code: str = None, full_name: str = None
    ) -> Department:
        if not (short_code or full_name):
            raise ValueError("Department parameter not selected.")

        predicate = lambda d: (
            d.short_code == short_code
            if short_code
            else lambda d: d.full_name == full_name
        )

        for department in self.all_departments():
            if predicate(department):
                return department

        raise ValueError(f"Invalid department: {short_code or full_name}")

    def all_departments(self) -> list[Department]:
        with open(self.files.departments) as file_stream:
            json_contents: dict = json.load(file_stream)

        documents = self.all_documents()
        result = []

        for short_code, values in json_contents.items():
            matching_docs = list(
                filter(
                    lambda d: d.short_code in values["document_types"],
                    documents,
                )
            )

            result.append(
                Department(
                    short_code,
                    values["full_name"],
                    values["short_name"],
                    matching_docs,
                )
            )

        return result

    def document(
        self, short_code: str = None, full_name: str = None
    ) -> DocumentType:
        if not (short_code or full_name):
            raise ValueError("Document type parameter not selected.")

        predicate = lambda d: (
            d.short_code == short_code
            if short_code
            else lambda d: d.full_name == full_name
        )

        for doc in self.all_documents():
            if predicate(doc):
                return doc

        raise ValueError(f"Invalid document type: {short_code or full_name}")

    def all_documents(self) -> list[DocumentType]:
        with open(self.files.document_types) as file_stream:
            json_contents: JSONFormat = json.load(file_stream)

        return [
            DocumentType(
                short_code, values["full_name"], values["analysis_code"]
            )
            for short_code, values in json_contents.items()
        ]

    def load_user_settings(self, username: str) -> UserSettings:
        contents = self.user_settings_json()

        if username not in contents:
            raise ValueError(f"Could not find settings for user {username}.")

        all_settings = self._deserialise_user_settings(
            {username: contents[username]}
        )

        return all_settings[0]

    def user_exists(self, username: str) -> bool:
        return username in self.user_settings_json()

    def create_user(self, username: str) -> UserSettings:
        contents = self.user_settings_json()

        if username in contents:
            raise ValueError(f"User {username} already exists.")

        result = self._deserialise_individual_user_settings(
            username, contents["GSCAN_DEFAULT"]
        )

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
                "output_directory": settings.output_dir,
                "department": settings.department.short_code,
                "document_type": settings.document.short_code,
            }
        }

    def _deserialise_user_settings(
        self, settings: JSONFormat
    ) -> list[UserSettings]:
        return [
            self._deserialise_individual_user_settings(username, user_settings)
            for username, user_settings in settings.items()
        ]

    def _deserialise_individual_user_settings(
        self, username: str, values: dict[str, str | list[str]]
    ) -> UserSettings:
        return UserSettings(
            username,
            values["output_directory"],
            self.department(short_code=values["department"]),
            self.document(short_code=values["document_type"]),
        )

    @staticmethod
    def validate_option_selected(
        short_code: str | None, full_name: str | None
    ) -> Department:
        if not (short_code or full_name):
            raise ValueError("Department parameter not selected.")
