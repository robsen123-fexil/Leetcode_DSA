class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ls=[]
        for i in nums:
            if i==0:
                ls.append(-1)
            else:
                ls.append(1)
        hsh=defaultdict(int)
        hsh[0]=-1
        sums=0
        maxima=-inf
        print(ls)
        for i  , val in enumerate(ls):
            sums+=val
            if sums in hsh:
                maxima=max(maxima , i-hsh[sums])
            elif sums not in hsh:
                hsh[sums]=i

        print(hsh)
        return maxima if maxima!=-inf else 0 




            


