# Ard van Balkom
# Does today begin with the letter T?


import datetime # First we have to import the module 'datetime' and 'date' so that our python program can determine what date and time it is.

from datetime import date


if date.today().weekday() == 1 or date.today().weekday() == 3: # By using the weekday function (where Monday is 0 and Sunday 6, our program can determine what day of the week it is.
    # Since we start counting at 0, Tuesday is day 1 and Thursday is day 3. Check if today is Tuesday or Thursday.
    print ( "Yes, today begins with a T" ) # Display a message saying today starts with a T


else: # If it turned out not to be Tuesday or Thursday, then we display the following message:
    print ("No, today doesn't begin with a T") # Display a message saying today doesn't begin with a T