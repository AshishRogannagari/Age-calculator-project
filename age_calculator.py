# Save this code in a file named age_calculator.py
import time
from calendar import isleap


class AgeCalculator:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def judge_leap_year(self, year):
        return isleap(year)

    def month_days(self, month, leap_year):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2 and leap_year:
            return 29
        elif month == 2 and (not leap_year):
            return 28

    def calculate_age(self):
        localtime = time.localtime(time.time())
        year = self.age
        month = year * 12 + localtime.tm_mon
        day = 0

        begin_year = localtime.tm_year - year
        end_year = begin_year + year

        # Calculate the days
        for y in range(begin_year, end_year):
            if self.judge_leap_year(y):
                day += 366
            else:
                day += 365

        leap_year = self.judge_leap_year(localtime.tm_year)
        for m in range(1, localtime.tm_mon):
            day += self.month_days(m, leap_year)

        day += localtime.tm_mday

        age_in_years = year
        age_in_months = month
        age_in_days = day

        return f"{self.name}'s age is {age_in_years} years or {age_in_months} months or {age_in_days} days."
