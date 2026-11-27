class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)): 
            x = abs(nums[i])
            if nums[x-1] > 0: 
                nums[x-1] -= 2*(nums[x-1])
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res
            