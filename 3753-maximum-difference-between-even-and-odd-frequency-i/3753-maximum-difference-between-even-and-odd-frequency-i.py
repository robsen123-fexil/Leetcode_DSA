class Solution:
    def maxDifference(self, s: str) -> int:
        cnt=Counter(s)
        even=[]
        odd=[]
        for v in cnt.values():
            if v%2==0:
                even.append(v)
            else:
                odd.append(v)
        maxi=-inf
        for o in odd:
            for e in even:
                maxi=max(maxi , o-e)
        return maxi