import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from random import choice

# The sentence to modify
sentence = "the cat jumped."
# Tokenize the sentence into words
words = word_tokenize(sentence)

# Iterate over each word in the sentence
for i, word in enumerate(words):
    # Get synonyms for the word
    synonyms = wordnet.synsets(word)

    # If there are any synonyms, replace the word with a random synonym
if synonyms:
    lemmas = [lemma.name() for synset in synonyms for lemma in synset.lemmas()]
    new_word = choice(lemmas[:random])
    words[i] = new_word

# Join the words back into a sentence
new_sentence = " ".join(words)

print(new_sentence)