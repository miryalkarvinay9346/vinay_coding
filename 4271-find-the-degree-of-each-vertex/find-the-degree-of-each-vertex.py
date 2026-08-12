class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        a=[]
        for i in range(len(matrix)):
            c=0
            for j in range(len(matrix)):
                if matrix[i][j]==1:
                    c+=1
            a.append(c)
        return a