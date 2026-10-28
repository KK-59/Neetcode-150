class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        r = sum(nums) - nums[0]
        p = 0
        l = 0
        while p < len(nums)-1 and r != l:
            l += nums[p]
            r -= nums[p+1]
            p += 1
        if l == r:
            return p
        else:
            return -1