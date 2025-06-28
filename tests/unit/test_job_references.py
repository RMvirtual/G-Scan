import pytest

from date import Date
from job_references import create_job_reference


class TestJobReference:
    def test_should_create_full_reference(self) -> None:
        assert create_job_reference("GR250601234") == "GR250601234"

        assert (
            create_job_reference("1234", date=Date(6, 2025)) == "GR250601234"
        )

    def test_should_set_job_number_of_date_generated_ref(self) -> None:
        deduced_reference = create_job_reference(
            reference="01", date=Date(12, 2023)
        )
        assert deduced_reference == "GR231200001"

        full_reference = create_job_reference(
            date=Date(12, 2023), reference="12345"
        )

        assert full_reference == "GR231212345"

    def test_should_error_setting_invalid_job_number(self) -> None:
        with pytest.raises(ValueError):
            create_job_reference("GR1")
            create_job_reference("0123456789")
            create_job_reference(date=Date(12, 2023), reference="")
            create_job_reference(date=Date(12, 2023), reference="123456")
            create_job_reference(date=Date(12, 2023), reference="123lol")
