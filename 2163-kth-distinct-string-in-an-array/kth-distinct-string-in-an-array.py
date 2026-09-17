class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        a=[]
        for i in range(len(arr)):
            v=arr.count(arr[i])
            if v==1:
                if v not in a:
                    a.append(arr[i])
        if k<=len(a):
            return a[k-1]
        else:
            return ""
        """
        return a
        """
