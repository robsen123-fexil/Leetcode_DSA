class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        l=0
        r=len(citations)-1
        maxi=-inf
        while l<=r:
            mid=(l+(r-l)//2)
            if (citations[mid])>=len(citations)-mid:
                maxi=max(maxi, len(citations)-mid)
                r=mid-1
            else:
                l=mid+1
        return maxi
        