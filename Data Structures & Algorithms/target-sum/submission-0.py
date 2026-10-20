class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        rec = {} # (index, curr) -> 0
        def backtrack(index, curr): 
            if (index, curr) in rec:
                return rec[(index, curr)]
            else:
                if curr == target and index == len(nums):
                    return 1 
                if index == len(nums):
                    return 0
                ways = backtrack(index + 1, curr + nums[index]) + backtrack(index + 1, curr - nums[index])
                rec[(index,curr)] = ways
                return ways
        return backtrack(0,0)