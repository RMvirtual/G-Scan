import datetime
import math


def create_job_reference(
    reference: str, date: datetime.date | None = None
) -> str:
    """
    GR + 9 digits. First 4 digits: yymm; last 5 digits: job no. If
    date is provided, passing the job number will overwrite from
    right to left.
    """
    reference_no = reference.strip().lower().removeprefix("gr")

    if not reference_no:
        raise ValueError("Job number cannot be empty.")

    if not reference_no.isnumeric():
        raise ValueError(f"Job number must be numeric. Received {reference}.")

    if date is not None:
        if len(reference_no) > 5:
            raise ValueError(
                "Should not pass both date and suffix reference number "
                f"greater than 5 characters. Received {date} and {reference}."
            )

        padded_zeroes = "0" * (5 - len(reference_no))
        job_number = padded_zeroes + reference_no

    else:
        if len(reference_no) != 9:
            raise ValueError(
                "Job number must be full 9 digits if a date is not "
                f"provided to prefix from. Received {reference}."
            )

        current_century = math.floor(datetime.date.today().year / 100)

        date = datetime.date(
            int(f"{current_century}{reference_no[0:2]}"),
            int(reference_no[2:4]),
            1,
        )

        job_number = reference_no[-5:]

    return f"GR{date.strftime("%y%m")}{job_number}"
