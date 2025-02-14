class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=sums=0
        minima=float('inf')
        for i in range(len(nums)):
            sums+=nums[i]
            while sums>=target:
                print('here')
                minima=min(minima , i-l+1)
                sums-=nums[l]
                l+=1
        return minima if minima!=float('inf') else 0
