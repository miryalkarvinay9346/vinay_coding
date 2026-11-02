class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        s=0
        for i in nums:
            k=0
            for j in str(i):
                k=max(k,int(j))
            s+=int(str(k)*len(str(i)))
        return s
