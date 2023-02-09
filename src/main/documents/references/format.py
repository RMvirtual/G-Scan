from __future__ import annotations
import re


class ReferenceFormat:
    def __init__(self, prefix: str = None, regex_format: str = None):
        """Regex format must include prefix if one is used."""
        self.prefix = prefix
        self.regex_format = regex_format


class AbstractReference:
    def __init__(self, format: ReferenceFormat, number: str or int) -> None:
        self._format = format
        self._number = str(number)
        self._remove_prefix_from_number()

        if not self._is_number_valid():
            raise ValueError(f"Invalid number of {self._number}")

    def __str__(self) -> str:
        return self._format.prefix + self._number

    def __eq__(self, other: AbstractReference) -> bool:
        return str(self) == str(other)

    def _is_number_valid(self) -> bool:
        return bool(re.fullmatch(
            pattern=self._format.regex_format,
            string=f"{self._format.prefix}{self._number}", flags=re.IGNORECASE
        ))

    def _remove_prefix_from_number(self) -> None:
        number_has_prefix = bool(re.match(
            pattern=self._format.prefix, string=self._number,
            flags=re.IGNORECASE
        ))

        if number_has_prefix:
            self._number = re.sub(
                pattern=self._format.prefix, repl="", string=self._number,
                count=1, flags=re.IGNORECASE
            )

    def format(self) -> ReferenceFormat:
        return ReferenceFormat(self._format.prefix, self._format.regex_format)


class JobReference(AbstractReference):
    def __init__(self, number: str or int) -> None:
        super().__init__(
            number=number,
            format=ReferenceFormat(prefix="GR", regex_format=r"GR\d{9}")
        )
