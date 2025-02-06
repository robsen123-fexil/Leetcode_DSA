class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                r=j
                k=i
                val=matrix[i][j]
                while k<len(matrix) and r<len(matrix[0]):
                    if val!=matrix[k][r]:
                        return False
                    k+=1
                    r+=1
        return True

