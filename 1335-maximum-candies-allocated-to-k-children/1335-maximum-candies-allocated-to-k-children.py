class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l=1
        r=max(candies)
        mini=min(candies)
        best=-inf
        while l<=r:
            mid=(l+(r-l)//2)
            cnt=0
            for i in candies:
                cnt+=(i//mid)
            if cnt<k:
                r=mid-1
            else:
                best=max(best , mid)
                l=mid+1
        return best if best!=-inf else 0