class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        maxima=0
        for i in range(2 , len(nums)):
            if nums[i]<(nums[i-1]+nums[i-2]):
                maxima=max(maxima , nums[i-2]+nums[i-1]+nums[i])
        return maxima
            