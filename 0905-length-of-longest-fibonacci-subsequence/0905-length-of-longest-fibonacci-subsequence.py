class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        maxima=0
        sets=set(arr)
        for i in range(len(arr)-1):
            for j in range(i+1 , len(arr)):
                frsts , scnd=arr[i] , arr[j]
                sums1=frsts+scnd
                leng=2
                while sums1 in sets:
                    leng+=1
                    frsts , scnd=scnd , sums1
                    sums1=frsts+scnd
                if leng!=2:
                    maxima=max(maxima , leng)
        return maxima

