from profanity_functions import censor, provide, checking_list_exist

if __name__ == '__main__':

    print("Hello in Profanity Censor version 1.0!")

    while True:
        your_text = input("Enter here text wtich you want to censor: ")
        have_blacklist = input("Do you have own list of profanities? (check: YES or NO)")

        if checking_list_exist(have_blacklist) == False:
            blacklist = provide()
            print(censor(your_text, blacklist))

        elif checking_list_exist(have_blacklist) == True:
            blacklist = input("Enter all your profanities separating them with spaces: ")
            print(censor(your_text, blacklist.split()))

        go_or_not = input("Do you want to censor another text? (check: YES or NO)")
        if go_or_not == "NO":
            break