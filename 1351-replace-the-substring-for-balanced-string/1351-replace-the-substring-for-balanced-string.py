class Solution:
    def balancedString(self, s: str) -> int:
        cnt=Counter(s)
        hsh={}
        for key , val in cnt.items():
            if val>(len(s))//4:
                hsh[key]=val-(len(s)//4)
        if not hsh:
            return 0

        def checker(frst , sec):
            

            for k , v in sec.items():
                if frst[k]<v:
                    return False
            return True
        wnd=Counter()
        l=0
        ans=inf
        for i in range(len(s)):
            wnd[s[i]]+=1
            while l<=i and checker(wnd , hsh):
                curr=(i-l+1)
                if curr<ans:
                    ans=curr
                wnd[s[l]]-=1
                
                l+=1
        return ans if ans!=inf else 0                
                



        