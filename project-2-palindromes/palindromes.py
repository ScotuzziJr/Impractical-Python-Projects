import load_dict

word_list = load_dict.load("2of4brif.txt")

palindromes = []

for word in word_list:
    if word == word[::-1]:
        palindromes.append(word)

print(f"There are {len(word_list)} words in this word list and {len(palindromes)} palindromes. The palindromes are:")

print(*palindromes, sep='\n')
