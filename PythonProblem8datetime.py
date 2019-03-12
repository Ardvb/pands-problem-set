#This program will output today's date and time.

import datetime #this module imports the current date and time into this python program

from datetime import date
from datetime import time
from datetime import datetime

datum = datetime.now()

if date.today().weekday() == 0: #assigning the names of the days to every weekday. Trying to figure out an easier and prettier way to do this.....
    weekday = "Monday"
elif date.today().weekday() == 1:
    weekday = "Tuesday"
elif date.today().weekday() == 2:
    weekday = "Wednesday"
elif date.today().weekday() == 3:
    weekdday = "Thursday"
elif date.today().weekday() == 4:
    weekdday = "Friday"
elif date.today().weekday() == 5:
    weekdday = "Saturday"
elif date.today().weekday() == 6:
    weekdday = "Sunday"


if datum.month == 1:
    month = "January"
elif datum.month == 2:
    month = "February"
elif datum.month == 3:
    month = "March"
elif datum.month == 4:
    month = "April"
elif datum.month == 5:
    month = "May"
elif datum.month == 6:
    month = "June"
elif datum.month == 7:
    month = "July"
elif datum.month == 8:
    month = "August"
elif datum.month == 9:
    month = "September"
elif datum.month == 10:
    month = "October"
elif datum.month == 11:
    month = "November"
elif datum.month == 12:
    month = "December"

if datum.day >= 3: #it works, but doesnt look pretty at all. Will have to figure out another way of doing it.
    day = str((datum.day, "th"))
elif datum.day == 2:
    day = str((datum.day, "nd"))
else:
    day = str((datum.day, "st"))

print(weekday, month, day)


