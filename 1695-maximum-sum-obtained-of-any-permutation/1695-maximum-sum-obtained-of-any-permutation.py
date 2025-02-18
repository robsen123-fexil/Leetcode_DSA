class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        lists=[0]*(len(nums)+2)
        sums=0
        for a , b in requests:
            lists[a]+=1
            lists[b+1]-=1
        for i in range(1 , len(lists)):
            lists[i]+=lists[i-1]
        lists.sort(reverse=True)
        print(lists)
        nums.sort(reverse=True)
        ans=0
        for a , b in zip(lists , nums):
            ans+=(a*b)
        return ans % (10**9+7)