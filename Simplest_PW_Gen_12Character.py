import random
import string


def create_password():
    password = ["\n"]
    while len(password) < 12:
        password_character = random.choice(string.ascii_letters +
                                           string.digits +
                                           string.punctuation)
        password.append(password_character)
    password_string = ''.join(str(e) for e in password)
    print(password_string)


create_password()
