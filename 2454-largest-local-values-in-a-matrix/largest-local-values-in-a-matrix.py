class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n=len(grid)
        m=[[0]*(n-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                k=0
                for a in range(i,i+3):
                    for b in range(j,j+3):
                        k=max(k,grid[a][b])
                m[i][j]=k
        return m
        """
        result = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                result[i][j] = max(
                    grid[i][j],     grid[i][j+1],     grid[i][j+2],
                    grid[i+1][j],   grid[i+1][j+1],   grid[i+1][j+2],
                    grid[i+2][j],   grid[i+2][j+1],   grid[i+2][j+2]
                )

        return result
        """
