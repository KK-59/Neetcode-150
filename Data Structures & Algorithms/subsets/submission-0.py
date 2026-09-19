class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        template:
        def backtrack(index, solution):
            if base case condition:
                results.append(solution)
                return 

            for choice in choices:
                if violates constraint:
                    continue
                
                make choice
                backtrack
                undo choice -- this is the backtracking step
                backtrack
        """
        results = []

        def backtrack(index, path):
            if index == len(nums):
                results.append(path.copy())
                return 
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            backtrack(index + 1, path)
        backtrack(0,[])
        return results