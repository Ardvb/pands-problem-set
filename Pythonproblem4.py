# Asking user for a positive integer. then output the successive value.
# If current value is even, then it is divided by 2. If current value is odd, it is multiplied by 3 and 1 is added. If current value is 1, the program ends.


num = int( input("Please enter a positive integer: ")) # Ask the user to input a positive integer. The input from the user is the variable 'num'.


total = 0 # Create a variable called 'total', that starts at 0.


while num != 1: # Keep running the loop until num == 1
    if num %2 == 0: # Check if 'num' is an even number by using the modulo operator. If it is, divide it by 2.
        total = int((num /2)) # Calculate the new total as an integer.
        print(total, end= " ") # Print the new total, and display it with a space between the numbers.
        num = total # When starting the loop again the new value of 'num' will be the value of 'total'.
    else:
        total = int((num * 3 +1)) # If 'num' is an odd number, multiply it by 3 and add 1.
        print(total, end= " ") # Print the new total, and display it with a space between the numbers.
        num = total # When starting the loop again the new value of 'num' will be the value of 'total'.