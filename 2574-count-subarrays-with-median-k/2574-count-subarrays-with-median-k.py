class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        indx=nums.index(k)
        hsh=defaultdict(int)
        hsh[0]+=1
        sums=0
        for i in range(indx+1 , len(nums)):
            if nums[i]>k:
                sums+=1
            else:
                sums-=1
            hsh[sums]+=1
        ans=sums=0
        print(hsh)
        for i in range(indx, -1 , -1):
            if nums[i]>k:
                sums+=1
            else:
                if nums[i]<k:
                    sums-=1
                else:
                    sums+=0

            #odd
            ans+=hsh[-sums]
            #even
            ans+=hsh[-sums+1]
        return ans
