class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        
        c = 1
        
        if len(nums) <1:
            return 0
        m = 1
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                c+=1
                m = max(c,m)
            else :
                c =1
        return m
       