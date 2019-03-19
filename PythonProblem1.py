# Ard van Balkom
# Problem 1, enter a positive integer and calculate the sum of all numbers between 1 and the integer entered

while True: # only run the rest of the program if the user enters an integer
    # otherwise display a message and start program again.
    try:
        i = int(input(" Please enter a positive integer: ")) # ask the user to enter a positive integer.
    except ValueError:
        print(" That is not an integer, try again") #show message if user inputs something other than an integer.
        continue #return to the beginning of the loop, so user can try again to enter an integer.

    x = sum (range(1, i + 1)) # a formula that gives the user the sum of all numbers between 1 and the integer entered (including the entered integer, hence the +1 at the end)

    if i>0: # only run the calculation if the input was a positive integer
        print (" The sum of all numbers between 1 and the integer you entered is" , x) # display the sum of all numbers between 1 and the entered integer.
        break
    else: 
        print (" That is not a positive integer, try again ") # if user did not enter a positive integer, display a message saying what went wrong.
        
