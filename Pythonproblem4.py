# Ard van Balkom, 9-2-19
# Problem 4. Asking user for a positive integer. then output the successive value.
# If current value is even, then it is divided by 2. If current value is odd, it is multiplied by 3 and 1 is added. If current value is 1, the program ends.

while True: # Run a while loop that will run indefinitely.
    try: # Test the next block of code for errors
        num = int( input("Please enter a positive integer: ")) # Ask the user to input a positive integer. The input from the user is the variable 'num'.
    except ValueError: # Don't run the rest of the program if the user makes a ValueError (enters a non-integer), instead run the following print command.
        print("That is not an integer, try again") # If the user enters a non numeric input, a message will show and program runs again.
        continue # Return to the beginning of the loop, so user can try again to enter an integer.
    if num <= 0: # If the user enters a number that is 0 or lower than 0, a message will show and program runs again.
        print("That is not a positive integer, try again") 
        continue  # Return to the beginning of the loop, so user can try again to enter an integer.
        # Adapted from: https://stackoverflow.com/questions/23326099/how-can-i-limit-the-user-input-to-only-integers-in-python
        # Used page 82 of http://spronck.net/pythonbook/pythonbook.pdf for the infinite while loop.
    total = 0 # Create a variable 'total', starting at 0, that will be calculated after user enters 'num' and will be printed.


    while num != 1 and num >= 0: # Keep running the loop until num == 1
        if num %2 == 0: # Check if 'num' is an even number by using the modulo operator. If it is, divide it by 2.
            total = int((num /2)) # Calculate the new total as an integer.
            print(total, end= " ") # Print the new total, and display it with a space between the numbers.
            num = total # When starting the loop again the new value of 'num' will be the value of 'total'.
        else:
            total = int((num * 3 +1)) # If 'num' is an odd number, multiply it by 3 and add 1.
            print(total, end= " ") # Print the new total, and display it with a space between the numbers.
            num = total # When starting the loop again the new value of 'num' will be the value of 'total'.
    break # The program ends after ending this the while loop.