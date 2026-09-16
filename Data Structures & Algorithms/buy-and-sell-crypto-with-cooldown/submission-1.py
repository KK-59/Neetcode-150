class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        K = [[0 for _ in range(3)] for _ in range(len(prices))]
        K[0][0] = -prices[0]
        K[0][1] = -10000
        K[0][2] = 0

        for i in range(1,len(prices)):
            print("in here")
            K[i][0] = max(K[i-1][2] - prices[i],K[i-1][0])
            K[i][1] = K[i-1][0] + prices[i]
            K[i][2] = max(K[i-1][0],K[i-1][1],K[i-1][2])
        print(K)
        n = len(prices)
        return max(K[n-1][0],K[n-1][1],K[n-1][2])