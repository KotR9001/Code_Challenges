class Solution:
    def twoSum(self, nums: list([int]), target: int) -> list([int]):
        #Assign Values to the Object Properties 
        self.nums = nums
        self.target = target

        #Map the Elements Whose Values Add to the Target Value
        new_nums_list = list(filter(lambda i, j: (self.nums[i] + self.nums[j] == self.target), range(len(self.nums))))
        
        #Create List to Push Values from Map Object
        #new_nums_list1 = []
        #for k in new_nums_list:
            #new_nums_list1.append(k)
        print(new_nums_list)
        return new_nums_list
        
#Instantiate the Class
answer = Solution()

#Call the Function from the Class
answer.twoSum([2,3,7,9], 10)
answer.twoSum([3,2,4], 6)
answer.twoSum([3,3], 6)