# Ard van Balkom, 7-2-19
# Problem 2. Display if today begins with the letter T.


import datetime # Import the module 'datetime' and 'date', so that our python program can determine what date and time it is.

if datetime.date.today().weekday() == 1 or datetime.date.today().weekday() == 3: # Use the weekday function (Every day has a number (Monday is 0, Tuesday is 1 etc.).
    # Counting starts at 0, so Tuesday is day 1 and Thursday is day 3. Check if today is either Tuesday or Thursday.
    print ( "Yes, today begins with a T" ) # Display a message saying today starts with a T.

else: # If today is not day 1 or day 3:
    print ("No, today doesn't begin with a T") # Display a message saying today doesn't begin with a T.

# I came across the option of using a dictionary of all days of the week, in the python tutorial.
# You turn the numbers for the days of the week, 0-6, into a string with the actual name of the weekday.
# Then you can check if the first letter [0] is a T by using an 'if', 'else' statement.
# I considered using it, and would have if we had to use the names of the days of the week for other things as well. However, since all we had to do is display 
# if today started with a T or not, I decided to take the quicker option.