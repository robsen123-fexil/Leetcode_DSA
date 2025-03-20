class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums=[]
        for i in range(1 , n+1):
            nums.append(i)
        print(nums)
        sol , ans=[] , []
        def back(i):
            if len(sol)==k:
                ans.append(sol[:])
                return 
            for i in range(i , len(nums)+1):
                sol.append(i)
                back(i+1)
                sol.pop()
        back(1)
        return ans
