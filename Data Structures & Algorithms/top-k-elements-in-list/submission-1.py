class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        final = {}
        i=0
        while i < len(nums):
            count = 1
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
                else :
                    break
            final[nums[i]] = count
            i += count
        

        finals = sorted(final,key = final.get )
        finals.reverse()

        return finals[:k]

  