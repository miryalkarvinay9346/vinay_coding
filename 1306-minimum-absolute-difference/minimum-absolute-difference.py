class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        a=[]
        arr.sort()
        m=float('inf')
        for i in range(1,len(arr)):
            d=arr[i]-arr[i-1]
            if d<m:
                m=d
                a=[[arr[i-1],arr[i]]]  
            elif d==m:
                k=[arr[i-1],arr[i]]
                a.append(k)
        return a


        