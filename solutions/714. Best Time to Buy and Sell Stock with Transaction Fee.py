class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        return self.sol2(prices, fee)
        
    def sol1(self, prices, fee):
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0], dp[0][1] = -prices[0], 0
        
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], -prices[i], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee)
        
        
        return max(dp[-1])
    
        #  greedy ?
    
