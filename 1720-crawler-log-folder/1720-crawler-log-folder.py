class Solution:
    def minOperations(self, logs: List[str]) -> int:
        logs=''.join(logs)
        logs=logs.split('/')
        stack=[]
        for i in logs:
            if i=='.' or i=='':
                continue
            elif i=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        print(stack)
        return len(stack)