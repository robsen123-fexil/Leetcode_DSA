class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        plsh=['+'  , '-' , '/' , '*']

        for i in tokens:
            if i in plsh:
                a=stack.pop()
                b=stack.pop()
                if i== '+' :
                    stack.append(b+a)
                elif i=='/':
                    print(a , b)
                    print(b//a , int(b/a))
                    stack.append(int(b/a))
                elif i=='*':
                    stack.append(b*a)
                else: 
                    stack.append(b-a)
            else:
                stack.append(int(i))
        return stack[-1]


