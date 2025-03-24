# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        best=n
        l=0
        r=n
        while l<=r:
            md=(l+r)//2
            if isBadVersion(md):
                best=md
                r=md-1
            else:
                l=md+1
        return best