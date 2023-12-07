class Date(object):
    def __init__(self, month_number: int, month_name: str, year: int):
        self._month_number = month_number
        self._month_name = month_name
        self._year = year

    def month_number(self) -> int:
        return self._month_number

    def mm(self) -> str:
        return str(self._month_number).zfill(2)

    def month_name(self) -> str:
        return self._month_name

    def year(self) -> int:
        return self._year

    def yy(self) -> str:
        return str(self._year)[-2:]

    def yymm(self) -> str:
        return self.yy() + self.mm()

    def month_name_hyphen_number(self) -> str:
        month_name = self.month_name()
        month_number = self.mm()
        
        return month_name + " - " + month_number
