class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a=[0]*len(heights)
        for i in range(len(heights)):
            a[i] = heights[i]
        for i in range(len(heights)):
            j=i
            while(j>0 and a[j-1] >a[j]):
                temp=a[j-1]
                a[j-1]= a[j]
                a[j] = temp
                j-=1
        c=0
        for i in range(len(a)):
            if(a[i] != heights[i]):
                c+=1
        return c