# Ard van Balkom, 5-3-19
# Problem 6. This program takes a user input string and outputs every second word.


sentence = str(input("Please enter a sentence: ")) # Ask user to enter a string

wordlist = sentence.split() # Split the entered sentence into separate words, using the blank space to recognize the seperate words, and makes it into a list.
n = 0 # Sets 'n' as variable which will be used as a count.
for word in wordlist:
    n+=1 # Adds 1 to n, so all words in wordlist are considered, ony by one, for the criteria 'if n != 0', which then prints only all odd words, and removes every second (even) word.
    if n%2 != 0:
        print(word, end=' ') # Print all odd words, without going to a new line after every word, with a space between them.

# The code to split the sentence into a list of words is adapted from https://stackoverflow.com/questions/743806/how-to-split-a-string-into-a-list





# Below is how I first had done it, for some reason I went about it too complicated for a long time.
# It worked, but took away odd or even words, depending if the enterend string had an odd or even amount of words. Not exactly the assignment.


# sentence = str(input("Please enter a sentence: "))

# wordlist = sentence.split() # This splits the entered sentence into separate words, using the blank space to recognize the seperate words, and makes it into a list.
# length = (len(wordlist)) # This counts the total amount of words in the sentence
# half = len(wordlist) //2 # The variable 'half' is used to make the while loop stop on time.
# x = -1 # This removes the last word from the string


# while length > half: # The loop will stop when half of all words are removed.
    # wordlist.pop(x) # 'pop' removes an element from a list. x keeps changing so every second word is removed.
    # length = len(wordlist)
   #  x = x - 1 # After removing the last word, x becomes -2, so it removes the second last word (after the previous one is already removed, so from the string that was entered, the last and third last word are gone etc.)
    
# joinedstring = ' '.join([str(word) for word in wordlist]) # Make the list of words into a string again and then join them with a single space in between every separate word.
    
# print(joinedstring) # Print the new joined string



