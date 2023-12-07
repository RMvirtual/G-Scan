from date import Date


def test_should_format_date_correctly() -> None:
    date = Date(12, "December", 2023)

    correct_results = {
        "yymm": "2312",
        "mmyy": "1223",
        "yyyymm": "202312",
        "yy mmm": "23 December",
        "mmm yyyy": "December 2023"
    }

    for format, correct_result in correct_results.items():
        assert date.format(format) == correct_result
