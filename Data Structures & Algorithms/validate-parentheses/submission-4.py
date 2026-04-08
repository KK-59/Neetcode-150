class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 == 1: 
            return False
        for i in range(len(s)):
            y = s[i]
            
            if y == ")" or y == "]"  or y == "}" :
                if len(stack) == 0:
                    return False
                x = stack.pop()
                if y == ")" and x != "(":
                    return False
                if y == "]" and x != "[":
                    return False
                if y == "}" and x != "{":
                    return False
            else:
                stack.append(y)
            print(stack)
            print(y)
        if len(stack) != 0:
            return False
        return True

        