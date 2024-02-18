""" alterative.py pseudo code

write program that reads a string
    store an input
    store an empty string
makes each alternate character upper and lower case
    store an integer length counter of for the variable
    for loop with the range
    modulus to split to odd and even
    then concatenate the odds characters to a recasted upper case string
    else the rest with lower case


then it makes each alternating word upper and lower case
    take sentence and split into new list
    for loop in new list with same casting
    join the new list to a new string variable
    print string
 """


phrase = input("Please enter a sentence: ")
final_phrase = "" # Empty string to be completed
length_phrase = len(phrase) # Allows the string to be quantified and looped

for i in range(length_phrase):
    if i % 2 == 1: # checks for odd indexing
        final_phrase += phrase[i].upper()

    else:
        final_phrase += phrase[i].lower()

print("\n" + final_phrase)

words = phrase.split() # Turns the sentence into a list of individual words
new_words = []

for j, word in enumerate(words): # enumerate allows me to keep track of the indexing alongside the text
    if j % 2 == 0:  # Check if j is even
        new_words.append(word.lower())
    else:
        new_words.append(word.upper())

final_words = " ".join(new_words) # Combines the list with spaces
print("\n" + final_words)