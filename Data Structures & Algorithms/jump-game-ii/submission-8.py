class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        i = 0
        steps = 0
        while i < len(nums)-1: 
            furthest = 0
            furthestIndex = 0
            if i + nums[i] >= len(nums) - 1:
                return steps + 1
            for j in range(1,nums[i]+1): 
                if i + j < len(nums) and nums[j+i] + j + i >= furthest: 
                    furthest = nums[j+i] + j + i
                    furthestIndex = j
            steps += 1
            i += furthestIndex 
        return steps

