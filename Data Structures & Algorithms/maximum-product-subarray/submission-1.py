class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        rec = [0] * len(nums)
        rec[0] = (nums[0],nums[0])
        res = nums[0]
        for i in range(1,len(nums)):
            curMax = max(rec[i-1][0]*nums[i], rec[i-1][1]*nums[i], nums[i])
            curMin = min(rec[i-1][0]*nums[i], rec[i-1][1]*nums[i], nums[i])
            if curMax > res:
                res = curMax
            rec[i] = (curMax,curMin)
        return res

