class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        template:
        def backtrack():
            if base case:
                return 
            for choice in choices:
                append
                backtrack
                pop

                backtrack (?)
        """
        results = [] # list of lists
        def backtrack(index, path):
            if len(path) == len(nums):
                results.append(path.copy())
                return 
            if index >= len(nums):
                return 
            if nums[index] not in path:
                path.append(nums[index])
                backtrack(0, path)
                path.pop()
            backtrack(index + 1, path)
        backtrack(0,[])
        return results