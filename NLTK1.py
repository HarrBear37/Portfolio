for line in open("python-nlp/avatarSpeeches.txt"):
    for word in line.split():
        if word.endswith('ing'):
            print(word)