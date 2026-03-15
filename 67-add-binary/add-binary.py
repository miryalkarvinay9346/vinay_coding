class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # we use  slicing to avoid "0b" in output
        return bin(int(a,2)+int(b,2))[2:]

        