import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic_dict = {row_data.letter.lower():row_data.code.lower() for index, row_data in data.iterrows()}

def generate_phonetics():
    while True:
        user_word = input("Enter a word: ").lower()

        try:
            letter_coded = [nato_phonetic_dict[letter] for letter in user_word]
        except KeyError:
            print("Enter Only Alphabets")
        else:
            print(letter_coded)
            break

generate_phonetics()