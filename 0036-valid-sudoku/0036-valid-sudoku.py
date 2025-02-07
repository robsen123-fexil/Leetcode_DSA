class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checker(rw):
            cnt=Counter()
            for i in rw:
                if i!='.':
                    if cnt[i]>0:
                        return False
                    cnt[i]+=1
            return True
        for i in board:
            if not checker(i):
                return False
        for i in range(9):
            cnt=Counter()
            for j in range(9):
                if board[j][i]!='.':
                    if cnt[board[j][i]]>0:
                        return False
                    cnt[board[j][i]]+=1
           
        def subchecker(i , j , mat):
            cnt=Counter()
            for a in range(i , i+3):
                for b in range(j , j+3):
                    if mat[a][b]!='.':
                        if cnt[mat[a][b]]>0:
                            return False
                        cnt[mat[a][b]]+=1
            return True
        for i in range(0 , 9 , 3):
            for j in range(0 , 9 , 3):
                if not subchecker(i , j , board):
                    return False
        return True
                    



                