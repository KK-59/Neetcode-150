class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins) == 1:
            if amount % coins[0] == 0:
                return amount//coins[0]
            else:
                return -1
        if amount == 0:
            return 0
        c = [float("inf")] * (amount+1)
        for i in range(len(coins)):
            if coins[i] < amount:
                c[coins[i]] = 1
        # print(c)
        for i in range(1,amount+1):
            tempMin = float("inf")
            # print(i, " : ", tempMin)
            for j in range(len(coins)):
                if i - coins[j] == 0:
                    tempMin = 0
                elif i - coins[j] >= 0 and c[i - coins[j]] != 0:
                    tempMin = min(c[i - coins[j]], tempMin)
            if tempMin != float("inf"):
                c[i] = 1 + tempMin
        print(c)
        if c[-1] == float("inf"):
            return -1
        else:
            return c[-1]
        
       