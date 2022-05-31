"""Testing out date import
30/05/2022"""


from datetime import datetime, timedelta

# Current day
current_date = datetime.now()
print(f"Today is: {str(current_date)}\n")

# Breaking down the date
print(f"The day is: {current_date.day}")
print(f"The Month is: {current_date.month}")
print(f"The Year is: {current_date.year}")
print(f"The Hour is: {current_date.hour}")
print(f"The Minute is: {current_date.minute}")
print(f"The Second is: {current_date.second}\n")


# Yesterday
one_day = timedelta(days=1)
yesterday = current_date - one_day
print(f"Yesterday was: {str(yesterday)}\n")

# Week
one_week = timedelta(weeks=1)
last_week = current_date - one_week
print(f"Last week was: {last_week}\n")




