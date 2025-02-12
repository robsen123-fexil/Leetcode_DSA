class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hsh=defaultdict(list)
        def sdchecker(num):
            sums=0
            while num:
                sums+=(num%10)
                num=num//10
            return sums
        
        for i in range(len(nums)):
            value=sdchecker(nums[i])
            hsh[value].append(nums[i])
        print(hsh)
        maxima=-1   
        for v in hsh.values():
            sums=0
            if len(v)>=2:
                srt=sorted(v)
                sums=srt[-2]+srt[-1]
            maxima=max(maxima , sums)
        return maxima if maxima!=0 else -1