import calendar
from datetime import datetime

today = datetime.now()

print(today.day)
current_week = today.isocalendar()[1]
print(current_week)

current_month = today.month
print(current_month)

current_year = today.year
print(current_year)