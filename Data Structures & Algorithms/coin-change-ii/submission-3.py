class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        K = []

        if amount == 0:
            return 1

        for i in range(amount+1):
            K.append([])
        for i in range(amount+1):
            for j in range(len(coins)):
                K[i].append(0)
        for i in range(1,amount+1):
            for j in range(len(coins)):
                if coins[j] == i:
                    K[i][j] = 1

        for i in range(1,amount+1):
            for j in range(len(coins)):
                if i-coins[j] >= 0:
                    K[i][j] += K[i-coins[j]][j]
                if j >= 1:
                    K[i][j] += K[i][j-1]
        return K[-1][-1]
