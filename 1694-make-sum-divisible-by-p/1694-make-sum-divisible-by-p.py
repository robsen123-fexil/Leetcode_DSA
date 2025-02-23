class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        hsh={0:-1}
        minima=inf
        sums=0
        sms=sum(nums)
        if sms%p==0:
            return 0
        for i , val  in enumerate(nums):
            sums+=val
            mod=sums%p
            if (mod-sms+p)%p in hsh:
                minima=min(minima , i-hsh[(mod-sms+p)%p])
            hsh[mod]=i

        return minima if minima!=len(nums) else -1