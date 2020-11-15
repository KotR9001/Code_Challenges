class Solution:
    def twoSum(self, nums: list([int]), target: int) -> list([int]):
        #Assign Values to the Object Properties 
        self.nums = nums
        self.target = target

        #Sort the Number List
        new_nums = sorted(enumerate(self.nums), key=lambda x: x[1])
        #print(new_nums)
        #Create List of List of Elements Whose Numbers Add Up to the Target Value
        new_nums_list = [[new_nums[i][0], new_nums[j][0]] for i in range(len(new_nums)) for j in range(i+1, len(new_nums)) 
            if new_nums[i][1] + new_nums[j][1] == self.target][0]
        #print(new_nums_list)
        #Keep List of Elements Whose Numbers Add Up to the Target Value
        #new_nums = new_nums_list[0]
        #print(new_nums)
        return new_nums_list

#Instantiate the Class
answer = Solution()

#Call the Function from the Class
answer.twoSum([2,3,7,9], 10)
answer.twoSum([3,2,4], 6)
answer.twoSum([3,3], 6)