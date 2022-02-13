import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(data)

nato_dict = {data.letter: data.code for (index, data) in df.iterrows()}
print(nato_dict)

word = input('Enter word for phonetic code words list: ')
nato_list = [nato_dict[letter.upper()] for letter in word]
print(nato_list)
