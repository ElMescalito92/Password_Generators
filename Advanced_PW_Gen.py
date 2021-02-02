import random
import time
import string
import sys


def prnt_hold(n, messages):
    print(messages)
    time.sleep(n)


def start_generator():
    pass_len = []
    character_select = []
    password = [""]
    prnt_hold(0, "\nWelcome!\n ")
    password_length(character_select, pass_len, password)


def password_length(character_select, pass_len, password):
    pass_len = input("\nPlease enter desired password length:\n")
    if int(pass_len) >= 12 and int(pass_len) <= 64:
        password_characters(character_select, pass_len, password)
    else:
        prnt_hold(2, "\nPassword needs to be at least 12 Characters "
                     "to be safe!\n"
                     "Length is limited to 64 Characters at the most!\n")
        password_length(character_select, pass_len, password)


def password_characters(character_select, pass_len, password):
    prnt_hold(0, "\nPlease select the character contents for your Password.")
    characters = input("Enter 1: Alphabetical only. "
                       "(not recommended)\n"
                       "Enter 2: Alphabetical and numerical. (Safe)\n"
                       "Enter 3: Alphabetical, numerical "
                       "and punctuations. (Safest)\n")
    if int(characters) <= 3:
        character_select.append(characters)
        create_password(character_select, pass_len, password)
    else:
        prnt_hold(2, "\nPlease enter number between 1 and 3.\n")
        password_characters(character_select, pass_len, password)


def create_password(character_select, pass_len, password):
    if "3" in character_select:
        while len(password) < int(pass_len):
            password_character = random.choice(string.ascii_letters +
                                               string.digits +
                                               string.punctuation)
            password.append(password_character)
    elif "2" in character_select:
        while len(password) < int(pass_len):
            password_character = random.choice(string.ascii_letters +
                                               string.digits)
            password.append(password_character)
    else:
        while len(password) < int(pass_len):
            password_character = random.choice(string.ascii_letters)
            password.append(password_character)
    password_string(character_select, pass_len, password)


def password_string(character_select, pass_len, password):
    password_string = ''.join(str(e) for e in password)
    prnt_hold(0.4, "")
    prnt_hold(0.4, "\n.")
    prnt_hold(0.4, ". .")
    prnt_hold(0.4, ". . .")
    prnt_hold(0.4, "\nYour generated password:\n")
    print(password_string)
    prnt_hold(5, '')
    repeat_generator(character_select, pass_len, password)


def repeat_generator(character_select, pass_len, password):
    restart_generator = input("\nGenerate again? (Y/N):\n").lower()
    if restart_generator == "y":
        password_length(character_select, pass_len, password)
    elif restart_generator == "n":
        exit()
    else:
        prnt_hold(2, "\nPlease choose Y or N.")
        repeat_generator(character_select, pass_len, password)


def exit():
    prnt_hold(1, "\nGoodbye!\n")
    sys.exit()


start_generator()
