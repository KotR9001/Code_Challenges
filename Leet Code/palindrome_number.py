class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Assign Value to Object Property
        self.x = x

        #Convert Value to a String
        string = str(self.x)
        #Convert String to a List
        digits = list(string)
        #Reverse the Direction of the Digits
        reverse_digits = reversed(digits)
        #print(reverse_digits)
        #Convert Digits Back to Integers
        nums = []
        for digit in reverse_digits:
            if digit in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                nums.append(int(digit))
            else:
                nums.append(digit)
        #print(nums)

        #Create a List for Boolean Values
        bool_list = []
        #Loop through Digits
        for index in range(len(nums)):
            #Compare Digits in List
            if nums[index] == nums[-index-1]:
                bool_list.append(True)
            else:
                bool_list.append(False)

        #Check to See if All Values in the Boolean List are True
        if all(bool_list) == True:
            print(True)
            return True
        else:
            print(False)
            return False

answer = Solution()

answer.isPalindrome(121)
answer.isPalindrome(-121)
answer.isPalindrome(10)
answer.isPalindrome(1000021)