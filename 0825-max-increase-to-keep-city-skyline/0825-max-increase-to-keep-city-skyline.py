class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        frsts=[]
        scnd=[]
        l=maxima=0
        for i in range(len(grid)):
            maxima=0
            maxi=0
            for j in range(len(grid[0])):
                maxima=max(maxima , grid[i][j])
                maxi=max(maxi , grid[j][i])
            frsts.append(maxima)
            scnd.append(maxi)
        sums=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                sums+=(min(scnd[i] , frsts[j])-grid[i][j])
        return sums

        

