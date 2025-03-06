class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0]*(len(temperatures))
        for i , val in enumerate(temperatures):
            while stack and stack[-1][1]<val:
                a , b =stack.pop()
                ans[a]=i-a
            stack.append([i , val])
        return ans