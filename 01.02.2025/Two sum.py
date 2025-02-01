class Solution:
    def twoSum(self, nums, target):
        num_range = {}  
        for i in range(len(nums)): 
            num = nums[i] 
            x = target - num  
            if x in num_range:  
                return [num_range[x], i]  
            num_range[num] = i
