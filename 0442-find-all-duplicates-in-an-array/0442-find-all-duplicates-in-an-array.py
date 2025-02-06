class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cnt=Counter(nums)
        result=[k for k , v in cnt.items() if v==2]
        return result
            