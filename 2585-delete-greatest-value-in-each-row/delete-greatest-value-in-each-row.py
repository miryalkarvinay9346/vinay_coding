class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        s=0
        """
        for i in range(len(grid)):
            s+=sum(grid[i])-min(grid[i])
        return s
        """
        for row in grid:
            row.sort()
        for j in range(len(grid[0])):
            s += max(row[j] for row in grid)
        return s
        