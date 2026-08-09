import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        x = bisect.bisect_left(nums,target)
        if x < len(nums) and nums[x] == target :
            return x
        return -1