class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        def aranole(i, j, mat):
            ll = []
            while i >= 0 and j < len(mat[0]):
                ll.append(mat[i][j])
                i -= 1
                j += 1
            return [i ,j, ll]  
        def arangade(i, j, mat):
            ll = []
            while i < len(mat) and j >= 0: 
                ll.append(mat[i][j])
                i += 1
                j -= 1
            return [i, j, ll]  
        if not mat or not mat[0]:  
            return []
        l, r = 0, 0
        ans = []
        while len(ans) < (len(mat) * len(mat[0])):
            a, b, ll = aranole(l, r, mat)
            ans.extend(ll)
            if b == len(mat[0]):
                l = a+2
                r = b -1
            else:
                l = a + 1
                r = b
            if len(ans) == len(mat) * len(mat[0]):
                break
            a, b, ll = arangade(l, r, mat)
            ans.extend(ll)
            if a==len(mat):
                l = a -1
                r = b+2
            else:
                l = a
                r = b + 1
        return ans
