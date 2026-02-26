class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        a=[]
        for i in range(left,(right+1)):
            if(i%10!=0):
                k=i
                count=0
                while(k>0):
                    rem=k%10
                    if(rem==0 ):
                        break 
                    elif(i%rem==0):
                        count=count+1
                    k=k/10   
                if(count==len(str(abs(i)))):
                    a.append(i)
        return a