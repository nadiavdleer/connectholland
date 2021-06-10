"""
Assessment assignment 5
Nadia van der Leer for Connect Holland
10 June 2021
"""

from word2number import w2n
from num2words import num2words

def sort_numerically():
    # initialise word list
    word_list = [
        "seventy five",
        "two hundred forty one",
        "three thousand",
        "one million thirty five thousand twelve",
        "twenty",
        "five hundred thousand",
        "two hundred",
        "one billion",
    ]

    i = 0
    number_list = []
    # convert each word to number, add to list
    for word in word_list:
        word = w2n.word_to_num(word_list[i])
        i += 1
        number_list.append(word)
        
    # sort number list in descending order
    number_list.sort(reverse = True)

    # convert numbers back to words, create new list
    num = 0
    new_list = []
    for number in number_list:
        number = num2words(number_list[num])
        num += 1
        new_list.append(number)
        
    return new_list

if __name__ == "__main__":
    print(sort_numerically())