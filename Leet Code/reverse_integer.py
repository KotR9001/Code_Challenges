class Solution:
    def reverse(self, x: int) -> int:
        #Assign Value to Object Property
        self.x = x
        #Convert Value Object to String
        string = str(self.x)
        #Create a List of Characters from the Value Object
        digits = list(string)
        #Check if the Value Object is Negative
        if '-' in digits:
            neg = '-'
            digits.pop(0)
            #Reverse the Order of the Digits in the List
            rev = reversed(digits)
            #Rejoin the Digits to Form the Number String
            new_num = "".join(rev)
            #Add a Minus Sign to the Front of the New Value Object
            new_num = neg + new_num
            #Convert the Number String to an Integer
            new_int = int(new_num)
            print(new_int)
        else:
            #Reverse the Order of the Digits in the List
            rev = reversed(digits)
            #Rejoin the Digits to Form the Number String
            new_num = "".join(rev)
            #Convert the Number String to an Integer
            new_int = int(new_num)
            print(new_int)

        #Check to See if the Integer is Outside the Range of [−2^31,  2^31 − 1]
        #If Outside the Range, Return Zero, Otherwise, Keep the Current Integer Value
        if new_int < (-2**31):
            new_int = 0
        elif new_int > (2**31-1):
            new_int = 0
        else:
            new_int = new_int
        print(new_int)
        return new_int

answer = Solution()

answer.reverse(234)
answer.reverse(-123)
answer.reverse(120)
answer.reverse(1534236469)
answer.reverse(153423646999999)