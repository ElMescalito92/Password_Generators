import random
import time
import string


def prnt_hold_0(messages):
    print(messages)
    time.sleep(1)


def generate_password():
    password = []
    while True:
        start_generator = input("Generate a password? (Y/N):\n").lower()
        if start_generator == "y":
            # create PW
            while len(password) < 12:
                password_character = random.choice(string.ascii_letters +
                                                   string.digits +
                                                   string.punctuation)
                password.append(password_character)
            password_string = ''.join(str(e) for e in password)
            print(password_string)
            generate_another()
        elif start_generator == "n":
            prnt_hold_0("Goodbye!")
            return False
        else:
            prnt_hold_0("Please choose Y or N.")
            generate_password()


def generate_another():
    another_password = []
    while True:
        restart_generator = input("Generate again? (Y/N):\n").lower()
        if restart_generator == "y":
            # create PW
            while len(another_password) < 12:
                password_character = random.choice(string.ascii_letters +
                                                   string.digits +
                                                   string.punctuation)
                another_password.append(password_character)
            password_string = ''.join(str(e) for e in another_password)
            print(password_string)
            generate_another()
        elif restart_generator == "n":
            prnt_hold_0("Goodbye!")
            return False
        else:
            prnt_hold_0("Please choose Y or N.")
            generate_another()


generate_password()
