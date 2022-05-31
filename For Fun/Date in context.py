"""Put date function into possible real-life context
30/05/2022"""

from datetime import datetime, timedelta

birthday = input("What is your birthday? ")

birthday_date = datetime.strptime(birthday, "%d/%m/%Y")

# Birthday date
print(f"Your birthday is {str(birthday_date)} ")

# Day before Bday
one_day = timedelta(days=1)
eve = birthday_date - one_day
print(f"The day before your birthday is: {str(eve)}")


