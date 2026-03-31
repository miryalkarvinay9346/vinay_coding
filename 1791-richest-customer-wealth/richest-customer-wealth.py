class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        high_wealth=0
        for i in range(len(accounts)):
            current_wealth=0
            for j in range(len(accounts[i])):
                current_wealth+=accounts[i][j]
            if current_wealth>high_wealth:
                high_wealth=current_wealth
        return high_wealth            
        