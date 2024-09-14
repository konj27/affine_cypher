import string
import math

alphabet = list(string.ascii_lowercase)
alphabet_len = len(alphabet)

# set input variables
word = input("Give a word to cypher: ")
a_param = int(input("write a parameter: "))
b_param = int(input("write b parameter: "))

# translate a word into indexes of the alphabet
word_indexed = []
for item in word:
    for index in range(len(alphabet)):
        if item.lower() == alphabet[index]:
            word_indexed.append(index)
        else:
            pass
# reindex word with chosen parameters (ax+b)
word_reindex = [i * a_param + b_param for i in word_indexed]
# find new corresponding characters in alphabet list
final_word = ""
for number in word_reindex:
    if number / alphabet_len > 1:
        final_word += alphabet[number - (alphabet_len * math.floor(number / alphabet_len))]
    else:
        final_word += alphabet[number]
print(final_word)
