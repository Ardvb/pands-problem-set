#This is a program that prints all numbers between 1000 and 10000 that are divisable by 6, but not 12.

for i in range( 1000, 10000): # Set 'i' as the variable we will use for our calculations in the range of numbers from 1000 up to 10000.
    if (( i%6 ) == 0 and ( i%12 ) != 0 ): # By using the 'if' and the 'and' statement, we only include the numbers for which both conditions are true. 
        # We use the modulo operator to calculate which numbers are divisible by 6. If the result of i%6 is 0, that means the number can be divided by 6.
        # By using the != operator we can then exclude all numbers that are divisible by 12.
        print( i ) # print the numbers in the set range, that are divisible by 6, but not by 12.
    