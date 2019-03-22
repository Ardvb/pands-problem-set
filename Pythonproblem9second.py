# Ard van Balkom, 13-3-19
# Problem 9. This program reads in a text ﬁle and outputs every second line. The program will take the ﬁlename from an argument on the command line.

import sys # Import system-specific parameters and functions, so we can use sys.argv

filename = sys.argv[0] # This will get the last argument on the command line. ref: https://stackoverflow.com/questions/7033987/python-get-files-from-command-line

with open(filename, "r") as f: # From now on the file that the user has opened and is read by the program, will be called 'f'.
    # Adapted from video material week 7 by Ian McLoughlin: https://web.microsoftstream.com/video/72484dfc-1b50-4223-8039-bd6a69cab573
    n = 0 # n will be used as a count, to count all the lines in the textfile.
    for line in f: # This is going to be a loop that will read every line in the textfile 'f' one by one.
        n += 1 # Increases the count by 1 every time the loop is repeated. 
        if n%2 == 0: # Using the module operator, only even lines are included (eg. second, fourth, etc.)
            print(line) # Prints all even lines from the textfile the user has opened.


# At first I had no clue what "The program should take the ﬁlename from an argument on the command line" meant. 
# At first, I thought I had to ask the user for an input. But after rereading the problem for at least 10 times, and googling it, I figured out what had to be done.
# Implementing it was easier, although I had to use a lot of code found online (the most I had to for any of the 10 problems). 
# I used https://stackoverflow.com/questions/7033987/python-get-files-from-command-line and https://www.pythonforbeginners.com/system/python-sys-argv
# to learn how to use sys.argv in order to take the filename from an argument on the command line.