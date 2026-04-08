class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        record = {} # floor -> cost to get to that floor

        record[0] = 0
        record[1] = 0
        for i in range(2,len(cost)+1):
            record[i] = min(cost[i-1],cost[i-2])
            if record[i-1] + cost[i-1] < record[i-2] + cost[i-2]:
                record[i] = cost[i-1] + record[i-1]
            else:
                record[i] = cost[i-2] + record[i-2]
        print(record)
        return record[len(cost)]