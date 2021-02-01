import random
import time
import string
import sys


def prnt_hold_0(messages):
    print(messages)
    time.sleep(1)


def create_password():
    password = ["\n"]
    while len(password) < 12:
        password_character = random.choice(string.ascii_letters +
                                           string.digits +
                                           string.punctuation)
        password.append(password_character)
    password_string = ''.join(str(e) for e in password)
    print(password_string)
    repeat_generator()


def start_generator():
    while True:
        start_generator = input("\nGenerate a password? (Y/N):\n").lower()
        if start_generator == "y":
            # create PW-Function
            create_password()
        elif start_generator == "n":
            exit()
        else:
            prnt_hold_0("Please choose Y or N.")
            start_generator()


def repeat_generator():
    while True:
        restart_generator = input("\nGenerate again? (Y/N):\n").lower()
        if restart_generator == "y":
            # create PW-function
            create_password()
        elif restart_generator == "n":
            exit()
        else:
            prnt_hold_0("\nPlease choose Y or N.")
            repeat_generator()


def exit():
    prnt_hold_0("\nGoodbye!\n")
    sys.exit()


start_generator()
