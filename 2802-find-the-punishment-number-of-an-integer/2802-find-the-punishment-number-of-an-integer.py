class Solution:
    def punishmentNumber(self, n: int) -> int:
        lists=[]
        def checker(i , cur ,target , strs ):
            if i==len(strs) and cur==target:
                return True
            for j in range(i , len(strs)):
                strs[i:j+1]
                if checker(j+1 , cur+int(strs[i:j+1]), target , strs):

                    return True
            return False
        ans=0
        for i in range(1 , n+1):
            if checker(0 , 0 , i , str(i*i)):
                ans+=(i*i)
        return ans

