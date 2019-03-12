#This program will output today's date and time.

import datetime #this module imports the current date and time into this python program

from datetime import date
from datetime import time
from datetime import datetime


if date.today().weekday() == 0: #assigning the names of the days to every weekday. Trying to figure out an easier and prettier way to do this.....
    day = "Monday"
elif date.today().weekday() == 1:
    day = "Tuesday"
elif date.today().weekday() == 2:
    day = "Wednesday"
elif date.today().weekday() == 3:
    day = "Thursday"
elif date.today().weekday() == 4:
    day = "Friday"
elif date.today().weekday() == 5:
    day = "Saturday"
elif date.today().weekday() == 6:
    day = "Sunday"

print(date.today())