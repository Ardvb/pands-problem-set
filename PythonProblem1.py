# Ard van Balkom, 7-2-19
# Problem 1. Enter a positive integer and calculate the sum of all numbers between 1 and the integer entered.

# The code to check if user enters an integer, using 'try' and 'except' is adapted from: https://stackoverflow.com/questions/23326099/how-can-i-limit-the-user-input-to-only-integers-in-python

while True: # Run a while loop that will run indefinitely.
    try: # Test the next block of code for errors
        i = int(input(" Please enter a positive integer: ")) # Ask the user to enter a positive integer.
    except ValueError:  # Don't run the rest of the program if the user makes a ValueError (enters a non-integer), instead run the following print command.
        print(" That is not an integer, try again")
        continue # Return to the beginning of the loop, so user can try again to enter an integer.
# Used page 82 of http://spronck.net/pythonbook/pythonbook.pdf to learn about the infinite while loop.
    x = sum (range(1, i + 1)) # Calculate the sum of all numbers betweem 1, and the integer entered (including the entered integer, hence the +1 at the end).

    if i>0: # Only run the calculation if the input was a positive integer
        print (" The sum of all numbers between 1 and the integer you entered is" , x) # Display the sum of all numbers between 1 and the entered integer.
        break # End the indefinite while loop and the program.
    else: 
        print (" That is not a positive integer, try again ") # If user entered a negative number, display a message asking user to try again.
        
# I worked through chapters 1 till 12 from http://spronck.net/pythonbook/pythonbook.pdf and learned about things such as 'break' and 'continue' (page 74).