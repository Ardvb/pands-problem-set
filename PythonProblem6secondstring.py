# This program takes a user input string and outputs every second word.
# Finally figured out how to remove every second word!

sentence = str(input("Please enter a sentence: "))

wordlist = sentence.split() # This splits the entered sentence into seperate words, using the blank space to recognize the seperate words, and makes it into a list.
length = (len(wordlist)) # this counts the total amount of words in the sentence
half = len(wordlist) //2 #the variable 'half' is needed to make the while loop stop on time.
x = -1 #this removes the last word from the string


while length > half: #the loop will stop when half of all words are removed.
    wordlist.pop(x) # 'pop' removes an element from a list. x keeps changing so every second word is removed.
    length = len(wordlist)
    x = x - 1 #after removing the last word, x becomes -2, so it removes the second last word.
    #  (after the last one is already gone, so from the string that was entered, the last and third last word are gone etc.)
    
joinedstring = ' '.join([ str(word) for word in wordlist ]) #Make the list of words into a string again and then join them with a single space in between every seperate word.
    
print(joinedstring) #print the new joined string



