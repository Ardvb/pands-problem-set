# Ard van Balkom
# Problem 1, enter a positive integer and calculate the sum of all numbers between 1 and the integer entered

i = input( " Please enter an integer: " )

i = int( i )

x = sum (range(1, i + 1))

x = int( x )

print ( " The sum of all numbers between 1 and the integer you entered is" , x)

