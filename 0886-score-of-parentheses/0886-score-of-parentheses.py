class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        for i in s:
            if i==')':
                if stack[-1]=='(':
                    stack.pop()
                    if stack and str(stack[-1]).isdigit():
                        stack.append(stack.pop()+1)
                    else:
                        stack.append(1)
                elif str(stack[-1]).isdigit():
                    a=stack.pop()
                    b=stack.pop()
                    if stack and str(stack[-1]).isdigit():
                       stack.append((a*2)+stack.pop())
                    else:
                        stack.append(a*2)
            else:
                stack.append(i)
        return stack[0]