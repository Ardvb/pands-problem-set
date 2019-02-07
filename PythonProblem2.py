# Ard van Balkom
# Does today begin with the letter T?

import datetime

from datetime import date

if date.today().weekday() == 1 or date.today().weekday() == 3: 
    print ("Yes, today begins with a T")

else:
    print ("No, today doesn't begin with a T")


