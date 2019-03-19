# Ask user for a positive integer and tell user if it is a prime number.
# A prime number is a number that can only be divided by itself and 1. This program will check every number from 1 up to and including the number entered by the user.
# If the number entered is divisible by more than 2 other numbers, that means it is not a prime number.

num = int( input("enter a positive integer: ")) # Ask user to enter an integer. This input will be 'num'.

count = 0 # This variable starts at 0 and will be used to count up and check every number up to the user input 'num'.
total = 0 # This variable will be used to count the times the input 'num' can be divided by the variable 'count'. 


while count <= num: # This loop will keep going until it reaches the number entered by the user( or until 'total' >2).
        count += 1 # The count is now 1, and will increase with 1 every time the loop is started.
        if num % count == 0: 
                total += 1 # If 'num' is divisible by 'count', 1 will be added to the total.
if total > 2: # If 'total' reaches 3, this means 'num' is divisible by at least 3 numbers, and so it is not a prime number.
        # The loop will end and a message "this is not a prime number" will be displayed.
        print(" This is not a prime number ")
else:
        print(" This is a prime number ")
# If the loop is completed until it reaches 'num', with a 'total' of 2 or lower, this means the number entered is not divisible by any numbers, other than 1 or itself. 
# Therefore we can display "this is a prime number".
 


