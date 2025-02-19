class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        cl=len(matrix[0])+1
        rw=len(matrix)+1
        self.prefx=[[0]*cl for _ in range(rw)]
        for i in range(1,rw):
            for j in range(1, cl):
                self.prefx[i][j] = matrix[i-1][j-1] + self.prefx[i-1][j] +self.prefx[i][j-1]-self.prefx[i-1][j-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.prefx[row2+1][col2+1]-self.prefx[row2+1][col1] -self.prefx[row1][col2+1] +self.prefx[row1][col1]
        return ans
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)