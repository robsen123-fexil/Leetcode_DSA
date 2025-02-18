class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        lists=[0]*(len(nums)+1)
        sums=0
        for a , b in requests:
            lists[a]+=1
            lists[b+1]-=1
        lists = list(itertools.accumulate(lists))
        lists = sorted(lists,reverse=True)
        #print(lists)
        nums = sorted(nums, reverse=True)
        ans=0
        for a , b in zip(lists , nums):
            ans+=(a*b) % (10**9+7)
        return ans  % (10**9+7)