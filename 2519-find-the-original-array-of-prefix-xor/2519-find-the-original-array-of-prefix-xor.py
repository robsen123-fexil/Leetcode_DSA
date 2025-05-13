class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans=[]
        prev=0
        for i in pref:
            ans.append(i^prev)
            prev=i
        return ans