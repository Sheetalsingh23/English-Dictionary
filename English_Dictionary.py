import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: 
        return data[word.title()]
    elif word.upper() in data: 
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys()))>0:
        yn = input("Did you mean %s instead??\nEnter Y if Yes, or N if No : "% get_close_matches(word,data.keys())[0])
        if yn =="Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn =="N":
            return"Word doesn't exists. Please check it again!!"
        else:
            return"We didn't understand your entry."

    else:
        return"Word doesn't exists. Please check it again!!"

word = input("Enter Word : ")
output = translate(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)