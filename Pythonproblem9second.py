# This program reads a textfile of the user's choice and displays every second line.

text = input("Please enter the filename of the textfile you would like to open: ") # Let the user input a textfile he or she would like to open

with open(text, "r") as f: # From now on the file that the user has opened and is read by the program, will be called 'f'.
    n = 0 # n will be used as a count, to count all the lines in the textfile.
    for line in f: # This is going to be a loop that will read every line in the textfile 'f' one by one.
        n += 1 # Increases the count by 1 every time the loop is repeated. 
        if n%2 == 0: # Using the module operator, only even lines are included (eg. second, fourth, etc.)
            print(line) # Prints all even lines from the textfile the user has opened.


