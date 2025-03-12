class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def solver(s , n ):
            if n==0:
                return s
            l=len(s)-1
            s.append('1')
            res=s[:]
            while l>=0:
                if s[l]=='0':
                    res.append('1')
                else:
                    res.append('0')
                l-=1
            
            return solver(res , n-1)
        return solver(['0'] , n-1)[k-1]