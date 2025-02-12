class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l=0
        while l<len(nums):
            if nums[l]==0:
                r=l
                while r<len(nums) and nums[r]==0:
                    r+=1
                if r<len(nums):
                    nums[r] , nums[l]=nums[l]  , nums[r]
            l+=1
            