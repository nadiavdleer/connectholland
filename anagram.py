"""
Assessment assignment 2
Nadia van der Leer for Connect Holland
10 June 2021
"""

from itertools import groupby

def all_anagram_groups():
    word_source = [
        "pear",
        "dirty room",
        "amleth",
        "reap",
        "tinsel",
        "tesla",
        "hamlet",
        "dormitory",
        "listen",
        "silent"
    ]

    # simple version without spaces (time-wise)
    for words, group in groupby(sorted(word_source, key=sorted), sorted):
        group = list(group)
        print(group)

if __name__ == "__main__":
    all_anagram_groups()