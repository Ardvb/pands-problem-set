# Ard van Balkom
# Problem 1, enter a positive integer and calculate the sum of all numbers between 1 and the integer entered

# ask the user to enter a positive integer
i = input( " Please enter a positive integer: " )

# make sure the input is an integer.
i = int( i )

# a formula that gives the user the sum of all numbers between 1 and the integer entered (including the entered integer, hence the +1 at the end)
x = sum (range(1, i + 1))

# make sure the output is an integer
x = int( x )

# only run the calculation if the input was a positive integer
if i>0:
    print ( " The sum of all numbers between 1 and the integer you entered is" , x)
# if user did not enter a positive integer, make sure he knows so he can try again and enter a positive integer.
else:
    print ( " That is not a positive integer ")

