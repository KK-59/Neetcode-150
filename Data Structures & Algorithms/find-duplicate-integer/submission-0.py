class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        rec = {} # num to frequency

        for i in range(len(nums)): 
            if nums[i] in rec: 
                rec[nums[i]] += 1
            else:
                rec[nums[i]] = 1
        for key in rec:
            if rec[key] > 1: 
                return key