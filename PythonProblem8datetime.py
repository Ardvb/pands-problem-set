# Ard van Balkom, 12-3-19
# Problem 8. This program will output today's date and time.

import datetime # This module imports the current date and time into this python program
# Took a few things (such as the datetime.now option) from https://docs.python.org/3.7/library/datetime.html#datetime.datetime
from datetime import date
from datetime import time
from datetime import datetime

datum = datetime.now() # Created variable "datum" that will represent the exact date and time when the program is ran.
year = datum.year # Created variable "year", that will represent the value of datum.year. Did the same for day, hour and minute.
day = datum.day
hour = datum.hour
minute = datum.minute
add0 = "" # Added this variable that changes to 0 if it is less than 10 minutes past the hour, to display 5 past 7, as 7:05, instead of 7:5.



if date.today().weekday() == 0: # Assigning the names of the days to every weekday. (I found the calender module on stackoverflow, but I prefer to do it this way for now.)
    weekday = "Monday" # This way I can see exactly what I am doing and I think that, as a beginner, I learn more doing it this way.
elif date.today().weekday() == 1:
    weekday = "Tuesday"
elif date.today().weekday() == 2:
    weekday = "Wednesday"
elif date.today().weekday() == 3:
    weekday = "Thursday"
elif date.today().weekday() == 4:
    weekday = "Friday"
elif date.today().weekday() == 5:
    weekday = "Saturday"
elif date.today().weekday() == 6:
    weekday = "Sunday"


if datum.month == 1: # Assigning the names of the months to each months' number. (Again choosing not to use the calender module).
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

if datum.day >= 4: # Adding the correct 'addon' to the date. If it is the 1st or the 2nd this will be different from the other dates.
    addon = "th" # Variable 'addon' will display the correct addon to the date.
elif datum.day == 2:
    addon = "nd"
elif datum.day == 3:
    addon = "rd"
else:
    addon = "st"


if hour >= 12: # Adding the correct 12-hour indication to the hours and minutes (am or pm). After 12 noon this will show 'pm', otherwise it will show 'am'.
    pmam = "pm"   
else: 
    pmam = "am"

if hour >= 13: # By subtracting 12 from all hours 13 or higher, all hours apart from 12, will be shown with 1 digit.
    hour = hour-12

if minute <10: # If it is less than 10 minutes past the hour, the variable 'add0' will become 0.
    add0 = "0"

print("Today's date and time is {}, {} {}{} {} at {}:{}{}{}".format( weekday, month, day, addon, year, hour, add0, minute, pmam )) # Print it like this: "Today's date and time is Tuesday, March 12th 2019 at 7:20pm"
# How to do the '.format' part, I learned from page 42 of http://spronck.net/pythonbook/pythonbook.pdf