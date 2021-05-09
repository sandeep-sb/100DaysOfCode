import pandas

nato_phonetic_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
new_dict = {row.letter: row.code for (index, row) in nato_phonetic_data.iterrows()}
print(new_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
word_list = [new_dict for letter in word]
print(word_list)