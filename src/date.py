import datetime


MONTHS = {
    1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 
    7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 
    12: "December"
}


class Date:
    def __init__(self, month_no: int, year: int) -> None:
        self.month_no = month_no
        self.year = year

    def format_as(self, format: str) -> str:
        """Accepts formats of a combination of yy, yyyy, mm, mmm."""

        return (
            format.lower()
            .replace("mmm", MONTHS[self.month_no])
            .replace("yyyy", str(self.year))
            .replace("mm", str(self.month_no).zfill(2))
            .replace("yy", str(self.year)[-2:])
        )
    
    @property
    def month_name(self) -> str:
        return MONTHS[self.month_no]

    def month_name_hyphen_number(self) -> str:
        return f"{self.month_name} - {str(self.month_no).zfill(2)}"


class Calendar:
    def date(self, month: int, year: int) -> Date:
        return self.months(year)[month - 1]

    def date_from_month_name_and_number(
            self, month_name_and_number: str, year) -> Date:
        month_names_and_nos = self.months_as_xxx_mm_to_number()
        month_no = month_names_and_nos[month_name_and_number]

        return Date(month_no, year)

    def months(self, year: int) -> list[Date]:
        return list(map(
            lambda month_no: Date(month_no, year), MONTHS.keys()))

    def month_name_from_number(self, number: int) -> str:
        return self.months_as_strings()[number-1]

    def month_names_and_numbers(self) -> list[str]:
        return list(map(
            Date.month_name_hyphen_number,
            self.months(self.current_year)
        ))

    def months_as_xxx_mm_to_number(self) -> dict[str, int]:
        result = {}
        month_no = 1

        for formatted_date in self.month_names_and_numbers():
            result[formatted_date] = month_no
            month_no += 1

        return result

    def months_as_strings(self) -> list[str]:
        return list(map(
            lambda m: m.month_name, self.months(self.current_year)))

    def last_two_years(self) -> tuple[int, int]:
        return self.current_year, self.current_year - 1
    
    @property
    def current_month(self):
        return Date(
            int(datetime.datetime.now().strftime("%m")), 
            self.current_year
        )

    @property
    def current_year(self) -> int:
        return int(datetime.datetime.now().strftime("%Y"))
    