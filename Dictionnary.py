import json
from difflib import get_close_matches


def Definition(word, data):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0 :
        print("Did you mean the word {}?".format(get_close_matches(word, data.keys())[0]))
        decide = input("Press 'y' if yes or 'n' if no ")
        if decide == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == 'n':
            return "There is no definition for your word {}".format(word)
        else:
            return "No definition found for {} ".format(word)
    else:
        return "No definition found for {} ".format(word)


def Adapt(definition):
    if type(definition) == list:
        for item in definition:
            print(item)
    else:
        print(definition)


result = json.load(open('data.json'))

wordToLookAt = input('Write the word you want to look at:')
definitionForWordToLookAt = Definition(wordToLookAt, result)
Adapt(definitionForWordToLookAt)
