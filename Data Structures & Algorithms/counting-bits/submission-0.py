class Solution:
    def countBits(self, n: int) -> List[int]:
        resList = []
        def hammingWeight(n: int) -> int: 
            res = 0
            while n > 0: 
                x = int(n/2)
                res += (n % 2)
                n = x
            return res
        for i in range(n+1):
            resList.append(hammingWeight(i))
        return resList