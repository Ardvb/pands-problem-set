# Ard van Balkom
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

    count = 0 # This variable will be used as a count for the amount of times the answer will be approximated.
    guess = 1.0 # The first guess is set as 1.0. This will change while running the loop, and will get closer and closer to the answer.

    while count <= 5: # Run the loop 5 times, after some trial and error this seems a good amount to get a close enough approximation.
        guess = 0.5*(guess+number/guess) # Start with guess = 1.0, so if the user entered 64, the first result would be 0.5*(1+64/1)=32.5. 32.5 will then become the new guess.
    # Every time the loop is ran, the guess will get closer to the answer.
        count += 1                      

    print("The square root of", number, "is approximately", round(guess,1)) # Display the final guess and round to 1 decimal
    break # The program ends after the user enters a floating point number and the square root is displayed
# Figured out most it myself, but took a bit of inspiration of: https://stackoverflow.com/questions/28036087/better-way-to-approximate-the-square-root-using-exhaustive-enumeration





#Below is my old solution. However, I got inspired after watching the video in week 8 about approximating the squareroot, and changed it.

    #sqroot = number**(0.5) # Calculate the square root by raising the variable 'number' to the power of 0.5

    #print("The square root of", number, "is approximately", round(sqroot, 1)) # Print the approximated square root and round to 1 decimal
    #break # The program ends after the user enters a floating point number and the square root is displayed