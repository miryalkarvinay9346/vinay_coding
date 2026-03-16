class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        a=[]
        a.append(celsius+273.15)
        a.append(celsius*1.80+32.00)
        return a
        