class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [len(temperatures)-1]
        i = len(temperatures)-2
        while i >= 0:
            count = 0
            while len(stack) != 0:
                n = stack.pop()
                if temperatures[i] < temperatures[n]:
                    count += n - i
                    stack.append(n)
                    break
            res[i] = count   
            stack.append(i)
            i -= 1
        return res

        