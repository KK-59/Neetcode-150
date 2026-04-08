class Solution:
    def climbStairs(self, n: int) -> int:
        record = {} # number of stairs -> number of ways
        i = 1
        while i <= n:
            # if i + 2 > n and i + 1 <= n:
            #     if i - 2 > 0:
            #         record[i] = record[i-1] + record[i-2]
            #     elif i - 1 > 0:
            #         record[i] = record[i-1]
            #     else:
            #         record[i] = 1
            # elif i + 2 <= n:
            #     if i - 2 > 0:
            #         record[i] = record[i-1] + record[i-2]
            #     elif i - 1 > 0:
            #         record[i] = record[i-1]
            #     else:
            #         record[i] = 2
            # else:
            #     if i - 2 > 0:
            #         record[i] = record[i-1] + record[i-2]
            #     elif i - 1 > 0:
            #         record[i] = record[i-1]
            #     else: 
            #         record[n] = 0
            # i += 1

            if i == 1:
                record[i] = 1
            elif i == 2:
                record[i] = 2
            else:
                record[i] = record[i-1] + record[i-2]
            i += 1
        print(record)
        
        return record[n]