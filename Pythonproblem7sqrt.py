# This program takes a positive floating point number and returns an approximation of it's square root

while True:
    try:
        number = float(input("Please enter a positive floating point number: ")) # Get the user the input a floating point number
    except ValueError:
        print("That is not a floating point number, try again") # If user enters a non numeric value, an error message will appear, and the program will start again.
        continue   
    if number <= 0:
        print("That is not a positive number, please try again") # check if input is not 0 or a negative number. If it is, show a message and run program again.
        continue
 # Adapted from: https://stackoverflow.com/questions/23326099/how-can-i-limit-the-user-input-to-only-integers-in-python
    sqroot = number**(0.5) # Calculate the square root by raising the variable 'number' to the power of 0.5

    print("The square root of", number, "is approximately", round(sqroot, 1)) # Print the approximated square root and round to 1 decimal
    break # The program ends after the user enters a floating point number and the square root is displayed