class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        def backtrack(index, path): 
            if len(path) == k and path not in results:
                results.append(path.copy())
            if index > n:
                return 
            
            path.append(index)
            backtrack(index + 1, path) 
            path.pop()
            backtrack(index + 1, path) 
        backtrack(1,[])
        return results