class Date:
    def __init__(self, month_number: int, month_name: str, year: int) -> None:
        self.month_no = month_number
        self.month_name = month_name
        self.year = year

    def format(self, format: str) -> str:
        """Accepts formats of a combination of yy, yyyy, mm, mmm."""
        return format.lower() \
            .replace("mmm", self.month_name) \
            .replace("yyyy", str(self.year)) \
            .replace("mm", self._two_digit_month_no()) \
            .replace("yy", str(self.year)[-2:])

    def month_name_hyphen_number(self) -> str:
        return self.month_name + " - " + self._two_digit_month_no()

    def _two_digit_month_no(self) -> str:
        return str(self.month_no).zfill(2)
