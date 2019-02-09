# Ard van Balkom
# Problem 1, enter a positive integer and calculate the sum of all numbers between 1 and the integer entered

i = input( " Please enter a positive integer: " )

i = int( i )

x = sum (range(1, i + 1))

x = int( x )

if i>0:
    print ( " The sum of all numbers between 1 and the integer you entered is" , x)
else:
    print ( " That is not a positive integer ")

