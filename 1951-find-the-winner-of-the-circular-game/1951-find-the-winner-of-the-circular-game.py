class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums=[]
        for i in range(1 , n+1):
            nums.append(i)
        print(nums)
        frstind=0
        while len(nums)!=1:
            removedind=(frstind+(k-1))%len(nums)
            nums.remove(nums[removedind])
            frstind=removedind
        return nums[0]
        