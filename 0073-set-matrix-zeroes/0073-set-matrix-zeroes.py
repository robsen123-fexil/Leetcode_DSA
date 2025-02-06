class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        result=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    result.append([i , j])
       
        for i in range(len(result)):
            col , row= result[i]
            l=0
            for j in matrix[col]:
                matrix[col][l]=0
                l+=1
            for k in matrix:
                
                k[row]=0
        print(matrix)
        return []



        return [] 
        