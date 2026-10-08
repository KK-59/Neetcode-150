class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curMax = nums[0]
        curr = nums[0]
        if curr < 0:
            curr = 0
        for i in range(1,len(nums)): 
            curr += nums[i]
            print(curr)
            if curr > curMax:
                curMax = curr
            if curr < 0: 
                curr = 0

        return curMax