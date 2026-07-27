class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a=[]#stack
        for i in operations:
            if i=="C":
                a.pop()#invalid previous score
            elif i=="D":
                a.append(a[-1]*2)#double previous score
            elif i=="+":
                a.append(a[-1]+a[-2])#sum of last two scores
            else:
                a.append(int(i))#new score
        return sum(a)

        