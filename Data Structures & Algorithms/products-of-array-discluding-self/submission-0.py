class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        left.append(1)
        right = [0]*len(nums)
        right[-1] = 1
        p =nums[0] 
        for i in range(1,len(nums)):
            left.append(p)
            p *= nums[i]
        r = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            right[i] = r
            r *= nums[i]
        out = []
        for i in range(len(nums)):
            out.append(left[i]*right[i])
        
        return out
        