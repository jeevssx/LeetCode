class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        per=0
        def walaco(i,j,grid):
            w=0
            r=len(grid)
            c=len(grid[0])
            if j==0 or grid[i][j-1]==0 :
                w+=1  
            if i==0 or grid[i-1][j]==0:
                w+=1
            if i==r-1 or grid[i+1][j]==0 :
                w+=1
            if j==c-1 or grid[i][j+1]==0:
                w+=1
            return w
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    per+=walaco(i,j,grid)
        return per