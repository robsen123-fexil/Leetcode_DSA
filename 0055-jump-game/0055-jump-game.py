class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l=0
        for i in range(len(nums)):
            if l<0:
                return False
            l=max(l , nums[i])
            
            l-=1
        return True 