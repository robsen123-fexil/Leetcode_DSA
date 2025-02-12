class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        ls=[i for i in range(int(c**0.5)+1)]
        print(ls)
        l=0
        r=len(ls)-1
        while l<=r:
            res=ls[l]**2+ls[r]**2
            if res==c:
                return True
            elif res>=c:
                r-=1
            else:
                l+=1
        return False

        