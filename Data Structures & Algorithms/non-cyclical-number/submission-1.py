class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()
        while n != 1:
            if n == 1:
                break
            x = str(n)
            z = 0
            for i in x:
                z += int(i) * int(i)
            n = z
            if n in record:
                return False
            record.add(n)
        if n == 1:
            return True
        else:
            return False