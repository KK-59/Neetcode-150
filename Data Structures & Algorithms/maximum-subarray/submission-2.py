class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # [4,-1,-4,5,-4,2,-8,1]

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