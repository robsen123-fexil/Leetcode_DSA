class Solution:
    def countBits(self, n: int) -> List[int]:
        def solver(i):
            count=0
            if i!=0:
                count+=1
            while i>1:
                if i%2!=0:
                    count+=1
                i//=2
            return count
        ans=[]
        for i in range(n+1):
            ans.append(solver(i))
        return ans