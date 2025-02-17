class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxima=-inf
        sums=0
        for i in range(len(nums)):
            sums+=nums[i]
            maxima=max(maxima  ,sums)
            if sums<0:
                sums*=0
        return maxima
