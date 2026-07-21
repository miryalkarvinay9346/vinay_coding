class Solution:
    def convertDateToBinary(self, date: str) -> str:
        y=int(date[:4])
        m=int(date[5:7])
        d=int(date[8:])
        r=str(bin(y)[2:])+"-"+str(bin(m)[2:])+"-"+str(bin(d)[2:])
        return r

        