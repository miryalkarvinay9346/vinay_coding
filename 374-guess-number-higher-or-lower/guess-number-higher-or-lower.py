# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        for i in range(0,n+1):
            if guess(i)==0:
                return i
        """
        s=1#start
        e=n #end
        while True:
            mid=(s+e)//2 #middle value
            result=guess(mid) #returns -1 ,0 ,+1
            if result==0:
                return mid #return mid if matched
            elif result>0:
                s=mid+1 #number is greater, so move s to mid + 1
            else:
                e=mid-1 #number is smaller than mid, so move e to mid - 1