class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def solver(n):
            if n==1:
                return True
            elif n<1:
                return False
            return solver(n/4)
        return True if solver(n) else False