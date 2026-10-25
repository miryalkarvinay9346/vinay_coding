class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        c=0
        k=x
        while x>0:
            c+=x%10
            x=x//10
        if k%c==0:
            return c
        return -1