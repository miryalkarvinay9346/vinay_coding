class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in range(0,len(order)):
            if(order[i] in friends):
                a.append(order[i])
        return a