class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        record = {} # nums[i] -> frequency of nums[i] in nums
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if nums[i] in record:
                record[nums[i]] += 1
            else:
                record[nums[i]] = 1
        result = [1] * len(nums)
        longest = result[0]
        for i in range(len(nums)):
            temp = nums[i]
            if temp - 1 not in record: 
                while temp + 1 in record:
                    result[i] += 1
                    temp += 1
            if result[i] > longest:
                longest = result[i]
        return longest
        
            
