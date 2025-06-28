import pytest

from date import Date
from job_references import JobReference


class TestJobReference:
    def test_should_create_full_reference(self) -> None:
        assert JobReference(reference="GR250601234") == "GR250601234"

        assert (
            JobReference(date=Date(6, 2025), reference="1234") == "GR250601234"
        )

    def test_should_set_job_number_of_date_generated_ref(self) -> None:
        deduced_reference = JobReference(date=Date(12, 2023), reference="01")
        assert deduced_reference == "GR231200001"

        full_reference = JobReference(date=Date(12, 2023), reference="12345")
        assert full_reference == "GR231212345"

    def test_should_error_setting_invalid_job_number(self) -> None:
        with pytest.raises(ValueError):
            JobReference("GR1")
            JobReference("0123456789")
            JobReference(date=Date(12, 2023), reference="")
            JobReference(date=Date(12, 2023), reference="123456")
            JobReference(date=Date(12, 2023), reference="123lol")
