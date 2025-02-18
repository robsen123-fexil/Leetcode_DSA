class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        for i,x in enumerate(nums):
            if prefix * 2 + x == total:
                return i
            prefix += x
        
        return -1