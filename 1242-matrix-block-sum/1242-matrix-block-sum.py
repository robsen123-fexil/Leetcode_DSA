class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rw=len(mat)+1
        col=len(mat[0])+1
        pref=[[0]*col for _ in range(rw)]
        print(pref)
        for i in range(1 , rw):
            for j in range(1 , col):
                pref[i][j] = pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1] + mat[i-1][j-1]
        matrix=[[0]*(col-1) for _ in range(rw-1)]
        real=[[0]*(col-1) for _ in range(rw-1)]
        for i in range(1 , len(pref)):
            for j in range(1 , len(pref[i])):
                real[i-1][j-1]=pref[i][j]
        print(real)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                row1=max(0 , i-k)
                row2=min(len(mat)-1 , i+k)
                col1=max(0 , j-k)
                col2=min(len(mat[0])-1 , j+k)
                matrix[i][j]= pref[row2+1][col2+1]-pref[row2+1][col1] -pref[row1][col2+1] +pref[row1][col1]
        return matrix
                