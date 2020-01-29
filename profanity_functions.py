import requests


def provide():
    return requests.get('https://www.cs.cmu.edu/~biglou/resources/bad-words.txt').text.split()


def censor(text: str, blacklist=()) -> str:
    correct_text = ""
    for word in text.split(" "):
        if word not in blacklist:
            correct_text += word + " "
        else:
            correct_text += "***** "
    return correct_text


def checking_list_exist(list) -> bool:
    if list.lower() == "yes":
        return True
    return False