import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic_dict = {row_data.letter.lower():row_data.code.lower() for index, row_data in data.iterrows()}

user_word = input("Enter a word: ").lower()
letter_coded = [nato_phonetic_dict[letter] for letter in user_word]

print(letter_coded)