class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.split('/')
        strs=[]
        for i in path:
            if i:
                strs.append(i)
        stack=[]
        for i in strs:
            if i=='.':
                continue
            if i=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return '/'+'/'.join(stack)
