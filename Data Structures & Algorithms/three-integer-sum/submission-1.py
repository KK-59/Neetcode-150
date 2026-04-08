class Solution:
    def threeSum(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)

        output = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            p = i + 1
            q = len(nums) - 1
            while p < q:
                curr = nums[p] + nums[q]
                if curr < target:
                    p += 1
                elif curr > target:
                    q -= 1
                else:
                    output.append([nums[i], nums[p], nums[q]])
                    p += 1
                    q -= 1
                    while p < q and nums[p] == nums[p-1]:
                        p += 1

        return output