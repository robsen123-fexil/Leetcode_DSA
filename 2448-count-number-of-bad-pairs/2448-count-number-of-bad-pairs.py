class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        cnt=Counter()
        for i  , val in enumerate(nums):
            cnt[val-i]+=1
        count=0
        for v in cnt.values():
            if v>=2:
                count+=((v*(v-1))//2)
        all_pairs=(len(nums)*(len(nums)-1))//2
        return all_pairs-count
        
        