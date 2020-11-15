def twoSum(nums, target):
    
    #Loop Through the nums List
    for i in range(len(nums)):
        #Loop through the nums List Again
        for j in range(len(nums)):
            #Check to See if The Element Positions are the Same
            if i != j:
                #Check to See if The Sum of Numbers from Elements i & j Equals the Target
                if nums[i] + nums[j] == target:
                    print([i, j])
                    return [i, j]
        
#Call the Function from the Class
twoSum([2,3,7,9], 10)
twoSum([3,2,4], 6)
twoSum([3,3], 6)