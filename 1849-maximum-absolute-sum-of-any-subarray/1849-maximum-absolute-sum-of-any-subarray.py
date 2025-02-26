class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxima=sums=0
        for i in nums:
            sums+=i
            if sums<0:
                sums = 0
            maxima=max(maxima , sums)
        minima=sums=0
        for i in nums:
            sums+=i
            if sums>0:
                sums=0
            minima=min(minima , sums)
        return max(maxima , abs(minima))





        