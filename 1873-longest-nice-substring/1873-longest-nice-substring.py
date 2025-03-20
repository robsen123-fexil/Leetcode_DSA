class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def solver(s):
            if len(s)<2:
                return ""
            for i in range(len(s)):
                if s[i].swapcase() not in s:
                    left=solver(s[:i])
                    right=solver(s[i+1:])
                    if len(left)>=len(right):
                        return left
                    else:
                        return right
            return s
        return solver(s)
                    