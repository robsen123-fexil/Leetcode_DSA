class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hsh=defaultdict(int)
        hsh[0]+=1
        sums=count=0
        for i in range(len(nums)):
            sums+=nums[i]
            if sums-goal in hsh:
                count+=hsh[sums-goal]

            hsh[sums]+=1
        print(hsh)
        return count
