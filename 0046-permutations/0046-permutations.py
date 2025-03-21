class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        ans=[]
        def backtrack():
            if len(res)==len(nums):
                
                ans.append(res[:])
                return 
            for x in nums:
                if x not in res:
                    res.append(x)
                    backtrack()
                    res.pop()
            return ans
        
        return backtrack()
