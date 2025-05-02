import nltk
import os
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import wordnet as wn

filepath= 'pokemonMoves/status.txt'
f = open(filepath, 'r', encoding='utf8').read()
tokenList = word_tokenize(f)
lowercaseTokens = [token.lower() for token in tokenList]
uniqueTokens = set(lowercaseTokens)
print(uniqueTokens)

POStagged = pos_tag(uniqueTokens)
tagsIwant = ['VB', 'VBZ']
shortList = [word for word, tag in POStagged if tag in tagsIwant]
print(len(shortList))
print(shortList)

for w in sorted(shortList):
    lemma = wn.morphy(w)
    lemma = lemma if lemma else w
    print(f"Word: {w} | Wordnet Lemma: {lemma}")
    synsets = wn.synsets(lemma)
    pos = {synset.pos() for synset in synsets}
    if synsets:
        print(f" Word: {w}, POS-according-to-WordNet {pos} Number of Synsets (Ambiguity): {len(synsets)}")

cwd = os.getcwd()
print(cwd)