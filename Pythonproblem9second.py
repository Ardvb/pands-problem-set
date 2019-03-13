n = input("Please enter the filename of the textfile you would like to open: ") #Let the user input a textfile he or she would like to open

text = open(n, 'r') #open the textfile 'Gedicht' from the same folder as this program

for line in text:
    print(line, end=" ") #prints all lines from the file the user has opened. I have to figure out next how to display only the second line


