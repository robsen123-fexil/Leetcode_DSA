class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt=defaultdict(int)
        for i in range(len(nums)):
            cnt[i+1]+=1
        cnt2=Counter(nums)
        print(cnt)
        ans=[]
        for k , v in cnt2.items():
            if v==2:
                ans.append(k)
        for k , v in cnt.items():
            if k not in cnt2:
                ans.append(k)
                return ans
        
     