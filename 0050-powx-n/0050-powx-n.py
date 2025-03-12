class Solution:
    def myPow(self, x: float, n: int) -> float:
        def solver(x , n):
            if n==0:
                return 1
            frsts=solver(x , n//2)
            if n%2==0:
                return frsts*frsts
            else:
                return x*frsts*frsts
        ans=solver(x , abs(n))
        if n<0:
            return 1/ans
        return ans
