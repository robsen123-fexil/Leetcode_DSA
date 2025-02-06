class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if target==mat:
            return True
        def checker(mat):
            result=[]
            l=r=0
            while l<len(mat[0]):
                result.append([])
            
                for i in range(len(mat)):
                   result[-1].append(mat[i][l])
                l+=1
            return result[::-1]
        print(checker(mat))
        if checker(mat)==target:
            return True
        else:
            val=checker(mat)
            r=len(mat)
            while r>0:
                val=checker(val)
                if val==target:
                    return True
                r-=1
            return False
        

    