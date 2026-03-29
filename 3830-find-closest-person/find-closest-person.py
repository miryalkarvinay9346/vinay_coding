class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        if(abs(x-z)==abs(y-z)):
            return 0
        elif abs(x-z)>abs(y-z):
            return 2
        else:
            return 1    