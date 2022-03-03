class LeapYear:
    def __init__(self, year_input: int):
        self._year_input = year_input

    def is_year_input_equal_century_year(self) -> bool:
        return self._year_input % 100 == 0

    def is_century_year_equal_leap_year(self) -> bool:
        return self._year_input % 400 == 0

    def is_normal_year_equal_leap_year(self) -> bool:
        return self._year_input % 4 == 0


class CliHandler:

    def start(self):
        while True:
            try:
                year_input = int(input('Enter the year:'))
            except ValueError:
                print("Invalid input.\tTry again.")
                continue
            leap_year = LeapYear(year_input)
            if leap_year.is_century_year():
                print(leap_year.is_century_year_equal_leap_year())
                break
            else:
                print(leap_year.is_normal_year_year_leap_year())
                break


if __name__ == "__main__":
    CliHandler().start()
