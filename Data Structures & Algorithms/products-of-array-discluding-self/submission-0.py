class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        tally = 1
        for i in range(len(nums)):
            prefix[i] *= tally
            tally *= nums[i]
        print(prefix)
        tally = nums[-1]
        print(tally)
        for i in range(len(nums)-2, -1, -1):
            suffix[i] *= tally
            print(tally)
            tally *= nums[i]
        print(suffix)

        output = [1] * len(nums)
        for i in range(0,len(prefix)):
            output[i] = prefix[i] * suffix[i]
        return output
            
