class Solution:
    def trailingZeroes(self, n: int) -> int:
        def helper(n ):
            if n==0 or n==1:
                return 1
            return n*helper(n-1 )
        ans=(helper(n))
        count=0
        while ans!=0:
            if ans%10!=0:
                return count
            count+=1
            ans//=10
        return count