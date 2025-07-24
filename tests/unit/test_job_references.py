import datetime

import pytest

from job_references import create_job_reference


class TestJobReference:
    def test_should_create_full_reference(self) -> None:
        assert create_job_reference("GR250601234") == "GR250601234"

        reference_from_date = create_job_reference(
            "1234", datetime.date(2025, 6, 1)
        )

        assert reference_from_date == "GR250601234"

    def test_should_set_job_number_of_date_generated_ref(self) -> None:
        deduced_reference = create_job_reference(
            reference="01", date=datetime.date(2023, 12, 1)
        )
        assert deduced_reference == "GR231200001"

        full_reference = create_job_reference(
            date=datetime.date(2023, 12, 1), reference="12345"
        )

        assert full_reference == "GR231212345"

    def test_should_error_setting_invalid_job_number(self) -> None:
        with pytest.raises(ValueError):
            create_job_reference("GR1")
            create_job_reference("0123456789")

            job_date = datetime.date(2023, 12, 1)
            create_job_reference(date=job_date, reference="")
            create_job_reference(date=job_date, reference="123456")
            create_job_reference(date=job_date, reference="123lol")
