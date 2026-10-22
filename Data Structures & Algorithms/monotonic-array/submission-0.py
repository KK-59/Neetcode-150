class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        increasing = False
        for i in range(len(nums)-1): 
            if nums[i+1] > nums[i]:
                increasing = True
                break
            elif nums[i+1] > nums[i]:
                increasing = False
                break
        if i == len(nums) - 1: 
            return True
        else:
            if increasing == True:
                for i in range(len(nums) - 1): 
                    if nums[i+1] >= nums[i]:
                        continue
                    else:
                        return False
                return True
            else:
                for i in range(len(nums) - 1): 
                    if nums[i+1] <= nums[i]:
                        continue
                    else:
                        return False
                return True