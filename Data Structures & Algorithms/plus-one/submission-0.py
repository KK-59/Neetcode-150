class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = [0] * (len(digits) + 1)
        for i in range(1,len(digits)+1):
            result[i] = digits[i-1]
        result[-1] += 1
        print(result)
        if result[-1] > 9:
            carry = 1
            result[-1] -= 10
        else:
            carry = 0
        i = len(result)-2
        while i > 0:
            result[i] = digits[i-1] + carry
            if result[i] > 9:
                carry = 1
                result[i] -= 10
            else:
                carry = 0  
            i -= 1
        print(result) 
        if carry == 1:
            result[0] = 1
            return result
        else:
            return result[1:] 