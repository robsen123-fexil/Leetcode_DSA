class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt=0
        for i in range(len(nums)-2):
            print(nums[i+2])
            if nums[i]==0:
                cnt+=1
                nums[i]=1 
                nums[i+1]=0 if nums[i+1]==1 else 1
                nums[i+2]=0 if nums[i+2]==1 else 1
        if len(set((nums)))==1 and nums[0]==1:
            return cnt
        return -1