import os
import spacy
import pandas as pd

from spaCy import spacyRead

nlp = spacy.load("en_core_web_lg")

def wordCollector(words, unit):
    wordList = []
    nodeAtts = []
    unitList = []
    for token in words:
        if token.pos_ == "ADJ":
            wordList.append(token.lemma_)
            nodeAtts.append(token.pos_)
            unitList.append(unit)
    data = {
        'word': wordList,
        'nodeType': nodeAtts,
        'unit': unitList
    }
    df = pd.DataFrame(data)
    return df

collPath = 'pokemonMoves'
for file in os.listdir(collPath):
    if file.endswith('.txt'):
        filepath = f"{collPath}/{file}"
        name, extension = os.path.splitext(file)
        with open(filepath, 'r', encoding='utf8') as f:
            readFile = f.read()
            spacyRead = nlp(readFile)
            myDataFrame = wordCollector(spacyRead, name)
            print(myDataFrame)