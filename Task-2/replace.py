"""replace.py pseudo code

input the sentence
use the function .replace("!"," ") on string
make string upper case useing upper() function
reverse it by stepping (::-1)
print statement """

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
sentence = sentence.replace("!", " ") # replaces "!" with spaces
sentence = sentence.upper() # converts the string to block caps
print(sentence[::-1]) # prints the string with a step of -1



