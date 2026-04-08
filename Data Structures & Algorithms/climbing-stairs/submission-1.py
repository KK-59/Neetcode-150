class Solution:
    def climbStairs(self, n: int) -> int:
        record = {} # number of stairs -> number of ways
        i = 1
        while i <= n:
            if i == 1:
                record[i] = 1
            elif i == 2:
                record[i] = 2
            else:
                record[i] = record[i-1] + record[i-2]
            i += 1
        print(record)
        
        return record[n]