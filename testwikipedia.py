import wikipedia

#ask what the user want
searchRequest = input("type what you want")

#display the result of the original search
print(wikipedia.summary(searchRequest, sentences= 5))

#display some suggestion
searchResult = wikipedia.search(str(searchRequest),results=10,suggestion=True)
print(searchResult)

