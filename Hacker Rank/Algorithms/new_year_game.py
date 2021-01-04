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

            #Loop Through Each Element in Score Sequence
            for e in range(len(sequence)):
                #print(f"The score sequence is: {sequence[e]}")
                #Add Even Indices to Balsa's Score
                if e %2 == 0:
                    #Check if Adding the Element Would Make the Modulus 3 of diff == 0
                    if (abs(sum(Sb_list) - sum(Sk_list)) + sequence[e]) %3 == 0:
                        #print(f"The index is {e} and the element is {sequence[e]}")
                        #Check if the Element is the Last in the Sequence
                        if all(sequence) %3 == 0:
                            Sb_list.append(sequence[e])
                        else:
                            sequence.append(sequence[e])
                        #print(f"The index is {e} and the element is {sequence[e]}")
                    else:
                        Sb_list.append(sequence[e])
                #Add Odd Indices to Koca's Score
                else:
                    #Check if Adding the Element Would Make the Modulus 3 of diff != 0
                    if (abs(sum(Sb_list) - sum(Sk_list)) - sequence[e]) %3 != 0:
                        #print(f"The index is {e} and the element is {sequence[e]}")
                        #Check if the Element is the Last in the Sequence
                        if all(sequence) %3 != 0:
                            Sk_list.append(sequence[e])
                        else:
                            sequence.append(sequence[e])
                        #print(f"The index is {e} and the element is {sequence[e]}")
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
        #print(f"koca_list is: {koca_list}")
        #print(f"balsa_list is: {balsa_list}")
        #print(f"The length of koca_list is: {len(koca_list)}")
        #print(f"The length of balsa_list is: {len(balsa_list)}")

        if len(koca_list) > len(balsa_list):
            print('Koca')
        elif len(balsa_list) > len(koca_list):
            print('Balsa')
