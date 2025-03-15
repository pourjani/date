class Date:
    def __init__(self, day, month, year):
        self.validate_date(day, month, year)
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    #a year is a leap year if it is divisible by 4, except for end-of-century years, which must be divisible by 400.
    #This means that the year 2000 was a leap year, while the year 1900 was not
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def get_days_in_month(month, year):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            return 29 if Date.is_leap_year(year) else 28
        else:
            raise ValueError("Invalid month")

    def add_days(self, days):
        while days != 0:
            if days > 0:
                days_in_month = self.get_days_in_month(self.month, self.year)
                if self.day + days > days_in_month:
                    days -= (days_in_month - self.day + 1)
                    self.day = 1
                    if self.month == 12:
                        self.month = 1
                        self.year += 1
                    else:
                        self.month += 1
                else:
                    self.day += days
                    days = 0
            else:
                if self.day + days < 1:
                    if self.month == 1:
                        self.month = 12
                        self.year -= 1
                    else:
                        self.month -= 1
                    days_in_month = self.get_days_in_month(self.month, self.year)
                    days += self.day
                    self.day = days_in_month
                else:
                    self.day += days
                    days = 0

    def compare_to(self, other):
        if self.year != other.year:
            return self.year - other.year
        if self.month != other.month:
            return self.month - other.month
        return self.day - other.day

    def equals(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day

    def get_days_from(self, other):
        days_count = 0
        temp_date = Date(self.day, self.month, self.year)
        while not temp_date.equals(other):
            if temp_date.compare_to(other) > 0:
                temp_date.add_days(-1)
                days_count -= 1
            else:
                temp_date.add_days(1)
                days_count += 1
        return days_count

    @staticmethod
    def validate_date(day, month, year):
        if not (1 <= month <= 12):
            raise ValueError("Invalid month")
        if not (1 <= day <= Date.get_days_in_month(month, year)):
            raise ValueError("Invalid day")
        if year <= 0:
            raise ValueError("Invalid year")

# Example usage:
try:
    date1 = Date(1, 1, 2024)
    date2 = Date(1, 1, 2025)
    date1.add_days(15)  # Moves date1 to January 16, 2024
    print(f"Days from date1 to date2: {date1.get_days_from(date2)}")
    date1.add_days(-date1.get_days_from(date2))  # Adjusts date1 to match date2
    print(f"Date1 equals date2: {date1.equals(date2)}")
except ValueError as e:
    print(e)
