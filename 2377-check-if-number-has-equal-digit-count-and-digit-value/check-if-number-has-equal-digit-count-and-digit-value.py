class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in range(0,len(num)):#loop for running each digit
            count=0 #count a digit, that is how many times is repeated in loop
            for j in range(0,len(num)):#running for matching i'th digit with every digit in loop
                if (num[j]==str(i)):#checking each digit is matched and increment count
                    count=count+1#increment count is digit is matched
            if(count!=int(num[i])):#if count of digit is not equal to num at index i
                return False#returns false and exit the entire loops
            #else continues for checking another digit in the string     
        return True        