class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        s=""
        for i in range(0,len(num)):
            s+=str(num[i])
        total=str(int(s)+k)
        a=[]
        for i in range(0,len(total)):
            a.append(int(total[i]))
        return a
        