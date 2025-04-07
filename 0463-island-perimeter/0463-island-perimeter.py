class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if   grid[r][c] == 1:
                    perimeter += 4

                    # Check above
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 2  # one shared edge (up and down)
                    
                    # Check left
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 2  # one shared edge (left and right)

        return perimeter