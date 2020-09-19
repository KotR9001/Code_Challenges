class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for int in nums:
            nums.pop(index(int))
            for int1 in nums:
                if int + int1 == target:
                    return [index(int), index(int1)]
        
twoSum(self, nums: [2,3,7,9], target: 10)