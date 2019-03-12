# This program takes a user input string and outputs every second word.
# Finally figured out how to remove every second word!

sentence = str(input("Please enter a sentence: "))

wordlist = sentence.split()
length = len(wordlist)
half = len(wordlist) /2
x = 1


while length > half:
    wordlist.pop(x)
    print(wordlist)
    length = len(wordlist)
    x = x + 1
print (wordlist)