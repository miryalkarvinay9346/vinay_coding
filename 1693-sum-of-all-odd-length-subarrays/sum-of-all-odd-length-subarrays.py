class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        s=0
        n=len(arr)
        for i in range(n):
            for j in range(i,n):
                k=arr[i:j+1]
                if len(k)%2!=0:
                    s+=sum(k)
        return s