class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt=Counter(t)
        cnt2=Counter()
        if len(s)<len(t):
            return ''
        minilength=float('inf')
        ans=""
        def checker(cnt , cnt2):
            for k , v in cnt.items():
                if cnt2[k]<v:
                   return False
            return True
        l=0
        hsh=defaultdict(list)
        for i in range(len(s)):
            cnt2[s[i]]+=1
            while checker(cnt , cnt2):
                if minilength>(i-l+1):
                    ans=s[l:i+1]
                    minilength=i-l+1
                cnt2[s[l]]-=1
                l+=1
        return ans