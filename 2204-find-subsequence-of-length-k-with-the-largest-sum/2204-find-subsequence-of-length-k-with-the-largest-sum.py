class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        mp=[(num, i ) for i , num in enumerate(nums)]
        mp.sort(key=lambda x:-x[0])
        print(mp)
        ans=mp[:k]
        ans.sort(key=lambda x:x[1])
        print(ans)
        return [num for num , i in ans]