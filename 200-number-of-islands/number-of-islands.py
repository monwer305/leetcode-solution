class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rowL = len(grid)
        colL = len(grid[0])

        def recLand(n,m):
            if n<0 or n>=rowL or m<0 or m >= colL:
                return
            
            if grid[n][m] == "0":
                return 
            
            grid[n][m] = "0"

            recLand(n+1,m)
            recLand(n-1,m)
            recLand(n,m+1)
            recLand(n,m-1)

            return

        total = 0
        
        for i in range(rowL):
            for j in range(colL):
                if grid[i][j] == "1":
                    recLand(i,j)
                    total+=1
        
        return total

        


        