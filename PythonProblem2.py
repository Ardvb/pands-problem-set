# Ard van Balkom
# Does today begin with the letter T?

#First we have to import the module 'datetime' so that our python program can determine what date and time it is.
import datetime

from datetime import date

#Since we start counting at 0, Tuesday is day 1 and Thursday is day 3. 
#Check if today is Tuesday or Thursday.

if date.today().weekday() == 1 or date.today().weekday() == 3: 
    print ( "Yes, today begins with a T" )

#If it turned out not to be Tuesday or Thursday, then we display the following message:
else:
    print ( "No, today doesn't begin with a T" )


