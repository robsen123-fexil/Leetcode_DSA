class Solution:
    def trailingZeroes(self, n: int) -> int:
        def solver(n , ans):
            if n<5:
                return ans
            n//=5
            ans+=n
            return solver(n , ans)
        return solver(n , 0)
        
            