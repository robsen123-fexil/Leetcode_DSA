class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        hsh={}
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                hsh[mat[i][j]]=(i , j)
        print(hsh)
        rw=[0]*len(mat)
        col=[0]*len(mat[0])
        for i in range(len(arr)):
            a , b=hsh[arr[i]]
            rw[a]+=1
            col[b]+=1
            if rw[a]==len(mat[0]) or col[b]==len(mat):
                return i
        

