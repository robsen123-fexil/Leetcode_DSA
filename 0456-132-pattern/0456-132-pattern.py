class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        minima=-inf
        for i in nums[::-1]:
            if i<minima:
                return True
            while stack and stack[-1]<i:
                minima= stack.pop()
            stack.append(i)
        return False
