class Solution:
    def findLucky(self, arr: List[int]) -> int:
        l=-1
        for i in range(len(arr)):
            c=0
            for j in range(len(arr)):
                if arr[i]==arr[j]:
                    c+=1
            if c==arr[i]:
                l=max(l,arr[i])
        return l