class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = [] # list of lists
        def backtrack(index, path):
            results.append(path.copy())

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]: 
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return results