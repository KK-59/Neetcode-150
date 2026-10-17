class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones, reverse=True)
        while (len(stones)) > 1: 
            print(stones)
            if stones[0] == stones[1]: 
                stones = stones[2:]
            else:
                stones[1] = stones[0] - stones[1]
                stones = stones[1:]
                if len(stones) > 1:
                    i = 1
                    while i < len(stones) and stones[i-1] < stones[i]: 
                        temp = stones[i-1]
                        stones[i-1] = stones[i]
                        stones[i] = temp
                        i += 1
        if len(stones) == 0:
            return 0
        return stones[0]