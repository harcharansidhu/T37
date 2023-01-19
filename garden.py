# Intro to NLP
# Task 37

# import the relevant libraries
import spacy

# load a spacy object
nlp = spacy.load("en_core_web_sm")

# A list of garden path sentences
garden_sentences =[
    "The old man the boat.",
    "The complex houses married and single soldiers and their families.", 
    "The horse raced past the barn fell.",
    "The florist sent the flowers was pleased",
    "The man pushed through the door fell.",
    "I told the girl the cat scratched Bill would help her.",
    "The old dog the footsteps of the young."
    "The cotton clothing is made of grows in Mississippi.",
    "The florist sent the bouquet of flowers was very flattered.",
    "Because he always jogs a mile seems a short distance to him.",
    "The barge that floated down the river sank.",
    "The man who whistled tunes pianos.",
    "The sour drink from the ocean.",
    "Have the students who failed the exam take the supplementary.",
    "We painted the wall with cracks.",
    "The man who hunts ducks out on weekends.",
    "The raft floated down the river sank.",
    "When Fred eats food gets thrown.",
    "Mary gave the child the dog bit a Band-Aid.",
    "The girl told the story cried.",
    "I convinced her children are noisy.",
    "Helen is expecting tomorrow to be a bad day.",
    "Fat people eat accumulates.",
    "I know the words to that song about the queen don't rhyme.",
    "She told me a little white lie will come back to haunt me.",
    "The dog that I had really loved bones.",
    "That Jill is never here hurts."
]

# Initialise list to store the tokenisation of the list of garden sentences
tokens = []
for sentence in garden_sentences:
    doc = nlp(sentence)
    # Tokenisation
    tokens.append([token.orth_ for token in doc])

# print tokenisation
#print("\n=== Tokenisation ===\n")
#for tokens_elt in tokens:
#    print(tokens_elt)

# Initialise list of entity recognition of the list of garden sentences
gardenpathSentences = []
for sentence in garden_sentences:
    doc = nlp(sentence)
    # Entity recognition
    gardenpathSentences.append([(i, i.label_) for i in doc.ents])

# print nonempty lists
print("\n=== Entity Recognition ===\n")
for sentence in gardenpathSentences:
    if sentence != []:
        print(sentence)

# Comments

# Comment 1:
# 'a bad day' was recognised as a date. I did not expect it for a description of a day.

# Comment 2:
# I did not expect so many of the garden sentences to not have any named entities. In particular, 'Fred', 'Mary' were ignored.
