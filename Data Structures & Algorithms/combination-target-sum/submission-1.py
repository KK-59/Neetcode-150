class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        template:
        
        def backtrack(index, path):
            if stopping condition:
                result.append(path)
                return 

            for choice in choices:
                make choice (path.append)
                backtrack(index, path)
                undo choice

                backtrack(index, path) (?)
            
        """

        result = [] # list of lists

        def backtrack(index, path):
            if sum(path) == target and path not in result:
                result.append(path.copy())
                return 
            if index >= len(nums):
                return 
            # path.append(nums[index]) # choose to include number once 
            # backtrack(index + 1, path)
            # path.pop() # undo choice 

            # choose to include number again k times
            # path.append(nums[index])
            # path.append(nums[index])
            # backtrack(index + 1, path)
            # path.pop()
            # path.pop()

            k = 0
            while sum(path) + (k * nums[index]) <= target: 
                for i in range(k):
                    path.append(nums[index])
                backtrack(index + 1, path)
                for i in range(k):
                    path.pop()
                k += 1

            # backtrack(index + 1, path) 
        backtrack(0,[])
        return result


