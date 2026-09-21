class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = [] # list of lists
        def backtrack(index, path):
            if index >= len(nums) and path not in results:
                results.append(path.copy())
                return 
            # path.append(nums[index])
            # backtrack(index + 1, path)
            # path.pop()
            # backtrack(index + 1, path)

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]: 
                    continue
                path.append(nums[i])
                print("here: ", path)
                backtrack(i + 1, path)
                path.pop()
                backtrack(i + 1, path)

        backtrack(0, [])
        return results