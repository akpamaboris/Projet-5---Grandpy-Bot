import wikipedia

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#je crée une phrase test
searchRequestUser = input('type what you want to search here =>   ')

#je spécifie que les stopwords seront en Français

stopWords= set(stopwords.words('french'))

#je tokenize la phrase test, c'est à dire que je sépare une phrase, ou
#un paragraphe dans des unités plus petites
wordTokens = word_tokenize(searchRequestUser)

phrase_avec_filtre =[]
for w in wordTokens:
    if w not in stopWords:
        phrase_avec_filtre.append(w)


print(phrase_avec_filtre)
full_str=' '.join([str(elem) for elem in phrase_avec_filtre])
print(full_str)

#ask what the user want
searchRequest = str(full_str)

#j'initialise la librairie wikipedia pour des recherches en français
wikipedia.set_lang("fr")

try:
    #display the result of the original search
    print(wikipedia.summary(searchRequest, sentences= 5))
except:

    #display some suggestion
    searchResult = wikipedia.search(str(searchRequest),results=10,suggestion=True)
    print(searchResult)
