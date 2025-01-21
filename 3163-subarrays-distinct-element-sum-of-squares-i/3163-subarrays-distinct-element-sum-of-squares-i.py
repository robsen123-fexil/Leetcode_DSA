class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        result=[]
        for i in range(len(nums)):
            cnt=Counter()
            for j in range(i, len(nums)):
                cnt[nums[j]]+=1
                result.append(len(cnt))
        sums=0
        
        for i in result:
            sums+=(int(i)**2)
        return sums
                