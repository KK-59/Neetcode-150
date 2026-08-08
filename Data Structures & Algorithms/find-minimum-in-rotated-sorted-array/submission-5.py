class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums)-1
        print("here ", l,r)
        while l <= r:
            if l == r:
                return nums[l]
            if l == r-1:
                return min(nums[r],nums[l])
            m = (l + r) // 2
            print("hello ", m)
            if nums[m] < nums[m-1] and nums[m] < nums[m+1]:
                return nums[m]
            if nums[m] < nums[r] and nums[m] < nums[l]:
                r = m-1
            elif nums[m] > nums[r] and nums[m] > nums[l]:
                l = m+1
            elif nums[m] > nums[r]:
                l = m+1
            elif nums[m] > nums[l]:
                print("in here")
                r = m-1
        