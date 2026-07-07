class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # max you can reach from a certain 
        if len(nums) == 1:
            return True
        goal = len(nums) - 1
        i = goal - 1
        record = [0*len(nums)]
        while i > 0:
            if i + nums[i] >= goal:
                goal = i
            i -= 1
        if i + nums[i] >= goal:
            return True
        return False