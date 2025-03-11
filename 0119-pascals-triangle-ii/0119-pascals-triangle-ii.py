class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def helper(given , lists, s):
            if s==given:
                return lists
            frsts=[0]*(len(lists)+1)
            for i  , val in enumerate(lists):
                frsts[i]+=val
                frsts[i+1]+=val

            s+=1
            return helper(given , frsts , s)
        return helper(rowIndex , [1] , 0)



