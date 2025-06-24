class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res=[]
        result=[]
        for i , val in enumerate(nums):
            if val==key:
                res.append(i)
        for i in res:
            for j , val in enumerate(nums):
                if abs(i-j)<=k:
                    result.append(j)
        return list(set(result))
