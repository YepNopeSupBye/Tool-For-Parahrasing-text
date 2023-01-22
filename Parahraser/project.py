import nltk

nltk.download('punkt')
nltk.download('wordnet')
from nltk import punkt
from nltk.corpus import wordnet as wn
from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.meteor_score import meteor_score
from nltk.translate.gleu_score import sentence_gleu

# Define the text you want to paraphrase
text = "yataatatata david won"

# Use NLTK's WordNetLemmatizer to get the base form of the words
lemmatizer = nltk.stem.WordNetLemmatizer()
words = nltk.word_tokenize(text)
base_words = [lemmatizer.lemmatize(word) for word in words]

# Use NLTK's to replace words with their synonyms
#make a list of all the words
# for each word
#find a list of synonyms
# choose a synonym
# replace the original word or add to a new list
synonyms = nltk.corpus.wordnet.all_synsets
replacer = nltk.WordNetSynonymReplacer(synonyms)
paraphrased_words = replacer.replace(base_words)

# Join the words back into a sentence
paraphrased_text = ' '.join(paraphrased_words)

# Print the paraphrased text
print(paraphrased_text)



