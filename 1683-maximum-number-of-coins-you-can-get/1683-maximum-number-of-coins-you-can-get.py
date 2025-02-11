class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l=0
        r=len(piles)-1
        count=0
        while r>=l:
            count+=piles[r-1]
            r-=2
            l+=1
        return count
