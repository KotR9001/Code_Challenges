class Solution:
    def romanToInt(self, s: str) -> int:
        #Assign Value to Object Property
        self.s = s

        #Create a List of Roman Numerals
        symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        #Create a List of Integers
        #values = [1, 5, 10, 50, 100, 500, 1000]
        #Create a Dictionary to Link Roman Numerals with their Respective Values
        numeral_values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        #Loop through the Roman Numerals
        #for self.s in symbols:
        #Condition Where the Numeral is in the Numeral List
        if self.s in symbols:
            value = numeral_values[self.s]
            print(value)
            return value
        #Condition Where the Numeral is Not in the Numeral List
        if self.s not in symbols:
            #Break the Numeral into a List of Numerals
            numeral_list = list(self.s)
            print(numeral_list)
            #Initialize the List for Storing Values
            value_list = []
            value_list1 = []
            value_list2 = []
            #Loop through the Numeral List and Compare Positions of Numerals
            for element in range(len(numeral_list)):
                #See if there is Only I
                if numeral_list == ['I']:
                    value_list.append(1)
                #See if there is Only II
                if numeral_list == ['I', 'I']:
                    value_list.append(2)
                #See if there is Only III
                if numeral_list == ['I', 'I', 'I']:
                    value_list.append(3)
                #See if there is Only X in Series
                if numeral_list == ['X']:
                    value_list.append(10)
                #See if there is Only XX in Series
                if numeral_list == ['X', 'X']:
                    value_list.append(20)
                #See if there is Only TripleX in Series
                if numeral_list == ['X', 'X', 'X']:
                    value_list.append(30)
                #See if there is Only C in Series
                if numeral_list == ['C']:
                    value_list.append(100)
                #See if there is Only CC in Series
                if numeral_list == ['C', 'C']:
                    value_list.append(200)
                #See if there is Only CCC in Series
                if numeral_list == ['C', 'C', 'C']:
                    value_list.append(300)
                #See if there is Only M in Series
                if numeral_list == ['M']:
                    value_list.append(1000)
                #See if there is Only MM in Series
                if numeral_list == ['M', 'M']:
                    value_list.append(2000)
                #See if there is Only MMM in Series
                if numeral_list == ['M', 'M', 'M']:
                    value_list.append(3000)
            #Loop through the Numeral List and Compare Positions of Numerals
            for element in range(len(numeral_list)):
                #See if I Comes Before V
                if numeral_list[element] == 'I' and numeral_list[element + 1] == 'V':
                    value_list.append(4)
                #Check if V Comes Before I
                elif numeral_list[element] == 'V' and numeral_list[element + 1] == 'I':
                    #If V Comes Before I, See How Many I Occur
                    if len(numeral_list) == 2:
                            value_list.append(6)
                    if len(numeral_list) >= 3:
                        if numeral_list[element + 2] != 'I':
                            value_list.append(6)
                    if len(numeral_list) == 3 and numeral_list[element + 2] == 'I':
                            value_list.append(7)
                    if len(numeral_list) >= 4:
                        if numeral_list[element + 2] == 'I' and numeral_list[element + 3] != 'I':
                            value_list.append(7)
                    if len(numeral_list) == 4 and numeral_list[element + 3] == 'I':
                            value_list.append(8)
                    if len(numeral_list) >= 5:
                        if numeral_list[element + 2] == 'I' and numeral_list[element + 3] == 'I':
                            value_list.append(8)
                #Check if XIX is in Series
                if numeral_list[element] == 'X' and numeral_list[element + 1] == 'I' and numeral_list[element + 2] == 'X':
                    value_list.append(19)
                #Check if I Comes Before X
                elif numeral_list[element] == 'I' and numeral_list[element + 1] == 'X':
                    value_list.append(9)
                #Check if X Comes Before I
                elif numeral_list[element] == 'X' and numeral_list[element + 1] == 'I':
                    #If X Comes Before I, See How Many I Occur
                    if len(numeral_list) == 2:
                            value_list.append(11)
                    if len(numeral_list) >= 3:
                        if numeral_list[element + 2] != 'I':
                            value_list.append(11)
                    if len(numeral_list) == 3 and numeral_list[element + 2] == 'I':
                            value_list.append(12)
                    if len(numeral_list) >= 4:
                        if numeral_list[element + 2] == 'I' and numeral_list[element + 3] != 'I':
                            value_list.append(12)
                    if len(numeral_list) == 4 and numeral_list[element + 3] == 'I':
                            value_list.append(13)
                    if len(numeral_list) >= 5:
                        if numeral_list[element + 2] == 'I' and numeral_list[element + 3] == 'I':
                            value_list.append(13)
                    #Check if X Comes Before L
                if numeral_list[element] == 'X' and numeral_list[element + 1] == 'L':
                    value_list.append(40)
                #Check if L Comes Before X
                elif numeral_list[element] == 'L' and numeral_list[element + 1] == 'X':
                    #If L Comes Before X, See How Many X Occur
                    if len(numeral_list) == 2:
                            value_list.append(60)
                    if len(numeral_list) >= 3:
                        if numeral_list[element + 2] != 'X':
                            value_list.append(60)
                    if len(numeral_list) == 3 and numeral_list[element + 2] == 'X':
                            value_list.append(70)
                    if len(numeral_list) >= 4:
                        if numeral_list[element + 2] == 'X' and numeral_list[element + 3] != 'X':
                            value_list.append(70)
                    if len(numeral_list) == 4 and numeral_list[element + 3] == 'X':
                            value_list.append(80)
                    if len(numeral_list) >= 5:
                        if numeral_list[element + 2] == 'X' and numeral_list[element + 3] == 'X':
                            value_list.append(80)
                    #Check if CXC is in Series
                if numeral_list[element] == 'C' and numeral_list[element + 1] == 'X' and numeral_list[element + 2] == 'C':
                    value_list.append(190)
                #Check if X Comes Before C
                elif numeral_list[element] == 'X' and numeral_list[element + 1] == 'C':
                    value_list.append(90)
                #Check if C Comes Before X
                elif numeral_list[element] == 'C' and numeral_list[element + 1] == 'X':
                    #If C Comes Before X, See How Many X Occur
                    if len(numeral_list) == 2:
                            value_list.append(110)
                    if len(numeral_list) >= 3:
                        if numeral_list[element + 2] != 'X':
                            value_list.append(110)
                    if len(numeral_list) == 3 and numeral_list[element + 2] == 'X':
                            value_list.append(120)
                    if len(numeral_list) >= 4:
                        if numeral_list[element + 2] == 'X' and numeral_list[element + 3] != 'X':
                            value_list.append(120)
                    if len(numeral_list) == 4 and numeral_list[element + 3] == 'X':
                            value_list.append(130)
                    if len(numeral_list) >= 5:
                        if numeral_list[element + 2] == 'X' and numeral_list[element + 3] == 'X':
                            value_list.append(130)
                    #Check if C Comes Before D
                if numeral_list[element] == 'C' and numeral_list[element + 1] == 'D':
                    value_list.append(400)
                #Check if D Comes Before C
                elif numeral_list[element] == 'D' and numeral_list[element + 1] == 'C':
                    #If D Comes Before C, See How Many C Occur
                    if len(numeral_list) == 2:
                            value_list.append(600)
                    if len(numeral_list) >= 3:
                        if numeral_list[element + 2] != 'C':
                            value_list.append(600)
                    if len(numeral_list) == 3 and numeral_list[element + 2] == 'C':
                            value_list.append(700)
                    if len(numeral_list) >= 4:
                        if numeral_list[element + 2] == 'C' and numeral_list[element + 3] != 'C':
                            value_list.append(700)
                    if len(numeral_list) == 4 and numeral_list[element + 3] == 'C':
                            value_list.append(800)
                    if len(numeral_list) >= 5:
                        if numeral_list[element + 2] == 'C' and numeral_list[element + 3] == 'C':
                            value_list.append(800)
                #Check if MCM is in Series
                if numeral_list[element] == 'M' and numeral_list[element + 1] == 'C' and numeral_list[element + 2] == 'M':
                    value_list.append(1900)
                #Check if C Comes Before M
                elif numeral_list[element] == 'C' and numeral_list[element + 1] == 'M':
                    value_list.append(900)
                #Check if M Comes Before C
                elif numeral_list[element] == 'M' and numeral_list[element + 1] == 'C':
                    #If M Comes Before C, See How Many C Occur
                    if len(numeral_list) == 2:
                            value_list.append(1100)
                    if len(numeral_list) >= 3:
                        if numeral_list[element + 2] != 'C':
                            value_list.append(1100)
                    if len(numeral_list) == 3 and numeral_list[element + 2] == 'C':
                            value_list.append(1200)
                    if len(numeral_list) >= 4:
                        if numeral_list[element + 2] == 'C' and numeral_list[element + 3] != 'C':
                            value_list.append(1200)
                    if len(numeral_list) == 4 and numeral_list[element + 3] == 'C':
                            value_list.append(1300)
                    if len(numeral_list) >= 5:
                        if numeral_list[element + 2] == 'C' and numeral_list[element + 3] == 'C':
                            value_list.append(1300)
                    #Check if L Comes Before I
                if numeral_list[element] == 'L' and numeral_list[element + 1] == 'I':
                    #If L Comes Before I, See How Many I Occur
                    if len(numeral_list) == 2:
                            value_list.append(51)
                    if len(numeral_list) >= 3:
                        if numeral_list[element + 2] != 'I':
                            value_list.append(51)
                    if len(numeral_list) == 3 and numeral_list[element + 2] == 'I':
                            value_list.append(52)
                    if len(numeral_list) >= 4:
                        if numeral_list[element + 2] == 'I' and numeral_list[element + 3] != 'I':
                            value_list.append(52)
                    if len(numeral_list) == 4 and numeral_list[element + 3] == 'I':
                            value_list.append(53)
                    if len(numeral_list) >= 5:
                        if numeral_list[element + 2] == 'I' and numeral_list[element + 3] == 'I':
                            value_list.append(53)
                #Check if L Comes Before V
                if numeral_list[element] == 'L' and numeral_list[element + 1] == 'V':
                    value_list.append(55)
                #Check if C Comes Before I
                if numeral_list[element] == 'C' and numeral_list[element + 1] == 'I':
                    #If I Comes Before C, See How Many C Occur
                    if len(numeral_list) == 2:
                            value_list.append(101)
                    if len(numeral_list) >= 3:
                        if numeral_list[element + 2] != 'I':
                            value_list.append(101)
                    if len(numeral_list) == 3 and numeral_list[element + 2] == 'I':
                            value_list.append(102)
                    if len(numeral_list) >= 4:
                        if numeral_list[element + 2] == 'I' and numeral_list[element + 3] != 'I':
                            value_list.append(102)
                    if len(numeral_list) == 4 and numeral_list[element + 3] == 'I':
                            value_list.append(103)
                    if len(numeral_list) >= 5:
                        if numeral_list[element + 2] == 'I' and numeral_list[element + 3] == 'I':
                            value_list.append(103)
                #Check if C Comes Before V
                if numeral_list[element] == 'C' and numeral_list[element + 1] == 'V':
                    value_list.append(105)
                #Check if C Comes Before L
                if numeral_list[element] == 'C' and numeral_list[element + 1] == 'L':
                    value_list.append(150)
                print(value_list)
                print(value_list1)
                print(value_list2)
                return value_list

answer = Solution()

answer.romanToInt("III")
answer.romanToInt("IV")
answer.romanToInt("VI")
answer.romanToInt("VII")
answer.romanToInt("VIII")
answer.romanToInt("IX")
answer.romanToInt("LVIII")
answer.romanToInt("MCMXCIV")