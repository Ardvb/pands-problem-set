#This program reads a textfile of the user's choice and displays every second line.

text = input("Please enter the filename of the textfile you would like to open: ") #Let the user input a textfile he or she would like to open

with open(text, "r") as f: #from now on the file that the user has opened and is read by the program, will be called 'f'.
    n = 0 #I will use variable n as a count, to count all the lines in the textfile.
    for line in f:
        n += 1 #increases the count by 1 every time the loop is repeated. 
        if n%2 == 0: #using the module operator, I only include the even lines (eg. second, fourth, etc.)
            print(line) #prints all even lines from the textfile the user has opened.


