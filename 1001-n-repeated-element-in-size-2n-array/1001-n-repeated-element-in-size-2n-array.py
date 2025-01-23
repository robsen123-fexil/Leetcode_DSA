class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        leng=len(nums)//2
        cnt=Counter(nums)
       
        for k , v in cnt.items():
            if v==leng:
                return k
