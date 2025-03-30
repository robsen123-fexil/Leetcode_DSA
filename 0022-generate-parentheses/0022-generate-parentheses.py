class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        strs=''
        if n==0:
            return strs
        result=[]
        def backtrack(strs , opn , clos  ):
            if len(strs)==2*n:
                result.append(strs)
                return
            if opn<n:
                backtrack(strs +'(' , opn+1 , clos)
            if clos<opn:
                backtrack(strs+')' , opn , clos+1)
        backtrack('' , 0 , 0 )
        return result


