class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = [0] * (ord("z") + 1)
        letters_t = [0] * (ord("z") + 1)
        print(ord("z"))
        print(ord("r"))
        for i in range(len(s)):
            x = ord(s[i])
            letters[x] += 1

        for i in range(0,len(t)):
            x = ord(t[i])
            letters_t[x] += 1
        print(letters)
        print(letters_t)
        if letters == letters_t:
            return True
        else:
            return False
                