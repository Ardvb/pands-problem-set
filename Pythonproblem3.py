# Ard van Balkom, 9-2-19
# This is a program that prints all numbers between 1000 and 10000 that are divisable by 6, but not 12.

for i in range(1000, 10000): # All numbers between 1000 and 10000 are used for the following if statement.
    if ((i%6) == 0 and (i%12) != 0 ): # By using the 'if' and the 'and' statement, only numbers for which both conditions are true are included. 
        # Using the modulo operator % to calculate which numbers are divisible by 6. If the result of i%6 is 0, that means the number can be divided by 6.
        # By using the != operator we can then exclude all numbers that are divisible by 12.
        print(i, end= " ") # Print the numbers in the set range, that are divisible by 6, but not by 12. 
        # Used the 'end' function to make it all fit on the screen, with a space between each number.

# I used page 18 of http://spronck.net/pythonbook/pythonbook.pdf to learn about the modulo operator. 
# I used the same book to learn about the 'for' loop using a range of numbers on page 73.   