class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        hsh=defaultdict(list)
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                sums=nums[i]+nums[l]+nums[r]
                clo=abs(sums-target)
                hsh[clo].append(sums)
                if sums<target:
                    l+=1
                elif sums>target:
                    r-=1
                else:
                    return sums
        mini=min(hsh.keys())
        return max(hsh[mini])


        # minima=float('inf')
        # nums.sort()
        # for i in range(len(nums)-2):
        #     l=i+1
        #     r=len(nums)-1
        #     while l<r:
        #         res=nums[i]+nums[l]+nums[r]
        #         if abs(target-res) < abs(target-minima):
        #             minima=res
        #         if res>target:
        #             r-=1
        #         elif res<target:
        #             l+=1
        #         else:
        #             return res
        # return minima if minima!=float('inf') else 0

