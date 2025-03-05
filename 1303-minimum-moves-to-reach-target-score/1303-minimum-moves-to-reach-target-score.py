class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        count=0
        while maxDoubles and target>1:
            if target%2!=0:
                count+=1
                target-=1
            else:
                target//=2
                count+=1
                maxDoubles-=1
        if target:
            return count+(target-1)
        else:
            return count