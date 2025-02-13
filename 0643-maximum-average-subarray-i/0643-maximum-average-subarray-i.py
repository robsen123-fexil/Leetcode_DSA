class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        frst=sum(nums[:k])
        avg=frst/k
        l=0
        for i in range(k ,len(nums)):
            frst+=nums[i]
            frst-=nums[l]
            l+=1
            hr=frst/k
            avg=max(hr , avg)
        return avg
            