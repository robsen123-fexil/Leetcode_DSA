class Solution:
    def removeStars(self, s: str) -> str:
        strs=[]
        for  val in s:
            if strs and val=='*':
                strs.pop()
            else:
                strs.append(val)
        return ''.join(strs)