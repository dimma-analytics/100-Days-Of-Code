import pandas
data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index , row) in data_frame.iterrows()}
#print(data_dict)


user_word = input("Enter a word: ").upper()
output_list = [data_dict[letter] for letter in user_word]
print(output_list)

