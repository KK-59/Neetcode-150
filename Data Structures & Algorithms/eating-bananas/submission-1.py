class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        upper = max(piles)
        if sum(piles) <= h:
            return 1
        def helper(lower, upper) -> int: 
            # print(lower, upper)
            half = int((lower + upper) / 2)
            if upper - lower <= 1:
                return upper
            tot = 0
            print(half)
            for i in range(len(piles)): 
                if piles[i] < half: 
                    tot += 1
                else:
                    x = piles[i] / half
                    temp = int(x) + (x - int(x) > 0)
                    tot += temp
            # print("half, tot: ", half, tot)
            if tot <= h: 
                return helper(lower, half)
            elif tot > h: 
                return helper(half, upper)
        return helper(lower,upper)
                