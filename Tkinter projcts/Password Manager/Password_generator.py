# Importing modules
from random import choice, randint, shuffle

# --------------------- Constants ---------------------
ALPHABETS = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
CHARACTERS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

# --------------------- Function ---------------------
def create_password():
    password_list = []

    # assigning values
    letters = [choice(ALPHABETS) for _ in range(randint(8, 10))]
    digits = [choice(DIGITS) for _ in range(randint(2, 4))]
    chars = [choice(CHARACTERS) for _ in range(randint(2, 4))]
    password_list = letters + digits + chars

    shuffle(password_list)
    return password_list

