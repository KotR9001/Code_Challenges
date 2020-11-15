class Solution:
    def twoSum(self, nums: list([int]), target: int) -> list([int]):
        #Assign Values to the Object Properties 
        self.nums = nums
        self.target = target

        #Sort the Number List
        new_nums = sorted(enumerate(self.nums), key=lambda x: x[1])
        #print(new_nums)
        #Loop Through the nums List
        for i in range(len(new_nums)):
            #Loop through the nums List Again
            for j in range(i+1, len(new_nums)):

                #Check to See if The Sum of Numbers from Elements i & j Equals the Target
                if new_nums[i][1] + new_nums[j][1] == self.target:
                    #print(new_nums[i][0], new_nums[j][0])
                    return [new_nums[i][0], new_nums[j][0]]
                    
#Instantiate the Class
answer = Solution()

#Call the Function from the Class
answer.twoSum([2,3,7,9], 10)
answer.twoSum([3,2,4], 6)
answer.twoSum([3,3], 6)