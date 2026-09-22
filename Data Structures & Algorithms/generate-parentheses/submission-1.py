class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = [] # list of strings
        curr = ""
        def backtrack(index, curr): 
            if len(curr) == 2*n:
                results.append(curr)
                curr = ""
                return 
            backtrack(index + 1, curr + "(")
            backtrack(index + 1, curr + ")")
        def filter_results(results): 
            stack = []
            real = []
            for i in range(len(results)):
                stack = []
                for j in range(len(results[i])):
                    this = results[i][j]
                    if len(stack) != 0:
                        popped = stack[-1]
                    else:
                        stack.append(this)
                        continue
                    if this == ")" and popped == "(":
                        stack.pop()
                        continue
                    else:
                        stack.append(this)
                if len(stack) == 0:
                    real.append(results[i])
            return real
        backtrack(0,curr)
        return filter_results(results)