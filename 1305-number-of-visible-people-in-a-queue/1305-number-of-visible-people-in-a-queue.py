class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack=[]
        ans=[0]*(len(heights))
        for i , val in enumerate(reversed(heights)):
            count = 0
            while stack and stack[-1]<val:
                stack.pop()
                count += 1
            if stack:
                ans[i] = count + 1
            else:
                ans[i] = count
            stack.append(val)
                
        return ans[::-1]