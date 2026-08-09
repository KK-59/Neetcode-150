class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        rec = [0]*(len(nums) + 1)
        rec[0] = 0
        rec[1] = nums[0]
        for i in range(1,len(nums)):
            rec[i+1] = max(nums[i] + rec[i-1], rec[i]) 
        print(rec)
        return rec[len(nums)]