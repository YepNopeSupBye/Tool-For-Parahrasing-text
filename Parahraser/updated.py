import nltk
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from random import choice

# The sentence to modify
sentence = "The cat sat on the mat"

# Tokenize and POS-tag the sentence
tagged_words = pos_tag(word_tokenize(sentence))

# Iterate over each word and POS tag in the sentence
for i, (word, pos) in enumerate(tagged_words):
    # Convert the POS tag to the format accepted by wordnet.synsets()
    pos = {'N':'n', 'V':'v', 'J':'a', 'R':'r'}.get(pos[0], 'n')
    # Get synonyms for the word, filtered by POS tag
    synonyms = wordnet.synsets(word, pos=pos)

    # If there are any synonyms, replace the word with a random synonym
    if synonyms:
        lemmas = [lemma.name() for synset in synonyms for lemma in synset.lemmas()]
        new_word = choice(lemmas)
        tagged_words[i][0] = new_word

# Join the words back into a sentence
new_sentence = " ".join([x[0] for x in tagged_words])

print(new_sentence)