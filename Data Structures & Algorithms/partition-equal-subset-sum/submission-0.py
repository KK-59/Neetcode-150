class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        x = sum(nums)
        if x % 2 == 1:
            return False
        half = int(x/2)
        rec = {} # (cur,index) -> bool
        def backtrack(cur, index):
            if index == len(nums):
                return False
            if cur == half:
                return True
            if (cur, index) in rec:
                return rec[(cur, index)]
            else:
                x = backtrack(cur + nums[index], index + 1) or backtrack(cur, index + 1)
                rec[(cur,index)] = x
            return x
        return backtrack(0,0)