class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        n = ""
        print(ord('0'))
        print(ord('9'))
        for i in s:
            if ord(i) > 96 and ord(i) < 123:
                n += i
            if ord(i) > 47 and ord(i) < 58:
                n += i
        print(n)

        j = len(n) - 1
        i = 0
        while (i < j):
            if n[i] != n[j]:
                return False
            i += 1
            j -= 1

        return True