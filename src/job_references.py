from __future__ import annotations

from date import Calendar, Date


class JobReference:
    def __init__(self, reference: str, date: Date | None = None) -> None:
        """
        GR + 9 digits. First 4 digits: yymm; last 5 digits: job no. If
        date is provided, passing the job number will overwrite from
        right to left.
        """
        reference_no = reference.strip().lower().removeprefix("gr")

        if not reference_no.isnumeric():
            raise ValueError(
                f"Job number must be numeric. Received {reference}."
            )

        if date is None:
            if len(reference_no) != 9:
                raise ValueError(
                    "Job number must be full 9 digits if a date is not "
                    f"provided to prefix from. Received {reference}."
                )

            self._date = Calendar().date(
                int(reference_no[2:4]), int(reference_no[0:2])
            )

            self._job_number = reference_no[-5:]

        else:
            if len(reference_no) > 5:
                raise ValueError(
                    "Should not pass both date and suffix reference number "
                    "greater than 5 characters. "
                    f"Received {date} and {reference}"
                )

            self._date = date
            padded_zeroes = "0" * (5 - len(reference_no))
            self._job_number = padded_zeroes + reference_no

    def __str__(self) -> str:
        return f"GR{self._date.format_as("yymm")}{self._job_number}"

    def __eq__(self, value: JobReference | str) -> bool:
        if isinstance(value, str):
            return str(self) == value

        elif isinstance(value, JobReference):
            return str(self) == str(value)

        else:
            raise TypeError(
                f"Cannot compare JobReference and type {type(value)}"
            )

    @property
    def job_number(self) -> str:
        return self._job_number
