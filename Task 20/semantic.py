import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp('cat')
word2 = nlp('monkey')
word3 = nlp('banana')

print(f"{word1} & {word2} similarity: {word1.similarity(word2)}") # Cat and monkey have a decent similarity because they're both animals
print(f"{word1} & {word3} similarity: {word3.similarity(word1)}") # Banana and cat don't have a high similarity rating
print(f"{word2} & {word3} similarity: {word3.similarity(word2)}") # Banana and monkey have a medium similarity rating as monkeys tend to eat bananas in pop culture

print("\n" + ("-" * 15) + "\n")

# ------------------------------------------

tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(f"Word 1: {token1.text}, Word 2: {token2.text}, Similarity: {token1.similarity(token2)}")

print("\n" + ("-" * 15) + "\n")

# ------------------------------------------

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I've lost my car in my car",
"I'd like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

print(f"Sentence to compare is: {sentence_to_compare}.\n")
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(f"Sentence: {sentence}. Similarity: {similarity}.\n")

print("\n" + ("-" * 15) + "\n")

# ------------------------------------------

nlp2 = spacy.load('en_core_web_sm')

new_word1 = nlp2('tree')
new_word2 = nlp2('fowl')
new_word3 = nlp2('bird')
print("en_core_web_sm")
print(f"{new_word1} & {new_word2} similarity: {new_word1.similarity(new_word2)}")
print(f"{new_word1} & {new_word3} similarity: {new_word3.similarity(new_word1)}")
print(f"{new_word2} & {new_word3} similarity: {new_word3.similarity(new_word2)}")

print("\n" + ("-" * 15) + "\n")

new_word1 = nlp('tree')
new_word2 = nlp('fowl')
new_word3 = nlp('bird')

print("en_core_web_md")
print(f"{new_word1} & {new_word2} similarity: {new_word1.similarity(new_word2)}")
print(f"{new_word1} & {new_word3} similarity: {new_word3.similarity(new_word1)}")
print(f"{new_word2} & {new_word3} similarity: {new_word3.similarity(new_word2)}")

print("\n" + ("-" * 15) + "\n")

"""
The values for the smaller model size is higher than the medium sized model size.
This is probably because the sample size is smaller so statistically it'll be more skewed.
The accuracy will always be less with a smaller sample size.
"""