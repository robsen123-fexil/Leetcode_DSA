class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def revrs(mat):
            if len(mat)==0:
                return 0
            r=len(mat[0])-1
            
            result=[]
            
            while r>=0:
                k=0
                result.append([])
                while k<len(mat):
                    result[-1].append(mat[k][r])
                    k+=1
                r-=1
            print(result)
            return result
        res=matrix
        ans=[]
        while matrix:
            for i in matrix[0]:
                ans.append(i)
            matrix.remove(matrix[0])
            matrix=revrs(matrix)
        return ans
