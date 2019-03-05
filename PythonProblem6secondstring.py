# This program takes a user input string and outputs every second word.
# first attempt

sentence = str(input("Please enter a sentence: "))

wordlist = sentence.split()

del wordlist[2]
del wordlist[4]

print(wordlist)