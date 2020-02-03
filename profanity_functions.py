import requests


def provide():
    return requests.get('https://www.cs.cmu.edu/~biglou/resources/bad-words.txt').text.split()


def filter_special_signs(text):
    for char in ('@', '#', '$', '%', '&', '*', '.'):
        text = text.replace(char, '')
    return text


def censor(text: str, blacklist=()) -> str:
    correct_text = ""
    for word in text.split(" "):
        if word.lower() in blacklist:
            correct_text += "***** "
        else:
            correct_text += word + " "
    return correct_text


def checking_list_exist(list) -> bool:
    if list.lower() == "yes":
        return True
    return False
