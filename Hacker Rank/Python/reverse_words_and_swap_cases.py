#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    word_list = sentence.split(" ")
    new_word_list = []
    
    for word in word_list:
        letter_list = list(word)
        new_letter_list = []
        for letter in letter_list:
            if letter == letter.upper():
                new_letter_list.append(letter.lower())
            elif letter == letter.lower():
                new_letter_list.append(letter.upper())
        new_word = "".join(new_letter_list)
        new_word_list.append(new_word)
    print(new_word_list)
    new_word_list.reverse()
    print(new_word_list)

    new_sentence = " ".join(new_word_list)
    print(new_sentence)
    return new_sentence

if __name__ == '__main__':
    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)