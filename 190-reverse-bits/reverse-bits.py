class Solution:
    def reverseBits(self, n: int) -> int:
        b=format(n,'032b')#32-bit binary string
        return int(b[::-1],2)