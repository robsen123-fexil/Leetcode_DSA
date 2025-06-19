class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        frst=nums[0]
        ans=1
        for i in nums:
            if i-frst>k:
                ans+=1
                frst=i
        return ans