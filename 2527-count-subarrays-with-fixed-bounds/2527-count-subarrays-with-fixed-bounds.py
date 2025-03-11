class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        frsts=large=second=-1
        ans=0
        for i in range(len(nums)):
            if minK<=nums[i]<=maxK:
                if nums[i]==minK:
                    frsts=i
                if nums[i]==maxK:
                    second=i
            else:
                large=i
            ans+=(max(0 , min(frsts ,second)-large))
            
        return ans
            
                