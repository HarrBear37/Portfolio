import spacy
import os

from spaCy import spacyRead

nlp = spacy.load("en_core_web_lg")

collPath = 'pokemonMoves'

def wordCollector(words, unit):
    wordList = []
    for token in words:
        if token.pos_ == "ADJ":
            wordList.append((token.lemma_, unit))
    uniqueLems = set(wordList)
    return uniqueLems

for file in os.listdir(collPath):
    if file.endswith(".txt"):
        filepath = f"{collPath}/{file}"
        name, extension = os.path.splitext(file)
        print(name)
        with open(filepath, 'r', encoding='utf8') as f:
            readFile = f.read()
            lengthFile = len(readFile)
            print(lengthFile)
        
        with open (filepath, 'r', encoding='utf8') as f:
            readFile = f.read()
            spacyRead = nlp(readFile)
            myWords = wordCollector(spacyRead, name)
            print(myWords)

