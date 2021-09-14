import random

password = []


def generate_pass(pass_len, upper_quantity, lower_quantity, symbols_quantity):
    pass_as_string = ""
    for i in range(pass_len):
        password.append("")
    get_chars(True, upper_quantity)
    get_chars(False, lower_quantity)
    get_symbols(symbols_quantity)
    for c in password:
        pass_as_string += c
    return pass_as_string


def get_chars(isupper, char_quantity):
    total_chars = 0
    while total_chars != char_quantity:
        rand_char = random.randint(0, len(password) - 1)
        if password[rand_char] == "":
            if isupper:
                password[rand_char] = chr(random.randint(65, 90))
                total_chars += 1
            else:
                password[rand_char] = chr(random.randint(97, 122))
                total_chars += 1


def get_symbols(symbols_quantity):
    total_symbols = 0
    while total_symbols != symbols_quantity:
        rand_char = random.randint(0, len(password) - 1)
        if password[rand_char] == "":
            password[rand_char] = chr(random.randint(35, 47))
            total_symbols += 1


print(generate_pass(6, 3, 2, 1))
