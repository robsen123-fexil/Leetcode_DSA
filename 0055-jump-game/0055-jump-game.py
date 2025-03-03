class Solution:
    def canJump(self, nums: List[int]) -> bool:
        x=0
        for i in nums:
            if x<0:
                return False
            elif i>x:
                x=i
            x-=1
        return True