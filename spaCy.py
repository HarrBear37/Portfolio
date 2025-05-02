import spacy
import pygal
import nltk
from pygal.style import DarkSolarizedStyle
from nltk.corpus import wordnet as wn
from collections import Counter

nlp = spacy.load("en_core_web_lg")

filepath = 'pokemonMoves/physical.txt'
f = open(filepath, 'r', encoding='utf8').read()

spacyRead = nlp(f)
for token in spacyRead:
    print(token.text, "---->", token.pos_, ":::::", token.lemma_)

spacy.explain("VERB")

def wordCollector(words):
    wordList = []
    count = 0
    for token in words:
        if token.pos_ == "VERB":
            count += 1
            wordList.append(token.lemma_)
    return wordList
myWords = wordCollector(spacyRead)
print(myWords)

word_freq = Counter(myWords)
ranked = word_freq.most_common()
topTen = word_freq.most_common(10)
print(topTen)
lastTen = word_freq.most_common()[:-11:-1]
print(lastTen)

bar_chart = pygal.Bar(style=DarkSolarizedStyle)
bar_chart.title = 'Top 10 Most Frequent Verbs in Sixteen Candles'
for word, freq in topTen:
    bar_chart.add(word, freq)
bar_chart.render_to_file('top10_verbs.svg')

setOfWords = set(myWords)
lowerCased = [w.lower() for w in setOfWords]

sortedWords = sorted(lowerCased)
print(sortedWords)
for w in myWords:
    synsets = len(wn.synsets(w))
    print("The word ", w, "belongs to ", synsets, "synsets in WordNet.")