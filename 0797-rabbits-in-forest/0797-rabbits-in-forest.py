class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt=defaultdict(int)
        ans=defaultdict(int)
        result=0
        for i in answers:
            if i!=0:
                if not ans[i]:
                    ans[i]+=(i+1)
                cnt[i]+=1
                if cnt[i]==ans[i]:
                    result+=(ans[i])
                    ans[i]*=0
                    cnt[i]*=0
            else:
                result+=1
        for i in ans.values():
            result+=i
        return result                
