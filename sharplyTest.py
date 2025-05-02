import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

filepath= 'pokemonMoves/status.txt'
f = open(filepath, 'r', encoding='utf8').read()
tokenList = word_tokenize(f)
lowercaseTokens = [token.lower() for token in tokenList]
uniqueTokens = set(lowercaseTokens)
pos_tag(uniqueTokens)
print(uniqueTokens)

for line in open("pokemonMoves/physical.txt"):
    for word in line.split():
        if word in ['sharply']:
            print(word)

for line in open("pokemonMoves/special.txt"):
    for word in line.split():
        if word in ['sharply']:
            print (word)

for line in open("pokemonMoves/status.txt"):
    for word in line.split():
        if word in ['sharply']:
            print (word)