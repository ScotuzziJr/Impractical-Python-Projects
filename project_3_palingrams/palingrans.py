import sys

sys.path.append('../')

from project_2_palindromes.load_dict import load

word_list = load('../project_2_palindromes/2of4brif.txt')

def find_palingrams():
    pali_list = []

    for word in word_list:
        end = len(word)
        rev_word = word[::-1]

        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                    pali_list.append((rev_word[:end-i], word))
        
        return pali_list
    
palingrams = find_palingrams()

palingrams_sorted = sorted(palingrams)

print(f"There are {len(word_list)} words in this word list and {len(palingrams)} palingrams. The palingrams are:")

for first, second in palingrams_sorted:
    print(f"{first} {second}", palingrams_sorted)
