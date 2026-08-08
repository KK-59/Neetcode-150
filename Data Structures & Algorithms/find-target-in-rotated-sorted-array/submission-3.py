class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        l = 0 
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[r] == target:
                return r
            if nums[l] == target:
                return l
            if l == r-1:
                return -1
            if nums[m] < nums[r]:
                if target > nums[m] and target < nums[r]:
                    l = m+1
                else:
                    r = m-1
            elif nums[m] > nums[l]:
                if target < nums[m] and target > nums[l]:
                    r = m-1
                else:
                    l = m+1

        return -1