class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        record = [0] * (len(nums) + 1)
        record[0] = 1
        
        for i in range(1,len(nums)):
            record[i] = 1
            for j in range(i):
                if nums[j] < nums[i] and record[j] >= record[i]:
                    record[i] = record[j] + 1

        return max(record) 