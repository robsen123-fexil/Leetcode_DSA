class Solution(object):
    def isZeroArray(self, nums, queries):
        lsts=[0]*(len(nums)+1)
        for a , b in queries:
            lsts[a]+=1
            if b+1<len(nums):
                lsts[b+1]-=1
        cnt=0
        for i in range(len(nums)):
            cnt+=lsts[i]
            if nums[i]>cnt:
                return False
        return True
