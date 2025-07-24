from date import Date


class TestDate:
    def test_should_format_date_correctly(self) -> None:
        date = Date(12, 2023)

        correct_results = {
            "yymm": "2312",
            "mmyy": "1223",
            "yyyymm": "202312",
            "yy mmm": "23 December",
            "mmm yyyy": "December 2023",
        }

        for format, correct_result in correct_results.items():
            assert date.format_as(format) == correct_result, format

    def test_should_format_as_month_name_hyphen_number(self) -> None:
        double_digit_date = Date(12, 2023).month_name_hyphen_number()
        assert double_digit_date == "December - 12"

        single_digit_date = Date(1, 2023).month_name_hyphen_number()
        assert single_digit_date == "January - 01"
