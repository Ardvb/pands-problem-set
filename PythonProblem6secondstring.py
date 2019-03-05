# This program takes a user input string and outputs every second word.
# first attempt. Can't figure out how to program it so it takes away every other word.

sentence = str(input("Please enter a sentence: "))

wordlist = sentence.split()

del wordlist[2]
del wordlist[4]

print(wordlist)