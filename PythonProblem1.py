# Ard van Balkom
# Problem 1, enter a positive integer and calculate the sum of all numbers between 1 and the integer entered

while True: # only run the rest of the program if the user enters an integer
    # otherwise display a message and start program again. #Now I have to figure out how to make the program stop if the user DOES enter an integer.
    try:
        i = int(input(" Please enter a positive integer: ")) # ask the user to enter a positive integer.
    except ValueError:
        print("That is not an integer, try again")
        continue 

    x = sum (range(1, i + 1)) # a formula that gives the user the sum of all numbers between 1 and the integer entered (including the entered integer, hence the +1 at the end)


    x = int(x) # make sure the output is an integer

    if i>0: # only run the calculation if the input was a positive integer
        print (" The sum of all numbers between 1 and the integer you entered is" , x) # display the sum of all numbers between 1 and the entered integer.

    else:
        print (" That is not a positive integer ") # if user did not enter a positive integer, display a message saying what went wrong.

