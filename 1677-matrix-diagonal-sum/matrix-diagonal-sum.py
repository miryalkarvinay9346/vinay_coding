class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s=0
        for i in range(len(mat)):
            s+=mat[i][i]# main diagonal
            s+=mat[i][len(mat)-1-i]# other diagonal
        if len(mat)%2==1:
            s-=mat[len(mat)//2][len(mat)//2]# remove middle  element counted twice
        return s
        