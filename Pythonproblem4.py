# Asking user for a positive integer. then output the successive value.
# If current value is even, then it is divided by 2. If current value is odd, it is multiplied by 3 and 1 is added. If current value is 1, the program ends.

# Ask the user to input a positive integer. The input from the user is the variable 'num'.
num = int( input( "Please enter a positive integer: " ))

# Create a variable called 'total'.
total = 0

# Stop running the loop once the value of num is 1
while num != 1:
# Check if 'num' is an even number by using the modulo operator. If it is, divide it by 2.
    if num %2 == 0:
        total = int(( num /2 )) # calculate the new total as an integer.
        print( total, end= " " ) # Print the new total, and display it with a space between the numbers.
        num = total # When starting the loop again the new value of 'num' will be the value of 'total'.
    else:
        total = int(( num * 3 +1 )) # If 'num' is an odd number, multiply it by 3 and add 1.
        print( total, end= " " )
        num = total # When starting the loop again the new value of 'num' will be the value of 'total'.