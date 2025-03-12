class Solution:
    def kthCharacter(self, k: int) -> str:
        def solver(s  , k):
            if len(s)>k:
                return s
            
            l=len(s)-1
            res=[]
            while l>=0:
                res.append(chr(((ord(s[l])+1)-97)%26+97))
                l-=1

            return solver(s+res[::-1], k)
        ans=solver(['a'] , k)
        return ans[k-1]
        
            
