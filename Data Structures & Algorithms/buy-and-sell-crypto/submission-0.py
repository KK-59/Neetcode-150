class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        minimum = prices[0]
        for i in prices:
            if i < minimum:
                minimum = i
            else:
                if i - minimum > diff:
                    diff = i - minimum
        print(diff)
        return diff

        