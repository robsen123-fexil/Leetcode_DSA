class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hsh=defaultdict(int)
        hsh[0]+=1
        sums=count=0
        for i in range(len(nums)):
            sums+=nums[i]
            if (sums%k) in hsh:
                count+=hsh[((sums%k))]
            hsh[sums%k]+=1
        return count
        
            
            
