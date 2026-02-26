class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        a=0
        for i in range(0,len(operations)):
            if(operations[i]=="++X" or operations[i]=="X++"):
                a=a+1
            else:
                a=a-1
        return a;     
