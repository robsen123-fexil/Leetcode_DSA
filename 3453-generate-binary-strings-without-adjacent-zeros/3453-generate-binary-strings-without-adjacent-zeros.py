class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans=[]
        strs=[]
        def backtracker(strs):
            if len(strs)>1 and ''.join(set(strs[-2:]))=='0':
                return 
            if len(strs)==n:
                ans.append(''.join((strs[:])))
                return 
         
          
            strs.append('0')
            backtracker(strs)
            strs[-1]='1'
            backtracker(strs)
            strs.pop()
            
        backtracker(strs)
        return ans
        

            