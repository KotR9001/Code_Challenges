#!/bin/python3

import math
import os
import random
import re
import sys
import itertools



if __name__ == '__main__':
    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        #Create Lists of Winners by Game
        balsa_list = []
        koca_list = []

        #Create a List of Every Possible Score Sequence
        score_sequence_list = itertools.permutations(a, n)
        #print(score_sequence_list)
        score_sequence_list1 = []
        for sequence in score_sequence_list:
            score_sequence_list1.append(list(sequence))
        #print(list(score_sequence_list1))
        #Loop Through Each Score Sequence
        for sequence in score_sequence_list1:
            #print(sequence)
            # Initialize Player Scores & Difference
            Sb_list = []
            Sk_list = []
            diff = 0

            #Loop Through Each Element in Score Sequence
            for e in range(len(sequence)):
                #print(f"The score sequence is: {sequence[e]}")
                #Add Even Indices to Balsa's Score
                if e %2 == 0:
                    Sb_list.append(sequence[e])
                #Add Odd Indices to Koca's Score
                else:
                    Sk_list.append(sequence[e])
            #print(Sb_list)
            #print(Sk_list)
            Sb = sum(Sb_list)
            #print(Sb)
            Sk = sum(Sk_list)
            #print(Sk)
            #Append the Score Difference to the 
            #Calculate the Difference in Scores
            diff = abs(Sb - Sk)
            #print(f"The difference is: {diff}")

            #Determine the Winner
            if diff %3 == 0:
                koca_list.append('Koca')
            else:
                balsa_list.append('Balsa')
        #print(koca_list)
        #print(balsa_list)
        #print(len(koca_list))
        #print(len(balsa_list))

        if len(koca_list) > len(balsa_list):
            print('Koca')
        elif len(balsa_list) > len(koca_list):
            print('Balsa')
