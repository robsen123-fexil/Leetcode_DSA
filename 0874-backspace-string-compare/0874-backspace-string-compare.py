class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack=[]
        for i in s:
            if i=='#':
                if stack:
                    stack.pop()
                continue
            stack.append(i)
        st2=[]
        for i in t:
            if i=='#':
                if st2:
                    st2.pop()
                continue
            st2.append(i)
        return st2==stack