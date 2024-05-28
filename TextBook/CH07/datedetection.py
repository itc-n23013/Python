import re
from datetime import datetime

date_pattern = re.compile(r'(?P<day>0[1-9]|[12][0-9]|3[01])/(?P<month>0[1-9]|1[0-2])/(?P<year>[12][0-9]{3})')

def is_valid_date(day, month, year):
    try:
        datetime(int(year), int(month), int(day))
        return True
    except ValueError:
        return False

def find_dates(text):
    matches = date_pattern.finditer(text)
    for match in matches:
        day = match.group('day')
        month = match.group('month')
        year = match.group('year')
        if is_valid_date(day, month, year):
            print(f"{day}/{month}/{year}この日付は存在します:")
        else:
            print(f"{day}/{month}/{year}この日付は存在しません:")

text = "These are some dates: 29/02/2020, 31/04/2021, 15/08/2022, 31/11/2023."

find_dates(text)

