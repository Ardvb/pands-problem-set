# This program takes a positive floating point number and returns an approximation of it's square root

number = float(input("Please enter a positive floating point number: ")) # Get the user the input a floating point number

sqroot = number**(0.5) # Calculate the square root by raising the variable 'number' to the power of 0.5

print("The square root of", number, "is approximately", round(sqroot, 1)) # Print the approximated square root and round to 1 decimal