
#j'importe les modules nécessaires pour enlever les stop words
#des phrases avec NLTK
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


#je crée une phrase test
examplePhrase = """
Hey je voulais savoir ce qu'est la France
"""

#je spécifie que les stopwords seront en Français

stopWords= set(stopwords.words('french'))

#je tokenize la phrase test, c'est à dire que je sépare une phrase, ou
#un paragraphe dans des unités plus petites
wordTokens = word_tokenize(examplePhrase)

phrase_avec_filtre =[]
for w in wordTokens:
    if w not in stopWords:
        phrase_avec_filtre.append(w)

print(phrase_avec_filtre)