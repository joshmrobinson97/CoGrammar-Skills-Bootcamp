import spacy
nlp = spacy.load('en_core_web_sm')

gardenpathsentences = ["The old man the boats.", 
"We painted the wall with cracks.",
"The prime number few", 
"Mary gave the child a Band-Aid.", 
"That Jill is never here hurts.", 
"The cotton clothing is made of grows in Mississippi.",
"The Sour Drink from the Ocean"]

ner_results = []

for sentence in gardenpathsentences:
    # Process the sentence with SpaCy
    doc = nlp(sentence)

    # Extract tokens and named entities
    tokens = [token.text for token in doc]
    entities = [(ent.text, ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]

    # Store the results
    ner_results.append({
        'sentence': sentence,
        'tokens': tokens,
        'entities': entities
    })

# Print the results
for result in ner_results:
    print(f"Sentence: {result['sentence']}")
    print(f"Tokens: {result['tokens']}")
    print(f"Entities: {result['entities']}\n")


print(spacy.explain("GPE"))
print(spacy.explain("PERSON"))

# I looked up the entities Mississippi and Mary, the labels GPE and PERSON make perfect sense with all things considered.