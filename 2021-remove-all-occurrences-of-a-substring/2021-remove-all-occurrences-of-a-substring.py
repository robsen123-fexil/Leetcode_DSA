class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack=[]
        for i in range(len(s)):
            stack.append(s[i])
            
            
            if ''.join(stack[-len(part):])==part:
                stack=stack[:-len(part)]
        return ''.join(stack)

        