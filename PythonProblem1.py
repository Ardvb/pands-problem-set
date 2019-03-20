# Ard van Balkom
# Problem 1, enter a positive integer and calculate the sum of all numbers between 1 and the integer entered

while True: # Only run the rest of the program if the user enters an integer
    # Otherwise display a message and start program again.
    # Adapted from: https://stackoverflow.com/questions/23326099/how-can-i-limit-the-user-input-to-only-integers-in-python
    try:
        i = int(input(" Please enter a positive integer: ")) # Ask the user to enter a positive integer.
    except ValueError:
        print(" That is not an integer, try again") # Show message if user inputs something other than an integer.
        continue # Return to the beginning of the loop, so user can try again to enter an integer.

    x = sum (range(1, i + 1)) # A formula that gives the user the sum of all numbers between 1 and the integer entered (including the entered integer, hence the +1 at the end)

    if i>0: # Only run the calculation if the input was a positive integer
        print (" The sum of all numbers between 1 and the integer you entered is" , x) # Display the sum of all numbers between 1 and the entered integer.
        break
    else: 
        print (" That is not a positive integer, try again ") # If user did not enter a positive integer, display a message saying what went wrong.
        
