class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        def aranoledemi(i, j, matriksi):
            ll = []
            while i >= 0 and j < len(matriksi[0]):
                ll.append(matriksi[i][j])
                i -= 1
                j += 1
            return [i ,j, ll]  
        def arangadedemi(i, j, matriksi):
            ll = []
            while i < len(matriksi) and j >= 0: 
                ll.append(matriksi[i][j])
                i += 1
                j -= 1
            return [i, j, ll]  
        
        l, r = 0, 0
        ans = []
        while len(ans) < (len(mat) * len(mat[0])):
            a, b, ll = aranoledemi(l, r, mat)
            ans.extend(ll)
            if b == len(mat[0]):
                l = a+2
                r = b -1
            else:
                l = a + 1
                r = b
            if len(ans) == len(mat) * len(mat[0]):
                break
            a, b, ll = arangadedemi(l, r, mat)
            ans.extend(ll)
            if a==len(mat):
                l = a -1
                r = b+2
            else:
                l = a
                r = b + 1
        return ans
