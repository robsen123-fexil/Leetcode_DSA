class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        res.append([])
        for i in nums:
            for k in range(len(res)):
                sub=res[k].copy()
                sub.append(i)
                res.append(sub)
        return res
        